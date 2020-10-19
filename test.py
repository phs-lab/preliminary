#-*- coding:utf-8 -*-

# Usage ----------------------------------------------------------------------------------
# import myKerasOCR as mko

# # keras-ocr will automatically download pretrained weights for the detector and recognizer.
# #   MIT License, Pretrained Model
# #   - Text Detection   : Looking for /root/.keras-ocr/craft_mlt_25k.h5 # https://github.com/clovaai/CRAFT-pytorch
# #   -      Recognition : Looking for /root/.keras-ocr/crnn_kurapan.h5  # https://github.com/kurapan/CRNN
# pipeline = mko.Pipeline()
#
# # Get a set of three example images + arbitrary web images
# images = [
#     mko.read(url) for url in [  # mko.tools.read(url)
#         'https://upload.wikimedia.org/wikipedia/commons/b/bd/Army_Reserves_Recruitment_Banner_MOD_45156284.jpg',
#         'https://upload.wikimedia.org/wikipedia/commons/e/e8/FseeG2QeLXo.jpg',
#         'https://upload.wikimedia.org/wikipedia/commons/b/b4/EUBanana-500x112.jpg',
#         'https://image.slidesharecdn.com/koreanclassificationkeras-190306143336/95/ios-with-keras-9-638.jpg?cb=1551883257',
#         'https://www.pyimagesearch.com/wp-content/uploads/2019/01/ubuntu1804_dl_install_header.jpg'
#     ]
# ]
#
# # Each list of predictions in prediction_groups is a list of (word, box) tuples.
# prediction_groups = pipeline.recognize(images)
#
# # Plot the predictions : 4번(한글), 5번(특수문자) 인식 문제점
# fig, axs = mko.plt.subplots(nrows=len(images), figsize=(20, 20))
# for ax, image, predictions in zip(axs, images, prediction_groups):
#     mko.drawAnnotations(image=image, predictions=predictions, ax=ax)  # mko.tools.drawAnnotations()
# ----------------------------------------------------------------------------------------

### ==================================================================================== #
##  Source Script : https://github.com/faustomorales/keras-ocr/tree/master/keras_ocr    ##
# ==================================================================================== ###

#  data_generation.py
#  datasets.py
#  detection.py
#  evaluation.py
#  pipeline.py
#  recognition.py
#  tools.py

### ==================================================================================== #
##  Google Colab                                                                        ##
# ==================================================================================== ###

# ## !pip install keras-ocr  
# !git clone 'https://github.com/faustomorales/keras-ocr.git'
# !mkdir keras_ocr
# !cp ./keras-ocr/keras_ocr/* keras_ocr
# pip install efficientnet validators essential_generators fontTools pyclipper
# import keras_ocr

### ==================================================================================== #
##  Libraries                                                                           ##
# ==================================================================================== ###

import os
import math
import glob
import typing
import random
import zipfile
import string
import itertools

import cv2
import tqdm
import numpy as np
import essential_generators
import PIL.Image
import PIL.ImageDraw
import PIL.ImageFont
import fontTools.ttLib

# -------------------------------------------------------------------------------------- #
import concurrent
import itertools
import warnings
import json
import imgaug

# -------------------------------------------------------------------------------------- #
import tensorflow as tf
import efficientnet.tfkeras as efficientnet
from tensorflow import keras

# -------------------------------------------------------------------------------------- #
import copy
import editdistance
import pyclipper

# -------------------------------------------------------------------------------------- #

# -------------------------------------------------------------------------------------- #
import io
import hashlib
import urllib.request
import urllib.parse
import validators
import matplotlib.pyplot as plt
from shapely import geometry
from scipy import spatial

### ==================================================================================== #
##  https://github.com/faustomorales/keras-ocr/blob/master/keras_ocr/data_generation.py ##
# ==================================================================================== ###
#
#   _strip_line
#   _strip_lines
#   compute_transformed_contour
#   convert_image_generator_to_recognizer_input     xxx
#   convert_lines_to_paragraph
#   draw_text_image
#   font_supports_alphabet                          Verify that a font contains a specific set of characters.
#   get_backgrounds
#   get_fonts
#   get_image_generator
#   get_maximum_uniform_contour                     Get the largest possible contour of light or dark area in an image
#   get_rotation_matrix                             Provide a rotation matrix about the center of a rectangle with a given width and height.
#   get_text_generator                              Generates strings of sentences using only the letters in alphabet.
#         

LIGATURES = {'\U0000FB01': 'fi', '\U0000FB02': 'fl'}
LIGATURE_STRING = ''.join(LIGATURES.keys())

def get_rotation_matrix(width, height, thetaX=0, thetaY=0, thetaZ=0):
    """Provide a rotation matrix about the center of a rectangle with
    a given width and height.
    Args:
        width: The width of the rectangle
        height: The height of the rectangle
        thetaX: Rotation about the X axis
        thetaY: Rotation about the Y axis
        thetaZ: Rotation about the Z axis
    Returns:
        A 3x3 transformation matrix
    """
    translate1 = np.array([[1, 0, width / 2], [0, 1, height / 2], [0, 0, 1]])
    rotX = np.array([[1, 0, 0], [0, np.cos(thetaX), -np.sin(thetaX)],
                     [0, np.sin(thetaX), np.cos(thetaX)]])
    rotY = np.array([[np.cos(thetaY), 0, np.sin(thetaY)], [0, 1, 0],
                     [-np.sin(thetaY), 0, np.cos(thetaY)]])
    rotZ = np.array([[np.cos(thetaZ), -np.sin(thetaZ), 0], [np.sin(thetaZ),
                                                            np.cos(thetaZ), 0], [0, 0, 1]])
    translate2 = np.array([[1, 0, -width / 2], [0, 1, -height / 2], [0, 0, 1]])
    M = translate1.dot(rotX).dot(rotY).dot(rotZ).dot(translate2)
    return M


def get_maximum_uniform_contour(image, fontsize, margin=0):
    """Get the largest possible contour of light or
    dark area in an image.
    Args:
        image: The image in which to find a contiguous area.
        fontsize: The fontsize for text. Will be used for blurring
            and for determining useful areas.
        margin: The minimum margin required around the image.
    Returns:
        A (contour, isDark) tuple. If no contour is found, both
        entries will be None.
    """
    if margin > 0:
        image = image[margin:-margin, margin:-margin]
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blurred = cv2.blur(src=gray, ksize=(fontsize // 2, fontsize // 2))
    _, threshold = cv2.threshold(src=blurred, thresh=255 / 2, maxval=255, type=cv2.THRESH_BINARY)
    contoursDark = cv2.findContours(255 - threshold,
                                    mode=cv2.RETR_TREE,
                                    method=cv2.CHAIN_APPROX_SIMPLE)[-2]
    contoursLight = cv2.findContours(threshold, mode=cv2.RETR_TREE,
                                     method=cv2.CHAIN_APPROX_SIMPLE)[-2]
    areasDark = list(map(cv2.contourArea, contoursDark))
    areasLight = list(map(cv2.contourArea, contoursLight))
    maxDarkArea = max(areasDark) if areasDark else 0
    maxLightArea = max(areasLight) if areasLight else 0

    if max(maxDarkArea, maxLightArea) < (4 * fontsize)**2:
        return None, None

    contour = None
    isDark = None
    if areasDark and (not areasLight or maxDarkArea >= maxLightArea):
        contour = contoursDark[np.argmax(areasDark)]
        isDark = True
    else:
        contour = contoursLight[np.argmax(areasLight)]
        isDark = False
    if contour is not None:
        contour += margin
    return contour, isDark


def font_supports_alphabet(filepath, alphabet):
    """Verify that a font contains a specific set of characters.
    Args:
        filepath: Path to fsontfile
        alphabet: A string of characters to check for.
    """
    if alphabet == '':
        return True
    font = fontTools.ttLib.TTFont(filepath)
    if not all(any(ord(c) in table.cmap.keys() for table in font['cmap'].tables) for c in alphabet):
        return False
    font = PIL.ImageFont.truetype(filepath)
    try:
        for character in alphabet:
            font.getsize(character)
    # pylint: disable=bare-except
    except:
        return False
    return True


def get_text_generator(alphabet=None, lowercase=False, max_string_length=None):
    """Generates strings of sentences using only the letters in alphabet.
    Args:
        alphabet: The alphabet of permitted characters
        lowercase: Whether to convert all strings to lowercase.
        max_string_length: The maximum length of the string
    """
    gen = essential_generators.DocumentGenerator()
    while True:
        sentence = gen.sentence()
        if lowercase:
            sentence = sentence.lower()
        sentence = ''.join([s for s in sentence if (alphabet is None or s in alphabet)])
        if max_string_length is not None:
            sentence = sentence[:max_string_length]
        yield sentence


def _strip_line(line):
    """Modify a line so that spaces are excluded."""
    first_character_index = next(
        (index for index, (box, character) in enumerate(line) if not character.isspace()), None)
    if first_character_index is None:
        return []
    last_character_index = len(line) - next(
        index for index, (box, character) in enumerate(reversed(line)) if not character.isspace())
    return line[first_character_index:last_character_index]


def _strip_lines(lines):
    """Modify a set of lines so that spaces are excluded."""
    lines = [line for line in lines if len(line) > 0]
    lines = [_strip_line(line) for line in lines]
    lines = [line for line in lines if len(line) > 0]
    return lines


def get_backgrounds(cache_dir=None):
    """Download a set of pre-reviewed backgrounds.
    Args:
        cache_dir: Where to save the dataset. By default, data will be
            saved to ~/.keras-ocr.
    Returns:
        A list of background filepaths.
    """
    if cache_dir is None:
        cache_dir = os.path.expanduser(os.path.join('~', '.keras-ocr'))
    backgrounds_dir = os.path.join(cache_dir, 'backgrounds')
    backgrounds_zip_path = tools.download_and_verify(
        url='https://github.com/faustomorales/keras-ocr/releases/download/v0.8.4/backgrounds.zip',
        sha256='f263ed0d55de303185cc0f93e9fcb0b13104d68ed71af7aaaa8e8c91389db471',
        filename='backgrounds.zip',
        cache_dir=cache_dir)
    if len(glob.glob(os.path.join(backgrounds_dir, '*'))) != 1035:
        with zipfile.ZipFile(backgrounds_zip_path) as zfile:
            zfile.extractall(backgrounds_dir)
    return glob.glob(os.path.join(backgrounds_dir, '*.jpg'))


def get_fonts(cache_dir=None,
              alphabet=string.ascii_letters + string.digits,
              exclude_smallcaps=False):
    """Download a set of pre-reviewed fonts.
    Args:
        cache_dir: Where to save the dataset. By default, data will be
            saved to ~/.keras-ocr.
        alphabet: An alphabet which we will use to exclude fonts
            that are missing relevant characters. By default, this is
            set to `string.ascii_letters + string.digits`.
        exclude_smallcaps: If True, fonts that are known to use
            the same glyph for lowercase and uppercase characters
            are excluded.
    Returns:
        A list of font filepaths.
    """
    if cache_dir is None:
        cache_dir = os.path.expanduser(os.path.join('~', '.keras-ocr'))
    fonts_zip_path = tools.download_and_verify(
        url='https://github.com/faustomorales/keras-ocr/releases/download/v0.8.4/fonts.zip',
        sha256='d4d90c27a9bc4bf8fff1d2c0a00cfb174c7d5d10f60ed29d5f149ef04d45b700',
        filename='fonts.zip',
        cache_dir=cache_dir)
    fonts_dir = os.path.join(cache_dir, 'fonts')
    if len(glob.glob(os.path.join(fonts_dir, '**/*.ttf'))) != 2746:
        print('Unzipping fonts ZIP file.')
        with zipfile.ZipFile(fonts_zip_path) as zfile:
            zfile.extractall(fonts_dir)
    font_filepaths = glob.glob(os.path.join(fonts_dir, '**/*.ttf'))
    if exclude_smallcaps:
        with open(
                tools.download_and_verify(
                    url=
                    'https://github.com/faustomorales/keras-ocr/releases/download/v0.8.4/fonts_smallcaps.txt',
                    sha256='6531c700523c687f02852087530d1ab3c7cc0b59891bbecc77726fbb0aabe68e',
                    filename='fonts_smallcaps.txt',
                    cache_dir=cache_dir), 'r') as f:
            smallcaps_fonts = f.read().split('\n')
            font_filepaths = [
                filepath for filepath in font_filepaths
                if os.path.join(*filepath.split(os.sep)[-2:]) not in smallcaps_fonts
            ]
    if alphabet != '':
        font_filepaths = [
            filepath for filepath in tqdm.tqdm(font_filepaths, desc='Filtering fonts.')
            if font_supports_alphabet(filepath=filepath, alphabet=alphabet)
        ]
    return font_filepaths


def convert_lines_to_paragraph(lines):
    """Convert a series of lines, each consisting of
    (box, character) tuples, into a multi-line string."""
    return '\n'.join([''.join([c[-1] for c in line]) for line in lines])


def convert_image_generator_to_recognizer_input(image_generator,
                                                max_string_length,
                                                target_width,
                                                target_height,
                                                margin=0):
    """Convert an image generator created by get_image_generator
    to (image, sentence) tuples for training a recognizer.
    Args:
        image_generator: An image generator created by get_image_generator
        max_string_length: The maximum string length to allow
        target_width: The width to warp lines into
        target_height: The height to warp lines into
        margin: The margin to apply around a single line.
    """
    while True:
        image, lines = next(image_generator)
        if len(lines) == 0:
            continue
        for line in lines:
            line = _strip_line(line[:max_string_length])
            if not line:
                continue
            box, sentence = tools.combine_line(line)

            # remove multiple sequential spaces
            while "  " in sentence:
                sentence = sentence.replace("  ", " ")

            crop = tools.warpBox(image=image,
                                 box=box,
                                 target_width=target_width,
                                 target_height=target_height,
                                 margin=margin,
                                 skip_rotate=True)
            yield crop, sentence


def draw_text_image(text,
                    fontsize,
                    height,
                    width,
                    fonts,
                    use_ligatures=False,
                    thetaX=0,
                    thetaY=0,
                    thetaZ=0,
                    color=(0, 0, 0),
                    permitted_contour=None,
                    draw_contour=False):
    """Get a transparent image containing text.
    Args:
        text: The text to draw on the image
        fontsize: The size of text to show.
        height: The height of the output image
        width: The width of the output image
        fonts: A dictionary of {subalphabet: paths_to_font}
        thetaX: Rotation about the X axis
        thetaY: Rotation about the Y axis
        thetaZ: Rotation about the Z axis
        color: The color of drawn text
        permitted_contour: A contour defining which part of the image
            we can put text. If None, the entire canvas is permitted
            for text.
        use_ligatures: Whether to render ligatures. If True,
            ligatures are always used (with an initial check for support
            which sometimes yields false positives). If False, ligatures
            are never used.
    Returns:
        An (image, lines) tuple where image is the
        transparent text image and lines is a list of lines
        where each line itself is a list of (box, character) tuples and
        box is an array of points with shape (4, 2) providing the coordinates
        of the character box in clockwise order starting from the top left.
    """
    if not use_ligatures:
        fonts = {
            subalphabet: PIL.ImageFont.truetype(font_path, size=fontsize)
            if font_path is not None else PIL.ImageFont.load_default()
            for subalphabet, font_path in fonts.items()
        }
    if use_ligatures:
        for subalphabet, font_path in fonts.items():
            ligatures_supported = True
            font = PIL.ImageFont.truetype(
                font_path,
                size=fontsize) if font_path is not None else PIL.ImageFont.load_default()
            for ligature in LIGATURES:
                try:
                    font.getsize(ligature)
                except UnicodeEncodeError:
                    ligatures_supported = False
                    break
            if ligatures_supported:
                del fonts[subalphabet]
                subalphabet += LIGATURE_STRING
            fonts[subalphabet] = font
        for insert, search in LIGATURES.items():
            for subalphabet in fonts.keys()():
                if insert in subalphabet:
                    text = text.replace(search, insert)
    character_font_pairs = [(character,
                             next(font for subalphabet, font in fonts.items()
                                  if character in subalphabet)) for character in text]
    M = get_rotation_matrix(width=width, height=height, thetaZ=thetaZ, thetaX=thetaX, thetaY=thetaY)
    if permitted_contour is None:
        permitted_contour = np.array([[0, 0], [width, 0], [width, height],
                                      [0, height]]).astype('float32')
    character_sizes = np.array(
        [font.font.getsize(character) for character, font in character_font_pairs])
    min_character_size = character_sizes.sum(axis=1).min()
    transformed_contour = compute_transformed_contour(width=width,
                                                      height=height,
                                                      fontsize=max(min_character_size, 1),
                                                      M=M,
                                                      contour=permitted_contour)
    start_x = transformed_contour[:, 0].min()
    start_y = transformed_contour[:, 1].min()
    end_x = transformed_contour[:, 0].max()
    end_y = transformed_contour[:, 1].max()
    image = PIL.Image.new(mode='RGBA', size=(width, height), color=(255, 255, 255, 0))
    draw = PIL.ImageDraw.Draw(image)
    lines = [[]]
    x = start_x
    y = start_y
    max_y = start_y
    out_of_space = False
    for character_index, (character, font) in enumerate(character_font_pairs):
        if out_of_space:
            break
        (character_width, character_height), (offset_x, offset_y) = character_sizes[character_index]
        if character in LIGATURES:
            subcharacters = LIGATURES[character]
            dx = character_width / len(subcharacters)
        else:
            subcharacters = character
            dx = character_width
        x2, y2 = (x + character_width + offset_x, y + character_height + offset_y)
        while not all(
                cv2.pointPolygonTest(contour=transformed_contour, pt=pt, measureDist=False) >= 0
                for pt in [(x, y), (x2, y), (x2, y2), (x, y2)]):
            if x2 > end_x:
                dy = max(1, max_y - y)
                if y + dy > end_y:
                    out_of_space = True
                    break
                y += dy
                x = start_x
            else:
                x += fontsize
            if len(lines[-1]) > 0:
                # We add a new line whether we have advanced
                # in the y-direction or not because we also want to separate
                # horizontal segments of text.
                lines.append([])
            x2, y2 = (x + character_width + offset_x, y + character_height + offset_y)
        if out_of_space:
            break
        max_y = max(y + character_height + offset_y, max_y)
        draw.text(xy=(x, y), text=character, fill=color + (255, ), font=font)
        for subcharacter in subcharacters:
            lines[-1].append((np.array([[x + offset_x, y + offset_y],
                                        [x + dx + offset_x, y + offset_y], [x + dx + offset_x, y2],
                                        [x + offset_x, y2]]).astype('float32'), subcharacter))
            x += dx
    image = cv2.warpPerspective(src=np.array(image), M=M, dsize=(width, height))
    if draw_contour:
        image = cv2.drawContours(image,
                                 contours=[permitted_contour.reshape((-1, 1, 2)).astype('int32')],
                                 contourIdx=0,
                                 color=(255, 0, 0, 255),
                                 thickness=int(width / 100))
    lines = _strip_lines(lines)
    lines = [[(cv2.perspectiveTransform(src=coords[np.newaxis], m=M)[0], character)
              for coords, character in line] for line in lines]
    return image, lines


def compute_transformed_contour(width, height, fontsize, M, contour, minarea=0.5):
    """Compute the permitted drawing contour
    on a padded canvas for an image of a given size.
    We assume the canvas is padded with one full image width
    and height on left and right, top and bottom respectively.
    Args:
        width: Width of image
        height: Height of image
        fontsize: Size of characters
        M: The transformation matrix
        contour: The contour to which we are limited inside
            the rectangle of size width / height
        minarea: The minimum area required for a character
            slot to qualify as being visible, expressed as
            a fraction of the untransformed fontsize x fontsize
            slot.
    """
    spacing = math.ceil(fontsize / 2)
    xslots = int(np.floor(width / spacing))
    yslots = int(np.floor(height / spacing))
    ys, xs = np.mgrid[:yslots, :xslots]
    basis = np.concatenate([xs[..., np.newaxis], ys[..., np.newaxis]], axis=-1).reshape((-1, 2))
    basis *= spacing
    slots_pretransform = np.concatenate(
        [(basis + offset)[:, np.newaxis, :]
         for offset in [[0, 0], [spacing, 0], [spacing, spacing], [0, spacing]]],
        axis=1)
    slots = cv2.perspectiveTransform(src=slots_pretransform.reshape((1, -1, 2)).astype('float32'),
                                     m=M)[0]
    inside = np.array([
        cv2.pointPolygonTest(contour=contour, pt=(x, y), measureDist=False) >= 0 for x, y in slots
    ]).reshape(-1, 4).all(axis=1)
    slots = slots.reshape(-1, 4, 2)
    areas = np.abs((slots[:, 0, 0] * slots[:, 1, 1] - slots[:, 0, 1] * slots[:, 1, 0]) +
                   (slots[:, 1, 0] * slots[:, 2, 1] - slots[:, 1, 1] * slots[:, 2, 0]) +
                   (slots[:, 2, 0] * slots[:, 3, 1] - slots[:, 2, 1] * slots[:, 3, 0]) +
                   (slots[:, 3, 0] * slots[:, 0, 1] - slots[:, 3, 1] * slots[:, 0, 0])) / 2
    slots_filtered = slots_pretransform[(areas > minarea * spacing * spacing) & inside]
    temporary_image = cv2.drawContours(image=np.zeros((height, width), dtype='uint8'),
                                       contours=slots_filtered,
                                       contourIdx=-1,
                                       color=255)
    temporary_image = cv2.dilate(src=temporary_image, kernel=np.ones((spacing, spacing)))
    newContours, _ = cv2.findContours(temporary_image,
                                      mode=cv2.RETR_TREE,
                                      method=cv2.CHAIN_APPROX_SIMPLE)
    x, y = slots_filtered[0][0]
    contour = newContours[next(
        index for index, contour in enumerate(newContours)
        if cv2.pointPolygonTest(contour=contour, pt=(x, y), measureDist=False) >= 0)][:, 0, :]
    return contour


def get_image_generator(height,
                        width,
                        font_groups,
                        text_generator,
                        font_size: typing.Union[int, typing.Tuple[int, int]] = 18,
                        backgrounds: typing.List[typing.Union[str, np.ndarray]] = None,
                        background_crop_mode='crop',
                        rotationX: typing.Union[int, typing.Tuple[int, int]] = 0,
                        rotationY: typing.Union[int, typing.Tuple[int, int]] = 0,
                        rotationZ: typing.Union[int, typing.Tuple[int, int]] = 0,
                        margin=0,
                        use_ligatures=False,
                        augmenter=None,
                        draw_contour=False,
                        draw_contour_text=False):
    """Create a generator for images containing text.
    Args:
        height: The height of the generated image
        width: The width of the generated image.
        font_groups: A dict mapping of { subalphabet: [path_to_font1, path_to_font2] }.
        text_generator: See get_text_generator
        font_size: The font size to use. Alternative, supply a tuple
            and the font size will be randomly selected between
            the two values.
        backgrounds: A list of paths to image backgrounds or actual images
            as numpy arrays with channels in RGB order.
        background_crop_mode: One of letterbox or crop, indicates
            how backgrounds will be resized to fit on the canvas.
        rotationX: The X-axis text rotation to use. Alternative, supply a tuple
            and the rotation will be randomly selected between
            the two values.
        rotationY: The Y-axis text rotation to use. Alternative, supply a tuple
            and the rotation will be randomly selected between
            the two values.
        rotationZ: The Z-axis text rotation to use. Alternative, supply a tuple
            and the rotation will be randomly selected between
            the two values.
        margin: The minimum margin around the edge of the image.
        use_ligatures: Whether to render ligatures (see `draw_text_image`)
        augmenter: An image augmenter to be applied to backgrounds
        draw_contour: Draw the permitted contour onto images (debugging only)
        draw_contour_text: Draw the permitted contour inside the text
            drawing function.
    Yields:
        Tuples of (image, lines) where image is the
        transparent text image and lines is a list of lines
        where each line itself is a list of (box, character) tuples and
        box is an array of points with shape (4, 2) providing the coordinates
        of the character box in clockwise order starting from the top left.
    """
    if backgrounds is None:
        backgrounds = [np.zeros((height, width, 3), dtype='uint8')]
    alphabet = ''.join(font_groups.keys())
    assert len(set(alphabet)) == len(
        alphabet), 'Each character can appear in the subalphabet for only one font group.'
    for text, background_index, current_font_groups in zip(
            text_generator, itertools.cycle(range(len(backgrounds))),
            zip(*[
                itertools.cycle([(subalphabet, font_filepath)
                                 for font_filepath in font_group_filepaths])
                for subalphabet, font_group_filepaths in font_groups.items()
            ])):
        if background_index == 0:
            random.shuffle(backgrounds)
        current_font_groups = dict(current_font_groups)
        current_font_size = np.random.randint(low=font_size[0], high=font_size[1]) if isinstance(
            font_size, tuple) else font_size
        current_rotation_X, current_rotation_Y, current_rotation_Z = [
            (np.random.uniform(low=rotation[0], high=rotation[1])
             if isinstance(rotation, tuple) else rotation) * np.pi / 180
            for rotation in [rotationX, rotationY, rotationZ]
        ]
        current_background_filepath_or_array = backgrounds[background_index]
        current_background = tools.read(current_background_filepath_or_array) if isinstance(
            current_background_filepath_or_array, str) else current_background_filepath_or_array
        if augmenter is not None:
            current_background = augmenter(images=[current_background])[0]
        if current_background.shape[0] != height or current_background.shape[1] != width:
            current_background = tools.fit(current_background,
                                           width=width,
                                           height=height,
                                           mode=background_crop_mode)
        permitted_contour, isDark = get_maximum_uniform_contour(image=current_background,
                                                                fontsize=current_font_size,
                                                                margin=margin)
        if permitted_contour is None:
            # We can't draw on this background. Boo!
            continue
        random_color_values = np.random.randint(low=0, high=50, size=3)
        text_color = tuple(np.array([255, 255, 255]) -
                           random_color_values) if isDark else tuple(random_color_values)
        text_image, lines = draw_text_image(text=text,
                                            width=width,
                                            height=height,
                                            fontsize=current_font_size,
                                            fonts=current_font_groups,
                                            thetaX=current_rotation_X,
                                            thetaY=current_rotation_Y,
                                            thetaZ=current_rotation_Z,
                                            use_ligatures=use_ligatures,
                                            permitted_contour=permitted_contour,
                                            color=text_color,
                                            draw_contour=draw_contour_text)
        alpha = text_image[..., -1:].astype('float32') / 255
        image = (alpha * text_image[..., :3] + (1 - alpha) * current_background).astype('uint8')
        if draw_contour:
            image = cv2.drawContours(
                image,
                contours=[permitted_contour.reshape((-1, 1, 2)).astype('int32')],
                contourIdx=0,
                color=(255, 0, 0),
                thickness=int(width / 100))
        yield image, lines

### ==================================================================================== #
##  https://github.com/faustomorales/keras-ocr/blob/master/keras_ocr/datasets.py        ##
# ==================================================================================== ###

def _read_born_digital_labels_file(labels_filepath, image_folder):
    """Read a labels file and return (filepath, label) tuples.
    Args:
        labels_filepath: Path to labels file
        image_folder: Path to folder containing images
    """
    with open(labels_filepath, encoding='utf-8-sig') as f:
        labels = [l.strip().split(',') for l in f.readlines()]
        labels = [(os.path.join(image_folder,
                                segments[0]), None, ','.join(segments[1:]).strip()[1:-1])
                  for segments in labels]
    return labels


def get_cocotext_recognizer_dataset(split='train',
                                    cache_dir=None,
                                    limit=None,
                                    legible_only=False,
                                    english_only=False,
                                    return_raw_labels=False):
    """Get a list of (filepath, box, word) tuples from the
    COCO-Text dataset.
    Args:
        split: Which split to get (train, val, or trainval)
        limit: Limit the number of files included in the download
        cache_dir: The directory in which to cache the file. The default is
            `~/.keras-ocr`.
        return_raw_labels: Whether to return the raw labels object
    Returns:
        A recognition dataset as a list of (filepath, box, word) tuples.
        If return_raw_labels is True, you will also get a (labels, images_dir)
        tuple containing the raw COCO data and the directory in which you
        can find the images.
    """
    assert split in ['train', 'val', 'trainval'], f'Unsupported split: {split}'
    if cache_dir is None:
        cache_dir = tools.get_default_cache_dir()
    main_dir = os.path.join(cache_dir, 'coco-text')
    images_dir = os.path.join(main_dir, 'images')
    labels_zip = tools.download_and_verify(
        url='https://github.com/bgshih/cocotext/releases/download/dl/cocotext.v2.zip',
        cache_dir=main_dir,
        sha256='1444893ce7dbcd8419b2ec9be6beb0dba9cf8a43bf36cab4293d5ba6cecb7fb1')
    with zipfile.ZipFile(labels_zip) as z:
        with z.open('cocotext.v2.json') as f:
            labels = json.loads(f.read())
    selected_ids = [cocoid for cocoid, data in labels['imgs'].items() if data['set'] in split]
    if limit:
        flatten = lambda l: [item for sublist in l for item in sublist]
        selected_ids = selected_ids[:limit]
        labels['imgToAnns'] = {k: v for k, v in labels['imgToAnns'].items() if k in selected_ids}
        labels['imgs'] = {k: v for k, v in labels['imgs'].items() if k in selected_ids}
        anns = set(flatten(list(labels.values())))
        labels['anns'] = {k: v for k, v in labels['anns'].items() if k in anns}
    selected_filenames = [labels['imgs'][cocoid]['file_name'] for cocoid in selected_ids]
    with concurrent.futures.ThreadPoolExecutor() as executor:
        for future in tqdm.tqdm(concurrent.futures.as_completed([
                executor.submit(tools.download_and_verify,
                                url=f'http://images.cocodataset.org/train2014/{filename}',
                                cache_dir=images_dir,
                                verbose=False) for filename in selected_filenames
        ]),
                                total=len(selected_filenames),
                                desc='Downloading images'):
            _ = future.result()
    dataset = []
    for selected_id in selected_ids:
        filepath = os.path.join(images_dir, selected_filenames[selected_ids.index(selected_id)])
        for annIdx in labels['imgToAnns'][selected_id]:
            ann = labels['anns'][str(annIdx)]
            if english_only and ann['language'] != 'english':
                continue
            if legible_only and ann['legibility'] != 'legible':
                continue
            dataset.append((filepath, np.array(ann['mask']).reshape(-1, 2), ann['utf8_string']))
    if return_raw_labels:
        return dataset, (labels, images_dir)
    return dataset


def get_born_digital_recognizer_dataset(split='train', cache_dir=None):
    """Get a list of (filepath, box, word) tuples from the
    BornDigital dataset. This dataset comes pre-cropped so
    `box` is always `None`.
    Args:
        split: Which split to get (train, test, or traintest)
        cache_dir: The directory in which to cache the file. The default is
            `~/.keras-ocr`.
    Returns:
        A recognition dataset as a list of (filepath, box, word) tuples
    """
    data = []
    if cache_dir is None:
        cache_dir = tools.get_default_cache_dir()
    main_dir = os.path.join(cache_dir, 'borndigital')
    assert split in ['train', 'traintest', 'test'], f'Unsupported split: {split}'
    if split in ['train', 'traintest']:
        train_dir = os.path.join(main_dir, 'train')
        training_zip_path = tools.download_and_verify(
            url=
            'https://github.com/faustomorales/keras-ocr/releases/download/v0.8.4/Challenge1_Training_Task3_Images_GT.zip',  # pylint: disable=line-too-long
            filename='Challenge1_Training_Task3_Images_GT.zip',
            cache_dir=main_dir,
            sha256='8ede0639f5a8031d584afd98cee893d1c5275d7f17863afc2cba24b13c932b07')
        if len(
                glob.glob(os.path.join(train_dir, '*.png')) +
                glob.glob(os.path.join(train_dir, '*.txt'))) != 3568:
            with zipfile.ZipFile(training_zip_path) as zfile:
                zfile.extractall(train_dir)
        data.extend(
            _read_born_digital_labels_file(labels_filepath=os.path.join(train_dir, 'gt.txt'),
                                           image_folder=train_dir))
    if split in ['test', 'traintest']:
        test_dir = os.path.join(main_dir, 'test')
        test_zip_path = tools.download_and_verify(
            url=
            'https://github.com/faustomorales/keras-ocr/releases/download/v0.8.4/Challenge1_Test_Task3_Images.zip',
            filename='Challenge1_Test_Task3_Images.zip',
            cache_dir=main_dir,
            sha256='8f781b0140fd0bac3750530f0924bce5db3341fd314a2fcbe9e0b6ca409a77f0')
        if len(glob.glob(os.path.join(test_dir, '*.png'))) != 1439:
            with zipfile.ZipFile(test_zip_path) as zfile:
                zfile.extractall(test_dir)
        test_gt_path = tools.download_and_verify(
            url=
            'https://github.com/faustomorales/keras-ocr/releases/download/v0.8.4/Challenge1_Test_Task3_GT.txt',
            cache_dir=test_dir,
            filename='Challenge1_Test_Task3_GT.txt',
            sha256='fce7f1228b7c4c26a59f13f562085148acf063d6690ce51afc395e0a1aabf8be')
        data.extend(
            _read_born_digital_labels_file(labels_filepath=test_gt_path, image_folder=test_dir))
    return data


def get_icdar_2013_recognizer_dataset(cache_dir=None):
    """Get a list of (filepath, box, word) tuples from the
    ICDAR 2013 dataset.
    Args:
        cache_dir: The directory in which to cache the file. The default is
            `~/.keras-ocr`.
    Returns:
        A recognition dataset as a list of (filepath, box, word) tuples
    """
    dataset = []
    for image_path, lines, _ in get_icdar_2013_detector_dataset(cache_dir=cache_dir,
                                                                skip_illegible=True):
        for line in lines:
            box, text = tools.combine_line(line)
            dataset.append((image_path, box, text))
    return dataset


def get_icdar_2013_detector_dataset(cache_dir=None, skip_illegible=False):
    """Get the ICDAR 2013 text segmentation dataset for detector
    training. Only the training set has the necessary annotations.
    For the test set, only segmentation maps are provided, which
    do not provide the necessary information for affinity scores.
    Args:
        cache_dir: The directory in which to store the data.
        skip_illegible: Whether to skip illegible characters.
    Returns:
        Lists of (image_path, lines, confidence) tuples. Confidence
        is always 1 for this dataset. We record confidence to allow
        for future support for weakly supervised cases.
    """
    if cache_dir is None:
        cache_dir = tools.get_default_cache_dir()
    main_dir = os.path.join(cache_dir, 'icdar2013')
    training_images_dir = os.path.join(main_dir, 'Challenge2_Training_Task12_Images')
    training_zip_images_path = tools.download_and_verify(
        url=
        'https://github.com/faustomorales/keras-ocr/releases/download/v0.8.4/Challenge2_Training_Task12_Images.zip',  # pylint: disable=line-too-long
        cache_dir=main_dir,
        filename='Challenge2_Training_Task12_Images.zip',
        sha256='7a57d1699fbb92db3ad82c930202938562edaf72e1c422ddd923860d8ace8ded')
    if len(glob.glob(os.path.join(training_images_dir, '*.jpg'))) != 229:
        with zipfile.ZipFile(training_zip_images_path) as zfile:
            zfile.extractall(training_images_dir)
    training_gt_dir = os.path.join(main_dir, 'Challenge2_Training_Task2_GT')
    training_zip_gt_path = tools.download_and_verify(
        url=
        'https://github.com/faustomorales/keras-ocr/releases/download/v0.8.4/Challenge2_Training_Task2_GT.zip',  # pylint: disable=line-too-long
        cache_dir=main_dir,
        filename='Challenge2_Training_Task2_GT.zip',
        sha256='4cedd5b1e33dc4354058f5967221ac85dbdf91a99b30f3ab1ecdf42786a9d027')
    if len(glob.glob(os.path.join(training_gt_dir, '*.txt'))) != 229:
        with zipfile.ZipFile(training_zip_gt_path) as zfile:
            zfile.extractall(training_gt_dir)

    dataset = []
    for gt_filepath in glob.glob(os.path.join(training_gt_dir, '*.txt')):
        image_id = os.path.split(gt_filepath)[1].split('_')[0]
        image_path = os.path.join(training_images_dir, image_id + '.jpg')
        lines = []
        with open(gt_filepath, 'r') as f:
            current_line = []
            for row in f.read().split('\n'):
                if row == '':
                    lines.append(current_line)
                    current_line = []
                else:
                    row = row.split(' ')[5:]
                    character = row[-1][1:-1]
                    if character == '' and skip_illegible:
                        continue
                    x1, y1, x2, y2 = map(int, row[:4])
                    current_line.append((np.array([[x1, y1], [x2, y1], [x2, y2], [x1,
                                                                                  y2]]), character))
        # Some lines only have illegible characters and if skip_illegible is True,
        # then these lines will be blank.
        lines = [line for line in lines if line]
        dataset.append((image_path, lines, 1))
    return dataset


def get_icdar_2019_semisupervised_dataset(cache_dir=None):
    """EXPERIMENTAL. Get a semisupervised labeled version
    of the ICDAR 2019 dataset. Only images with Latin-only
    scripts are available at this time.
    Args:
        cache_dir: The cache directory to use.
    """
    warnings.warn(
        "You may need to get this dataset manually in-browser by downloading "
        "https://www.mediafire.com/file/snekaezeextc3ee/ImagesPart1.zip/file "
        "and https://www.mediafire.com/file/i2snljkfm4t2ojm/ImagesPart2.zip/file "
        "and putting them in ~/.keras-ocr/icdar2019. The files are too big "
        "for GitHub Releases and we may run out of direct download  bandwidth on "
        "MediaFire where they are hosted. See "
        "https://github.com/faustomorales/keras-ocr/issues/117 for more details.", UserWarning)
    if cache_dir is None:
        cache_dir = tools.get_default_cache_dir()
    main_dir = os.path.join(cache_dir, 'icdar2019')
    training_dir_1 = os.path.join(main_dir, 'ImagesPart1')
    training_dir_2 = os.path.join(main_dir, 'ImagesPart2')
    if len(glob.glob(os.path.join(training_dir_1, '*'))) != 5000:
        training_zip_1 = tools.download_and_verify(
            url='https://www.mediafire.com/file/snekaezeextc3ee/ImagesPart1.zip/file',  # pylint: disable=line-too-long
            cache_dir=main_dir,
            filename='ImagesPart1.zip',
            sha256='1968894ef93b97f3ef4c97880b6dce85b1851f4d778e253f4e7265b152a4986f')
        with zipfile.ZipFile(training_zip_1) as zfile:
            zfile.extractall(main_dir)
    if len(glob.glob(os.path.join(training_dir_2, '*'))) != 5000:
        training_zip_2 = tools.download_and_verify(
            url='https://www.mediafire.com/file/i2snljkfm4t2ojm/ImagesPart2.zip/file',  # pylint: disable=line-too-long
            cache_dir=main_dir,
            filename='ImagesPart2.zip',
            sha256='5651b9137e877f731bfebb2a8b75042e26baa389d2fb1cfdbb9e3da343757241')
        with zipfile.ZipFile(training_zip_2) as zfile:
            zfile.extractall(main_dir)
    ground_truth = tools.download_and_verify(
        url=
        'https://github.com/faustomorales/keras-ocr/releases/download/v0.8.4/mlt2019_dataset.json',  # pylint: disable=line-too-long
        cache_dir=main_dir,
        filename='mlt2019_dataset.json')
    with open(ground_truth, 'r') as f:
        character_level_dataset = json.loads(f.read())['dataset']
    for gif_filepath in glob.glob(os.path.join(main_dir, '**', '*.gif')):
        # We need to do this because we cannot easily read GIFs.
        PIL.Image.open(gif_filepath).convert('RGB').save(os.path.splitext(gif_filepath)[0] + '.jpg')
        os.remove(gif_filepath)
    return [(os.path.join(main_dir,
                          entry['filepath']), [[(np.array(box).clip(0, np.inf), None)
                                                for box in line['line']] for line in entry['lines']
                                               if line['line']], entry['percent_complete'])
            for entry in character_level_dataset if entry['percent_complete'] > 0.5]


def get_detector_image_generator(labels,
                                 width,
                                 height,
                                 augmenter=None,
                                 area_threshold=0.5,
                                 focused=False,
                                 min_area=None):
    """Generated augmented (image, lines) tuples from a list
    of (filepath, lines, confidence) tuples. Confidence is
    not used right now but is included for a future release
    that uses semi-supervised data.
    Args:
        labels: A list of (image, lines, confience) tuples.
        augmenter: An augmenter to apply to the images.
        width: The width to use for output images
        height: The height to use for output images
        area_threshold: The area threshold to use to keep
            characters in augmented images.
        min_area: The minimum area for a character to be
            included.
        focused: Whether to pre-crop images to width/height containing
            a region containing text.
    """
    labels = labels.copy()
    for index in itertools.cycle(range(len(labels))):
        if index == 0:
            random.shuffle(labels)
        image_filepath, lines, confidence = labels[index]
        image = tools.read(image_filepath)
        if augmenter is not None:
            image, lines = tools.augment(boxes=lines,
                                         boxes_format='lines',
                                         image=image,
                                         area_threshold=area_threshold,
                                         min_area=min_area,
                                         augmenter=augmenter)
        if focused:
            boxes = [tools.combine_line(line)[0] for line in lines]
            if boxes:
                selected = np.array(boxes[np.random.choice(len(boxes))])
                left, top = selected.min(axis=0).clip(0, np.inf).astype('int')
                if left > 0:
                    left -= np.random.randint(0, min(left, width / 2))
                if top > 0:
                    top -= np.random.randint(0, min(top, height / 2))
                image, lines = tools.augment(
                    boxes=lines,
                    augmenter=imgaug.augmenters.Sequential([
                        imgaug.augmenters.Crop(px=(int(top), 0, 0, int(left))),
                        imgaug.augmenters.CropToFixedSize(width=width,
                                                          height=height,
                                                          position='right-bottom')
                    ]),
                    boxes_format='lines',
                    image=image,
                    min_area=min_area,
                    area_threshold=area_threshold)
        image, scale = tools.fit(image,
                                 width=width,
                                 height=height,
                                 mode='letterbox',
                                 return_scale=True)
        lines = tools.adjust_boxes(boxes=lines, boxes_format='lines', scale=scale)
        yield image, lines, confidence


def get_recognizer_image_generator(labels, height, width, alphabet, augmenter=None):
    """Generate augmented (image, text) tuples from a list
    of (filepath, box, label) tuples.
    Args:
        labels: A list of (filepath, box, label) tuples
        height: The height of the images to return
        width: The width of the images to return
        alphabet: The alphabet which limits the characters returned
        augmenter: The augmenter to apply to images
    """
    n_with_illegal_characters = sum(any(c not in alphabet for c in text) for _, _, text in labels)
    if n_with_illegal_characters > 0:
        print(f'{n_with_illegal_characters} / {len(labels)} instances have illegal characters.')
    labels = labels.copy()
    for index in itertools.cycle(range(len(labels))):
        if index == 0:
            random.shuffle(labels)
        filepath, box, text = labels[index]
        cval = cval = np.random.randint(low=0, high=255, size=3).astype('uint8')
        if box is not None:
            image = tools.warpBox(image=tools.read(filepath),
                                  box=box.astype('float32'),
                                  target_height=height,
                                  target_width=width,
                                  cval=cval)
        else:
            image = tools.read_and_fit(filepath_or_array=filepath,
                                       width=width,
                                       height=height,
                                       cval=cval)
        text = ''.join([c for c in text if c in alphabet])
        if not text:
            continue
        if augmenter:
            image = augmenter.augment_image(image)
        yield (image, text)

### ==================================================================================== #
##  https://github.com/faustomorales/keras-ocr/blob/master/keras_ocr/detection.py       ##
# ==================================================================================== ###

# The PyTorch portions of this code are subject to the following copyright notice.
# Copyright (c) 2019-present NAVER Corp.

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.  IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

def compute_input(image):
    # should be RGB order
    image = image.astype('float32')
    mean = np.array([0.485, 0.456, 0.406])
    variance = np.array([0.229, 0.224, 0.225])

    image -= mean * 255
    image /= variance * 255
    return image


def invert_input(X):
    X = X.copy()
    mean = np.array([0.485, 0.456, 0.406])
    variance = np.array([0.229, 0.224, 0.225])

    X *= variance * 255
    X += mean * 255
    return X.clip(0, 255).astype('uint8')


def get_gaussian_heatmap(size=512, distanceRatio=3.34):
    v = np.abs(np.linspace(-size / 2, size / 2, num=size))
    x, y = np.meshgrid(v, v)
    g = np.sqrt(x**2 + y**2)
    g *= distanceRatio / (size / 2)
    g = np.exp(-(1 / 2) * (g**2))
    g *= 255
    return g.clip(0, 255).astype('uint8')


def upconv(x, n, filters):
    x = keras.layers.Conv2D(filters=filters, kernel_size=1, strides=1, name=f'upconv{n}.conv.0')(x)
    x = keras.layers.BatchNormalization(epsilon=1e-5, momentum=0.9, name=f'upconv{n}.conv.1')(x)
    x = keras.layers.Activation('relu', name=f'upconv{n}.conv.2')(x)
    x = keras.layers.Conv2D(filters=filters // 2,
                            kernel_size=3,
                            strides=1,
                            padding='same',
                            name=f'upconv{n}.conv.3')(x)
    x = keras.layers.BatchNormalization(epsilon=1e-5, momentum=0.9, name=f'upconv{n}.conv.4')(x)
    x = keras.layers.Activation('relu', name=f'upconv{n}.conv.5')(x)
    return x


def make_vgg_block(x, filters, n, prefix, pooling=True):
    x = keras.layers.Conv2D(filters=filters,
                            strides=(1, 1),
                            kernel_size=(3, 3),
                            padding='same',
                            name=f'{prefix}.{n}')(x)
    x = keras.layers.BatchNormalization(momentum=0.1, epsilon=1e-5, axis=-1,
                                        name=f'{prefix}.{n+1}')(x)
    x = keras.layers.Activation('relu', name=f'{prefix}.{n+2}')(x)
    if pooling:
        x = keras.layers.MaxPooling2D(pool_size=(2, 2),
                                      padding='valid',
                                      strides=(2, 2),
                                      name=f'{prefix}.{n+3}')(x)
    return x


def compute_maps(heatmap, image_height, image_width, lines):
    assert image_height % 2 == 0, 'Height must be an even number'
    assert image_width % 2 == 0, 'Width must be an even number'

    textmap = np.zeros((image_height // 2, image_width // 2)).astype('float32')
    linkmap = np.zeros((image_height // 2, image_width // 2)).astype('float32')

    src = np.array([[0, 0], [heatmap.shape[1], 0], [heatmap.shape[1], heatmap.shape[0]],
                    [0, heatmap.shape[0]]]).astype('float32')

    for line in lines:
        line, orientation = tools.fix_line(line)
        previous_link_points = None
        for [(x1, y1), (x2, y2), (x3, y3), (x4, y4)], c in line:
            x1, y1, x2, y2, x3, y3, x4, y4 = map(lambda v: max(v, 0),
                                                 [x1, y1, x2, y2, x3, y3, x4, y4])
            if c == ' ':
                previous_link_points = None
                continue
            yc = (y4 + y1 + y3 + y2) / 4
            xc = (x1 + x2 + x3 + x4) / 4
            if orientation == 'horizontal':
                current_link_points = np.array([[
                    (xc + (x1 + x2) / 2) / 2, (yc + (y1 + y2) / 2) / 2
                ], [(xc + (x3 + x4) / 2) / 2, (yc + (y3 + y4) / 2) / 2]]) / 2
            else:
                current_link_points = np.array([[
                    (xc + (x1 + x4) / 2) / 2, (yc + (y1 + y4) / 2) / 2
                ], [(xc + (x2 + x3) / 2) / 2, (yc + (y2 + y3) / 2) / 2]]) / 2
            character_points = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]
                                         ]).astype('float32') / 2
            # pylint: disable=unsubscriptable-object
            if previous_link_points is not None:
                if orientation == 'horizontal':
                    link_points = np.array([
                        previous_link_points[0], current_link_points[0], current_link_points[1],
                        previous_link_points[1]
                    ])
                else:
                    link_points = np.array([
                        previous_link_points[0], previous_link_points[1], current_link_points[1],
                        current_link_points[0]
                    ])
                ML = cv2.getPerspectiveTransform(
                    src=src,
                    dst=link_points.astype('float32'),
                )
                linkmap += cv2.warpPerspective(heatmap,
                                               ML,
                                               dsize=(linkmap.shape[1],
                                                      linkmap.shape[0])).astype('float32')
            MA = cv2.getPerspectiveTransform(
                src=src,
                dst=character_points,
            )
            textmap += cv2.warpPerspective(heatmap, MA, dsize=(textmap.shape[1],
                                                               textmap.shape[0])).astype('float32')
            # pylint: enable=unsubscriptable-object
            previous_link_points = current_link_points
    return np.concatenate([textmap[..., np.newaxis], linkmap[..., np.newaxis]], axis=2).clip(
        0, 255) / 255


def map_to_rgb(y):
    return (np.concatenate([y, np.zeros(
        (y.shape[0], y.shape[1], 1))], axis=-1) * 255).astype('uint8')


def getBoxes(y_pred,
             detection_threshold=0.7,
             text_threshold=0.4,
             link_threshold=0.4,
             size_threshold=10):
    box_groups = []
    for y_pred_cur in y_pred:
        # Prepare data
        textmap = y_pred_cur[..., 0].copy()
        linkmap = y_pred_cur[..., 1].copy()
        img_h, img_w = textmap.shape

        _, text_score = cv2.threshold(textmap,
                                      thresh=text_threshold,
                                      maxval=1,
                                      type=cv2.THRESH_BINARY)
        _, link_score = cv2.threshold(linkmap,
                                      thresh=link_threshold,
                                      maxval=1,
                                      type=cv2.THRESH_BINARY)
        n_components, labels, stats, _ = cv2.connectedComponentsWithStats(np.clip(
            text_score + link_score, 0, 1).astype('uint8'),
                                                                          connectivity=4)
        boxes = []
        for component_id in range(1, n_components):
            # Filter by size
            size = stats[component_id, cv2.CC_STAT_AREA]

            if size < size_threshold:
                continue

            # If the maximum value within this connected component is less than
            # text threshold, we skip it.
            if np.max(textmap[labels == component_id]) < detection_threshold:
                continue

            # Make segmentation map. It is 255 where we find text, 0 otherwise.
            segmap = np.zeros_like(textmap)
            segmap[labels == component_id] = 255
            segmap[np.logical_and(link_score, text_score)] = 0
            x, y, w, h = [
                stats[component_id, key] for key in
                [cv2.CC_STAT_LEFT, cv2.CC_STAT_TOP, cv2.CC_STAT_WIDTH, cv2.CC_STAT_HEIGHT]
            ]

            # Expand the elements of the segmentation map
            niter = int(np.sqrt(size * min(w, h) / (w * h)) * 2)
            sx, sy = max(x - niter, 0), max(y - niter, 0)
            ex, ey = min(x + w + niter + 1, img_w), min(y + h + niter + 1, img_h)
            segmap[sy:ey, sx:ex] = cv2.dilate(
                segmap[sy:ey, sx:ex],
                cv2.getStructuringElement(cv2.MORPH_RECT, (1 + niter, 1 + niter)))

            # Make rotated box from contour
            contours = cv2.findContours(segmap.astype('uint8'),
                                        mode=cv2.RETR_TREE,
                                        method=cv2.CHAIN_APPROX_SIMPLE)[-2]
            contour = contours[0]
            box = cv2.boxPoints(cv2.minAreaRect(contour))

            # Check to see if we have a diamond
            w, h = np.linalg.norm(box[0] - box[1]), np.linalg.norm(box[1] - box[2])
            box_ratio = max(w, h) / (min(w, h) + 1e-5)
            if abs(1 - box_ratio) <= 0.1:
                l, r = contour[:, 0, 0].min(), contour[:, 0, 0].max()
                t, b = contour[:, 0, 1].min(), contour[:, 0, 1].max()
                box = np.array([[l, t], [r, t], [r, b], [l, b]], dtype=np.float32)
            else:
                # Make clock-wise order
                box = np.array(np.roll(box, 4 - box.sum(axis=1).argmin(), 0))
            boxes.append(2 * box)
        box_groups.append(np.array(boxes))
    return box_groups


class UpsampleLike(keras.layers.Layer):
    """ Keras layer for upsampling a Tensor to be the same shape as another Tensor.
    """

    # pylint:disable=unused-argument
    def call(self, inputs, **kwargs):
        source, target = inputs
        target_shape = keras.backend.shape(target)
        if keras.backend.image_data_format() == 'channels_first':
            raise NotImplementedError
        else:
            # pylint: disable=no-member
            return tf.compat.v1.image.resize_bilinear(source,
                                                      size=(target_shape[1], target_shape[2]),
                                                      half_pixel_centers=True)

    def compute_output_shape(self, input_shape):
        if keras.backend.image_data_format() == 'channels_first':
            raise NotImplementedError
        else:
            return (input_shape[0][0], ) + input_shape[1][1:3] + (input_shape[0][-1], )


def build_vgg_backbone(inputs):
    x = make_vgg_block(inputs, filters=64, n=0, pooling=False, prefix='basenet.slice1')
    x = make_vgg_block(x, filters=64, n=3, pooling=True, prefix='basenet.slice1')
    x = make_vgg_block(x, filters=128, n=7, pooling=False, prefix='basenet.slice1')
    x = make_vgg_block(x, filters=128, n=10, pooling=True, prefix='basenet.slice1')
    x = make_vgg_block(x, filters=256, n=14, pooling=False, prefix='basenet.slice2')
    x = make_vgg_block(x, filters=256, n=17, pooling=False, prefix='basenet.slice2')
    x = make_vgg_block(x, filters=256, n=20, pooling=True, prefix='basenet.slice3')
    x = make_vgg_block(x, filters=512, n=24, pooling=False, prefix='basenet.slice3')
    x = make_vgg_block(x, filters=512, n=27, pooling=False, prefix='basenet.slice3')
    x = make_vgg_block(x, filters=512, n=30, pooling=True, prefix='basenet.slice4')
    x = make_vgg_block(x, filters=512, n=34, pooling=False, prefix='basenet.slice4')
    x = make_vgg_block(x, filters=512, n=37, pooling=False, prefix='basenet.slice4')
    x = make_vgg_block(x, filters=512, n=40, pooling=True, prefix='basenet.slice4')
    vgg = keras.models.Model(inputs=inputs, outputs=x)
    return [
        vgg.get_layer(slice_name).output for slice_name in [
            'basenet.slice1.12',
            'basenet.slice2.19',
            'basenet.slice3.29',
            'basenet.slice4.38',
        ]
    ]


def build_efficientnet_backbone(inputs, backbone_name, imagenet):
    backbone = getattr(efficientnet, backbone_name)(include_top=False,
                                                    input_tensor=inputs,
                                                    weights='imagenet' if imagenet else None)
    return [
        backbone.get_layer(slice_name).output for slice_name in [
            'block2a_expand_activation', 'block3a_expand_activation', 'block4a_expand_activation',
            'block5a_expand_activation'
        ]
    ]


def build_keras_model(weights_path: str = None, backbone_name='vgg'):
    inputs = keras.layers.Input((None, None, 3))

    if backbone_name == 'vgg':
        s1, s2, s3, s4 = build_vgg_backbone(inputs)
    elif 'efficientnet' in backbone_name.lower():
        s1, s2, s3, s4 = build_efficientnet_backbone(inputs=inputs,
                                                     backbone_name=backbone_name,
                                                     imagenet=weights_path is None)
    else:
        raise NotImplementedError

    s5 = keras.layers.MaxPooling2D(pool_size=3, strides=1, padding='same',
                                   name='basenet.slice5.0')(s4)
    s5 = keras.layers.Conv2D(1024,
                             kernel_size=(3, 3),
                             padding='same',
                             strides=1,
                             dilation_rate=6,
                             name='basenet.slice5.1')(s5)
    s5 = keras.layers.Conv2D(1024,
                             kernel_size=1,
                             strides=1,
                             padding='same',
                             name='basenet.slice5.2')(s5)

    y = keras.layers.Concatenate()([s5, s4])
    y = upconv(y, n=1, filters=512)
    y = UpsampleLike()([y, s3])
    y = keras.layers.Concatenate()([y, s3])
    y = upconv(y, n=2, filters=256)
    y = UpsampleLike()([y, s2])
    y = keras.layers.Concatenate()([y, s2])
    y = upconv(y, n=3, filters=128)
    y = UpsampleLike()([y, s1])
    y = keras.layers.Concatenate()([y, s1])
    features = upconv(y, n=4, filters=64)

    y = keras.layers.Conv2D(filters=32, kernel_size=3, strides=1, padding='same',
                            name='conv_cls.0')(features)
    y = keras.layers.Activation('relu', name='conv_cls.1')(y)
    y = keras.layers.Conv2D(filters=32, kernel_size=3, strides=1, padding='same',
                            name='conv_cls.2')(y)
    y = keras.layers.Activation('relu', name='conv_cls.3')(y)
    y = keras.layers.Conv2D(filters=16, kernel_size=3, strides=1, padding='same',
                            name='conv_cls.4')(y)
    y = keras.layers.Activation('relu', name='conv_cls.5')(y)
    y = keras.layers.Conv2D(filters=16, kernel_size=1, strides=1, padding='same',
                            name='conv_cls.6')(y)
    y = keras.layers.Activation('relu', name='conv_cls.7')(y)
    y = keras.layers.Conv2D(filters=2, kernel_size=1, strides=1, padding='same',
                            name='conv_cls.8')(y)
    if backbone_name != 'vgg':
        y = keras.layers.Activation('sigmoid')(y)
    model = keras.models.Model(inputs=inputs, outputs=y)
    if weights_path is not None:
        if weights_path.endswith('.h5'):
            model.load_weights(weights_path)
        elif weights_path.endswith('.pth'):
            assert backbone_name == 'vgg', 'PyTorch weights only allowed with VGG backbone.'
            load_torch_weights(model=model, weights_path=weights_path)
        else:
            raise NotImplementedError(f'Cannot load weights from {weights_path}')
    return model


# pylint: disable=import-error
def load_torch_weights(model, weights_path):
    import torch

    pretrained = torch.load(weights_path, map_location=torch.device('cpu'))
    layer_names = list(
        set('.'.join(k.split('.')[1:-1]) for k in pretrained.keys()
            if k.split('.')[-1] != 'num_batches_tracked'))
    for layer_name in layer_names:
        try:
            layer = model.get_layer(layer_name)
        except Exception:  # pylint: disable=broad-except
            print('Skipping', layer.name)
            continue
        if isinstance(layer, keras.layers.BatchNormalization):
            gamma, beta, running_mean, running_std = [
                pretrained[k].numpy() for k in [
                    f'module.{layer_name}.weight',
                    f'module.{layer_name}.bias',
                    f'module.{layer_name}.running_mean',
                    f'module.{layer_name}.running_var',
                ]
            ]
            layer.set_weights([gamma, beta, running_mean, running_std])
        elif isinstance(layer, keras.layers.Conv2D):
            weights, bias = [
                pretrained[k].numpy()
                for k in [f'module.{layer_name}.weight', f'module.{layer_name}.bias']
            ]
            layer.set_weights([weights.transpose(2, 3, 1, 0), bias])

        else:
            raise NotImplementedError

    for layer in model.layers:
        if isinstance(layer, (keras.layers.BatchNormalization, keras.layers.Conv2D)):
            assert layer.name in layer_names


# pylint: disable=import-error,too-few-public-methods
def build_torch_model(weights_path=None):
    from collections import namedtuple, OrderedDict

    import torch
    import torch.nn as nn
    import torch.nn.init as init
    import torch.nn.functional as F
    from torchvision import models

    def init_weights(modules):
        for m in modules:
            if isinstance(m, nn.Conv2d):
                init.xavier_uniform_(m.weight.data)
                if m.bias is not None:
                    m.bias.data.zero_()
            elif isinstance(m, nn.BatchNorm2d):
                m.weight.data.fill_(1)
                m.bias.data.zero_()
            elif isinstance(m, nn.Linear):
                m.weight.data.normal_(0, 0.01)
                m.bias.data.zero_()

    class vgg16_bn(torch.nn.Module):
        def __init__(self, pretrained=True, freeze=True):
            super().__init__()
            # We don't bother loading the pretrained VGG
            # because we're going to use the weights
            # at weights_path.
            vgg_pretrained_features = models.vgg16_bn(pretrained=False).features
            self.slice1 = torch.nn.Sequential()
            self.slice2 = torch.nn.Sequential()
            self.slice3 = torch.nn.Sequential()
            self.slice4 = torch.nn.Sequential()
            self.slice5 = torch.nn.Sequential()
            for x in range(12):  # conv2_2
                self.slice1.add_module(str(x), vgg_pretrained_features[x])
            for x in range(12, 19):  # conv3_3
                self.slice2.add_module(str(x), vgg_pretrained_features[x])
            for x in range(19, 29):  # conv4_3
                self.slice3.add_module(str(x), vgg_pretrained_features[x])
            for x in range(29, 39):  # conv5_3
                self.slice4.add_module(str(x), vgg_pretrained_features[x])

            # fc6, fc7 without atrous conv
            self.slice5 = torch.nn.Sequential(
                nn.MaxPool2d(kernel_size=3, stride=1, padding=1),
                nn.Conv2d(512, 1024, kernel_size=3, padding=6, dilation=6),
                nn.Conv2d(1024, 1024, kernel_size=1))

            if not pretrained:
                init_weights(self.slice1.modules())
                init_weights(self.slice2.modules())
                init_weights(self.slice3.modules())
                init_weights(self.slice4.modules())

            init_weights(self.slice5.modules())  # no pretrained model for fc6 and fc7

            if freeze:
                for param in self.slice1.parameters():  # only first conv
                    param.requires_grad = False

        def forward(self, X):  # pylint: disable=arguments-differ
            h = self.slice1(X)
            h_relu2_2 = h
            h = self.slice2(h)
            h_relu3_2 = h
            h = self.slice3(h)
            h_relu4_3 = h
            h = self.slice4(h)
            h_relu5_3 = h
            h = self.slice5(h)
            h_fc7 = h
            vgg_outputs = namedtuple("VggOutputs",
                                     ['fc7', 'relu5_3', 'relu4_3', 'relu3_2', 'relu2_2'])
            out = vgg_outputs(h_fc7, h_relu5_3, h_relu4_3, h_relu3_2, h_relu2_2)
            return out

    class double_conv(nn.Module):
        def __init__(self, in_ch, mid_ch, out_ch):
            super().__init__()
            self.conv = nn.Sequential(nn.Conv2d(in_ch + mid_ch, mid_ch, kernel_size=1),
                                      nn.BatchNorm2d(mid_ch), nn.ReLU(inplace=True),
                                      nn.Conv2d(mid_ch, out_ch, kernel_size=3, padding=1),
                                      nn.BatchNorm2d(out_ch), nn.ReLU(inplace=True))

        def forward(self, x):  # pylint: disable=arguments-differ
            x = self.conv(x)
            return x

    class CRAFT(nn.Module):
        def __init__(self, pretrained=False, freeze=False):
            super().__init__()
            # Base network
            self.basenet = vgg16_bn(pretrained, freeze)
            # U network
            self.upconv1 = double_conv(1024, 512, 256)
            self.upconv2 = double_conv(512, 256, 128)
            self.upconv3 = double_conv(256, 128, 64)
            self.upconv4 = double_conv(128, 64, 32)

            num_class = 2
            self.conv_cls = nn.Sequential(
                nn.Conv2d(32, 32, kernel_size=3, padding=1),
                nn.ReLU(inplace=True),
                nn.Conv2d(32, 32, kernel_size=3, padding=1),
                nn.ReLU(inplace=True),
                nn.Conv2d(32, 16, kernel_size=3, padding=1),
                nn.ReLU(inplace=True),
                nn.Conv2d(16, 16, kernel_size=1),
                nn.ReLU(inplace=True),
                nn.Conv2d(16, num_class, kernel_size=1),
            )

            init_weights(self.upconv1.modules())
            init_weights(self.upconv2.modules())
            init_weights(self.upconv3.modules())
            init_weights(self.upconv4.modules())
            init_weights(self.conv_cls.modules())

        def forward(self, x):  # pylint: disable=arguments-differ
            # Base network
            sources = self.basenet(x)
            # U network
            # pylint: disable=E1101
            y = torch.cat([sources[0], sources[1]], dim=1)

            y = self.upconv1(y)

            y = F.interpolate(y, size=sources[2].size()[2:], mode='bilinear', align_corners=False)
            y = torch.cat([y, sources[2]], dim=1)
            y = self.upconv2(y)

            y = F.interpolate(y, size=sources[3].size()[2:], mode='bilinear', align_corners=False)
            y = torch.cat([y, sources[3]], dim=1)
            y = self.upconv3(y)

            y = F.interpolate(y, size=sources[4].size()[2:], mode='bilinear', align_corners=False)
            y = torch.cat([y, sources[4]], dim=1)
            # pylint: enable=E1101
            feature = self.upconv4(y)

            y = self.conv_cls(feature)

            return y.permute(0, 2, 3, 1), feature

    def copyStateDict(state_dict):
        if list(state_dict.keys())[0].startswith("module"):
            start_idx = 1
        else:
            start_idx = 0
        new_state_dict = OrderedDict()
        for k, v in state_dict.items():
            name = ".".join(k.split(".")[start_idx:])
            new_state_dict[name] = v
        return new_state_dict

    model = CRAFT(pretrained=True).eval()
    if weights_path is not None:
        model.load_state_dict(
            copyStateDict(torch.load(weights_path, map_location=torch.device('cpu'))))
    return model


PRETRAINED_WEIGHTS = {
    ('clovaai_general', True): {
        'url':
        'https://github.com/faustomorales/keras-ocr/releases/download/v0.8.4/craft_mlt_25k.pth',
        'filename': 'craft_mlt_25k.pth',
        'sha256': '4a5efbfb48b4081100544e75e1e2b57f8de3d84f213004b14b85fd4b3748db17'
    },
    ('clovaai_general', False): {
        'url':
        'https://github.com/faustomorales/keras-ocr/releases/download/v0.8.4/craft_mlt_25k.h5',
        'filename': 'craft_mlt_25k.h5',
        'sha256': '7283ce2ff05a0617e9740c316175ff3bacdd7215dbdf1a726890d5099431f899'
    }
}


class Detector:
    """A text detector using the CRAFT architecture.
    Args:
        weights: The weights to use for the model. Currently, only `clovaai_general`
            is supported.
        load_from_torch: Whether to load the weights from the original PyTorch weights.
        optimizer: The optimizer to use for training the model.
        backbone_name: The backbone to use. Currently, only 'vgg' is supported.
    """
    def __init__(self,
                 weights='clovaai_general',
                 load_from_torch=False,
                 optimizer='adam',
                 backbone_name='vgg'):
        if weights is not None:
            pretrained_key = (weights, load_from_torch)
            assert backbone_name == 'vgg', 'Pretrained weights available only for VGG.'
            assert pretrained_key in PRETRAINED_WEIGHTS, \
                'Selected weights configuration not found.'
            weights_config = PRETRAINED_WEIGHTS[pretrained_key]
            weights_path = tools.download_and_verify(url=weights_config['url'],
                                                     filename=weights_config['filename'],
                                                     sha256=weights_config['sha256'])
        else:
            weights_path = None
        self.model = build_keras_model(weights_path=weights_path, backbone_name=backbone_name)
        self.model.compile(loss='mse', optimizer=optimizer)

    def get_batch_generator(self,
                            image_generator,
                            batch_size=8,
                            heatmap_size=512,
                            heatmap_distance_ratio=1.5):
        """Get a generator of X, y batches to train the detector.
        Args:
            image_generator: A generator with the same signature as
                keras_ocr.tools.get_image_generator. Optionally, a third
                entry in the tuple (beyond image and lines) can be provided
                which will be interpreted as the sample weight.
            batch_size: The size of batches to generate.
            heatmap_size: The size of the heatmap to pass to get_gaussian_heatmap
            heatmap_distance_ratio: The distance ratio to pass to
                get_gaussian_heatmap. The larger the value, the more tightly
                concentrated the heatmap becomes.
        """
        heatmap = get_gaussian_heatmap(size=heatmap_size, distanceRatio=heatmap_distance_ratio)
        while True:
            batch = [next(image_generator) for n in range(batch_size)]
            images = np.array([entry[0] for entry in batch])
            line_groups = [entry[1] for entry in batch]
            X = compute_input(images)
            # pylint: disable=unsubscriptable-object
            y = np.array([
                compute_maps(heatmap=heatmap,
                             image_height=images.shape[1],
                             image_width=images.shape[2],
                             lines=lines) for lines in line_groups
            ])
            # pylint: enable=unsubscriptable-object
            if len(batch[0]) == 3:
                sample_weights = np.array([sample[2] for sample in batch])
                yield X, y, sample_weights
            else:
                yield X, y

    def detect(self,
               images: typing.List[typing.Union[np.ndarray, str]],
               detection_threshold=0.7,
               text_threshold=0.4,
               link_threshold=0.4,
               size_threshold=10,
               **kwargs):
        """Recognize the text in a set of images.
        Args:
            images: Can be a list of numpy arrays of shape HxWx3 or a list of
                filepaths.
            link_threshold: This is the same as `text_threshold`, but is applied to the
                link map instead of the text map.
            detection_threshold: We want to avoid including boxes that may have
                represented large regions of low confidence text predictions. To do this,
                we do a final check for each word box to make sure the maximum confidence
                value exceeds some detection threshold. This is the threshold used for
                this check.
            text_threshold: When the text map is processed, it is converted from confidence
                (float from zero to one) values to classification (0 for not text, 1 for
                text) using binary thresholding. The threshold value determines the
                breakpoint at which a value is converted to a 1 or a 0. For example, if
                the threshold is 0.4 and a value for particular point on the text map is
                0.5, that value gets converted to a 1. The higher this value is, the less
                likely it is that characters will be merged together into a single word.
                The lower this value is, the more likely it is that non-text will be detected.
                Therein lies the balance.
            size_threshold: The minimum area for a word.
        """
        images = [compute_input(tools.read(image)) for image in images]
        boxes = getBoxes(self.model.predict(np.array(images), **kwargs),
                         detection_threshold=detection_threshold,
                         text_threshold=text_threshold,
                         link_threshold=link_threshold,
                         size_threshold=size_threshold)
        return boxes

### ==================================================================================== #
##  https://github.com/faustomorales/keras-ocr/blob/master/keras_ocr/evaluation.py      ##
# ==================================================================================== ###

# Adapted from https://github.com/andreasveit/coco-text/blob/master/coco_evaluation.py
def iou_score(box1, box2):
    """Returns the Intersection-over-Union score, defined as the area of
    the intersection divided by the intersection over the union of
    the two bounding boxes. This measure is symmetric.
    Args:
        box1: The coordinates for box 1 as a list of (x, y) coordinates
        box2: The coordinates for box 2 in same format as box1.
    """
    if len(box1) == 2:
        x1, y1 = box1[0]
        x2, y2 = box1[1]
        box1 = np.array([[x1, y1], [x2, y1], [x2, y2], [x1, y2]])
    if len(box2) == 2:
        x1, y1 = box2[0]
        x2, y2 = box2[1]
        box2 = np.array([[x1, y1], [x2, y1], [x2, y2], [x1, y2]])
    if any(cv2.contourArea(np.int32(box)[:, np.newaxis, :]) == 0 for box in [box1, box2]):
        warnings.warn('A box with zero area was detected.')
        return 0
    pc = pyclipper.Pyclipper()
    pc.AddPath(np.int32(box1), pyclipper.PT_SUBJECT, closed=True)
    pc.AddPath(np.int32(box2), pyclipper.PT_CLIP, closed=True)
    intersection_solutions = pc.Execute(pyclipper.CT_INTERSECTION, pyclipper.PFT_EVENODD,
                                        pyclipper.PFT_EVENODD)
    union_solutions = pc.Execute(pyclipper.CT_UNION, pyclipper.PFT_EVENODD, pyclipper.PFT_EVENODD)
    union = sum(cv2.contourArea(np.int32(points)[:, np.newaxis, :]) for points in union_solutions)
    intersection = sum(
        cv2.contourArea(np.int32(points)[:, np.newaxis, :]) for points in intersection_solutions)
    return intersection / union


def score(true, pred, iou_threshold=0.5, similarity_threshold=0.5, translator=None):
    """
    Args:
        true: The ground truth boxes provided as a dictionary of {image_id: annotations}
            mappings. `annotations` should be lists of dicts with a `text` and `vertices` key.
            `vertices` should be a list of (x, y) coordinates. Optionally, an "ignore" key can be
            added to indicate that detecting an annotation should neither count as a false positive
            nor should failure to detect it count as a false negative.
        pred: The predicted boxes in the same format as `true`.
        iou_threshold: The minimum IoU to qualify a box as a match.
        similarity_threshold: The minimum texg similarity required to qualify
            a text string as a match.
        translator: A translator acceptable by `str.translate`. Used to
            modify ground truth / predicted strings. For example,
            `str.maketrans(string.ascii_uppercase, string.ascii_lowercase,
            string.punctuation)` would yield a translator that changes all
            strings to lowercase and removes punctuation.
    Returns:
        A results dictionary reporting false positives, false negatives, true positives
        and near matches (IoU > iou_threshold but similarity < similarity_threshold) along
        with the compute precision and recall.
    """
    true_ids = sorted(true)
    pred_ids = sorted(pred)
    assert all(true_id == pred_id for true_id, pred_id in zip(
        true_ids, pred_ids)), 'true and pred dictionaries must have the same keys'
    results = {
        'true_positives': [],
        'false_positives': [],
        'near_true_positives': [],
        'false_negatives': []
    }
    for image_id in true_ids:
        true_anns = true[image_id]
        pred_anns = copy.deepcopy(pred[image_id])
        pred_matched = set()
        for true_index, true_ann in enumerate(true_anns):
            match = None
            for pred_index, pred_ann in enumerate(pred_anns):
                iou = iou_score(true_ann['vertices'], pred_ann['vertices'])
                if iou >= iou_threshold:
                    match = {'true_idx': true_index, 'pred_idx': pred_index, 'image_id': image_id}
                    pred_matched.add(pred_index)
                    true_text = true_ann['text']
                    pred_text = pred_ann['text']
                    if true_ann.get('ignore', False):
                        # We recorded that this prediction matched something,
                        # so it won't be a false positive. But we're also ignoring
                        # this ground truth label so we won't count it as a true
                        # positive or a near true positive.
                        continue
                    if translator is not None:
                        true_text = true_text.translate(translator)
                        pred_text = pred_text.translate(translator)
                    edit_distance_norm = max(len(true_text), len(pred_text))
                    if edit_distance_norm == 0:
                        similarity = 1
                    else:
                        similarity = 1 - (editdistance.eval(true_text, pred_text) /
                                          max(len(true_text), len(pred_text)))
                    if similarity >= similarity_threshold:
                        results['true_positives'].append(match)
                    else:
                        results['near_true_positives'].append(match)
            if match is None and not true_ann.get('ignore', False):
                results['false_negatives'].append({'image_id': image_id, 'true_idx': true_index})
        results['false_positives'].extend({
            'pred_index': pred_index,
            'image_id': image_id
        } for pred_index, _ in enumerate(pred_anns) if pred_index not in pred_matched)
    fns = len(results['false_negatives'])
    fps = len(results['false_positives'])
    tps = len(
        set((true_positive['image_id'], true_positive['true_idx'])
            for true_positive in results['true_positives']))
    precision = tps / (tps + fps)
    recall = tps / (tps + fns)
    return results, (precision, recall)

### ==================================================================================== #
##  https://github.com/faustomorales/keras-ocr/blob/master/keras_ocr/pipeline.py        ##
# ==================================================================================== ###

class Pipeline:
    """A wrapper for a combination of detector and recognizer.
    Args:
        detector: The detector to use
        recognizer: The recognizer to use
        scale: The scale factor to apply to input images
        max_size: The maximum single-side dimension of images for
            inference.
    """
    def __init__(self, detector=None, recognizer=None, scale=2, max_size=2048):
        if detector is None:
            detector = detection.Detector()
        if recognizer is None:
            recognizer = recognition.Recognizer()
        self.scale = scale
        self.detector = detector
        self.recognizer = recognizer
        self.max_size = max_size

    def recognize(self, images, detection_kwargs=None, recognition_kwargs=None):
        """Run the pipeline on one or multiples images.
        Args:
            images: The images to parse (can be a list of actual images or a list of filepaths)
            detection_kwargs: Arguments to pass to the detector call
            recognition_kwargs: Arguments to pass to the recognizer call
        Returns:
            A list of lists of (text, box) tuples.
        """

        # Make sure we have an image array to start with.
        if not isinstance(images, np.ndarray):
            images = [tools.read(image) for image in images]
        # This turns images into (image, scale) tuples temporarily
        images = [
            tools.resize_image(image, max_scale=self.scale, max_size=self.max_size)
            for image in images
        ]
        max_height, max_width = np.array([image.shape[:2] for image, scale in images]).max(axis=0)
        scales = [scale for _, scale in images]
        images = np.array(
            [tools.pad(image, width=max_width, height=max_height) for image, _ in images])
        if detection_kwargs is None:
            detection_kwargs = {}
        if recognition_kwargs is None:
            recognition_kwargs = {}
        box_groups = self.detector.detect(images=images, **detection_kwargs)
        prediction_groups = self.recognizer.recognize_from_boxes(images=images,
                                                                 box_groups=box_groups,
                                                                 **recognition_kwargs)
        box_groups = [
            tools.adjust_boxes(boxes=boxes, boxes_format='boxes', scale=1 /
                               scale) if scale != 1 else boxes
            for boxes, scale in zip(box_groups, scales)
        ]
        return [
            list(zip(predictions, boxes))
            for predictions, boxes in zip(prediction_groups, box_groups)
        ]

### ==================================================================================== #
##  https://github.com/faustomorales/keras-ocr/blob/master/keras_ocr/recognition.py     ##
# ==================================================================================== ###

DEFAULT_BUILD_PARAMS = {
    'height': 31,
    'width': 200,
    'color': False,
    'filters': (64, 128, 256, 256, 512, 512, 512),
    'rnn_units': (128, 128),
    'dropout': 0.25,
    'rnn_steps_to_discard': 2,
    'pool_size': 2,
    'stn': True,
}

DEFAULT_ALPHABET = string.digits + string.ascii_lowercase

PRETRAINED_WEIGHTS = {
    'kurapan': {
        'alphabet': DEFAULT_ALPHABET,
        'build_params': DEFAULT_BUILD_PARAMS,
        'weights': {
            'notop': {
                'url':
                'https://github.com/faustomorales/keras-ocr/releases/download/v0.8.4/crnn_kurapan_notop.h5',
                'filename': 'crnn_kurapan_notop.h5',
                'sha256': '027fd2cced3cbea0c4f5894bb8e9e85bac04f11daf96b8fdcf1e4ee95dcf51b9'
            },
            'top': {
                'url':
                'https://github.com/faustomorales/keras-ocr/releases/download/v0.8.4/crnn_kurapan.h5',
                'filename': 'crnn_kurapan.h5',
                'sha256': 'a7d8086ac8f5c3d6a0a828f7d6fbabcaf815415dd125c32533013f85603be46d'
            }
        }
    }
}


def swish(x, beta=1):
    return x * keras.backend.sigmoid(beta * x)


keras.utils.get_custom_objects().update({'swish': keras.layers.Activation(swish)})


def _repeat(x, num_repeats):
    ones = tf.ones((1, num_repeats), dtype='int32')
    x = tf.reshape(x, shape=(-1, 1))
    x = tf.matmul(x, ones)
    return tf.reshape(x, [-1])


def _meshgrid(height, width):
    x_linspace = tf.linspace(-1., 1., width)
    y_linspace = tf.linspace(-1., 1., height)
    x_coordinates, y_coordinates = tf.meshgrid(x_linspace, y_linspace)
    x_coordinates = tf.reshape(x_coordinates, shape=(1, -1))
    y_coordinates = tf.reshape(y_coordinates, shape=(1, -1))
    ones = tf.ones_like(x_coordinates)
    indices_grid = tf.concat([x_coordinates, y_coordinates, ones], 0)
    return indices_grid


# pylint: disable=too-many-statements
def _transform(inputs):
    locnet_x, locnet_y = inputs
    output_size = locnet_x.shape[1:]
    batch_size = tf.shape(locnet_x)[0]
    height = tf.shape(locnet_x)[1]
    width = tf.shape(locnet_x)[2]
    num_channels = tf.shape(locnet_x)[3]

    locnet_y = tf.reshape(locnet_y, shape=(batch_size, 2, 3))

    locnet_y = tf.reshape(locnet_y, (-1, 2, 3))
    locnet_y = tf.cast(locnet_y, 'float32')

    output_height = output_size[0]
    output_width = output_size[1]
    indices_grid = _meshgrid(output_height, output_width)
    indices_grid = tf.expand_dims(indices_grid, 0)
    indices_grid = tf.reshape(indices_grid, [-1])  # flatten?
    indices_grid = tf.tile(indices_grid, tf.stack([batch_size]))
    indices_grid = tf.reshape(indices_grid, tf.stack([batch_size, 3, -1]))

    transformed_grid = tf.matmul(locnet_y, indices_grid)
    x_s = tf.slice(transformed_grid, [0, 0, 0], [-1, 1, -1])
    y_s = tf.slice(transformed_grid, [0, 1, 0], [-1, 1, -1])
    x = tf.reshape(x_s, [-1])
    y = tf.reshape(y_s, [-1])

    # Interpolate
    height_float = tf.cast(height, dtype='float32')
    width_float = tf.cast(width, dtype='float32')

    output_height = output_size[0]
    output_width = output_size[1]

    x = tf.cast(x, dtype='float32')
    y = tf.cast(y, dtype='float32')
    x = .5 * (x + 1.0) * width_float
    y = .5 * (y + 1.0) * height_float

    x0 = tf.cast(tf.floor(x), 'int32')
    x1 = x0 + 1
    y0 = tf.cast(tf.floor(y), 'int32')
    y1 = y0 + 1

    max_y = tf.cast(height - 1, dtype='int32')
    max_x = tf.cast(width - 1, dtype='int32')
    zero = tf.zeros([], dtype='int32')

    x0 = tf.clip_by_value(x0, zero, max_x)
    x1 = tf.clip_by_value(x1, zero, max_x)
    y0 = tf.clip_by_value(y0, zero, max_y)
    y1 = tf.clip_by_value(y1, zero, max_y)

    flat_image_dimensions = width * height
    pixels_batch = tf.range(batch_size) * flat_image_dimensions
    flat_output_dimensions = output_height * output_width
    base = _repeat(pixels_batch, flat_output_dimensions)
    base_y0 = base + y0 * width
    base_y1 = base + y1 * width
    indices_a = base_y0 + x0
    indices_b = base_y1 + x0
    indices_c = base_y0 + x1
    indices_d = base_y1 + x1

    flat_image = tf.reshape(locnet_x, shape=(-1, num_channels))
    flat_image = tf.cast(flat_image, dtype='float32')
    pixel_values_a = tf.gather(flat_image, indices_a)
    pixel_values_b = tf.gather(flat_image, indices_b)
    pixel_values_c = tf.gather(flat_image, indices_c)
    pixel_values_d = tf.gather(flat_image, indices_d)

    x0 = tf.cast(x0, 'float32')
    x1 = tf.cast(x1, 'float32')
    y0 = tf.cast(y0, 'float32')
    y1 = tf.cast(y1, 'float32')

    area_a = tf.expand_dims(((x1 - x) * (y1 - y)), 1)
    area_b = tf.expand_dims(((x1 - x) * (y - y0)), 1)
    area_c = tf.expand_dims(((x - x0) * (y1 - y)), 1)
    area_d = tf.expand_dims(((x - x0) * (y - y0)), 1)
    transformed_image = tf.add_n([
        area_a * pixel_values_a, area_b * pixel_values_b, area_c * pixel_values_c,
        area_d * pixel_values_d
    ])
    # Finished interpolation

    transformed_image = tf.reshape(transformed_image,
                                   shape=(batch_size, output_height, output_width, num_channels))
    return transformed_image


def CTCDecoder():
    def decoder(y_pred):
        input_shape = tf.keras.backend.shape(y_pred)
        input_length = tf.ones(shape=input_shape[0]) * tf.keras.backend.cast(
            input_shape[1], 'float32')
        unpadded = tf.keras.backend.ctc_decode(y_pred, input_length)[0][0]
        unpadded_shape = tf.keras.backend.shape(unpadded)
        padded = tf.pad(unpadded,
                        paddings=[[0, 0], [0, input_shape[1] - unpadded_shape[1]]],
                        constant_values=-1)
        return padded

    return tf.keras.layers.Lambda(decoder, name='decode')


def build_model(alphabet,
                height,
                width,
                color,
                filters,
                rnn_units,
                dropout,
                rnn_steps_to_discard,
                pool_size,
                stn=True):
    """Build a Keras CRNN model for character recognition.
    Args:
        height: The height of cropped images
        width: The width of cropped images
        color: Whether the inputs should be in color (RGB)
        filters: The number of filters to use for each of the 7 convolutional layers
        rnn_units: The number of units for each of the RNN layers
        dropout: The dropout to use for the final layer
        rnn_steps_to_discard: The number of initial RNN steps to discard
        pool_size: The size of the pooling steps
        stn: Whether to add a Spatial Transformer layer
    """
    assert len(filters) == 7, '7 CNN filters must be provided.'
    assert len(rnn_units) == 2, '2 RNN filters must be provided.'
    inputs = keras.layers.Input((height, width, 3 if color else 1))
    x = keras.layers.Permute((2, 1, 3))(inputs)
    x = keras.layers.Lambda(lambda x: x[:, :, ::-1])(x)
    x = keras.layers.Conv2D(filters[0], (3, 3), activation='relu', padding='same', name='conv_1')(x)
    x = keras.layers.Conv2D(filters[1], (3, 3), activation='relu', padding='same', name='conv_2')(x)
    x = keras.layers.Conv2D(filters[2], (3, 3), activation='relu', padding='same', name='conv_3')(x)
    x = keras.layers.BatchNormalization(name='bn_3')(x)
    x = keras.layers.MaxPooling2D(pool_size=(pool_size, pool_size), name='maxpool_3')(x)
    x = keras.layers.Conv2D(filters[3], (3, 3), activation='relu', padding='same', name='conv_4')(x)
    x = keras.layers.Conv2D(filters[4], (3, 3), activation='relu', padding='same', name='conv_5')(x)
    x = keras.layers.BatchNormalization(name='bn_5')(x)
    x = keras.layers.MaxPooling2D(pool_size=(pool_size, pool_size), name='maxpool_5')(x)
    x = keras.layers.Conv2D(filters[5], (3, 3), activation='relu', padding='same', name='conv_6')(x)
    x = keras.layers.Conv2D(filters[6], (3, 3), activation='relu', padding='same', name='conv_7')(x)
    x = keras.layers.BatchNormalization(name='bn_7')(x)
    if stn:
        # pylint: disable=pointless-string-statement
        """Spatial Transformer Layer
        Implements a spatial transformer layer as described in [1]_.
        Borrowed from [2]_:
        downsample_fator : float
            A value of 1 will keep the orignal size of the image.
            Values larger than 1 will down sample the image. Values below 1 will
            upsample the image.
            example image: height= 100, width = 200
            downsample_factor = 2
            output image will then be 50, 100
        References
        ----------
        .. [1]  Spatial Transformer Networks
                Max Jaderberg, Karen Simonyan, Andrew Zisserman, Koray Kavukcuoglu
                Submitted on 5 Jun 2015
        .. [2]  https://github.com/skaae/transformer_network/blob/master/transformerlayer.py
        .. [3]  https://github.com/EderSantana/seya/blob/keras1/seya/layers/attention.py
        """
        stn_input_output_shape = (width // pool_size**2, height // pool_size**2, filters[6])
        stn_input_layer = keras.layers.Input(shape=stn_input_output_shape)
        locnet_y = keras.layers.Conv2D(16, (5, 5), padding='same',
                                       activation='relu')(stn_input_layer)
        locnet_y = keras.layers.Conv2D(32, (5, 5), padding='same', activation='relu')(locnet_y)
        locnet_y = keras.layers.Flatten()(locnet_y)
        locnet_y = keras.layers.Dense(64, activation='relu')(locnet_y)
        locnet_y = keras.layers.Dense(6,
                                      weights=[
                                          np.zeros((64, 6), dtype='float32'),
                                          np.float32([[1, 0, 0], [0, 1, 0]]).flatten()
                                      ])(locnet_y)
        localization_net = keras.models.Model(inputs=stn_input_layer, outputs=locnet_y)
        x = keras.layers.Lambda(_transform,
                                output_shape=stn_input_output_shape)([x, localization_net(x)])
    x = keras.layers.Reshape(target_shape=(width // pool_size**2,
                                           (height // pool_size**2) * filters[-1]),
                             name='reshape')(x)

    x = keras.layers.Dense(rnn_units[0], activation='relu', name='fc_9')(x)

    rnn_1_forward = keras.layers.LSTM(rnn_units[0],
                                      kernel_initializer="he_normal",
                                      return_sequences=True,
                                      name='lstm_10')(x)
    rnn_1_back = keras.layers.LSTM(rnn_units[0],
                                   kernel_initializer="he_normal",
                                   go_backwards=True,
                                   return_sequences=True,
                                   name='lstm_10_back')(x)
    rnn_1_add = keras.layers.Add()([rnn_1_forward, rnn_1_back])
    rnn_2_forward = keras.layers.LSTM(rnn_units[1],
                                      kernel_initializer="he_normal",
                                      return_sequences=True,
                                      name='lstm_11')(rnn_1_add)
    rnn_2_back = keras.layers.LSTM(rnn_units[1],
                                   kernel_initializer="he_normal",
                                   go_backwards=True,
                                   return_sequences=True,
                                   name='lstm_11_back')(rnn_1_add)
    x = keras.layers.Concatenate()([rnn_2_forward, rnn_2_back])
    backbone = keras.models.Model(inputs=inputs, outputs=x)
    x = keras.layers.Dropout(dropout, name='dropout')(x)
    x = keras.layers.Dense(len(alphabet) + 1,
                           kernel_initializer='he_normal',
                           activation='softmax',
                           name='fc_12')(x)
    x = keras.layers.Lambda(lambda x: x[:, rnn_steps_to_discard:])(x)
    model = keras.models.Model(inputs=inputs, outputs=x)

    prediction_model = keras.models.Model(inputs=inputs, outputs=CTCDecoder()(model.output))
    labels = keras.layers.Input(name='labels', shape=[model.output_shape[1]], dtype='float32')
    label_length = keras.layers.Input(shape=[1])
    input_length = keras.layers.Input(shape=[1])
    loss = keras.layers.Lambda(lambda inputs: keras.backend.ctc_batch_cost(
        y_true=inputs[0], y_pred=inputs[1], input_length=inputs[2], label_length=inputs[3]))(
            [labels, model.output, input_length, label_length])
    training_model = keras.models.Model(inputs=[model.input, labels, input_length, label_length],
                                        outputs=loss)
    return backbone, model, training_model, prediction_model


class Recognizer:
    """A text detector using the CRNN architecture.
    Args:
        alphabet: The alphabet the model should recognize.
        build_params: A dictionary of build parameters for the model.
            See `keras_ocr.recognition.build_model` for details.
        weights: The starting weight configuration for the model.
        include_top: Whether to include the final classification layer in the model (set
            to False to use a custom alphabet).
    """
    def __init__(self, alphabet=None, weights='kurapan', build_params=None):
        assert alphabet or weights, 'At least one of alphabet or weights must be provided.'
        if weights is not None:
            build_params = build_params or PRETRAINED_WEIGHTS[weights]['build_params']
            alphabet = alphabet or PRETRAINED_WEIGHTS[weights]['alphabet']
        build_params = build_params or DEFAULT_BUILD_PARAMS
        if alphabet is None:
            alphabet = DEFAULT_ALPHABET
        self.alphabet = alphabet
        self.blank_label_idx = len(alphabet)
        self.backbone, self.model, self.training_model, self.prediction_model = build_model(
            alphabet=alphabet, **build_params)
        if weights is not None:
            weights_dict = PRETRAINED_WEIGHTS[weights]
            if alphabet == weights_dict['alphabet']:
                self.model.load_weights(
                    tools.download_and_verify(url=weights_dict['weights']['top']['url'],
                                              filename=weights_dict['weights']['top']['filename'],
                                              sha256=weights_dict['weights']['top']['sha256']))
            else:
                print('Provided alphabet does not match pretrained alphabet. '
                      'Using backbone weights only.')
                self.backbone.load_weights(
                    tools.download_and_verify(url=weights_dict['weights']['notop']['url'],
                                              filename=weights_dict['weights']['notop']['filename'],
                                              sha256=weights_dict['weights']['notop']['sha256']))

    def get_batch_generator(self, image_generator, batch_size=8, lowercase=False):
        """
        Generate batches of training data from an image generator. The generator
        should yield tuples of (image, sentence) where image contains a single
        line of text and sentence is a string representing the contents of
        the image. If a sample weight is desired, it can be provided as a third
        entry in the tuple, making each tuple an (image, sentence, weight) tuple.
        Args:
            image_generator: An image / sentence tuple generator. The images should
                be in color even if the OCR is setup to handle grayscale as they
                will be converted here.
            batch_size: How many images to generate at a time.
            lowercase: Whether to convert all characters to lowercase before
                encoding.
        """
        y = np.zeros((batch_size, 1))
        if self.training_model is None:
            raise Exception('You must first call create_training_model().')
        max_string_length = self.training_model.input_shape[1][1]
        while True:
            batch = [sample for sample, _ in zip(image_generator, range(batch_size))]
            if not self.model.input_shape[-1] == 3:
                images = [
                    cv2.cvtColor(sample[0], cv2.COLOR_RGB2GRAY)[..., np.newaxis] for sample in batch
                ]
            else:
                images = [sample[0] for sample in batch]
            images = np.array([image.astype('float32') / 255 for image in images])
            sentences = [sample[1].strip() for sample in batch]
            if lowercase:
                sentences = [sentence.lower() for sentence in sentences]
            assert all(c in self.alphabet
                       for c in ''.join(sentences)), 'Found illegal characters in sentence.'
            assert all(sentences), 'Found a zero length sentence.'
            assert all(
                len(sentence) <= max_string_length
                for sentence in sentences), 'A sentence is longer than this model can predict.'
            assert all("  " not in sentence for sentence in sentences), (
                'Strings with multiple sequential spaces are not permitted. '
                'See https://github.com/faustomorales/keras-ocr/issues/54')
            label_length = np.array([len(sentence) for sentence in sentences])[:, np.newaxis]
            labels = np.array([[self.alphabet.index(c)
                                for c in sentence] + [-1] * (max_string_length - len(sentence))
                               for sentence in sentences])
            input_length = np.ones((batch_size, 1)) * max_string_length
            if len(batch[0]) == 3:
                sample_weights = np.array([sample[2] for sample in batch])
                yield (images, labels, input_length, label_length), y, sample_weights
            else:
                yield (images, labels, input_length, label_length), y

    def recognize(self, image):
        """Recognize text from a single image.
        Args:
            image: A pre-cropped image containing characters
        """
        image = tools.read_and_fit(filepath_or_array=image,
                                   width=self.prediction_model.input_shape[2],
                                   height=self.prediction_model.input_shape[1],
                                   cval=0)
        if self.prediction_model.input_shape[-1] == 1 and image.shape[-1] == 3:
            # Convert color to grayscale
            image = cv2.cvtColor(image, code=cv2.COLOR_RGB2GRAY)[..., np.newaxis]
        image = image.astype('float32') / 255
        return ''.join([
            self.alphabet[idx] for idx in self.prediction_model.predict(image[np.newaxis])[0]
            if idx not in [self.blank_label_idx, -1]
        ])

    def recognize_from_boxes(self, images, box_groups, **kwargs) -> typing.List[str]:
        """Recognize text from images using lists of bounding boxes.
        Args:
            images: A list of input images, supplied as numpy arrays with shape
                (H, W, 3).
            boxes: A list of groups of boxes, one for each image
        """
        assert len(box_groups) == len(images), \
            'You must provide the same number of box groups as images.'
        crops = []
        start_end = []
        for image, boxes in zip(images, box_groups):
            image = tools.read(image)
            if self.prediction_model.input_shape[-1] == 1 and image.shape[-1] == 3:
                # Convert color to grayscale
                image = cv2.cvtColor(image, code=cv2.COLOR_RGB2GRAY)
            for box in boxes:
                crops.append(
                    tools.warpBox(image=image,
                                  box=box,
                                  target_height=self.model.input_shape[1],
                                  target_width=self.model.input_shape[2]))
            start = 0 if not start_end else start_end[-1][1]
            start_end.append((start, start + len(boxes)))
        if not crops:
            return [[] for image in images]
        X = np.float32(crops) / 255
        if len(X.shape) == 3:
            X = X[..., np.newaxis]
        predictions = [
            ''.join([self.alphabet[idx] for idx in row if idx not in [self.blank_label_idx, -1]])
            for row in self.prediction_model.predict(X, **kwargs)
        ]
        return [predictions[start:end] for start, end in start_end]

    def compile(self, *args, **kwargs):
        """Compile the training model."""
        if 'optimizer' not in kwargs:
            kwargs['optimizer'] = 'RMSprop'
        if 'loss' not in kwargs:
            kwargs['loss'] = lambda _, y_pred: y_pred
        self.training_model.compile(*args, **kwargs)

### ==================================================================================== #
##  https://github.com/faustomorales/keras-ocr/blob/master/keras_ocr/tools.py           ##
# ==================================================================================== ###

def read(filepath_or_buffer: typing.Union[str, io.BytesIO]):
    """Read a file into an image object
    Args:
        filepath_or_buffer: The path to the file, a URL, or any object
            with a `read` method (such as `io.BytesIO`)
    """
    if isinstance(filepath_or_buffer, np.ndarray):
        return filepath_or_buffer
    if hasattr(filepath_or_buffer, 'read'):
        image = np.asarray(bytearray(filepath_or_buffer.read()), dtype=np.uint8)
        image = cv2.imdecode(image, cv2.IMREAD_UNCHANGED)
    elif isinstance(filepath_or_buffer, str):
        if validators.url(filepath_or_buffer):
            return read(urllib.request.urlopen(filepath_or_buffer))
        assert os.path.isfile(filepath_or_buffer), \
            'Could not find image at path: ' + filepath_or_buffer
        image = cv2.imread(filepath_or_buffer)
    return cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


def get_rotated_width_height(box):
    """
    Returns the width and height of a rotated rectangle
    Args:
        box: A list of four points starting in the top left
        corner and moving clockwise.
    """
    w = (spatial.distance.cdist(box[0][np.newaxis], box[1][np.newaxis], "euclidean") +
         spatial.distance.cdist(box[2][np.newaxis], box[3][np.newaxis], "euclidean")) / 2
    h = (spatial.distance.cdist(box[0][np.newaxis], box[3][np.newaxis], "euclidean") +
         spatial.distance.cdist(box[1][np.newaxis], box[2][np.newaxis], "euclidean")) / 2
    return int(w[0][0]), int(h[0][0])


# pylint:disable=too-many-locals
def warpBox(image,
            box,
            target_height=None,
            target_width=None,
            margin=0,
            cval=None,
            return_transform=False,
            skip_rotate=False):
    """Warp a boxed region in an image given by a set of four points into
    a rectangle with a specified width and height. Useful for taking crops
    of distorted or rotated text.
    Args:
        image: The image from which to take the box
        box: A list of four points starting in the top left
            corner and moving clockwise.
        target_height: The height of the output rectangle
        target_width: The width of the output rectangle
        return_transform: Whether to return the transformation
            matrix with the image.
    """
    if cval is None:
        cval = (0, 0, 0) if len(image.shape) == 3 else 0
    if not skip_rotate:
        box, _ = get_rotated_box(box)
    w, h = get_rotated_width_height(box)
    assert (
        (target_width is None and target_height is None)
        or (target_width is not None and target_height is not None)), \
            'Either both or neither of target width and height must be provided.'
    if target_width is None and target_height is None:
        target_width = w
        target_height = h
    scale = min(target_width / w, target_height / h)
    M = cv2.getPerspectiveTransform(src=box,
                                    dst=np.array([[margin, margin], [scale * w - margin, margin],
                                                  [scale * w - margin, scale * h - margin],
                                                  [margin, scale * h - margin]]).astype('float32'))
    crop = cv2.warpPerspective(image, M, dsize=(int(scale * w), int(scale * h)))
    target_shape = (target_height, target_width, 3) if len(image.shape) == 3 else (target_height,
                                                                                   target_width)
    full = (np.zeros(target_shape) + cval).astype('uint8')
    full[:crop.shape[0], :crop.shape[1]] = crop
    if return_transform:
        return full, M
    return full


def flatten(list_of_lists):
    return [item for sublist in list_of_lists for item in sublist]


def combine_line(line):
    """Combine a set of boxes in a line into a single bounding
    box.
    Args:
        line: A list of (box, character) entries
    Returns:
        A (box, text) tuple
    """
    text = ''.join([character if character is not None else '' for _, character in line])
    box = np.concatenate([coords[:2] for coords, _ in line] +
                         [np.array([coords[3], coords[2]])
                          for coords, _ in reversed(line)]).astype('float32')
    first_point = box[0]
    rectangle = cv2.minAreaRect(box)
    box = cv2.boxPoints(rectangle)

    # Put the points in clockwise order
    box = np.array(np.roll(box, -np.linalg.norm(box - first_point, axis=1).argmin(), 0))
    return box, text


def drawAnnotations(image, predictions, ax=None):
    """Draw text annotations onto image.
    Args:
        image: The image on which to draw
        predictions: The predictions as provided by `pipeline.recognize`.
        ax: A matplotlib axis on which to draw.
    """
    if ax is None:
        _, ax = plt.subplots()
    ax.imshow(drawBoxes(image=image, boxes=predictions, boxes_format='predictions'))
    predictions = sorted(predictions, key=lambda p: p[1][:, 1].min())
    left = []
    right = []
    for word, box in predictions:
        if box[:, 0].min() < image.shape[1] / 2:
            left.append((word, box))
        else:
            right.append((word, box))
    ax.set_yticks([])
    ax.set_xticks([])
    for side, group in zip(['left', 'right'], [left, right]):
        for index, (text, box) in enumerate(group):
            y = 1 - (index / len(group))
            xy = box[0] / np.array([image.shape[1], image.shape[0]])
            xy[1] = 1 - xy[1]
            ax.annotate(s=text,
                        xy=xy,
                        xytext=(-0.05 if side == 'left' else 1.05, y),
                        xycoords='axes fraction',
                        arrowprops={
                            'arrowstyle': '->',
                            'color': 'r'
                        },
                        color='r',
                        fontsize=14,
                        horizontalalignment='right' if side == 'left' else 'left')
    return ax


def drawBoxes(image, boxes, color=(255, 0, 0), thickness=5, boxes_format='boxes'):
    """Draw boxes onto an image.
    Args:
        image: The image on which to draw the boxes.
        boxes: The boxes to draw.
        color: The color for each box.
        thickness: The thickness for each box.
        boxes_format: The format used for providing the boxes. Options are
            "boxes" which indicates an array with shape(N, 4, 2) where N is the
            number of boxes and each box is a list of four points) as provided
            by `keras_ocr.detection.Detector.detect`, "lines" (a list of
            lines where each line itself is a list of (box, character) tuples) as
            provided by `keras_ocr.data_generation.get_image_generator`,
            or "predictions" where boxes is by itself a list of (word, box) tuples
            as provided by `keras_ocr.pipeline.Pipeline.recognize` or
            `keras_ocr.recognition.Recognizer.recognize_from_boxes`.
    """
    if len(boxes) == 0:
        return image
    canvas = image.copy()
    if boxes_format == 'lines':
        revised_boxes = []
        for line in boxes:
            for box, _ in line:
                revised_boxes.append(box)
        boxes = revised_boxes
    if boxes_format == 'predictions':
        revised_boxes = []
        for _, box in boxes:
            revised_boxes.append(box)
        boxes = revised_boxes
    for box in boxes:
        cv2.polylines(img=canvas,
                      pts=box[np.newaxis].astype('int32'),
                      color=color,
                      thickness=thickness,
                      isClosed=True)
    return canvas


def adjust_boxes(boxes, boxes_format='boxes', scale=1):
    """Adjust boxes using a given scale and offset.
    Args:
        boxes: The boxes to adjust
        boxes_format: The format for the boxes. See the `drawBoxes` function
            for an explanation on the options.
        scale: The scale to apply
    """
    if scale == 1:
        return boxes
    if boxes_format == 'boxes':
        return np.array(boxes) * scale
    if boxes_format == 'lines':
        return [[(np.array(box) * scale, character) for box, character in line] for line in boxes]
    if boxes_format == 'predictions':
        return [(word, np.array(box) * scale) for word, box in boxes]
    raise NotImplementedError(f'Unsupported boxes format: {boxes_format}')


def augment(boxes,
            augmenter: imgaug.augmenters.meta.Augmenter,
            image=None,
            boxes_format='boxes',
            image_shape=None,
            area_threshold=0.5,
            min_area=None):
    """Augment an image and associated boxes together.
    Args:
        image: The image which we wish to apply the augmentation.
        boxes: The boxes that will be augmented together with the image
        boxes_format: The format for the boxes. See the `drawBoxes` function
            for an explanation on the options.
        image_shape: The shape of the input image if no image will be provided.
        area_threshold: Fraction of bounding box that we require to be
            in augmented image to include it.
        min_area: The minimum area for a character to be included.
    """
    if image is None and image_shape is None:
        raise ValueError('One of "image" or "image_shape" must be provided.')
    augmenter = augmenter.to_deterministic()

    if image is not None:
        image_augmented = augmenter(image=image)
        image_shape = image.shape[:2]
        image_augmented_shape = image_augmented.shape[:2]
    else:
        image_augmented = None
        width_augmented, height_augmented = augmenter.augment_keypoints(
            imgaug.KeypointsOnImage.from_xy_array(xy=[[image_shape[1], image_shape[0]]],
                                                  shape=image_shape)).to_xy_array()[0]
        image_augmented_shape = (height_augmented, width_augmented)

    def box_inside_image(box):
        area_before = cv2.contourArea(np.int32(box)[:, np.newaxis, :])
        if area_before == 0:
            return False, box
        clipped = box.copy()
        clipped[:, 0] = clipped[:, 0].clip(0, image_augmented_shape[1])
        clipped[:, 1] = clipped[:, 1].clip(0, image_augmented_shape[0])
        area_after = cv2.contourArea(np.int32(clipped)[:, np.newaxis, :])
        return ((area_after / area_before) >= area_threshold) and (min_area is None or
                                                                   area_after > min_area), clipped

    def augment_box(box):
        return augmenter.augment_keypoints(
            imgaug.KeypointsOnImage.from_xy_array(box, shape=image_shape)).to_xy_array()

    if boxes_format == 'boxes':
        boxes_augmented = [
            box for inside, box in [box_inside_image(box) for box in map(augment_box, boxes)]
            if inside
        ]
    elif boxes_format == 'lines':
        boxes_augmented = [[(augment_box(box), character) for box, character in line]
                           for line in boxes]
        boxes_augmented = [[(box, character)
                            for (inside, box), character in [(box_inside_image(box), character)
                                                             for box, character in line] if inside]
                           for line in boxes_augmented]
        # Sometimes all the characters in a line are removed.
        boxes_augmented = [line for line in boxes_augmented if line]
    elif boxes_format == 'predictions':
        boxes_augmented = [(word, augment_box(box)) for word, box in boxes]
        boxes_augmented = [(word, box) for word, (inside, box) in [(word, box_inside_image(box))
                                                                   for word, box in boxes_augmented]
                           if inside]
    else:
        raise NotImplementedError(f'Unsupported boxes format: {boxes_format}')
    return image_augmented, boxes_augmented


def pad(image, width: int, height: int, cval: int = 255):
    """Pad an image to a desired size. Raises an exception if image
    is larger than desired size.
    Args:
        image: The input image
        width: The output width
        height: The output height
        cval: The value to use for filling the image.
    """
    if len(image.shape) == 3:
        output_shape = (height, width, image.shape[-1])
    else:
        output_shape = (height, width)
    assert height >= output_shape[0], 'Input height must be less than output height.'
    assert width >= output_shape[1], 'Input width must be less than output width.'
    padded = np.zeros(output_shape, dtype=image.dtype) + cval
    padded[:image.shape[0], :image.shape[1]] = image
    return padded


def resize_image(image, max_scale, max_size):
    """Obtain the optimal resized image subject to a maximum scale
    and maximum size.
    Args:
        image: The input image
        max_scale: The maximum scale to apply
        max_size: The maximum size to return
    """
    if max(image.shape) * max_scale > max_size:
        # We are constrained by the maximum size
        scale = max_size / max(image.shape)
    else:
        # We are contrained by scale
        scale = max_scale
    return cv2.resize(image,
                      dsize=(int(image.shape[1] * scale), int(image.shape[0] * scale))), scale


# pylint: disable=too-many-arguments
def fit(image, width: int, height: int, cval: int = 255, mode='letterbox', return_scale=False):
    """Obtain a new image, fit to the specified size.
    Args:
        image: The input image
        width: The new width
        height: The new height
        cval: The constant value to use to fill the remaining areas of
            the image
        return_scale: Whether to return the scale used for the image
    Returns:
        The new image
    """
    fitted = None
    x_scale = width / image.shape[1]
    y_scale = height / image.shape[0]
    if x_scale == 1 and y_scale == 1:
        fitted = image
        scale = 1
    elif (x_scale <= y_scale and mode == 'letterbox') or (x_scale >= y_scale and mode == 'crop'):
        scale = width / image.shape[1]
        resize_width = width
        resize_height = (width / image.shape[1]) * image.shape[0]
    else:
        scale = height / image.shape[0]
        resize_height = height
        resize_width = scale * image.shape[1]
    if fitted is None:
        resize_width, resize_height = map(int, [resize_width, resize_height])
        if mode == 'letterbox':
            fitted = np.zeros((height, width, 3), dtype='uint8') + cval
            image = cv2.resize(image, dsize=(resize_width, resize_height))
            fitted[:image.shape[0], :image.shape[1]] = image[:height, :width]
        elif mode == 'crop':
            image = cv2.resize(image, dsize=(resize_width, resize_height))
            fitted = image[:height, :width]
        else:
            raise NotImplementedError(f'Unsupported mode: {mode}')
    if not return_scale:
        return fitted
    return fitted, scale


def read_and_fit(filepath_or_array: typing.Union[str, np.ndarray],
                 width: int,
                 height: int,
                 cval: int = 255,
                 mode='letterbox'):
    """Read an image from disk and fit to the specified size.
    Args:
        filepath: The path to the image or numpy array of shape HxWx3
        width: The new width
        height: The new height
        cval: The constant value to use to fill the remaining areas of
            the image
        mode: The mode to pass to "fit" (crop or letterbox)
    Returns:
        The new image
    """
    image = read(filepath_or_array) if isinstance(filepath_or_array, str) else filepath_or_array
    image = fit(image=image, width=width, height=height, cval=cval, mode=mode)
    return image


def sha256sum(filename):
    """Compute the sha256 hash for a file."""
    h = hashlib.sha256()
    b = bytearray(128 * 1024)
    mv = memoryview(b)
    with open(filename, 'rb', buffering=0) as f:
        for n in iter(lambda: f.readinto(mv), 0):
            h.update(mv[:n])
    return h.hexdigest()


def get_default_cache_dir():
    return os.environ.get('KERAS_OCR_CACHE_DIR', os.path.expanduser(os.path.join('~',
                                                                                 '.keras-ocr')))


def download_and_verify(url, sha256=None, cache_dir=None, verbose=True, filename=None):
    """Download a file to a cache directory and verify it with a sha256
    hash.
    Args:
        url: The file to download
        sha256: The sha256 hash to check. If the file already exists and the hash
            matches, we don't download it again.
        cache_dir: The directory in which to cache the file. The default is
            `~/.keras-ocr`.
        verbose: Whether to log progress
        filename: The filename to use for the file. By default, the filename is
            derived from the URL.
    """
    if cache_dir is None:
        cache_dir = get_default_cache_dir()
    if filename is None:
        filename = os.path.basename(urllib.parse.urlparse(url).path)
    filepath = os.path.join(cache_dir, filename)
    os.makedirs(os.path.split(filepath)[0], exist_ok=True)
    if verbose:
        print('Looking for ' + filepath)
    if not os.path.isfile(filepath) or (sha256 and sha256sum(filepath) != sha256):
        if verbose:
            print('Downloading ' + filepath)
        urllib.request.urlretrieve(url, filepath)
    assert sha256 is None or sha256 == sha256sum(filepath), 'Error occurred verifying sha256.'
    return filepath


def get_rotated_box(
    points
) -> typing.Tuple[typing.Tuple[float, float], typing.Tuple[float, float], typing.Tuple[
        float, float], typing.Tuple[float, float], float]:
    """Obtain the parameters of a rotated box.
    Returns:
        The vertices of the rotated box in top-left,
        top-right, bottom-right, bottom-left order along
        with the angle of rotation about the bottom left corner.
    """
    try:
        mp = geometry.MultiPoint(points=points)
        pts = np.array(list(zip(*mp.minimum_rotated_rectangle.exterior.xy)))[:-1]  # noqa: E501
    except AttributeError:
        # There weren't enough points for the minimum rotated rectangle function
        pts = points
    # The code below is taken from
    # https://github.com/jrosebr1/imutils/blob/master/imutils/perspective.py

    # sort the points based on their x-coordinates
    xSorted = pts[np.argsort(pts[:, 0]), :]

    # grab the left-most and right-most points from the sorted
    # x-roodinate points
    leftMost = xSorted[:2, :]
    rightMost = xSorted[2:, :]

    # now, sort the left-most coordinates according to their
    # y-coordinates so we can grab the top-left and bottom-left
    # points, respectively
    leftMost = leftMost[np.argsort(leftMost[:, 1]), :]
    (tl, bl) = leftMost

    # now that we have the top-left coordinate, use it as an
    # anchor to calculate the Euclidean distance between the
    # top-left and right-most points; by the Pythagorean
    # theorem, the point with the largest distance will be
    # our bottom-right point
    D = spatial.distance.cdist(tl[np.newaxis], rightMost, "euclidean")[0]
    (br, tr) = rightMost[np.argsort(D)[::-1], :]

    # return the coordinates in top-left, top-right,
    # bottom-right, and bottom-left order
    pts = np.array([tl, tr, br, bl], dtype="float32")

    rotation = np.arctan((tl[0] - bl[0]) / (tl[1] - bl[1]))
    return pts, rotation


def fix_line(line):
    """Given a list of (box, character) tuples, return a revised
    line with a consistent ordering of left-to-right or top-to-bottom,
    with each box provided with (top-left, top-right, bottom-right, bottom-left)
    ordering.
    Returns:
        A tuple that is the fixed line as well as a string indicating
        whether the line is horizontal or vertical.
    """
    line = [(get_rotated_box(box)[0], character) for box, character in line]
    centers = np.array([box.mean(axis=0) for box, _ in line])
    sortedx = centers[:, 0].argsort()
    sortedy = centers[:, 1].argsort()
    if np.diff(centers[sortedy][:, 1]).sum() > np.diff(centers[sortedx][:, 0]).sum():
        return [line[idx] for idx in sortedy], 'vertical'
    return [line[idx] for idx in sortedx], 'horizontal'
