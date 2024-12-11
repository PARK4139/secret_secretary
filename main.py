# -*- coding: utf-8 -*-  # python 3.x 하위버전 호환을 위한코드
__author__ = 'park4139'

import asyncio
import inspect
import json
import os.path
import pdb
import platform
import random
import re
import secrets
import shutil
import socket
import string
import subprocess
import threading
import time
import traceback
import urllib.parse
import urllib.parse as urllib_parser
import webbrowser
import zipfile
from collections import Counter
from datetime import datetime, timedelta
from enum import Enum
from functools import partial
from pathlib import Path
from typing import Callable, Literal, Optional, TypeVar, List
from uuid import uuid4
import BlurWindow.blurWindow
import clipboard
import cv2
import easyocr
import keyboard
import mutagen
import numpy
import numpy as np
import pandas as pd
import pyautogui
import pygetwindow
import pynput
import pywintypes
import send2trash  # pip install send2trash
import toml
import win32con
import win32gui
import win32process
from BlurWindow.blurWindow import GlobalBlur
from PIL import Image
from PIL import ImageFilter  # PIL : Py img lib
from PySide6 import QtCore, QtWidgets
from PySide6.QtCore import QEvent
from PySide6.QtCore import Qt, QTimer, QThread, Signal, QCoreApplication
from PySide6.QtGui import QCursor
from PySide6.QtGui import QScreen, QIcon, QShortcut, QKeySequence, QFontDatabase, QFont, QGuiApplication
from PySide6.QtWidgets import QWidget, QApplication, QGridLayout, QLabel, QPushButton, QVBoxLayout, QLineEdit, QDialog, QScrollArea, QTextBrowser
from bs4 import BeautifulSoup, ResultSet
from colorama import Fore
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from googletrans import Translator

from moviepy.editor import *
from mutagen.mp3 import MP3
from psutil._common import print_color
from pydantic import BaseModel, field_validator
from pynput import mouse
from pytube import Playlist
from screeninfo import get_monitors
from sqlalchemy import Column, Integer, String, text as sqlalchecdmy_text, VARCHAR, select, DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.orm import sessionmaker, declarative_base
from tomlkit import item
from tqdm import tqdm

# from click import command # todo 확인필요한데 command 같은 일반적인 단어는 못쓰네..
# from venv import create
# from app.routes import index, auth

if platform.system() == 'Linux':
    pass
else:
    pass

# logger = logging.getLogger('park4139_test_logger')
# hdlr = logging.FileHandler('park4139_logger.log')
# hdlr.setFormatter(logging.Formatter('%(asctime)s %(levelname)s %(message)s'))
# logger.addHandler(hdlr)
# logger.setLevel(logging.INFO)


T = TypeVar('T')  # 타입 힌팅 설정


class StateManagementUtil:
    # mkr_전역변수
    FOLDABLE_MODE = False
    USERPROFILE = os.environ.get('USERPROFILE', os.environ.get('HOME'))  # Windows나 Linux/macOS 모두 처리
    HOSTNAME = os.environ.get('HOSTNAME', socket.gethostname())  # Windows, Linux, macOS 모두 처리
    UNDERLINE = '_' * 59 + " "  # 제목작성 시 앞부분에 적용되는 기준인데 pep8 최대권장길이(79)를 기준으로 20 자 내외로 제목작성을 작성
    INDENTATION_PROMISED = ' ' * 5
    BLANK = ' '  # 시각적으로 명시하기 위함.
    IS_DO_ROUTINE_PROCESSING = False
    TIME_S = 0.0
    TIME_E = 0.0
    BIGGEST_PNXS = []  # 300 MB 이상 백업대상
    SMALLEST_PNXS = []
    # speak() 쓰레드 상태관리용
    # is_speak_as_async_running = False
    PYGLET_PLAYER = None
    PREVIOUS_MP3_LENGTH_USED_IN_SPEAK_AS_ASYNC = 0
    PLAYING_SOUNDS = []
    ROUTINES = [
        '물 한컵',
        '선풍기로 방환기 1분 이상',
        '세수',
        '로션',
        '아침식사',
        "프로폴리스 한알",
        '물가글(혹시 구내염 있으시면 가글양치)',
        '양치 WITHOUT TOOTH PASTE',
        '양치 WITH TOOTH PASTE',
        '양치 WITH GARGLE',
        '물가글',
        '즐거운일 1개',
        '스트레칭 밴드 V 유지 런지 30개',
        '계단 스쿼트 30 개',
        '푸쉬업 30 개',
        '점심식사',
        '저녁식사',
        # '음악틀기',
    ]
    COUNTS_FOR_GUIDE_TO_SLEEP = []
    VIDEO_IDS_ALLOWED = ['617', '616', '625', '620', '614', '609', '606',
                         '315', '313', '303', '302', '308',
                         '248', '247', '244',
                         '137', '136',
                         ]
    AUDIO_IDS_ALLOWED = ['234', '251', '250']
    members = []  # 리스트에 저장, 런타임 중에만 저장이 유지됨, 앱종료 시 데이터 삭제
    todos = []  # 리스트에 저장, 런타임 중에만 저장이 유지됨, 앱종료 시 데이터 삭제

    # mkr_URLs
    GIT_HUB_ADDRESS = "https://github.com/PARK4139"

    # mkr_DIRECTORIES
    PROJECT_DIRECTORY = str(Path(__file__).parent.parent.absolute())  # __init__ 해당파일로 되어 있기 때문에. 위치가 복잡하게 되어 버렸다. 이를 __file__ 로 기준을 잡아서 경로를 수정하였다. 빌드를 하면서 알게되었는데 상대경로의 사용은 필연적인데, 상대경로로 경로를 설정할때 기준이 되는 절대경로 하나는 반드시 필요한 것 같다.
    STORAGE_VIDEOES_MERGED = rf"{USERPROFILE}\Downloads\storage_videoes_merged"
    PROJECT_PARENTS_DIRECTORY = os.path.dirname(PROJECT_DIRECTORY)
    DESKTOP = rf'{USERPROFILE}\Desktop'
    DOWNLOADS = rf'{USERPROFILE}\Downloads'
    PKG_PNG = rf'{PROJECT_DIRECTORY}\pkg_png'
    PKG_LOG = rf'{PROJECT_DIRECTORY}\pkg_log'
    PKG_DPL = rf'{PROJECT_DIRECTORY}\pkg_dpl'
    PKG_JSON = rf'{PROJECT_DIRECTORY}\pkg_json'
    PKG_VIDEO = rf'{PROJECT_DIRECTORY}\pkg_video'
    PKG_TXT = rf'{PROJECT_DIRECTORY}\pkg_txt'
    PKG_CLOUD = rf'{PROJECT_DIRECTORY}\pkg_cloud'
    PKG_DOWNLOADING = rf"{USERPROFILE}\Downloads\pkg_Downloading"
    DIRECTORY_XLS_TO_MERGE = rf'{PROJECT_DIRECTORY}\pkg_xls\to_merge'
    DIRECTORY_XLS_MERGED = rf'{PROJECT_DIRECTORY}\pkg_xls\merged'
    CLASSIFYING = rf"D:\pkg_classifying"
    DEPRECATED = rf"F:\deprecated"
    ARCHIVED = rf"F:\archived"
    PKG_IMAGE = rf'{PROJECT_DIRECTORY}\pkg_image'

    # mkr_FILES
    LOCAL_PKG_CACHE_FILE = rf'{PROJECT_DIRECTORY}\pkg_alba\__pycache__\__init__.cpython-312.pyc'
    ICON_PNG = rf"{PROJECT_DIRECTORY}\pkg_png\icon.PNG"
    SUCCESS_LOG = rf'{PROJECT_DIRECTORY}\pkg_log\success.log'
    MACRO_LOG = rf'{PROJECT_DIRECTORY}\pkg_log\macro.log'
    # DIRSYNC_LOG = rf'{PROJECT_DIRECTORY}\pkg_log\dirsync.log'
    SCHECLUER_YAML = rf'{PROJECT_DIRECTORY}\pkg_yaml\schecluer.yaml'
    # YT_DLP_CMD = rf"{PROJECT_DIRECTORY}\pkg_yt_dlp\yt-dlp.cmd" # 2023.11.15 구버전
    YT_DLP_CMD = rf"{PROJECT_DIRECTORY}\pkg_yt_dlp\yt-dlp.exe"  # 2024.04.09 신버전
    JQ_WIN64_EXE = rf"{PROJECT_DIRECTORY}\pkg_jq\jq-win64.exe"
    FFMPEG_EXE = rf"{PROJECT_DIRECTORY}\pkg_tools\dev_tools_exe\LosslessCut-win-x64\resources\ffmpeg.exe"
    DB_YAML = rf"{PROJECT_DIRECTORY}\pkg_yaml\db.yaml"
    USELESS_FILE_NAMES_TXT = rf"{PROJECT_DIRECTORY}\pkg_txt\useless_file_names.txt"
    SILENT_MP3 = rf"{PROJECT_DIRECTORY}\pkg_sound\silent.mp3"
    POP_SOUND_POP_SOUND_WAV = rf"{PROJECT_DIRECTORY}\pkg_sound\pop_sound.wav"
    PKG_SOUND_POTPLAYER64_DPL = rf"{PROJECT_DIRECTORY}\pkg_sound\PotPlayer64.dpl"
    PKG_VIDEO_POTPLAYER64_DPL = rf"{PROJECT_DIRECTORY}\pkg_video\PotPlayer64.dpl"
    DB_JSON = rf"{PROJECT_DIRECTORY}\pkg_json\db.json"
    BOOKS_JSON = rf"{PROJECT_DIRECTORY}\pkg_json\books.json"
    USERS_JSON = rf"{PROJECT_DIRECTORY}\pkg_json\users.json"
    NAV_ITEMS_JSON = rf"{PROJECT_DIRECTORY}\pkg_json\nav_items.json"
    PYCHARM64_EXE: str = rf'{os.environ.get("PyCharm Community Edition").replace(";", "")}\pycharm64.exe'
    MERGED_EXCEL_FILE = rf'{PROJECT_DIRECTORY}\pkg_xls\merged\머지결과물.xlsx'
    MONTSERRAT_THIN_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Montserrat-Thin.ttf"
    NOTOSANSKR_VARIABLEFONT_WGHT_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Noto_Sans_KR\NotoSansKR-VariableFont_wght.ttf"
    NOTOSANSKR_BLACK_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\NotoSansKR-Black.ttf"
    NOTOSANSKR_BOLD_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\NotoSansKR-Bold.ttf"
    NOTOSANSKR_EXTRABOLD_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\NotoSansKR-ExtraBold.ttf"
    NOTOSANSKR_EXTRALIGHT_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\NotoSansKR-ExtraLight.ttf"
    NOTOSANSKR_LIGHT_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\NotoSansKR-Light.ttf"
    NOTOSANSKR_MEDIUM_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\NotoSansKR-Medium.ttf"
    NOTOSANSKR_REGULAR_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\NotoSansKR-Regular.ttf"
    NOTOSANSKR_SEMIBOLD_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\NotoSansKR-SemiBold.ttf"
    NOTOSANSKR_THIN_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\NotoSansKR-Thin.ttf"
    GMARKETSANSTTFBOLD_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\GmarketSansTTFBold.ttf"
    GMARKETSANSTTFLIGHT_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\GmarketSansTTFLight.ttf"
    GMARKETSANSTTFMEDIUM_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\GmarketSansTTFMedium.ttf"
    ITALIC_VARIABLEFONT_WGHT_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Montserrat\Montserrat-Italic-VariableFont_wght.ttf"
    MONTSERRAT_VARIABLEFONT_WGHT_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Montserrat\Montserrat-VariableFont_wght.ttf"
    MONTSERRAT_BLACK_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Montserrat-Black.ttf"
    MONTSERRAT_BLACKITALIC_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Montserrat-BlackItalic.ttf"
    MONTSERRAT_BOLD_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Montserrat-Bold.ttf"
    MONTSERRAT_BOLDITALIC_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Montserrat-BoldItalic.ttf"
    MONTSERRAT_EXTRABOLD_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Montserrat-ExtraBold.ttf"
    MONTSERRAT_EXTRABOLDITALIC_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Montserrat-ExtraBoldItalic.ttf"
    MONTSERRAT_EXTRALIGHT_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Montserrat-ExtraLight.ttf"
    MONTSERRAT_EXTRALIGHTITALIC_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Montserrat-ExtraLightItalic.ttf"
    MONTSERRAT_ITALIC_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Montserrat-Italic.ttf"
    MONTSERRAT_LIGHT_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Montserrat-Light.ttf"
    MONTSERRAT_LIGHTITALIC_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Montserrat-LightItalic.ttf"
    MONTSERRAT_MEDIUM_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Montserrat-Medium.ttf"
    MONTSERRAT_MEDIUMITALIC_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Montserrat-MediumItalic.ttf"
    MONTSERRAT_REGULAR_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Montserrat-Regular.ttf"
    MONTSERRAT_SEMIBOLD_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Montserrat-SemiBold.ttf"
    MONTSERRAT_SEMIBOLDITALIC_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Montserrat-SemiBoldItalic.ttf"
    MONTSERRAT_THINITALIC_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Montserrat-ThinItalic.ttf"
    POPPINS_BLACK_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Poppins-Black.ttf"
    POPPINS_BLACKITALIC_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Poppins-BlackItalic.ttf"
    POPPINS_BOLD_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Poppins-Bold.ttf"
    POPPINS_BOLDITALIC_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Poppins-BoldItalic.ttf"
    POPPINS_EXTRABOLD_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Poppins-ExtraBold.ttf"
    POPPINS_EXTRABOLDITALIC_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Poppins-ExtraBoldItalic.ttf"
    POPPINS_EXTRALIGHT_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Poppins-ExtraLight.ttf"
    POPPINS_EXTRALIGHTITALIC_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Poppins-ExtraLightItalic.ttf"
    POPPINS_ITALIC_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Poppins-Italic.ttf"
    POPPINS_LIGHT_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Poppins-Light.ttf"
    POPPINS_LIGHTITALIC_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Poppins-LightItalic.ttf"
    POPPINS_MEDIUM_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Poppins-Medium.ttf"
    POPPINS_MEDIUMITALIC_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Poppins-MediumItalic.ttf"
    POPPINS_REGULAR_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Poppins-Regular.ttf"
    POPPINS_SEMIBOLD_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Poppins-SemiBold.ttf"
    POPPINS_SEMIBOLDITALIC_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Poppins-SemiBoldItalic.ttf"
    POPPINS_THIN_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Poppins-Thin.ttf"
    POPPINS_THINITALIC_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\Poppins-ThinItalic.ttf"
    RUBIKDOODLESHADOW_REGULAR_TTF = rf"{PROJECT_DIRECTORY}\pkg_font\RubikDoodleShadow-Regular.ttf"  # 너무 귀여운 입체감 있는 영어폰트

    def __init__(self):
        try:
            os.system('chcp 65001 >nul')
            BusinessLogicUtil.PYCHARM64_EXE = rf'{os.environ.get("PyCharm Community Edition").replace(";", "")}\pycharm64.exe'
        except AttributeError:
            pass
        except Exception:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")


class TimeUtil:
    @staticmethod
    def get_weekday_as_korean():
        now = datetime.now()
        weekdays_korean = ['월', '화', '수', '목', '금', '토', '일']
        return weekdays_korean[now.weekday()]

    @staticmethod
    def get_time_as_(pattern: str):
        # %Y-%m-%d %H:%M:%S 의 형태도 모두 쓸 수 있고, 특정해둔 키워드도 쓸 수 있다
        now = datetime.now()
        weekday = TimeUtil.get_weekday_as_korean()
        epoch_time = time.time()
        seconds = int(epoch_time)
        nanoseconds = int((epoch_time - seconds) * 1e9)  # 나노초 부분
        milliseconds = (now.microsecond // 1000)  # 마이크로초 -> 밀리초
        time_styles = {
            'now': f"{now.year}_{now.month:02}_{now.day:02}_{weekday}_{now.hour:02}_{now.minute:02}_{now.second:02}_{milliseconds:03}_{nanoseconds:09}",
            'yyyy': str(now.year),
            'MM': str(now.month).zfill(2),
            'dd': str(now.day).zfill(2),
            'HH': str(now.hour).zfill(2),
            'mm': str(now.minute).zfill(2),
            'ss': str(now.second).zfill(2),
            'fff': str(milliseconds).zfill(3),  # 밀리초
            'fffffff': str(nanoseconds).zfill(9),  # 나노초
            'weekday': weekday,
            'elapsed_days_from_jan_01': str(now.timetuple().tm_yday),  # 금년 1월 1일부터 오늘까지의 일수
            'yyyy MM dd (weekday) HH mm': f"{now.year} {now.month:02} {now.day:02} ({weekday}) {now.hour:02} {now.minute:02}",
            'yyyy MM dd weekday HH mm ss': f"{now.year} {now.month:02} {now.day:02} {weekday} {now.hour:02} {now.minute:02} {now.second:02}",
            'yyyy MM dd weekday HH mm ss fff': f"{now.year} {now.month:02} {now.day:02} {weekday} {now.hour:02} {now.minute:02} {now.second:02} {milliseconds:03}",
            'yyyy MM dd weekday HH mm ss fff ffffff': f"{now.year} {now.month:02} {now.day:02} {weekday} {now.hour:02} {now.minute:02} {now.second:02} {milliseconds:03} {nanoseconds:09}",
        }
        if pattern in time_styles:
            return time_styles[pattern]
        return now.strftime(pattern)


class ColoramaUtil(Enum):
    RED = "RED"
    GREEN = "GREEN"
    BLACK = "BLACK"
    YELLOW = "YELLOW"
    BLUE = "BLUE"
    MAGENTA = "MAGENTA"
    CYAN = "CYAN"
    WHITE = "WHITE"
    RESET = "RESET"
    LIGHTBLACK_EX = "LIGHTBLACK_EX"
    LIGHTRED_EX = "LIGHTRED_EX"
    LIGHTGREEN_EX = "LIGHTGREEN_EX"
    LIGHTYELLOW_EX = "LIGHTYELLOW_EX"
    LIGHTBLUE_EX = "LIGHTBLUE_EX"
    LIGHTMAGENTA_EX = "LIGHTMAGENTA_EX"
    LIGHTCYAN_EX = "LIGHTCYAN_EX"
    LIGHTWHITE_EX = "LIGHTWHITE_EX"


class UiUtil:
    class CustomQdialog(QDialog):
        """순환참조 를 회피하기 위해서 객체를 복제했다."""

        def update_btn_text_clicked(self, text_of_clicked_button):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            self.btn_text_clicked = text_of_clicked_button

        def update_btn_text_clicked_and_close(self, text_of_clicked_button):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.play_wav_file(file_pnx=StateManagementUtil.POP_SOUND_POP_SOUND_WAV)
            self.btn_text_clicked = text_of_clicked_button
            self.close()

        def set_shortcut(self, key_plus_key: str, function):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            self.shortcut = QShortcut(QKeySequence(key_plus_key), self)
            self.shortcut.activated.connect(function)

        # 스택 마우스 제작 참고용
        # def eventFilter(self, obj, event):

        #     # 드래그 가능한 레이블의 이벤트 구현
        #     if isinstance(obj, DraggableLabel) and event.type() == QEvent.MouseButtonPress:
        #         obj.mousePressEvent(event)
        #         return True
        #     elif isinstance(obj, DraggableLabel) and event.type() == QEvent.MouseMove:
        #         obj.mouseMoveEvent(event)
        #         return True
        #
        #     return super().eventFilter(obj, event)

        def __init__(self, string: str, btns=None, parent=None, input_box_mode=False, input_box_text_default="", title="", auto_click_negative_btn_after_seconds: int = None, auto_click_positive_btn_after_seconds: int = None):
            function_name = inspect.currentframe().f_code.co_name
            class_name = self.__class__.__name__
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}class_name="{class_name}/{function_name}()" %%%FOO%%%''')

            try:
                super().__init__(parent)
                file_pnx = StateManagementUtil.POP_SOUND_POP_SOUND_WAV
                if BusinessLogicUtil.does_pnx_exist(src=file_pnx):
                    BusinessLogicUtil.play_wav_file(file_pnx=file_pnx)
                self.input_text_default = input_box_text_default
                self.context = string
                self.title = title
                if self.title == "":
                    self.setWindowTitle(".")
                else:
                    self.setWindowTitle(self.title)
                self.is_input_text_box = input_box_mode
                self.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: white;")  # 메시지박스창 스타일시트 적용 설정
                ICON_PNG = StateManagementUtil.ICON_PNG
                self.setWindowIcon(QIcon(ICON_PNG))  # 메시지박스창 아이콘 설정
                self.setAttribute(Qt.WA_TranslucentBackground)  # 메시지박스창 블러 설정
                # self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # 메시지박스창 최상단 프레임레스 설정
                BlurWindow.blurWindow.GlobalBlur(self.winId(), hexColor=False, Acrylic=False, Dark=True, QWidget=self)
                # self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)  # 메시지박스창 최대화 최소화 버튼숨기기
                # self.setWindowFlag(Qt.WindowCloseButtonHint, False)  # 메시지박스창 닫기 버튼 disable
                # self.setWindowFlag(Qt.WindowStaysOnTopHint)  # 모든 창들 중 가장 앞에 메시지박스창 위치하도록 설정
                # self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")  # 메시지박스창 스타일시트 적용 설정

                self.display_width = BusinessLogicUtil.get_display_info()['width'],
                self.display_height = BusinessLogicUtil.get_display_info()['height'],
                # self.pop_up_window_width_default = int(int(self.display_width[0]) * 0.4)
                # self.pop_up_window_height_default = int(int(self.display_height[0]) * 0.4)
                # self.resize(self.pop_up_window_width_default, self.pop_up_window_height_default)
                if len(string.split("\n")) < 20:
                    # self.resize(500, 250)
                    self.resize(int(self.display_width[0] * 0.3), int(self.display_height[0] * 0.2))
                else:
                    # self.resize(int(500 * 2.5), 250 * 2)
                    # self.resize(int(self.display_width[0] * 0.8), int(self.display_height[0] * 0.6))
                    self.resize(int(self.display_width[0] * 0.4), int(self.display_height[0] * 0.6))
                    # self.resize(int(self.display_width[0] * 0.9), int(self.display_height[0] * 0.6))

                # 창을 화면의 상단가운데로 이동
                screen = QGuiApplication.primaryScreen()
                screen_geometry = screen.availableGeometry()
                center_point = screen_geometry.center()
                self.move(center_point.x() - self.width() / 2, screen_geometry.top() + (center_point.y() * 0.1))

                # pyside6 표준버튼 설정
                # self.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
                # self.setButtonText(QMessageBox.StandardButton.Ok, "확인", )
                # self.setButton.setStyleSheet("background-color: rgba(0, 0, 0, 0);  color: white;")
                # self.setButtonText(QMessageBox.StandardButton.Cancel, "취소")
                self.btn_text_clicked = None
                self.layout_horizontal = None
                self.btn_positive = None
                self.btn_negative = None
                self.btn_third = None

                # 스크롤지역 설정
                self.scroll_area = None

                # 버튼 설정
                btn_to_copy = QPushButton(string)
                btn_to_copy.setStyleSheet("background-color: rgba(0, 0, 0, 0);  color: white;")
                btn_to_copy.setFocusPolicy(Qt.NoFocus)
                btn_to_copy.clicked.connect(self.copy_label_text_to_clipboard)
                # BusinessLogicUtil.print_as_log(context=len(contents.strip()))
                if 30 < len(string.strip()):
                    # btn_to_copy.setStyleSheet("text-align: left; font-size: 8px")
                    btn_to_copy.setStyleSheet("text-align: left; font-size: 16px")
                else:
                    btn_to_copy.setStyleSheet("text-align: center; font-size: 20px")
                file_pnx = StateManagementUtil.GMARKETSANSTTFLIGHT_TTF
                if BusinessLogicUtil.does_pnx_exist(src=file_pnx):
                    btn_to_copy.setFont(Pyside6Util.get_font_for_pyside6(font_path=file_pnx))

                self.set_shortcut(function=self.copy_label_text_to_clipboard, key_plus_key="alt+C")  # 단축키 설정

                self.scroll_area = QScrollArea()
                # self.scroll_area.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
                self.scroll_area.setWidget(btn_to_copy)
                self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
                self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
                self.scroll_area.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                self.scroll_area.setStyleSheet(" border: none;")
                # if 100 < len(contents):
                # self.scroll_area.setStyleSheet("text-align: center; border: none;")
                # else:
                # self.scroll_area.setStyleSheet("text-align: left; border: none; ")
                self.scroll_area.setFocusPolicy(Qt.NoFocus)  # focus 가 필요 없는 부분에는 이렇게 설정을 해두어야 원하는 곳으로 처음 창이 열렸을 때 focus 되도록 유도할 수 있었다
                # self.scroll_area.setMaximumSize(3000, 1000)

                # 입력 텍스트 박스 설정
                if self.is_input_text_box == True:
                    self.input_box = QLineEdit()
                    self.input_box.setText(self.input_text_default)
                    self.input_box.setFocusPolicy(Qt.StrongFocus)
                    self.input_box.setFocus()  # 창이 나타났을 때 focus 가 다른데 말고 입력 텍스트 박스에 있도록

                if btns is not None:
                    self.btns = btns

                else:
                    self.btns = [""]
                self.btns_etc = [None] * (len(self.btns) - 3)
                try:
                    # 버튼 설정 / 단축키 설정
                    # file_pnx = FONTS.RUBIKDOODLESHADOW_REGULAR_TTF
                    file_pnx = StateManagementUtil.GMARKETSANSTTFLIGHT_TTF
                    # if self.btns[0]:
                    #     self.btn_positive = QPushButton(f'{self.btns[0]} (F1)')
                    #     self.btn_positive.setStyleSheet("background-color: rgba(0, 0, 0, 0);  color: white;")
                    #     self.btn_positive.clicked.connect(partial(self.update_btn_text_clicked_and_close, self.btns[0]))
                    #     if BusinessLogicUtil.does_pnx_exist(pnx=file_pnx):
                    #         self.btn_positive.setFont(Pyside6Util.get_font_for_pyside6(font_path=file_pnx))
                    #     # self.set_shortcut(function=partial(self.update_btn_text_clicked_and_close, self.btns[0]), key_plus_key="alt+y")  # 단축키 설정
                    #     self.set_shortcut(function=partial(self.update_btn_text_clicked_and_close, self.btns[0]), key_plus_key="F1")  # 단축키 설정
                    # if self.btns[1]:
                    #     self.btn_negative = QPushButton(f'{self.btns[1]} (F2)')
                    #     self.btn_negative.setStyleSheet("background-color: rgba(0, 0, 0, 0);  color: white;")
                    #     self.btn_negative.clicked.connect(partial(self.update_btn_text_clicked_and_close, self.btns[1]))
                    #     if BusinessLogicUtil.does_pnx_exist(pnx=file_pnx):
                    #         self.btn_negative.setFont(Pyside6Util.get_font_for_pyside6(font_path=file_pnx))
                    #     self.set_shortcut(function=partial(self.update_btn_text_clicked_and_close, self.btns[1]), key_plus_key="F2")  # 단축키 설정
                    # if self.btns[2]:
                    #     self.btn_third = QPushButton(f'{self.btns[2]} (F3)')
                    #     self.btn_third.setStyleSheet("background-color: rgba(0, 0, 0, 0);  color: white;")
                    #     self.btn_third.clicked.connect(partial(self.update_btn_text_clicked_and_close, self.btns[2]))
                    #     if BusinessLogicUtil.does_pnx_exist(pnx=file_pnx):
                    #         self.btn_third.setFont(Pyside6Util.get_font_for_pyside6(font_path=file_pnx))
                    #     self.set_shortcut(function=partial(self.update_btn_text_clicked_and_close, self.btns[2]), key_plus_key="F3")  # 단축키 설정
                    #
                    # for n, item in enumerate(iterable=self.btns[3:]):
                    #     # 여기서 Unexpected type(s): (int, QPushButton | QPushButton) Possible type(s): (SupportsIndex, None) (slice, Iterable[None]) 이 메세지가
                    #     # self.btns_etc[n]  에서 나타났는데  결국 원인을 찾지 못하였고, n 에 대한 노란밑줄을 무시처리했다.
                    #     self.btns_etc[n] = QPushButton(f'{self.btns[3:][n]}')  # noqa
                    #     self.btns_etc[n].setStyleSheet("background-color: rgba(0, 0, 0, 0);  color: white;")  # noqa
                    #     self.btns_etc[n].clicked.connect(partial(self.update_btn_text_clicked_and_close, self.btns[3:][n]))  # noqa
                    #     self.btns_etc[n].setFont(Pyside6Util.get_font_for_pyside6(font_path=StateManagementUtil.GMARKETSANSTTFLIGHT_TTF))  # noqa
                    if len(self.btns) > 0 and self.btns[0]:
                        self.btn_positive = QPushButton(f'{self.btns[0]} (F1)')
                        self.btn_positive.setStyleSheet("background-color: rgba(0, 0, 0, 0);  color: white;")
                        self.btn_positive.clicked.connect(partial(self.update_btn_text_clicked_and_close, self.btns[0]))
                        if BusinessLogicUtil.does_pnx_exist(src=file_pnx):
                            self.btn_positive.setFont(Pyside6Util.get_font_for_pyside6(font_path=file_pnx))
                        self.set_shortcut(function=partial(self.update_btn_text_clicked_and_close, self.btns[0]),
                                          key_plus_key="F1")  # 단축키 설정

                    if len(self.btns) > 1 and self.btns[1]:
                        self.btn_negative = QPushButton(f'{self.btns[1]} (F2)')
                        self.btn_negative.setStyleSheet("background-color: rgba(0, 0, 0, 0);  color: white;")
                        self.btn_negative.clicked.connect(partial(self.update_btn_text_clicked_and_close, self.btns[1]))
                        if BusinessLogicUtil.does_pnx_exist(src=file_pnx):
                            self.btn_negative.setFont(Pyside6Util.get_font_for_pyside6(font_path=file_pnx))
                        self.set_shortcut(function=partial(self.update_btn_text_clicked_and_close, self.btns[1]),
                                          key_plus_key="F2")  # 단축키 설정

                    if len(self.btns) > 2 and self.btns[2]:
                        self.btn_third = QPushButton(f'{self.btns[2]} (F3)')
                        self.btn_third.setStyleSheet("background-color: rgba(0, 0, 0, 0);  color: white;")
                        self.btn_third.clicked.connect(partial(self.update_btn_text_clicked_and_close, self.btns[2]))
                        if BusinessLogicUtil.does_pnx_exist(src=file_pnx):
                            self.btn_third.setFont(Pyside6Util.get_font_for_pyside6(font_path=file_pnx))
                        self.set_shortcut(function=partial(self.update_btn_text_clicked_and_close, self.btns[2]),
                                          key_plus_key="F3")  # 단축키 설정

                    for n, item in enumerate(self.btns[3:]):
                        self.btns_etc[n] = QPushButton(f'{item}')
                        self.btns_etc[n].setStyleSheet("background-color: rgba(0, 0, 0, 0);  color: white;")
                        self.btns_etc[n].clicked.connect(partial(self.update_btn_text_clicked_and_close, item))
                        self.btns_etc[n].setFont(
                            Pyside6Util.get_font_for_pyside6(font_path=StateManagementUtil.GMARKETSANSTTFLIGHT_TTF))

                except:
                    BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

                # except IndexError:
                #     # btns=[]의 index 를 초과하거나 부족한 경우
                #     pass
                # except TypeError:
                #     # btns=None 인 경우
                #     pass

                # 타이머에 의한 자동 버튼 클릭 설정
                if auto_click_negative_btn_after_seconds is not None:
                    self.seconds_remaining_until_auto_click = auto_click_negative_btn_after_seconds
                    self.is_closing_timer = True
                else:
                    self.is_closing_timer = False
                if auto_click_positive_btn_after_seconds is not None:
                    self.seconds_remaining_until_auto_click = auto_click_positive_btn_after_seconds
                    self.is_starting_timer = True
                else:
                    self.is_starting_timer = False
                # print(rf'self.is_closing_timer : {self.is_closing_timer}')
                # print(rf'auto_closing_seconds : {auto_click_negative_btn_after_seconds}')
                # print(rf'self.is_starting_timer : {self.is_starting_timer}')
                # print(rf'auto_starting_seconds : {auto_click_positive_btn_after_seconds}')
                if self.is_closing_timer == True and self.is_starting_timer == True:
                    BusinessLogicUtil.print_as_gui("closing_timer 와 starting_timer 는 동시에 설정 할 수 없습니다")
                    return

                if self.is_closing_timer == True or self.is_starting_timer == True:
                    self.auto_choice_timer = QTimer()
                    if auto_click_negative_btn_after_seconds is not None:
                        self.auto_choice_timer.timeout.connect(self.countdown_and_click_negative_btn)  # noqa
                    elif auto_click_positive_btn_after_seconds is not None:
                        self.auto_choice_timer.timeout.connect(self.countdown_and_click_positive_btn)  # noqa
                    self.auto_choice_timer.start(1000)

                # 레이아웃 설정
                self.layout_horizontal = QGridLayout()
                BusinessLogicUtil.print_as_log(string=rf'''self.btns="{self.btns}" %%%FOO%%%''')
                BusinessLogicUtil.print_as_log(string=rf'''len(self.btns)="{len(self.btns)}" %%%FOO%%%''')
                try:
                    if len(self.btns) > 0 and self.btns[0]:  # btns 리스트의 길이가 0보다 크고, 첫 번째 요소가 True인 경우
                        self.layout_horizontal.addWidget(self.btn_positive, 0, 0)
                    if len(self.btns) > 1 and self.btns[1]:  # btns 리스트의 길이가 1보다 크고, 두 번째 요소가 True인 경우
                        self.layout_horizontal.addWidget(self.btn_negative, 0, 1)
                    if len(self.btns) > 2 and self.btns[2]:  # btns 리스트의 길이가 2보다 크고, 세 번째 요소가 True인 경우
                        self.layout_horizontal.addWidget(self.btn_third, 0, 2)
                    try:
                        for n, item in enumerate(iterable=self.btns_etc):
                            self.layout_horizontal.addWidget(self.btns_etc[n], 0, n + 3)
                    except:
                        BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
                except:
                    BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

                layout_vertical = QVBoxLayout()
                # if len(contents.split("\n")) < 10:
                #     layout_vertical.addWidget(self.label)
                # else:
                layout_vertical.addWidget(self.scroll_area)
                if input_box_mode:
                    layout_vertical.addWidget(self.input_box)
                layout_vertical.addLayout(self.layout_horizontal)
                self.setLayout(layout_vertical)

                self.bring_this_window()
            except:
                BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

        # deprecating test
        # def centerOnScreen(self):
        #     # 현재 화면의 가운데 좌표를 계산
        #     screen_geometry = QScreen().geometry()
        #     x = (screen_geometry.width() - self.width()) // 2
        #     y = (screen_geometry.height() - self.height()) // 2
        #     self.move(x, y)

        def copy_label_text_to_clipboard(self):
            clipboard.copy(self.context)
            file_pnx = StateManagementUtil.POP_SOUND_POP_SOUND_WAV
            if BusinessLogicUtil.does_pnx_exist(src=file_pnx):
                BusinessLogicUtil.play_wav_file(StateManagementUtil.POP_SOUND_POP_SOUND_WAV)

        def countdown_and_click_positive_btn(self):
            mins, secs_remaining = MathUtil.get_minuites_and_remaining_secs(seconds=self.seconds_remaining_until_auto_click)
            if secs_remaining != 0:
                secs_remaining_with_unit = f"{secs_remaining}초"
            else:
                secs_remaining_with_unit = ""
            if mins != 0:
                mins_with_unit = f"{mins}분"
            else:
                mins_with_unit = ""
            self.btn_positive.setText(f"{self.btns[0]} ({mins_with_unit} {secs_remaining_with_unit} 뒤 자동클릭)")

            if self.seconds_remaining_until_auto_click == 0:
                if self.btns[0]:
                    self.update_btn_text_clicked_and_close(self.btns[0])
            self.seconds_remaining_until_auto_click = self.seconds_remaining_until_auto_click - 1

        def countdown_and_click_negative_btn(self):
            mins, secs_remaining = MathUtil.get_minuites_and_remaining_secs(seconds=self.seconds_remaining_until_auto_click)
            if secs_remaining != 0:
                secs_remaining_with_unit = f"{secs_remaining}초"
            else:
                secs_remaining_with_unit = ""
            if mins != 0:
                mins_with_unit = f"{mins}분"
            else:
                mins_with_unit = ""
            self.btn_negative.setText(f"{self.btns[1]} ({mins_with_unit} {secs_remaining_with_unit} 뒤 자동클릭)")

            if self.seconds_remaining_until_auto_click == 0:
                if self.btns[1]:
                    self.update_btn_text_clicked_and_close(self.btns[1])
            self.seconds_remaining_until_auto_click = self.seconds_remaining_until_auto_click - 1

        def bring_this_window(self):
            # self.activateWindow() 와 self.show() 의 위치는 서로 바뀌면 의도된대로 동작을 하지 않는다
            self.show()
            self.activateWindow()
            # import win32gui
            # active_window = win32gui.GetForegroundWindow()
            # win32gui.SetForegroundWindow(active_window)

    class CustomDialog():
        def __init__(self, q_application: QApplication, q_wiget: QWidget, is_app_instance_mode=False, is_exec_mode=True):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            """
            이 함수는 특별한 사용요구사항이 있습니다
            pyside6 앱 내에서 해당 함수를 호출할때는 is_app_instance_mode 를 파라미터에 넣지 않고 쓰는 것을 default 로 디자인했습니다.
            pyside6 앱 밖에서 해당 함수를 호출할때는 is_app_instance_mode 를 True 로 설정하고 쓰십시오.

            해당 사용요구사항이 생기게 된 이유는 다음과 같습니다
            pyside6 는 app을 singletone으로 instance를 구현합니다. 즉, instance는 반드시 pyside6 app 내에서 하나여야 합니다.
            pyside6의 QApplication()이 앱 내/외에서도 호출이 될 수 있도록 디자인했습니다.
            앱 내에서 호출 시에는 is_app_instance_mode 파라미터를 따로 설정하지 않아도 되도록 디자인되어 있습니다.
            앱 외에서 호출 시에는 is_app_instance_mode 파라미터를 True 로 설정해야 동작하도록 디자인되어 있습니다.
            앱 외에서 호출 시에는 반드시 CustomDialog() 인스턴스로 close()를 호출해 pyside6 app instance 를 종료 해야 합니다.
            """
            # 테스트 해보니, QApplication가 먼저 생성된 뒤에 QDialog 는 instance 가 생성되어야 하는 것같다.
            # 그래서 QDialog instance 를 CustomDialog 생성자의 파라미터로 못받는 것 같다.
            # 다른 Qwiget 을 받을 생각 이었는데...
            # 갑자기 든 생각인데. QApplication 도 같이 넘겨주면 되지 않을까?
            # 된다! 내 생각이 맞은 것 같다. QApplicaion() QDialog() 인스턴스의 생성순서만 바꿨는데 동작하지 않는다. 아무튼 QDialog 를 instance 인자로 받을 수 있다.
            file_pnx = StateManagementUtil.POP_SOUND_POP_SOUND_WAV
            if BusinessLogicUtil.does_pnx_exist(src=file_pnx):
                BusinessLogicUtil.play_wav_file(file_pnx=StateManagementUtil.POP_SOUND_POP_SOUND_WAV)

            self.is_app_instance_mode = is_app_instance_mode
            if is_app_instance_mode == True:
                self.app_instance = q_application
            # if is_exec_mode == False:
            #     global dialog
            dialog = q_wiget
            if is_exec_mode == True:
                dialog.exec()  # noqa
            self.btn_text_clicked = dialog.btn_text_clicked  # noqa

        def close(self):
            if self.is_app_instance_mode == True:
                if isinstance(self.app_instance, QApplication):
                    self.app_instance.exec()
            if self.is_app_instance_mode == True:
                # self.app_instance.quit()  # QApplication 인스턴스 quit 시도 : fail
                self.app_instance.shutdown()  # QApplication 인스턴스 shutdown 시도 : success  # 성공요인은 app.shutdown()이 호출이 되면서 메모리를 해제까지 수행해주기 때문
                # del self.app_instance  # QApplication 인스턴스 del 시도 : fail
                # self.app_instance.deleteLater()  # QApplication delete later 시도 : fail
                # self.app_instance = None  # QApplication 인스턴스 None 시도 : fail
                # sys.exit()

    class RpaProgramMainWindow(QWidget):
        # class RpaProgramMainWindow(QDialog):
        # class RpaProgramMainWindow(QMainWindow):
        # def __init__(self, shared_obj): # shared_obj 는 창간 통신용 공유객체 이다. pyside6 app 의 상태관리
        def __init__(self, q_application):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

            file_pnx = StateManagementUtil.POP_SOUND_POP_SOUND_WAV
            if BusinessLogicUtil.does_pnx_exist(src=file_pnx):
                BusinessLogicUtil.play_wav_file(file_pnx=file_pnx)
            super().__init__()
            self.app = q_application

            # deprecated test started at 2023 12 23 01 28
            # self.prompt_window = None
            # self.sub_window = None
            # self.question = None

            #  앱 전역 변수 설정
            self.text = "text"
            self.pw = "`"
            self.id = "`"
            # self.is_window_maximized = False
            self.display_width = BusinessLogicUtil.get_display_info()['width'],
            self.display_height = BusinessLogicUtil.get_display_info()['height'],
            # self.display_width_default = int(int(self.display_width[0]) * 0.106)
            # self.display_width_default = int(int(self.display_width[0]) * 0.045)
            # self.display_width_default = int(int(self.display_width[0]) * 0.02)
            self.display_width_default = int(int(self.display_width[0]) * 0.01)
            self.display_height_default = int(int(self.display_height[0]) * 0.2)

            #  메인창 설정
            self.setWindowTitle('.')
            icon_png = rf"{StateManagementUtil.PROJECT_DIRECTORY}\pkg_png\icon.PNG"
            self.setWindowIcon(QIcon(icon_png))  # 메인창 아이콘 설정
            # self.setAttribute(Qt.WA_TranslucentBackground) # 메인창 블러 설정
            # self.setWindowFlags(Qt.WindowType.FramelessWindowHint) # 메인창 최상단 프레임레스 설정
            GlobalBlur(self.winId(), hexColor=False, Acrylic=False, Dark=True, QWidget=self)
            self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)  # 최대화 최소화 버튼 숨기기
            self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 모든 창 앞에 위치하도록 설정
            self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
            # self.setStyleSheet(pyqt6css.qss)
            # self.setAttribute(Qt.WA_TranslucentBackground)
            # blur(self.winId())
            # self.scale = 1/1
            # self.scale = 1/2
            # self.scale = 1/3
            # self.scale = 1 / 4
            # self.scale = 1 / 10
            # self.setGeometry(0, 0, int(self.display_width_default * self.scale), int(self.display_height_default * self.scale))
            # self.setGeometry(0, 0,self.display_width_default, self.display_height_default)
            # self.resize(self.display_width_default, self.display_height_default)

            # self.setGeometry(0, 0, int(self.display_width_default * self.scale), int(self.display_height[0]))
            self.windows_size_mode = 1  # 창크기 모드 설정  #0 ~ 3
            QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # 고해상도 스케일링을 활성화합니다.
            self.screens = QGuiApplication.screens()  # 사용 가능한 모든 화면을 가져옵니다.

            # inputbox 설정
            # self.inputbox = QLineEdit(self)
            # self.inputbox.setStyleSheet("color: rgba(255,255,255, 0.9);")
            # self.inputbox.setText("0,0")
            # self.inputbox.setFixedWidth(120)
            # # self.inputbox.setStyleSheet("text-shadow: 1px 1px 7px rgba(1, 1, 1, 1);") #텍스트에 그림자 넣고 싶었는데 안된다.
            # self.inputbox.textChanged.connect(self.inputbox_changed)
            # self.inputbox.editingFinished.connect(self.inputbox_edit_finished)
            # self.inputbox.returnPressed.connect(self.inputbox_return_pressed)

            # 이벤트 가 많으면 프로그램이 늦어지는 것 같아보였다

            # monitor_mouse_position 이벤트 설정
            # self.listener = pynput.mouse.Listener(on_move=self.monitor_mouse_position) # 아주 빠르게 마우스 움직임 감지
            # self.listener.start()

            # monitor_mouse_position_per_second 이벤트 설정 (마우스 멈춤 감지 이벤트/ 5초간 마우스 중지 시 메인화면 자동 숨김 이벤트)
            self.mouse_positions = []
            self.previous_position = None
            self.current_position = None
            self.timer = QTimer()
            self.timer.timeout.connect(self.monitor_mouse_position_per_second)  # noqa
            self.timer.start(1000)

            # mkr_단축키 설정
            self.available_shortcut_list = {
                # 버튼있는 SHORCUT #단축키 설정 #CODE RELATIONAL AREA 1/5
                'HIDE': 'Esc',  # GHOST MODE?
                'EXIT': 'Q',
                'BACK UP TARGET': 'S',
                'ASK AI QUESTION': 'A',
                'SHOOT SCREENSHOT FULL': 'F',
                'SHOOT SCREENSHOT CUSTOM': 'C',
                'SHOOT SCREENSHOT FOR RPA': '4',
                'ANI': '5',  # nyaa.si
                'EXPLORER': 'O',
                'SYNC SERVICES': '`',
                'TEST': '1',
                'BACKUP SERVICES': '2',  # BACK UP TARGET 인데, 버튼 지우게 되면 이걸로
                'PROJECT DIRECTORY': 'P',
                "CLASSIFY SPECIAL FILES": "F2",
                "GATHER EMPTY DIRECTORY": "F3",
                "GATHER SPECIAL FILES": "F4",
                "GATHER USELESS FILES": "F5",
                "MERGE DIRECTORIES": "F6",
                "CONVERT MKV TO WAV": "F7",
                'DOWNLOAD YOUTUBE(webm)': 'F8',
                'DOWNLOAD YOUTUBE(webm)_': 'F9',
                'DOWNLOAD VIDEO FROM WEB1': 'Alt+F1',
                'DOWNLOAD VIDEO FROM WEB2': 'Alt+F2',
                'ROTATE WINDOW MODE': 'Alt+W',
                'SYSTEM REBOOT': 'Alt+9',
                'SYSTEM SHUTDOWN': 'Alt+]',
                'SYSTEM POWER SAVING MODE': 'Alt+[',
                # 'LOGIN': 'Alt+F7',
                'EMPTY RECYCLE BIN': 'Alt+E',
                # 'RUN CMD.EXE AS ADMIN': 'Alt+C',
                'NAVER MAP': 'Alt+N',
                # 'WEB CRAWL HREF': "`+F1", # fail
                'WEB CRAWL HREF': "Ctrl+F1",
                'WEB CRAWL YOUTUBE VIDEO TITLE AND URL': "Ctrl+F2",
                'WEB CRAWL YOUTUBE VIDEO PLAYLIST': "Ctrl+F3",
                'rdp-82106': 'R+1',
                # 'DOWNLOAD YOUTUBE(wav)': 'S',
                # 'DOWNLOAD YOUTUBE(webm) ONLY SOUND': 'Alt+S',

            }

            # 버튼없는 SHORCUT #단축키 설정 #shortcut #mkr2024
            self.set_shortcut('TEST', self.should_i_start_test)
            self.set_shortcut('BACK UP TARGET', self.should_i_back_up_target)
            # self.set_shortcut('RUN CMD.EXE AS ADMIN', self.run_cmd_exe)
            # self.set_shortcut('DOWNLOAD YOUTUBE(wav)', self.download_youtube_as_wav)
            # self.set_shortcut('DOWNLOAD YOUTUBE(webm) ONLY SOUND', self.download_youtube_as_webm_only_sound)
            self.set_shortcut('DOWNLOAD YOUTUBE(webm)_', self.should_i_download_youtube_as_webm_alt)
            # self.set_shortcut('LOGIN', self.login)
            # self.set_shortcut('NO PASTE MEMO', self.run_no_paste_memo)
            self.set_shortcut('PROJECT DIRECTORY', self.open_project_directory)
            self.set_shortcut('rdp-82106', self.should_i_connect_to_rdp1)
            self.set_shortcut('ASK AI QUESTION', self.ask_something_to_ai)
            self.set_shortcut('DOWNLOAD YOUTUBE(webm)', self.should_i_download_youtube_as_webm)
            self.set_shortcut('EMPTY RECYCLE BIN', self.should_i_empty_trash_can)
            # self.set_shortcut('ENG TO KOR', self.should_i_translate_eng_to_kor)
            # self.set_shortcut('KOR TO ENG', self.should_i_translate_kor_to_eng)
            self.set_shortcut('HIDE', self.toogle_rpa_window)
            self.set_shortcut('EXIT', self.should_i_exit_this_program)
            self.set_shortcut('SYSTEM POWER SAVING MODE', self.should_i_enter_to_power_saving_mode)
            self.set_shortcut('SYSTEM REBOOT', self.should_i_reboot_this_computer)
            self.set_shortcut('SYSTEM SHUTDOWN', self.should_i_shutdown_this_computer)
            self.set_shortcut('ROTATE WINDOW MODE', self.rotate_window_size_mode)
            self.set_shortcut('SHOOT SCREENSHOT CUSTOM', self.shoot_screenshot_custom)
            self.set_shortcut('SHOOT SCREENSHOT FULL', self.shoot_screenshot_full)
            self.set_shortcut('NAVER MAP', self.should_i_find_direction_via_naver_map)
            self.set_shortcut('ANI', self.should_i_show_animation_information_from_web)
            self.set_shortcut('DOWNLOAD VIDEO FROM WEB1', self.download_video_from_web1)
            self.set_shortcut('DOWNLOAD VIDEO FROM WEB2', self.download_video_from_web2)
            # self.set_shortcut('RECORD MACRO', self.should_i_record_macro)
            # self.set_shortcut('UP AND DOWN GAME', self.run_up_and_down_game)
            self.set_shortcut("CLASSIFY SPECIAL FILES", self.should_i_classify_special_files)
            self.set_shortcut("GATHER EMPTY DIRECTORY", self.should_i_gather_empty_directory)
            # self.set_shortcut("GATHER SPECIAL FILES", self.should_i_gather_special_files)
            self.set_shortcut("GATHER USELESS FILES", self.should_i_gather_useless_files)
            self.set_shortcut("MERGE DIRECTORIES", self.should_i_merge_directories)
            self.set_shortcut("CONVERT MKV TO WAV", self.should_i_convert_mkv_to_wav)
            self.set_shortcut("WEB CRAWL HREF", self.should_i_crawl_a_tag_href)
            self.set_shortcut("WEB CRAWL YOUTUBE VIDEO TITLE AND URL", self.should_i_crawl_youtube_video_title_and_url)
            self.set_shortcut("WEB CRAWL YOUTUBE VIDEO PLAYLIST", self.should_i_crawl_youtube_playlist)
            self.set_shortcut("EXPLORER", self.should_i_explorer)
            self.set_shortcut("SYNC SERVICES", self.should_i_sync)
            self.set_shortcut("BACKUP SERVICES", self.should_i_back_up_target)

            # 버튼있는 버튼
            # self.btn_to_open_project_directory = self.get_btn(self.get_btn_name_promised('PROJECT DIRECTORY'), self.open_project_directory)

            # 버튼있는 단축키
            # self.btn_to_open_project_directory_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('PROJECT DIRECTORY'), function=self.open_project_directory)
            # self.btn_to_back_up_target_only_shortcut_name = self.get_btn(btn_text_align="right", btn_name=self.get_shortcut_name_promised('BACK UP TARGET'), function=self.should_i_back_up_target)

            print(f'{StateManagementUtil.UNDERLINE}단축키')
            temp = ''
            for key in self.available_shortcut_list:
                value = self.available_shortcut_list[key]
                print(f'{value}         {key}')
                temp = temp + '\n' + f'{value}         {key}'

            # 레이블로 설정
            html = f"<html><body><h1 style='color: white;'>{temp}</h1></body></html>"
            text_browser = QTextBrowser()
            text_browser.setHtml(html)
            text_browser.resize(800, 600)

            text_browser2 = QTextBrowser()
            text_browser2.setHtml(html)
            text_browser2.resize(800, 600)

            text_browser3 = QTextBrowser()
            text_browser3.setHtml(html)
            text_browser3.resize(800, 600)

            text_browser4 = QTextBrowser()
            text_browser4.setHtml(html)
            # text_browser4.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: white;")  # 메시지박스창 스타일시트 적용 설정
            text_browser4.resize(800, 600)

            # btns 설정 5/5
            btns = [
                # [text_browser, text_browser2],  # BLANK #여백
                # [text_browser3, text_browser4], #BLANK #여백
                # [self.btn_to_should_i_exit_this_program, self.btn_to_should_i_exit_this_program_only_shortcut_name],
                # [self.btn_to_toogle_rpa_window, self.btn_to_toogle_rpa_window_only_shorcut_name],
                # [self.btn_to_rotate_window_size_mode, self.btn_to_rotate_window_size_mode_only_shortcut_name],
                # [self.btn_to_should_i_empty_trash_can, self.btn_to_should_i_empty_trash_can_only_shortcut_name],
                # [self.btn_to_should_i_enter_to_power_saving_mode, self.btn_to_should_i_enter_to_power_saving_mode_only_shortcut_name],
                # [self.btn_to_classify_special_files, self.btn_to_classify_special_files_only_shortcut_name],
                # [self.btn_to_gather_empty_directory, self.btn_to_gather_empty_directory_only_shortcut_name],
                # [self.btn_to_merge_directories, self.btn_to_merge_directories_only_shortcut_name],
            ]

            # GRID SETTING
            grid = QtWidgets.QGridLayout(self)

            # GRID COORDINATION REFERENCE (ROW, COLUMN)
            #        0,0  0,1  0,2
            #        1,0  1,1  1,2
            #        2,0  2,1  2,2

            # spaver

            # GRID_COLUMN 1 폭 조절용 policy
            # size_policy = QSizePolicy()
            # grid.setHorizontalPolicy(QSizePolicy.Minimum)  # 그리드의 열의 폭을 최소로 설정합니다.
            grid.setVerticalSpacing(9)
            grid.setHorizontalSpacing(5)
            grid.setColumnMinimumWidth(1, 125)
            grid.setColumnMinimumWidth(2, 45)

            btns_grid = btns
            line_no = 0
            for btn in btns_grid:
                grid.addWidget(btn[0], line_no, 0)  # GRID_COLUMN 0 설정
                grid.addWidget(btn[1], line_no, 2)  # GRID_COLUMN 1 설정
                line_no = line_no + 1

            # 화면실행
            def do_once():
                self.rotate_window_size_mode()
                self.timer2.stop()

            self.timer2 = QTimer()
            self.timer2.timeout.connect(do_once)  # noqa
            # self.timer2.start(500)
            self.timer2.start(50)

            # TEST
            # self.inputbox = QPlainTextEdit(self)
            # self.inputbox = QTextEdit(self)
            # self.ta1 = QTableWidget(self)
            # self.ta1.resize(500, 500)
            # self.ta1.setColumnCount(3)
            # self.ta1.setStyleSheet("color: rgba(255,255,255, 0.9);")
            # self.ta1.setStyleSheet("background-color: rgba(255,255,255, 0.9);")
            # table_column = ["첫번째 열", "두번째 열", "Third 열"]
            # self.ta1.setHorizontalHeaderLabels(table_column)

            # # 행 2개 추가
            # self.ta1.setRowCount(2)

            # # 추가된 행에 데이터 채워넣음
            # self.ta1.setItem(0, 0, QTableWidgetItem("(0,0)"))
            # self.ta1.setItem(0, 1, QTableWidgetItem("(0,1)"))
            # self.ta1.setItem(1, 0, QTableWidgetItem("(1,0)"))
            # self.ta1.setItem(1, 1, QTableWidgetItem("(1,1)"))

            # 마지막에 행 1개추가
            # self.ta1.insertRow(2)
            # self.ta1.setItem(2, 0, QTableWidgetItem("New Data"))

            # 셀의 텍스트 변경
            # self.ta1.item(1, 1).setText("데이터 변경")

            # 셀에 있는 텍스트 출력
            # print(self.ta1.item(0, 1).text())

            # 테이블 데이터 전부 삭제
            # self.ta1.clear()

            # 테이블 행전부 삭제
            # self.ta1.setRowCount(0)

            self.scroll_area = QScrollArea()
            self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
            self.scroll_area.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
            self.scroll_area.setStyleSheet(f" border: none; width: {self.display_width_default}px; height: {self.display_height_default}px")
            self.scroll_area.setLayout(grid)

            # 레이아웃 설정
            layout = QVBoxLayout(self)
            layout.addWidget(self.scroll_area)

            self.setMouseTracking(True)  # pyside6 창 밖에서도 마우스 추적 가능 설정 # 마우스 움직임 이벤트 감지 허용 설정
            # self.toogle_rpa_window()
            # BusinessLogicUtil.press("alt", "w")

            self.move_this_window_to_front()

            self.btn_text_clicked = "foo"

            # self.event_loop = QEventLoop()
            # self.event_loop.exec()

            # self.exec()

        def monitor_mouse_position_per_second(self):
            """마우스 움직임 감지 함수"""
            x, y = pyautogui.position()  # 현재 마우스 위치 ( 이게 내가 원하던 수치 )
            # print(x, y)
            self.current_position = QCursor.pos()  # 현재 마우스 커서 위치 ( 이건 내가 원하는 수치는 아닌데... 뭘 의미하는 거지? )
            # print(self.current_position)
            if self.previous_position is not None and self.previous_position == self.current_position:
                # print("마우스가 멈췄습니다")
                # print(f"self.mouse_positions : {self.mouse_positions}") # 마우스 위치 리스트
                if 10 <= len(self.mouse_positions):
                    # 10번 연속 mouse 중지 감지
                    # self.mouse_positions 에 등록된 모든 self.current_position 가 동일하면 10번 연속으로 움직이지 않은 것으로 판단
                    if len(self.mouse_positions) == 10:
                        # 동일한 10개 원소를 갖는 리스트 내에서 요소의 중복을 제거하면 중복이 제거된 리스트의 요소의 수는 1개가 나올 것을 기대
                        mouse_positions_removed_duplicatd_elements = list(set(self.mouse_positions))  # orderless way
                        if len(mouse_positions_removed_duplicatd_elements) == 1:
                            # print("10번 연속 중지 감지")
                            self.hide()
                            pass

                if 5 <= len(self.mouse_positions):
                    self.mouse_positions = []  # 감지값들이 5개 이상이면 감지값목록 초기화

                elif len(self.mouse_positions) < 5:
                    self.mouse_positions.append(self.current_position)
                pass
            else:
                pass
                # print("마우스가 움직였습니다")

                # mkr_우측하단 꼭지점 부근 네비게이션
                # if 3440 - 25 <= x and 1440 - 25 <= y:
                #     BusinessLogicUtil.press("win", "d", interval=0.15)

                # 우측 네비게이션
                # if 3440 - 50 <= x <= 3440 and 300 <= y <= 1440:
                #     try:
                #         BusinessLogicUtil.run_pnx_via_explorer_exe(BusinessLogicUtil.PYCHARM64_EXE)
                #     except:
                #         BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
                #         pass

                # 좌측 네비게이션
                # elif 0 <= x <= 15 and 0 <= y <= 1440:
                #     self.toogle_rpa_window()
                #     pass

                # else:
                #     pass
            self.previous_position = self.current_position

        def monitor_mouse_position(self, x, y):
            # 상단 네비게이션
            if 0 <= x <= 3440 and 0 <= y <= 25:
                pass
            else:
                pass

        @staticmethod
        # def rpa_program_method_decorator(function):
        def rpa_program_method_decorator(function: Callable[[T], None]):
            def wrapper(self):
                file_pnx = StateManagementUtil.POP_SOUND_POP_SOUND_WAV
                if BusinessLogicUtil.does_pnx_exist(src=file_pnx):
                    BusinessLogicUtil.play_wav_file(file_pnx=file_pnx)
                self.hide()  # 비동기 전까지는 사용자가 다른 명령을 하지 못하도록 이 코드를 사용
                function(self)
                self.move_this_window_to_front()

            return wrapper

        def eventFilter(self, obj, event):
            # if event.type() == QEvent.MouseMove:
            #     x = event.globalX()
            #     y = event.globalY()
            #     print(f"마우스 이동 - X: {x}, Y: {y}")
            # return super().eventFilter(obj, event)
            if event.type() == QEvent.MouseButtonPress and not self.rect().contains(event.pos()):
                print("pyside6 창 외부 클릭 되었습니다")
            return super().eventFilter(obj, event)

        def mousePressEvent(self, e):
            if e.button() == Qt.LeftButton:  # 왼쪽 버튼 클릭 시 동작
                # print(f"mouse press event monitor: LeftButton pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
                pass
            elif e.button() == Qt.RightButton:
                print(f"mouse press event monitor: RightButton pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.BackButton:
                print(f"mouse press event monitor: BackButton pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton1:
                print(f"mouse press event monitor: ExtraButton1 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton10:
                print(f"mouse press event monitor: ExtraButton10 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton11:
                print(f"mouse press event monitor: ExtraButton11 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton12:
                print(f"mouse press event monitor: ExtraButton12 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton13:
                print(f"mouse press event monitor: ExtraButton13 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton14:
                print(f"mouse press event monitor: ExtraButton14 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton15:
                print(f"mouse press event monitor: ExtraButton15 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton16:
                print(f"mouse press event monitor: ExtraButton16 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton17:
                print(f"mouse press event monitor: ExtraButton17 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton18:
                print(f"mouse press event monitor: ExtraButton18 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton19:
                print(f"mouse press event monitor: ExtraButton19 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton2:
                print(f"mouse press event monitor: ExtraButton2 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton20:
                print(f"mouse press event monitor: ExtraButton20 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton21:
                print(f"mouse press event monitor: ExtraButton21 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton22:
                print(f"mouse press event monitor: ExtraButton22 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton23:
                print(f"mouse press event monitor: ExtraButton23 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton24:
                print(f"mouse press event monitor: ExtraButton24 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton3:
                print(f"mouse press event monitor: ExtraButton3 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton4:
                print(f"mouse press event monitor: ExtraButton4 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton5:
                print(f"mouse press event monitor: ExtraButton5 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton6:
                print(f"mouse press event monitor: ExtraButton6 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton7:
                print(f"mouse press event monitor: ExtraButton7 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton8:
                print(f"mouse press event monitor: ExtraButton8 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ExtraButton9:
                print(f"mouse press event monitor: ExtraButton9 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.ForwardButton:
                print(f"mouse press event monitor: ForwardButton pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.LeftButton:
                print(f"mouse press event monitor: LeftButton pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.MiddleButton:
                print(f"mouse press event monitor: MiddleButton pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.NoButton:
                print(f"mouse press event monitor: NoButton pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.TaskButton:
                print(f"mouse press event monitor: TaskButton pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.XButton1:
                print(f"mouse press event monitor: XButton1 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")
            elif e.button() == Qt.XButton2:
                print(f"mouse press event monitor: XButton2 pressed at {str(e.pos().x())} ,{str(e.pos().y())} ")

        # def mouseReleaseEvent(self, e):
        #     self.label10.setText(f"event monitor:\nmouseReleaseEvent : {str(e.pos().x())} ,{str(e.pos().y())} ")
        #
        # def mouseDoubleClickEvent(self, e):
        #     self.label10.setText(f"event monitor:\nmouseDoubleClickEvent : {str(e.pos().x())} ,{str(e.pos().y())} ")

        def keyPressEvent(self, e):
            self.mouse_positions = []  # 키보드가 눌리면 사용자가 사용중인 것으로 간주하고 마우스 위치 값 목록 초기화

        # def keyPressEvent(self, e):
        #     # these keys refered from https://doc.qt.io/qtforpython-6/PySide6/QtCore/Qt.html
        #     # 테스트 결과 한/영, 한자 인식안됨.
        #     if e.key() == Qt.Key_Return:
        #         self.label11.setText(f"keyboard event monitor:\nKey_Return : Key_Return ")
        #         self.showMinimized()
        #         BusinessLogicUtil.press("space")
        #         self.showMaximized()
        #     elif e.key() == Qt.Key_0:
        #         self.label11.setText(f"keyboard event monitor:\nKey_0 : Key_0 ")
        # deprecated test
        # def inputbox_changed(self):
        #     BusinessLogicUtil.print_as_log("inputbox 텍스트 change event 감지 되었습니다")
        #     print(self.inputbox.ment())
        #
        # def inputbox_edit_finished(self):
        #     BusinessLogicUtil.print_as_log("inputbox edit finish event 감지 되었습니다")
        #
        # def inputbox_return_pressed(self):
        #     BusinessLogicUtil.print_as_log("inputbox return pressed event 감지 되었습니다")

        def get_btn_name_with_shortcut_name(self, button_name_without_shortcut):
            # 버튼명과 shourtcut 명을 을 적당한 간격으로 띄워서 string 으로 반환하는 코드, 폰트 가 고정폭폰트 가 아니면 무용지물인 함수
            numbers = []
            for key, value in self.available_shortcut_list.items():
                numbers.append(len(value) + len(key))
            max_len_value = max(numbers)
            button_name_with_short_cut = ""
            for key, value in self.available_shortcut_list.items():
                if key == button_name_without_shortcut:
                    space_between = " " * (max_len_value - len(key) - len(value) + 1)
                    # space_between = "\t"
                    # button_name_with_short_cut = button_name_with_short_cut + f"{key}{space_between}{value}".strip()
                    # button_name_with_short_cut = button_name_with_short_cut + f"{key}{space_between}( {value} )".strip()
                    button_name_with_short_cut = button_name_with_short_cut + f"{value}{space_between}( {key} )".strip()
            print(button_name_with_short_cut)
            return button_name_with_short_cut

        def get_btn_name_promised(self, button_name_without_shortcut):
            button_name_with_short_cut = ""
            for key, value in self.available_shortcut_list.items():
                if key == button_name_without_shortcut:
                    button_name_with_short_cut = button_name_with_short_cut + f"{key}".strip()
            return button_name_with_short_cut

        def get_shortcut_name_promised(self, button_name_without_shortcut):
            button_name_with_short_cut = ""
            for key, value in self.available_shortcut_list.items():
                if key == button_name_without_shortcut:
                    button_name_with_short_cut = button_name_with_short_cut + f"{value}".strip()
            return button_name_with_short_cut

        # def show_available_shortcut_list(self):
        #     # global max
        #     # global 을 설정하면, 이 변수는 함수의 실행이 끝난 다음에도 없어지지 않는다.
        #     # 이 값을 나중에 함수 끝나고도 또 쓸려면 이렇게 쓰면 되겠다. @staticmethod 의 경우에는 변수 간의 값에 간섭이 되지 않도록 굳이 쓰지 않는 것이 좋겠다.
        #     # global 많이 쓰면 이는 변수가 전역화 되니까 메모리의 성능이 저하되는 것이 아닐까?
        #     # 그렇다면 함수 내에서만 전역적으로 변수를 쓰는 경우에, global 을 쓰지 않는 것이 성능을 위해서는 좋은 선택이겠다. 굳이 함수가 끝난 뒤에 밖에서 써야한다면 global 을 써야 겠지만, 나는 무척이나 이게 헷갈릴 것 같다
        #     # 그동안의 경험으로는 코드 맥락 상, global 선언을 하지 않아도 전역변수 처럼 작동 되는 것 같아 보인다.... 아니다 이게 global max 를 선언하지 않았다고 가정하면 max 는 show_available_shortcut_list() 가 종료되면 max 는 사라진다. 그런데 global max를 선언하면 max 는 유지된다!
        #     # 혹시 객체의 인스턴스 같은 것을 global 을 통해서 변수에 저장하고 쓰면 싱글톤 처럼 쓸 수 있는 것일까? 메모리 효율은 많이 나빠질까?
        #
        #     numbers = []
        #     for key_shortcut, value in self.available_shortcut_list.items():
        #         numbers.append(len(value))
        #     max_no: int
        #     max_no = max(numbers)
        #     for key_shortcut, value in self.available_shortcut_list.items():
        #         print(f"{{0: <{max_no}}} : {key_shortcut}".format(value))

        def rotate_window_size_mode(self):
            if self.windows_size_mode == 0:
                self.resize(self.display_width_default, self.display_height_default)
                self.move_window_to_center()  # 불필요 하면 주석하는 게 나쁘지 않겠다
                self.windows_size_mode = self.windows_size_mode + 1
            elif self.windows_size_mode == 1:
                self.setGeometry(0, 0, int(self.display_width_default), int(self.display_height[0]))
                # self.setWindowFlags(Qt.WindowStaysOnTopHint)  # 모든 창 앞에 위치하도록 설정
                self.windows_size_mode = self.windows_size_mode + 1
            elif self.windows_size_mode == 2:
                self.showMaximized()
                self.windows_size_mode = self.windows_size_mode + 1
            elif self.windows_size_mode == 3:
                self.setGeometry(1600 - int(self.display_width_default), 0, int(self.display_width_default), int(self.display_height[0]))
                self.windows_size_mode = 0

        def set_shortcut(self, shortcut_key_promised, function):
            # self.shortcut = QShortcut(QKeySequence(self.available_shortcut_list[btn_name_promised]), self)  # ctrl+1 2개 키들의 조합 설정
            self.shortcut = QShortcut(self.available_shortcut_list[shortcut_key_promised], self)  # ctrl+n+d 3개 키들의 조합 설정 시도
            self.shortcut.activated.connect(function)
            pass

        def get_btn(self, btn_name, function, btn_text_align="left"):
            button = QPushButton(btn_name, self)  # alt f4 로 가이드 해도 되겠다. 이건 그냥 설정 되어 있는 부분.
            button.clicked.connect(function)

            # 2023년 12월 14일 (목) 16:28:15
            # 결론, fixed width font로 시도해볼 수 있다 자릿 수를 맞출 수 있다.
            # non-fixed width font 이슈 JAVA 에서도 구현했을 때 마딱드렸던 내용인데,
            # 분명히 문장 전체 길이를 단어 사이의 공백의 수를 결정짓는 함수를 테스트 했음에도 자릿수가 맞지 않았는데
            # 이는 고정 폭이 아님이기 때문이었다 따라서 고정 폭 폰트로 출력되는 콘솔에서는 정상, 비고정 폭 폰트로 출력되는 콘솔에서는 비정상,
            # 이 경우에는 콘솔이 아니라 pyside6 로 만든 UI 에서 나타났다.
            # 새벽에 이 문제를 만나서 잠깐 넋나갔는데 아침에 다시보니 그때 경험이 떠올라서 실험해보니 잘 해결되었다. 덕분에 pyside6에서 위젯에 폰트 적용하는 법도 터득

            # pyside6 버튼 내장폰트 설정
            # pyside6 built in fixed width font
            # font = QFont("Monospace")
            # font = QFont("Ubuntu Mono")
            # font = QFont("Inconsolata")
            # font = QFont("Monaco")
            # font = QFont("Courier")
            # font = QFont("Courier 10 Pitch")
            # font = QFont("Courier Prime")
            # font = QFont("Droid Sans Mono")
            # font = QFont("Fira Mono")
            # font = QFont("Hack")
            # font = QFont("Menlo")
            # font = QFont("Monofur")
            # font = QFont("Noto Mono")
            # font = QFont("PT Mono")
            # font = QFont("Roboto Mono")
            # font = QFont("Source Code Pro")
            # font = QFont("Victor Mono")
            # font = QFont("Courier New")
            # font = QFont("Liberation Mono")
            # font = QFont("DejaVu Sans Mono")
            # font = QFont("Consolas")  # 그나마 가장 마음에 드는 폰트

            # pyside6 버튼 외부폰트 설정
            button.setFont(Pyside6Util.get_font_for_pyside6(font_path=StateManagementUtil.GMARKETSANSTTFLIGHT_TTF))
            if btn_text_align == "right":
                # button.setStyleSheet("QPushButton { text-align: right; color: rgba(255,255,255, 0.9); height: 20px; font-size: 8px}")
                # button.setStyleSheet("QPushButton { text-align: right; color: rgba(255,255,255, 0.9);               font-size: 8px}")
                button.setStyleSheet("QPushButton { text-align: right; color: rgba(255,255,255, 0.9);               font-size: 13px}")
                # button.setStyleSheet("QPushButton { text-align: right; color: rgba(255,255,255, 0.9); height: 20px; font-size: 13px}")
                button.setFixedWidth(65)
                # button.setMinimumWidth(button.sizeHint().width())
            else:
                # button.setStyleSheet("QPushButton { text-align: left; color: rgba(255,255,255, 0.9); height: 20px; font-size: 8px}")
                # button.setStyleSheet("QPushButton { text-align: left; color: rgba(255,255,255, 0.9);                 font-size: 8px}")
                button.setStyleSheet("QPushButton { text-align: left; color: rgba(255,255,255, 0.9);                 font-size: 13px}")
                # button.setStyleSheet("QPushButton { text-align: left; color: rgba(255,255,255, 0.9); height: 20px; font-size: 13px}")
                button.setFixedWidth(225)
                # button.setMinimumWidth(button.sizeHint().width())
            return button

        def move_window_to_center(self):
            center = QScreen.availableGeometry(self.app.primaryScreen()).center()
            geo = self.frameGeometry()
            geo.moveCenter(center)
            self.move(geo.topLeft())
            # if self.screens:
            #     primary_screen = self.screens[0]  # 첫 번째 화면을 기본 화면으로 설정합니다.
            #     center = primary_screen.availableGeometry().center()  # 기본 화면의 중앙 좌표를 가져옵니다.
            #     # 화면을 가운데로 이동시키는 코드를 작성하세요.
            #     # 예시로 윈도우를 생성하고 중앙 좌표를 이용하여 위치를 설정합니다.
            #     self.setGeometry(100, 100, 500, 300)  # 윈도우의 초기 위치와 크기를 설정합니다.
            #     self.move(center - self.rect().center())  # 윈도우를 화면 중앙으로 이동시킵니다.

        @rpa_program_method_decorator
        def run_no_paste_memo(self):
            BusinessLogicUtil.speak_that_service_is_in_preparing()

        @rpa_program_method_decorator
        def should_i_reboot_this_computer(self):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.should_i_reboot_this_computer()

        @QtCore.Slot()
        def login(self):
            BusinessLogicUtil.speak_that_service_is_in_preparing()

        @rpa_program_method_decorator
        def should_i_show_animation_information_from_web(self):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.should_i_show_animation_information_from_web()

        @rpa_program_method_decorator
        def should_i_exit_this_program(self):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.should_i_exit_this_program()

        @rpa_program_method_decorator
        def should_i_find_direction_via_naver_map(self):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.should_i_find_direction_via_naver_map()

        @rpa_program_method_decorator
        def download_youtube_as_wav(self):
            BusinessLogicUtil.speak_that_service_is_in_preparing()

        @rpa_program_method_decorator
        def should_i_download_youtube_as_webm(self):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.should_i_download_youtube_as_webm()

        @rpa_program_method_decorator
        def should_i_download_youtube_as_webm_alt(self):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.should_i_download_youtube_as_webm_alt()

        @rpa_program_method_decorator
        def download_youtube_as_webm_only_sound(self):
            BusinessLogicUtil.speak_that_service_is_in_preparing()

        @rpa_program_method_decorator
        def should_i_shutdown_this_computer(self):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.should_i_shutdown_this_computer()

        @rpa_program_method_decorator
        def shoot_screenshot_custom(self):
            while True:
                asyncio.run(BusinessLogicUtil.shoot_custom_screenshot_via_asyncio())
                break

        @rpa_program_method_decorator
        def shoot_screenshot_full(self):
            while True:
                BusinessLogicUtil.collect_img_for_autogui()
                break

        @rpa_program_method_decorator
        def should_i_back_up_target(self):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.should_i_back_up_target()

        @rpa_program_method_decorator
        def should_i_start_test(self):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.should_i_start_test_core()

        @rpa_program_method_decorator
        def open_project_directory(self):
            project_directory = str(StateManagementUtil.PROJECT_DIRECTORY)
            BusinessLogicUtil.run_via_explorer_exe(project_directory)

        @rpa_program_method_decorator
        def should_i_enter_to_power_saving_mode(self):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.should_i_enter_to_power_saving_mode()

        @rpa_program_method_decorator
        def should_i_translate_eng_to_kor(self):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.should_i_translate_eng_to_kor()

        @rpa_program_method_decorator
        def should_i_translate_kor_to_eng(self):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.should_i_translate_kor_to_eng()

        @rpa_program_method_decorator
        def should_i_empty_trash_can(self):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.should_i_do(string="쓰레기통을 비울까요?", function=BusinessLogicUtil.empty_recycle_bin, auto_click_negative_btn_after_seconds=10)

        @rpa_program_method_decorator
        def run_cmd_exe_as_admin(self):
            BusinessLogicUtil.run_cmd_exe_as_admin()

        @rpa_program_method_decorator
        def ask_something_to_ai(self):
            BusinessLogicUtil.ask_something_to_ai()

        @rpa_program_method_decorator
        def should_i_connect_to_rdp1(self):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.mstsc()

        @rpa_program_method_decorator
        def should_i_record_macro(self):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.should_i_record_macro()


        @rpa_program_method_decorator
        def should_i_classify_special_files(self):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.should_i_classify_special_files()

        @rpa_program_method_decorator
        def should_i_gather_empty_directory(self):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.should_i_gather_empty_directory()

        @rpa_program_method_decorator
        def should_i_gather_useless_files(self):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.should_i_gather_pnxs_useless()

        @rpa_program_method_decorator
        def should_i_merge_directories(self):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.should_i_merge_directories()

        @rpa_program_method_decorator
        def should_i_convert_mkv_to_wav(self):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.should_i_convert_mkv_to_wav()

        @rpa_program_method_decorator
        def should_i_crawl_a_tag_href(self):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.should_i_crawl_a_tag_href()

        @rpa_program_method_decorator
        def should_i_crawl_youtube_video_title_and_url(self):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.should_i_crawl_youtube_video_title_and_url()

        @rpa_program_method_decorator
        def should_i_crawl_youtube_playlist(self):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.should_i_crawl_youtube_playlist()

        @rpa_program_method_decorator
        def should_i_explorer(self):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.should_i_explorer()

        @rpa_program_method_decorator
        def should_i_sync(self):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            # BusinessLogicUtil.should_i_sync()
            BusinessLogicUtil.should_i_sync_V_0_0_2()

        @rpa_program_method_decorator
        def download_video_from_web1(self):
            BusinessLogicUtil.download_video_from_web1()

        @rpa_program_method_decorator
        def download_video_from_web2(self):
            BusinessLogicUtil.download_video_from_web2()

        def toogle_rpa_window(self):
            # BusinessLogicUtil.print_as_log(f"def {inspect.currentframe().f_code.co_name}() is called...")
            if self.isHidden() and not self.isVisible():
                # console_blurred 프로그램 창 활성화
                self.move_this_window_to_front()
            else:
                self.hide()

        def move_this_window_to_front(self):
            # self.activateWindow() 와 self.show() 의 위치는 서로 바뀌면 의도된대로 동작을 하지 않는다
            self.show()
            self.activateWindow()
            # import win32gui
            # active_window = win32gui.GetForegroundWindow()
            # win32gui.SetForegroundWindow(active_window)

    class MacroWindow(QDialog):
        # class MacroWindow(QWidget):
        def __init__(self):
            super().__init__()
            file_pnx = StateManagementUtil.POP_SOUND_POP_SOUND_WAV
            if BusinessLogicUtil.does_pnx_exist(src=file_pnx):
                BusinessLogicUtil.play_wav_file(file_pnx=StateManagementUtil.POP_SOUND_POP_SOUND_WAV)

            #  매크로 창 전역 변수 설정
            self.previus_pressed_keys = []
            self.display_width = BusinessLogicUtil.get_display_info()['width'],
            self.display_height = BusinessLogicUtil.get_display_info()['height'],
            # self.display_width_default = int(int(self.display_width[0]) * 0.106)
            self.display_width_default = int(int(self.display_width[0]) * 0.06)
            self.display_height_default = int(int(self.display_height[0]) * 0.2)

            # 마우스 위치, 클릭 정보, 시간 정보를 저장할 리스트
            # self.positions = []

            # 녹화 시작 시간
            self.time_recording_start = time.time()
            # self.time_recording_start_rel = 0.0
            self.elapsed_full_recording_time = 0.0
            self.previous_time = time.time()
            self.time_recording_end = 0.0
            #  메인창 설정
            self.setWindowTitle('.')
            self.setWindowIcon(QIcon(StateManagementUtil.ICON_PNG))  # 메인창 아이콘 설정
            # self.setAttribute(Qt.WA_TranslucentBackground) # 메인창 블러 설정
            # self.setWindowFlags(Qt.WindowType.FramelessWindowHint) # 메인창 최상단 프레임레스 설정
            GlobalBlur(self.winId(), hexColor=False, Acrylic=False, Dark=True, QWidget=self)
            self.setWindowFlags(Qt.WindowTitleHint | Qt.WindowCloseButtonHint)  # 최대화 최소화 버튼 숨기기
            self.setStyleSheet("background-color: rgba(0, 0, 0, 0)")
            self.scale = 1 / 10
            self.windows_size_mode = 0  # 창크기 모드 설정  #0 ~ 3

            QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)  # 고해상도 스케일링을 활성화합니다.
            self.screens = QGuiApplication.screens()  # 사용 가능한 모든 화면을 가져옵니다.
            self.rotate_window_size_mode()

            # label 설정
            self.label = QLabel(self)
            self.label.setStyleSheet("color: rgba(255,255,255, 0.9);")
            self.label.setText(f"녹화 중...\n녹화경과시간: None\n")

            # 단축키 설정
            self.available_shortcut_list = {
                'MACRO EXCUTE': 'Ctrl+E',
                'MACRO EXIT': 'Ctrl+Q',
            }
            # self.set_shortcut('MACRO RECORD',self.record_macro)
            self.set_shortcut('MACRO EXCUTE', self.excute_macro)
            self.set_shortcut('MACRO EXIT', self.exit_macro)

            # 버튼 설정
            btn_to_excute_macro = self.get_btn(self.get_btn_name_with_shortcut_name('MACRO EXCUTE'), self.excute_macro)
            btn_to_exit_macro = self.get_btn(self.get_btn_name_with_shortcut_name('MACRO EXIT'), self.exit_macro)

            # GRID SETTING
            grid = QtWidgets.QGridLayout(self)
            btns = [
                self.label,
                btn_to_excute_macro,
                btn_to_exit_macro
            ]
            cnt = 0
            for i in btns:
                grid.addWidget(i, cnt, 0)
                cnt = cnt + 1

            # 레이아웃 설정
            layout = QGridLayout(self)
            layout.addLayout(grid, 0, 0)

            # 단일 단축키가 같이 눌리는 문제 ( ctrl + v 를 누르면   ctrl + v 에 바인딩된 함수만 호출되길 기대하는데, ctrl 에 바인딩된 함수도 호출되는 문제 )
            # 이벤트를 나누어 만들어 하나의 이벤트가 호출되면 다른 하나의 이벤트는 호출되지 않도록 설정 시도
            self.is_processing_event = False

            # Condition 객체 생성
            # self.condition = threading.Condition()

            # 이벤트 우선순위 설정
            # self.is_event_shortcut_3_processing = False # highest priority
            # self.is_event_shortcut_1_processing = False

            # 마우스 이동 이벤트 핸들러 설정
            listener = pynput.mouse.Listener(on_move=self.on_mouse_move)
            listener.start()

            # 마우스 버튼 클릭 이벤트 핸들러 설정
            listener2 = pynput.mouse.Listener(on_click=self.on_mouse_btn_clicked)
            listener2.start()

            # 키보드 이벤트 핸들러 설정 ( 3개 조합 단축키 , 2개 조합 단축키 , 단일 단축키 모두가능)
            self.keyboard_main_listener = pynput.keyboard.Listener(on_press=self.on_keys_down, on_release=self.on_keys_up)
            self.keyboard_main_listener.start()
            # 충돌이 문제가 아니고 두 이벤트가 중복이 되면 안되고 이벤트에 우선순위를 더 두어서 두 이벤트 호출 시 우선순위가 높은 이벤트만 실행되도록

            # self.is_processing_event = False

            # 이벤트 핸들러 스레드 생성
            # event1_thread = threading.Thread(target=self.listener3)
            # event2_thread = threading.Thread(target=self.listner_2_combination_shorcuts)

            # 이벤트 핸들러 스레드 시작
            # event1_thread.start()
            # event2_thread.start()

            # 키보드 이벤트 핸들러 설정 ( 단일 단축키 )
            # self.listener3 = pynput.keyboard.Listener(on_press=self.on_keboard_press, suppress=True)
            # self.listener3.start()

            # 모니터링 이벤트 설정
            # self.mouse_positions = []
            # self.previous_position = None
            # self.current_position = None
            # self.timer = QTimer()
            # self.timer.timeout.connect(self.on_left_mouse_btn_clicked)
            # self.timer.start(900)

            # 녹화 경과시간 업데이트
            self.timer2 = QTimer()
            self.timer2.timeout.connect(self.update_label)  # noqa # 해당 검사에 대해서는 예외 목록에 "connect"를 넣는 것을 권장합니다. jetbrain 오류로 다년간 지속된 것으로 생각 중이다,
            self.timer2.start(1000)

            BusinessLogicUtil.speak_ment_experimental(ment="매크로녹화를 시작합니다", comma_delay=0.98)

            # 매크로녹화시작 로깅
            log_title = "매크로녹화시작"
            contents = f"{StateManagementUtil.UNDERLINE}{TimeUtil.get_time_as_('%Y-%m-%d_%H:%M:%S')}{log_title}"
            BusinessLogicUtil.print_cyan(contents)
            self.save_macro_log(contents=contents)

            self.bring_this_window()

            # event_loop = QEventLoop()
            # event_loop.exec()

        def on_mouse_move(self, x, y):  # 아주 빠르게 감지
            # 이방식으로 매크로 중지를 할까?
            # print(f"마우스 이동 - X: {x}, Y: {y}")
            # print("마우스가 움직였습니다")
            # 상단 네비게이션
            if 0 <= x <= 3440 and 0 <= y <= 25:
                self.rotate_window_size_mode()
            else:
                pass

        def eventFilter(self, obj, event):
            if event.type() == QEvent.MouseMove:
                x = event.globalX()
                y = event.globalY()
                print(f"pyside6 창 외부 마우스 이동 감지 시도 - X: {x}, Y: {y}")
            return super().eventFilter(obj, event)

            # if event.type() == QEvent.MouseButtonPress and not self.rect().contains(event.pos()):
            #     print("pyside6 창 외부 클릭 되었습니다")
            # return super().eventFilter(obj, event)

        def get_btn_name_with_shortcut_name(self, button_name_without_shortcut):
            numbers = []
            for key, value in self.available_shortcut_list.items():
                numbers.append(len(value) + len(key))
            max_len_value = max(numbers)
            # print(max_len_value)

            button_name_with_short_cut = ""
            for key, value in self.available_shortcut_list.items():
                # print(key == button_name_without_shortcut)
                # print(key)
                # print(button_name_without_shortcut)

                if key == button_name_without_shortcut:
                    space_between = " " * (max_len_value - len(key) - len(value) + 1)
                    # space_between = " "
                    # space_between = str(max_len_value - len(key) - len(value) + 1)
                    # button_name_with_short_cut = button_name_with_short_cut + f"{key}{space_between}{value}\n"
                    button_name_with_short_cut = button_name_with_short_cut + f"{key}{space_between}{value}".strip()
            print(button_name_with_short_cut)
            return button_name_with_short_cut

        def rotate_window_size_mode(self):
            if self.windows_size_mode == 0:
                self.bring_this_window()
                self.setGeometry(0, 0, int(self.display_width_default / 2), int(self.display_height[0] / 5))
                self.move_window_to_center()
                self.windows_size_mode = self.windows_size_mode + 1
            elif self.windows_size_mode == 1:
                self.showMinimized()
                self.windows_size_mode = 0

        def set_shortcut(self, btn_name_promised, function):
            self.shortcut = QShortcut(self.available_shortcut_list[btn_name_promised], self)  # ctrl+n+d 3개 키들의 조합 설정 시도
            self.shortcut.activated.connect(function)
            pass

        def get_btn(self, btn_name, function):
            button = QPushButton(btn_name, self)
            button.clicked.connect(function)

            # 폰트 설정
            button.setFont(Pyside6Util.get_font_for_pyside6(font_path=StateManagementUtil.RUBIKDOODLESHADOW_REGULAR_TTF))  # 입체감있는 귀여운 영어 폰트
            button.setStyleSheet("QPushButton { text-align: left; color: rgba(255,255,255, 0.9); height: 20px ; font-size: 10px}")
            # button.setLayoutDirection(QtCore.Qt.)
            return button

        def move_window_to_center(self):
            # center = QScreen.availableGeometry(app.primaryScreen()).center()
            # geo = self.frameGeometry()
            # geo.moveCenter(center)
            # self.move(geo.topLeft())
            if self.screens:
                primary_screen = self.screens[0]  # 첫 번째 화면을 기본 화면으로 설정합니다.
                center = primary_screen.availableGeometry().center()  # 기본 화면의 중앙 좌표를 가져옵니다.
                # 화면을 가운데로 이동시키는 코드를 작성하세요.
                # 예시로 윈도우를 생성하고 중앙 좌표를 이용하여 위치를 설정합니다.
                self.setGeometry(100, 100, 500, 300)  # 윈도우의 초기 위치와 크기를 설정합니다.
                self.move(center - self.rect().center())  # 윈도우를 화면 중앙으로 이동시킵니다.

                # self.show()

        def excute_macro(self):
            pass

        def exit_macro(self):
            # 매크로녹화종료 로깅
            log_title = "매크로녹화종료"
            self.time_recording_end = self.elapsed_full_recording_time
            contents = f"{StateManagementUtil.UNDERLINE}{TimeUtil.get_time_as_('%Y-%m-%d_%H:%M:%S')}{log_title}"
            BusinessLogicUtil.print_cyan(contents)
            self.save_macro_log(contents=contents)

            # 매크로 로그 확인
            BusinessLogicUtil.speak_ment_experimental(ment="저장된 매크로 로그를 확인합니다", comma_delay=0.98)
            BusinessLogicUtil.run_via_explorer_exe(StateManagementUtil.MACRO_LOG)

        # @Slot() # 최신 버전의 PySide6에서는 @Slot() 데코레이터를 사용하지 않고도 Slot 메서드를 정의할 수 있습니다. 이렇게 되면 자동으로 Slot으로 인식됩니다. 즉 최신버전 pyside6 에서는 쓸 필요 없다.
        def update_label(self):
            try:
                self.elapsed_full_recording_time = int(time.time() - self.time_recording_start)
                self.label.setText(f"녹화 중...\n녹화경과시간: {self.elapsed_full_recording_time} secs \n")
            except:
                traceback.print_exc(file=sys.stdout)

        def on_mouse_btn_clicked(self, x, y, button, pressed):

            # 현재 시간과 녹화 시작 시간의 차이 계산
            current_time = time.time()
            elapsed_time = int((current_time - self.previous_time) * 1000)
            # print(f"current_time : {current_time}")
            # print(f"self.previous_time : {self.previous_time}")

            # x, y = pyautogui.position() # parameter 에서 오는 값과 동일하므로 대안으로 남겨둠.

            if button == pynput.mouse.Button.left and pressed:
                info = f"BusinessLogicUtil.sleep({elapsed_time})   %%%FOO%%%    BusinessLogicUtil.click_mouse_left_btn(abs_x={x},abs_y={y}) "
                BusinessLogicUtil.print_cyan(info)
                self.save_macro_log(contents=f"{TimeUtil.get_time_as_('%Y-%m-%d_%H:%M:%S')} {info}")
            elif button == pynput.mouse.Button.right and pressed:
                info = f"BusinessLogicUtil.sleep({elapsed_time})   %%%FOO%%%    BusinessLogicUtil.click_mouse_right_btn(abs_x={x},abs_y={y}) "
                BusinessLogicUtil.print_cyan(info)
                self.save_macro_log(contents=f"{TimeUtil.get_time_as_('%Y-%m-%d_%H:%M:%S')} {info}")

            # 현재시간을 이전시간에 저장
            self.previous_time = current_time

        def save_macro_log(self, contents: str):
            macro_log = StateManagementUtil.MACRO_LOG
            BusinessLogicUtil.make_pnx(StateManagementUtil.MACRO_LOG, mode="f")
            with open(macro_log, "a", encoding="utf-8") as f:
                f.write(f"{contents}\n")

        def on_keboard_press(self, key):
            # global is_processing_event
            # if self.is_processing_event != False:
            print(f'키보드 입력: {key}')

            # isinstance()
            # all(list) # (iterable) 객체의 모든 요소가 참(True)인지 확인
            # all(dict) # (iterable) 객체의 모든 요소가 참(True)인지 확인
            # all(tuple) # (iterable) 객체의 모든 요소가 참(True)인지 확인

        def on_keys_down(self, key):
            # 현재 시간과 녹화 시작 시간의 차이 계산
            current_time = time.time()
            elapsed_time = int((current_time - self.previous_time) * 1000)

            # for hotkey in self.HOTKEYS:
            #     hotkey.release(self.keyboard_listener1.canonical(key))
            #     print(f"key : {key}")

            # 키이름 여러 형식으로 출력
            # try:
            #     print(key)
            #     print(key.value)
            #     print(key.value.vk)
            # except:
            #     print(key)
            #     pass

            # 키이름 전처리
            key: str = str(key)
            key: str = key.lower()
            key: str = key.replace("\'", "")
            key: str = key.replace("\"", "")
            key: str = key.replace("key.", "")
            key: str = key.replace("<25>", "한자 or ctrl_r")
            key: str = key.replace("<21>", "한영 or alt_r")
            key: str = key.replace("12", "텐키 5")  # 텐키
            key: str = key.replace("cmd", "win")
            key: str = key.replace("page", "pg")
            key: str = key.replace("down", "dn")
            if key != "num_lock":
                key: str = key.replace("_l", "")
            key: str = key.replace("_r", "")

            key: str = key.replace(" ", "")
            key: str = key.replace("<", "")
            key: str = key.replace(">", "")
            # key: str = key.replace("_", "")

            # 전처리 후 출력
            # print(str(key))

            # if key == "ctrl+alt":
            log_title = "키보드인풋"
            info = f"BusinessLogicUtil.sleep({elapsed_time})\nBusinessLogicUtil.keyDown('{key}') "
            BusinessLogicUtil.print_cyan(info)
            self.save_macro_log(contents=f"{TimeUtil.get_time_as_('%Y-%m-%d_%H:%M:%S')}{log_title} {info}")

            # 현재시간을 이전시간에 저장
            self.previous_time = current_time

            # if self.store = []
            # global is_processing_event
            # if self.is_processing_event == False:
            # self.is_processing_event = True
            # self.is_processing_event = False

            # pynput.keyboard.Listener()는 다시 self.listener3.start() 할 수 없다.
            # 새로 만들어야 한다
            # if self.listener3.is_alive():
            #     self.listener3.stop()
            # else:

            # self.listener3 = pynput.keyboard.Listener(on_press=self.on_keboard_press)
            # self.listener3.start()

            # self.condition.notify()  # event1에게 동작 신호 보내기

        def on_single_key_pressed(self, key):

            # 현재 시간과 녹화 시작 시간의 차이 계산
            current_time = time.time()
            elapsed_time = int((current_time - self.previous_time) * 1000)

            # print(str(key))
            if pynput.keyboard.GlobalHotKeys.name == "<ctrl>":
                log_title = "키보드단일키인풋"
                info = f"  BusinessLogicUtil.sleep({elapsed_time})   %%%FOO%%%    BusinessLogicUtil.press({str(key)}) "
                BusinessLogicUtil.print_cyan(info)
                self.save_macro_log(contents=f"{TimeUtil.get_time_as_('%Y-%m-%d_%H:%M:%S')}{log_title} {info}")

            # 현재시간을 이전시간에 저장
            self.previous_time = current_time

            # try:
            #     # alphanumeric key
            #     print('{0}'.format(key.char))
            # except AttributeError:
            #     # special key
            #     print('{0}'.format(key.char))

        def on_keys_up(self, key):
            # 현재 시간과 녹화 시작 시간의 차이 계산
            current_time = time.time()
            elapsed_time = int((current_time - self.previous_time) * 1000)

            # for hotkey in self.HOTKEYS:
            #     if hotkey
            #     hotkey.press(self.keyboard_listener1.canonical(key))
            #     print(f"key : {key}")

            # 키이름 전처리
            key: str = str(key)
            key: str = key.lower()
            key: str = key.replace("\'", "")
            key: str = key.replace("\"", "")
            key: str = key.replace("key.", "")
            key: str = key.replace("<25>", "한자 or ctrl_r")
            key: str = key.replace("<21>", "한영 or alt_r")
            key: str = key.replace("12", "텐키 5")  # 텐키
            key: str = key.replace("cmd", "win")
            key: str = key.replace("page", "pg")
            key: str = key.replace("down", "dn")
            if key != "num_lock":
                key: str = key.replace("_l", "")
            key: str = key.replace("_r", "")

            key: str = key.replace(" ", "")
            key: str = key.replace("<", "")
            key: str = key.replace(">", "")
            # key: str = key.replace("_", "")

            # 전처리 후 출력
            # print(str(key))

            log_title = "키보드릴리즈"
            info = f"BusinessLogicUtil.sleep({elapsed_time})\nBusinessLogicUtil.keyUp('{key}') "
            BusinessLogicUtil.print_cyan(info)
            self.save_macro_log(contents=f"{TimeUtil.get_time_as_('%Y-%m-%d_%H:%M:%S')}{log_title} {info}")

            # 현재시간을 이전시간에 저장
            self.previous_time = current_time
            pass

        def bring_this_window(self):
            self.show()
            self.activateWindow()
            # import win32gui
            # active_window = win32gui.GetForegroundWindow()
            # win32gui.SetForegroundWindow(active_window)

    class CustomQthread(QThread):
        """pyside6 app 전용 객체"""
        finished = Signal()  # run()의 성공 신호를 보내기 위해 필요, run() 은 상속된 QThread 객체의 run()을 통해서 오버라이딩 되는 것 보인다.

        def __init__(self, q_application):  # 이 생성자는 q_application 를 받기 위해서 내가 작성 q_application 가 필요없는 void method QThread 이용 시 그냥 없애면 되는 생성자.
            super().__init__()
            self.q_application = q_application

        def run(self):
            # QThread 동작 테스트 코드
            print("QThread 초기화 시작")
            for i in range(10):
                print(i)
                self.msleep(30)

            def tmp2(q_application: QApplication):
                global dialog2
                dialog2 = UiUtil.CustomDialog(q_application=q_application, q_wiget=UiUtil.CustomQdialog(string="테스트", btns=["실행", "실행하지 않기"]), is_app_instance_mode=False)
                if dialog2.btn_text_clicked == "실행":
                    BusinessLogicUtil.speak_ment_experimental("정상적으로 동작합니다", comma_delay=0.98)

            def tmp(string: str):
                BusinessLogicUtil.speak_ment_experimental(string, comma_delay=0.98)
                # global tmpc
                # dialog = CustomDialog(q_application=q_application, q_wiget=RpaProgramMainWindow(), is_app_instance_mode=True, is_exec_mode=True)
                # global dialog
                # dialog = UiUtil.CustomQdialog(context="테스트", buttons=["확인"], is_input_text_box=True, input_text_default="???")
                # dialog.show()
                # dialog = CustomDialog(q_application=q_application, q_wiget=UiUtil.CustomQdialog(context="테스트", buttons=["실행", "실행하지 않기"], starting_timer=True, closing_timer=False), is_app_instance_mode=True)

            # 프로그램 외 단축키 이벤트 설정
            shortcut_keys_up_promised = {
                # "<ctrl>+<cmd>": self.close, #success
                # "<ctrl>+T": partial(tmp, "test"), #success
                # "<ctrl>+Q": partial(tmp2, self.q_application), #fail
                # "<ctrl>+h": partial(q_wiget.toogle_rpa_window, "<ctrl>+h"), #fail
            }
            keyboard_main_listener = pynput.keyboard.GlobalHotKeys(hotkeys=shortcut_keys_up_promised)
            keyboard_main_listener.start()

            self.finished.emit()  # 작업이 성공되었음을 신호로 알림 # flutter 상태관리와 비슷
            print("QThread 실행 증...")

    # class SharedObject(QObject):
    #     """pyside6 app 전용 공유객체 (pyside6 app 상태관리용)"""
    #     dataChanged = Signal(str)  # 데이터 변경을 알리는 시그널
    #
    #     def __init__(self):
    #         super().__init__()
    #         self._data = ""
    #         self.answer = ""
    #         self.question = ""
    #         self.rpa_program_main_window = None
    #
    #     #  /////////////////////////////////////////////// SharedObject.data
    #     @property
    #     def data(self):
    #         return self._data
    #
    #     @data.setter
    #     def data(self, value):
    #         self._data = value
    #         self.dataChanged.emit(self._data)  # 데이터 변경 시 시그널 발생
    #
    #     #  /////////////////////////////////////////////// 공유객체 SharedObject.answer
    #     @property
    #     def data(self):
    #         return self.answer
    #
    #     @data.setter
    #     def data(self, value):
    #         self.answer = value
    #         self.dataChanged.emit(self.answer)
    #
    #     #  SharedObject.question
    #     @property
    #     def data(self):
    #         return self.question
    #
    #     @data.setter
    #     def data(self, value):
    #         self.question = value
    #         self.dataChanged.emit(self.question)
    #
    #     #  SharedObject.rpa_program_main_window ....이래도 되나 모르겠네... 성능 이슈 있을 수도...
    #     @property
    #     def data(self):
    #         return self.rpa_program_main_window
    #
    #     @data.setter
    #     def data(self, value):
    #         self.rpa_program_main_window = value
    #         self.dataChanged.emit(self.rpa_program_main_window)

    @staticmethod
    def pop_up_as_complete(title_: str, ment: str, auto_click_positive_btn_after_seconds: int, input_text_default="", btns=None):
        # should_i_do 가 앱 안과 밖에서도 잘 된다면 deprecated 하자
        if btns is None:
            btns = ["확인"]

        if platform.system() == 'Windows':
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            file_pnx = StateManagementUtil.POP_SOUND_POP_SOUND_WAV
            if BusinessLogicUtil.does_pnx_exist(src=file_pnx):
                BusinessLogicUtil.play_wav_file(file_pnx=file_pnx)

            app_foo = None

            # QApplication 인스턴스 확인
            app = QApplication.instance()
            if app is None:
                app_foo = QApplication()
            if input_text_default == "":
                is_input_text_box = False
            else:
                is_input_text_box = True

            dialog_ = UiUtil.CustomQdialog(title=title_, string=ment, btns=btns, input_box_mode=is_input_text_box, input_box_text_default=input_text_default, auto_click_positive_btn_after_seconds=auto_click_positive_btn_after_seconds)
            dialog_.exec()
            btn_text_clicked = dialog_.btn_text_clicked

            if btn_text_clicked == "":
                BusinessLogicUtil.print_cyan(f'버튼 입니다 {btn_text_clicked}')
            if app == True:  # .....app 은 bool 이 아닌데. 동작 되고있는데..
                BusinessLogicUtil.print_cyan("여기는 좀 확인을 해야하는데. 호출 안되면 좋겠는데1")
                if isinstance(app_foo, QApplication):
                    BusinessLogicUtil.print_cyan("여기는 좀 확인을 해야하는데. 호출 안되면 좋겠는데2")
                    app_foo.exec()
            if app == True:
                # app_foo.quit()# QApplication 인스턴스 제거시도 : fail
                # app_foo.deleteLater()# QApplication 인스턴스 파괴시도 : fail
                # del app_foo # QApplication 인스턴스 파괴시도 : fail
                # app_foo = None # QApplication 인스턴스 파괴시도 : fail
                BusinessLogicUtil.print_cyan("여기는 좀 확인을 해야하는데. 호출 안되면 좋겠는데3")
                app_foo.shutdown()  # QApplication 인스턴스 파괴시도 : success  # 성공요인은 app.shutdown()이 호출이 되면서 메모리를 해제까지 수행해주기 때문
                # sys.exit()
        else:
            BusinessLogicUtil.print_success(f"{ment}")


class Pyside6Util:
    @staticmethod
    def get_font_for_pyside6(font_path):
        font_id = QFontDatabase.addApplicationFont(font_path)
        font_name = QFontDatabase.applicationFontFamilies(font_id)[0]
        font = QFont(font_name)
        font.setFixedPitch(True)
        return font


class SecurityUtil:
    @staticmethod
    def aes_encrypt(key, plaintext):
        from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
        from cryptography.hazmat.primitives import padding
        from cryptography.hazmat.backends import default_backend
        """AES 암호화: 대칭키암호화 ECB 모드, 보안취약"""
        # 키 생성
        cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
        encryptor = cipher.encryptor()

        # 패딩 추가
        padder = padding.PKCS7(128).padder()
        padded_data = padder.update(plaintext) + padder.finalize()

        # 암호화 수행
        ciphertext = encryptor.update(padded_data) + encryptor.finalize()
        return ciphertext

    @staticmethod
    def aes_decrypt(key, ciphertext):
        from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
        from cryptography.hazmat.primitives import padding
        from cryptography.hazmat.backends import default_backend
        """AES 복호화"""
        # 키 생성
        cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=default_backend())
        decryptor = cipher.decryptor()

        # 복호화 수행
        decrypted_data = decryptor.update(ciphertext) + decryptor.finalize()

        # 언패딩
        unpadder = padding.PKCS7(128).unpadder()
        plaintext = unpadder.update(decrypted_data) + unpadder.finalize()
        return plaintext

    @staticmethod
    def encode_as_lzw_algorizm(plaintext: str):
        r"""
        LZW 알고리즘을 사용하여 문자열을 압축하는 함수
            def compress_string(original_string):
                 return compressed_string

        LZW 알고리즘을 사용하여 압축된 문자열을 해제하는 함수
            def decompress_string(compressed_string):
                 return original_string

        문자열 압축
            current_directory_state = compress_string(current_directory_state)

        문자열 압축해제
            current_directory_state = decompress_string(current_directory_state)
        """
        import zlib
        return zlib.compress(plaintext.encode('utf-8'))

    @staticmethod
    def decode_as_lzw_algorizm(encrypted_text):
        import zlib
        return zlib.decompress(encrypted_text.decode('utf-8'))

    @staticmethod
    def convent_bytes_to_str(target: bytes):
        return target.decode('utf-8')

    @staticmethod
    def convent_str_to_bytes(target: str):
        return target.encode('utf-8')

    @staticmethod
    def get_random_alphabet():
        # BusinessLogicUtil.print_as_log(f"{inspect.currentframe().f_code.co_name}()")
        return random.choice(string.ascii_letters)

    @staticmethod
    def get_random_bytes():
        return secrets.token_bytes(16)  # 16바이트의 보안적으로 안전한 난수 생성

    @staticmethod
    def get_random_int():
        # BusinessLogicUtil.print_as_log(f"{inspect.currentframe().f_code.co_name}()")
        return secrets.randbelow(100)  # 0부터 99까지의 난수 생성

    @staticmethod
    def get_random_name():
        return secrets.choice([
            "김민지", "이준호", "박지영", "정성민", "홍길동", "김지현", "박민수", "이서연", "정현우", "한지원", "박정훈"
        ])

    @staticmethod
    def get_random_phone_number():
        return secrets.choice([
            "010-1234-5678", "02-9876-5432", "031-111-2222", "051-555-7777", "070-1234-5678",
            # "+1-123-456-7890", "+44-20-1234-5678", "+81-3-1234-5678", "+86-10-1234-5678", "+61-2-1234-5678"
        ])

    @staticmethod
    def get_random_e_mail():
        return secrets.choice([
            'john.doe@gmail.com', 'jane.smith@yahoo.com', 'david.wilson@hotmail.com', 'emily.johnson@outlook.com', 'michael.brown@aol.com', 'sarah.jones@icloud.com', 'robert.davis@protonmail.com', 'lisa.thomas@zoho.com', 'william.martin@yandex.com', 'jessica.anderson@mail.com',
            'matthew.harris@live.com', 'laura.miller@gmx.com', 'james.jackson@fastmail.com', 'olivia.rodriguez@inbox.com',
            'benjamin.carter@ymail.com', 'mia.walker@rocketmail.com', 'ethan.white@tutanota.com', 'ava.hall@rediffmail.com', 'alexander.lee@mailinator.com', 'sophia.green@protonmail.ch', 'jacob.adams@yandex.ru', 'emma.baker@outlook.com', 'daniel.cook@zoho.eu', 'madison.lopez@google.com',
            'logan.morgan@yahoo.co.uk', 'chloe.roberts@icloud.com', 'jayden.kelly@mail.com', 'grace.bennett@fastmail.fm',
            'samuel.rogers@protonmail.com', 'harper.edwards@outlook.com'
        ])

    @staticmethod
    def get_random_address():
        import random
        def generate_random_address_usa():
            street_number = random.randint(1, 9999)
            street_name = random.choice(['Main Street', 'Park Avenue', 'Oak Lane', 'Maple Avenue', 'Cedar Road'])
            city = random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'])
            state = random.choice(['California', 'Texas', 'Florida', 'New York', 'Illinois'])
            zip_code = random.randint(10000, 99999)
            return f"{street_number} {street_name}, {city}, {state} {zip_code}"

        def generate_random_address_kor():
            street = random.choice(['서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시', '대전광역시', '울산광역시', '세종특별자치시', '경기도', '강원도', '충청북도', '충청남도', '전라북도', '전라남도', '경상북도', '경상남도', '제주특별자치도'])
            city = random.choice(['서초구', '강남구', '송파구', '강동구', '관악구', '강서구', '영등포구', '구로구', '금천구', '양천구', '마포구', '서대문구', '은평구', '동작구', '광진구', '성동구', '중랑구', '동대문구', '성북구', '강북구', '도봉구', '노원구', '중구', '종로구'])
            dong = random.choice(['반포동', '삼성동', '청담동', '논현동', '압구정동', '서초동', '잠실동', '천호동', '신림동', '구로동', '영등포동', '신도림동', '여의도동', '목동', '신정동', '신촌동', '홍대입구동', '이태원동', '성수동', '왕십리동'])
            street_number = random.randint(1, 200)
            building_name = random.choice(['아파트', '빌라', '주택', '오피스텔'])
            return f"{street} {city} {dong} {street_number}-{random.randint(1, 20)}, {building_name}"

        return random.choice([generate_random_address_kor() for _ in range(100)])

    @staticmethod
    def get_random_id(length_limit: int):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length_limit))

    @staticmethod
    def get_random_pw(length_limit: int):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length_limit))

    @staticmethod
    def get_random_korean(length_limit: int):
        result = ''
        for _ in range(length_limit):
            result += random.choice(string.printable)
        return result

    @staticmethod
    def get_random_date():
        # 현재 날짜 가져오기
        current_date = datetime.now()
        # 시작 날짜 설정 (예: 1970년 1월 1일)
        start_date = datetime(1970, 1, 1)
        # 현재 날짜와 시작 날짜 사이의 일수 계산
        days_diff = (current_date - start_date).days
        # 랜덤하게 선택된 일수 더하기
        random_date = start_date + timedelta(days=random.randint(0, days_diff))
        # "yyyy-yy-yy" 형식으로 포맷팅
        formatted_date = random_date.strftime("%Y-%y-%y")
        return formatted_date

    @staticmethod
    def get_random_special_character(length_limit: int):
        import string
        result = ''
        for _ in range(length_limit):
            result += random.choice(string.printable)
        return

    @staticmethod
    def get_random_user_trial_input_case():
        options = [
            SecurityUtil.get_random_name(),
            SecurityUtil.get_random_phone_number(),
            SecurityUtil.get_random_id(30),
            SecurityUtil.get_random_special_character(30),
            string.punctuation,
            SecurityUtil.get_random_special_character(30),
            # SecurityUtil.get_random_hex(),
            # SecurityUtil.get_random_bytes(),
            SecurityUtil.get_random_date(),
            "None",
            None,
            ""
        ]
        return random.choice(options)

    @staticmethod
    def get_random_hex():
        return secrets.token_hex(16)  # 16바이트의 난수를 16진수 문자열로 생성

    @staticmethod
    def get_random_urlsafe():
        return secrets.token_urlsafe(16)  # 16바이트의 난수를 URL-safe 문자열로 생성

    @staticmethod
    def is_sql_injection_safe_simply(data: str):
        sql_pattern = r"(SELECT|INSERT|UPDATE|DELETE|CREATE|ALTER|DROP|TRUNCATE|GRANT|REVOKE)"
        match = re.search(sql_pattern, data, re.IGNORECASE)
        if match:
            return False
        return True


class CustomErrorUtil(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class MentsUtil:
    NOT_PREPARED_YET = "아직 준비되지 않은 서비스입니다"
    NO = "그냥 닫아"
    YES = "응"
    CHECKED = "확인"
    OK_I_WILL_DO_IT_NOW = "지금할게"
    DONE = "했어"
    I_WANT_TO_TO_DO_NEXT_TIME = "다음에 할게"


class DataStructureUtil:
    @staticmethod
    def get_list_added_elements_alternatively(list_for_odd, list_for_even):  # from [1, 2, 3] + [ x, y, z] to [1,x,2,y,3,z]
        """
        두 리스트를 더할때 사용하는 함수
        list, ndarray 모두 사용이 가능한 함수이다.

        result = get_list_added_elements_alternatively(list1 = [1, 2, 3], list_to_added_as_even_order = ['x', 'y', 'z'])
        """
        result = []
        for i in range(len(list_for_odd)):
            result.append(list_for_odd[i])
            if i < len(list_for_even):
                result.append(list_for_even[i])
        return result

    @staticmethod
    def print_list_each_two_elements(list: []):  # print(rf'list[index] list[index+1] : {list[index]} {list[index+1]}') without out of index
        for index, item in enumerate(list):  # enumerate 로 리스트의 원소를 2개씩 출력
            if index + 1 < len(list):
                print(rf'list[index] list[index+1] : {list[index]} {list[index + 1]}')

    @staticmethod
    def get_list_each_two_elements_joined(list: []):  # from ["a", "b", "c", "d"] to ["ab", "cd"]
        return [f"{list[i]}{list[i + 1]}" for i in range(0, len(list), 2)]

    @staticmethod
    def get_nested_list_grouped_by_each_two_elements_in_list(list: []):  # from ["a", "b", "c", "d"] to [["a","b"], ["c","d"]]
        result = []
        for i in range(0, len(list), 2):
            if i + 1 < len(list):
                result.append([list[i], list[i + 1]])
        return result

    @staticmethod
    def get_column_of_2_dimension_list(list_2_dimension: [], column_no):  # return 은 list 아니고 ndarray 일 수 있다
        import numpy as np
        arr = np.array(list_2_dimension)
        second_column = arr[:, column_no]
        print(second_column)

    @staticmethod
    def get_nested_list_converted_from_ndarray(ndarray: numpy.ndarray):  # ndarray 에서 list 로 변환 # ndarray 에서 list 로 변환 # ndarray to nested []  from [[1 2]] to [[1, 2]] # from [ [str str] [str str] ]  to  [ [str, str], [str, str] ]
        return ndarray.tolist()

    @staticmethod
    def get_nested_list_sorted_by_column_index(nested_list: [[str]], column_index: int, decending_order=False):  # tree depth(sample[1]) 에 대한 내림차순 정렬 # list 2차원 배열의 특정 열의 내림차순 정렬 # from [[str, str]] to [[str, str]]
        """
         중첩리스트를 첫 번째 행을 기준으로 내림차순으로 정렬
         from
         [
             [ 1 a z ]
             [ 7 a b ]
             [ 4 a c ]
         ]
         to
         [
             [ 7 a b ]
             [ 4 a c ]
             [ 1 a z ]
         ]
         튜플도 된다
         from
         [
             ( 1 a z )
             ( 7 a b )
             ( 4 a c )
         ]
         to
         [
             ( 7 a b )
             ( 4 a c )
             ( 1 a z )
         ]
        """

        def bubble_sort_nested_list(nested_list, column_index):
            """버블 소팅 테스트"""
            if type(nested_list[0][column_index]) == float:
                column_index = int(column_index)
                n = len(nested_list)
                for i in range(n):
                    for j in range(0, n - i - 1):
                        if decending_order == True:
                            if int(str(nested_list[j][column_index]).replace(".", "")) < int(str(nested_list[j + 1][column_index]).replace(".", "")):
                                nested_list[j], nested_list[j + 1] = nested_list[j + 1], nested_list[j]
                        elif decending_order == False:
                            if int(str(nested_list[j][column_index]).replace(".", "")) > int(str(nested_list[j + 1][column_index]).replace(".", "")):
                                nested_list[j], nested_list[j + 1] = nested_list[j + 1], nested_list[j]
                return nested_list
            elif type(nested_list[0][column_index]) == int or nested_list[0][column_index].isdigit():  # 에고 힘들다. 머리아팠다
                column_index = int(column_index)
                n = len(nested_list)
                for i in range(n):
                    for j in range(0, n - i - 1):
                        if decending_order == True:
                            if int(nested_list[j][column_index]) < int(nested_list[j + 1][column_index]):
                                # print(rf'{nested_list[j][column_index]}>{nested_list[j + 1][column_index]}')
                                # print(rf'nested_list[j][column_index] > nested_list[j+1][column_index] : {int(nested_list[j][column_index]) > int(nested_list[j+1][column_index])}')
                                nested_list[j], nested_list[j + 1] = nested_list[j + 1], nested_list[j]
                        elif decending_order == False:
                            if int(nested_list[j][column_index]) > int(nested_list[j + 1][column_index]):
                                # print(rf'{nested_list[j][column_index]}>{nested_list[j + 1][column_index]}')
                                # print(rf'nested_list[j][column_index] > nested_list[j+1][column_index] : {int(nested_list[j][column_index]) > int(nested_list[j+1][column_index])}')
                                nested_list[j], nested_list[j + 1] = nested_list[j + 1], nested_list[j]
                return nested_list
            elif type(nested_list[0][column_index]) == str:
                column_index = int(column_index)
                n = len(nested_list)
                for i in range(n):
                    for j in range(0, n - i - 1):
                        if decending_order == True:
                            if nested_list[j][column_index] < nested_list[j + 1][column_index]:
                                # print(rf'{nested_list[j][column_index]}>{nested_list[j + 1][column_index]}')
                                # print(rf'nested_list[j][column_index] > nested_list[j+1][column_index] : {int(nested_list[j][column_index]) > int(nested_list[j+1][column_index])}')
                                nested_list[j], nested_list[j + 1] = nested_list[j + 1], nested_list[j]
                        if decending_order == False:
                            if nested_list[j][column_index] > nested_list[j + 1][column_index]:
                                # print(rf'{nested_list[j][column_index]}>{nested_list[j + 1][column_index]}')
                                # print(rf'nested_list[j][column_index] > nested_list[j+1][column_index] : {int(nested_list[j][column_index]) > int(nested_list[j+1][column_index])}')
                                nested_list[j], nested_list[j + 1] = nested_list[j + 1], nested_list[j]
                return nested_list

        return bubble_sort_nested_list(nested_list, column_index)

    @staticmethod
    def get_nested_list_removed_row_that_have_nth_element_dulplicated_by_column_index_for_ndarray(ndarray: [[]], column_index: int):  # 중복된 행 제거하는게 아니고 행의 2번째 요소가 중복되는 것을 제거
        seen = set()
        unique_rows = []
        for row in ndarray:
            if row[column_index] not in seen:
                unique_rows.append(row)
                seen.add(row[column_index])
        return unique_rows

    @staticmethod
    def get_nested_list_removed_row_that_have_nth_element_dulplicated_by_column_index(nested_list: [[]], column_index: int):  # 중복된 행 제거하는게 아니고 행의 2번째 요소가 중복되는 것을 제거
        seen = set()  # 중복된 행의 두 번째 요소를 추적하기 위한 집합(set) 생성
        unique_rows = []
        for row in nested_list:
            if row[column_index] not in seen:
                unique_rows.append(row)  # 중복된 행의 두 번째 요소가 중복되지 않는 행들만 추출하여 unique_rows 리스트에 추가
                seen.add(row[column_index])
        return unique_rows  # 중복된 행의 두 번째 요소가 중복되지 않는 행들만 남게 됩니다.

    @staticmethod
    def get_list_seperated_by_each_elements_in_nested_list(nested_list):
        return [item for sublist in nested_list for item in sublist]

    @staticmethod
    def is_two_lists_equal(list1, list2):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # 두 리스트의 요소들이 동일한지만 확인 # 하나라도 발견되면 탐색 중지 # 두 리스트의 동일 인덱스에서 진행하다 달라도 다른거다
        if len(list1) != len(list2):
            print(f"두 리스트의 줄 수가 다릅니다 {len(list1)}, {len(list2)}")
            return False
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                print(f"두 리스트의 같은 인덱스 중 다른 리스트 발견={list1[i]}, {list2[i]}")
                return False
        return True

    @staticmethod
    def get_elements_that_list1_only_have(list1, list2):  # 두 개의 리스트를 비교하여 특정 하나의 리스트 만 가진 요소만 모아서 리스트로 출력
        unique_elements_of_list1 = []
        for element in list1:
            if element not in list2:
                unique_elements_of_list1.append(element)
        return unique_elements_of_list1

    @staticmethod
    def get_different_elements(list1, list2):  # 두 개의 리스트를 비교하여 서로 다른 요소만 모아서 리스트로 출력
        different_elements = []
        # 두 리스트 중 더 긴 리스트의 길이를 구합니다.
        max_length = max(len(list1), len(list2))
        # 범위는 더 긴 리스트의 길이로 설정합니다.
        for i in range(max_length):
            # 리스트의 인덱스가 범위 내에 있는지 확인 후 비교합니다.
            if i < len(list1) and i < len(list2):
                if list1[i] != list2[i]:
                    different_elements.append(list1[i])
            else:
                # 한 리스트는 범위를 벗어났으므로 해당 요소를 추가합니다.
                if i >= len(list1):
                    different_elements.append(list2[i])
                else:
                    different_elements.append(list1[i])
        # 위의 코드는 5 초 경과

        different_elements = []
        # set1 = set(list1)  # list to set
        # set2 = set(list2)
        # different_elements = list(set1.symmetric_difference(set2))
        # 위의 코드는 12 초 경과
        return different_elements

    @staticmethod
    def get_common_elements(list1, list2):  # 두 개의 리스트를 비교하여 서로 동일한 요소만 새로운 리스트로 출력 # 중복값 색출
        common_elements = []
        for element in list1:
            if element in list2:
                common_elements.append(element)
        return common_elements

    @staticmethod
    def add_suffix_to_string_list(string_list, suffix):
        result = []
        for string in string_list:
            result.append(string + suffix)
        return result

    @staticmethod
    def add_prefix_to_string_list(string_list, prefix):
        result = []
        for string in string_list:
            result.append(prefix + string)
        return result


class PerformanceOptimizingUtil:
    @staticmethod
    def generate_mp3_file_for_time_performance():  # time performance : 9028 초 /60 /60  =  2.5 시간
        """
        deprecated
        시간에 대한 mp3 파일 미리 만들어 놓음으로 생성시간 저감 기대 > speaks() 메소드 최적화
        """
        for HH in range(24, 0, -1):
            for mm in range(0, 60):
                BusinessLogicUtil.print_with_underline(f'{int(HH)}시')
                BusinessLogicUtil.print_with_underline(f'{int(mm)}분 입니다')

    @staticmethod
    def gen_dictionary_for_monitor_pnx_edited_and_back_up(directory_pnx):
        r"""
        deprecated
        monitor_target_edited_and_back_up() 성능개량용 코드
        lzw 알고리즘 딕셔너리 생성용 성능개량용 코드 > 이건 추후에 생각해보기로
        딕셔너리 업데이트 필요한 경우에 사용해서 콘솔에 출력된 딕셔너리 초기화용 코드를
        딕셔너리를 코드베이스에 하드코딩하여 사용

        생성된 딕셔너리 코드 예시
        dictionary_based_on_tri_structure = [
            "{PROJECT_DIRECTORY}\pkg_font\Montserrat\static",
            "{PROJECT_DIRECTORY}\pkg_font\Noto_Sans_KR\static",
            "{PROJECT_DIRECTORY}\pkg_font\GmarketSans",
            "{PROJECT_DIRECTORY}\pkg_font\Montserrat",
            "{PROJECT_DIRECTORY}\pkg_font\Noto_Sans_KR",
            "{PROJECT_DIRECTORY}\pkg_font\Poppins",
            "{PROJECT_DIRECTORY}\pkg_yaml",
            "{PROJECT_DIRECTORY}",
        ]
        """
        current_directory_state = BusinessLogicUtil.get_list_pnxs_with_mtime_without_files_to_exclude(directory_pnx=directory_pnx)  # str to dict
        current_directory_state = [f"{key}" for key, value in current_directory_state.items()]  # from dict to ["key\n"]   # 이건 함수는 테스트해보고, # noqa 처리 해야할 듯
        print(rf'type(current_directory_state) : {type(current_directory_state)}')
        print(rf'len(current_directory_state) : {len(current_directory_state)}')

        current_pnxs = current_directory_state
        # current_pnxs = current_directory_state[0:100]  # 샘플 100개만 테스트
        dirnames = [os.path.dirname(item) for item in current_pnxs]  # 파일 dirname 목록
        tree_levels = [BusinessLogicUtil.get_tree_depth_level(item) for item in current_pnxs]  # 파일시스템 트리깊이레벨 목록
        dirnames_and_trees = DataStructureUtil.get_list_added_elements_alternatively(dirnames, tree_levels)  # from [][] to []
        dirnames_and_trees = DataStructureUtil.get_nested_list_grouped_by_each_two_elements_in_list(dirnames_and_trees)
        dirnames_and_trees = DataStructureUtil.get_nested_list_sorted_by_column_index(nested_list=dirnames_and_trees, column_index=1, decending_order=True)  # tree depth를 의미하는 column_index=1 에 대한 내림차순 정렬
        dirnames_and_trees = DataStructureUtil.get_nested_list_removed_row_that_have_nth_element_dulplicated_by_column_index(nested_list=dirnames_and_trees, column_index=0)  # from [[]] to [[]] # from [[1 2]] to [[1, 2]] # from [ [str str] [str str] ]  to  [ [str, str], [str, str]]
        dirnames = [x[0] for x in dirnames_and_trees]  # dirnames_and_trees 의 첫번째 컬럼인 dirname 만 추출
        BusinessLogicUtil.print_with_underline("딕셔너리 초기화용 코드 시작")
        print("dictionary_based_on_tri_structure = {")
        [print(rf'    r"{dirname}":"{index}빠릿{index}" ,') for index, dirname in enumerate(dirnames)]
        print("}")
        # print(rf'dirnames : {dirnames}')
        print(rf'type(dirnames) : {type(dirnames)}')
        print(rf'len(dirnames) : {len(dirnames)}')
        BusinessLogicUtil.print_with_underline("딕셔너리 초기화용 코드 종료")
        BusinessLogicUtil.pause()

    dictionary_for_monitoring_performance = {
        r"{PROJECT_DIRECTORY}\pkg_font\Montserrat\static": "이거지1",
        r"{PROJECT_DIRECTORY}\pkg_font\Noto_Sans_KR\static": "이거지2",
        r"{PROJECT_DIRECTORY}\pkg_font\GmarketSans": "이거지3",
        r"{PROJECT_DIRECTORY}\pkg_font\Montserrat": "이거지4",
        r"{PROJECT_DIRECTORY}\pkg_font\Noto_Sans_KR": "이거지5",
        r"{PROJECT_DIRECTORY}\pkg_font\Poppins": "이거지6",
        r"{PROJECT_DIRECTORY}\pkg_yaml": "이거지7",
        r"{PROJECT_DIRECTORY}": "이거지8",
    }

    @staticmethod
    def replace_words_based_on_tri_node(text, dictionary):
        """
        # 사용 예시
        dictionary = ["apple", "banana", "orange"]
        text = "I like apple and banana."
        replaced_text = replace_words(text, dictionary)
        print(replaced_text)
        """

        class TrieNode:
            def __init__(self):
                self.children = {}  # 자식 노드를 저장하는 딕셔너리
                self.is_end_of_word = False  # 단어의 끝인지 나타내는 플래그

        class Trie:
            def __init__(self):
                self.root = TrieNode()  # 루트 노드 생성

            def insert(self, word):
                current_node = self.root
                for char in word:
                    if char not in current_node.children:
                        current_node.children[char] = TrieNode()
                    current_node = current_node.children[char]
                current_node.is_end_of_word = True

            def search(self, word):
                current_node = self.root
                for char in word:
                    if char not in current_node.children:
                        return False
                    current_node = current_node.children[char]
                return current_node.is_end_of_word

        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        words = text.split()
        replaced_words = []
        for word in words:
            if trie.search(word):
                replaced_words.append("REPLACED")
            else:
                replaced_words.append(word)

        return " ".join(replaced_words)


class MathUtil:  # BusinessLogicUtil 로 통합하자
    pi = 3.141592  # 원주율은 여기까지만 외웠기 때문 ㅋ

    @staticmethod
    def get_minuites_from_(seconds):  # 큰단위로 단위변환 시 숫자는 작아지니 숫자가 작아지도록 약속된 숫자를 곱하면 된다. # seconds -> min  인 경우 큰단위로 변환되고 있고 약속된 숫자는 60 이다. 작은 숫자를 생성 위해서 1/60 을 곱한다.
        return round(seconds / 60, 2)

    @staticmethod
    def get_minuites_and_remaining_secs(seconds):  # 큰단위로 단위변환 시 숫자는 작아지니 숫자가 작아지도록 약속된 숫자를 곱하면 된다.
        mins = seconds // 60
        secs_remaining = seconds % 60
        return mins, secs_remaining

    @staticmethod
    def get_value_splited_integer_part_and_decimal_part_from_(value):  # 큰단위로 단위변환 시 숫자는 작아지니 숫자가 작아지도록 약속된 숫자를 곱하면 된다.
        import math
        decimal_part, integer_part = math.modf(value)
        decimal_part = abs(decimal_part)  # 음수 부호 제거
        return [integer_part, decimal_part]


class FastapiUtil:
    # def import_pkg_alba():  # 명령어 자체가 안되는데 /mir 은 되는데 /move 안된다
    # try:
    # 파이썬 프로젝트 외부 패키지 import 시키는 방법 : 일반적으로는 불가능하다.
    # services_directory_pnx = os.path.dirname(os.path.dirname(__file__))
    # external_pkg_pnx = rf'{services_directory_pnx}\archive_py\pkg_alba'
    # print(rf'external_pkg_pnx : {external_pkg_pnx}')
    # os.environ['pkg_alba_pnx'] = rf'{external_pkg_pnx}'
    # sys.path.append(external_pkg_pnx)
    # print(rf'sys.path : {sys.path}')
    # from ..archive_py.pkg_alba import FileSystemUtil, StateManagementUtil, TestUtil
    # except:
    #     pass
    # try:
    # 대안 global pkg 로 복사하고 쓰고 실행후에는 프로젝트 내에서 패키지를 삭제한다 > 자동화할것
    # 의존성을 추가하기 위해서, pkg_alba의 .venv 도 따라 복사한다.
    # CURRENT_PROJECT_DIRECTORY= os.path.dirname(__file__)
    # SERVICES_DIRECTORY = os.path.dirname(CURRENT_PROJECT_DIRECTORY)
    # EXTERNAL_PKG_pnx = rf'{SERVICES_DIRECTORY}\archive_py\pkg_alba'
    # # VIRTUAL_PKG_pnx = rf'{CURRENT_PROJECT_DIRECTORY}\.venv\Lib\site-packages'
    # INTERNAL_PKG_pnx = rf'{CURRENT_PROJECT_DIRECTORY}\pkg_alba'
    # print(rf'VIRTUAL_PKG_pnx : {INTERNAL_PKG_pnx}')
    # os.system(rf'chcp 65001')
    # os.system(rf'robocopy "{EXTERNAL_PKG_pnx}" "{INTERNAL_PKG_pnx}" /MIR')
    # # os.system("pause")
    # print("파이썬 프로젝트 외부 패키지 import 시도에 성공")
    # except Exception:
    #     print("파이썬 프로젝트 외부 패키지 import 시도에 실패")
    #     sys.exit()
    # try:
    # 그냥 pkg 내에 집어 넣었다. 가상환경도 동일하게 개발한다.
    # except:
    #     pass
    # pass

    @staticmethod
    def convert_file_from_cp_949_to_utf_8(file_pnx):
        # import codecs
        # file_pnx_converted = rf"{BusinessLogicUtil.get_target_as_pn(file_pnx)}_utf_8{BusinessLogicUtil.get_target_as_x(file_pnx)}"
        # print(file_pnx_converted)
        # # 기존 파일을 'utf-8'로 읽어오고, 새로운 파일에 'utf-8'로 저장
        # with codecs.open(file_pnx, 'r', encoding='cp949') as file_previous:
        #     contents = file_previous.read()
        #     with codecs.open(file_pnx_converted, 'w', encoding='utf-8') as new_file:
        #         new_file.write(contents)
        pass

    @staticmethod
    def init_cors_policy(app):
        # dev
        # op 에서는 이 함수는 사용하면 않기로 결정, nginx 에서 CORS 설정을 할 것 이므로
        # CORS 두개 설정하면 multi header 로 인한 Control-Allow-Origin' header contains multiple values '*, https://www.pjh4139.store', but only one is allowed. 에러가 발생할 것이다.
        app.add_middleware(
            # success, fastapi CORS allow_origins 동적 할당은 대안 못찾았고, # 초기 origins 값을 와일드카드로 설정
            CORSMiddleware,  # 노란줄 원인 뭘까? #_noqa 를 적용해야 할지 고민 중
            allow_credentials=True,  # cookie 포함 여부를 설정. 기본은 False
            allow_origins=['*'],
            allow_methods=["*"],  # 허용할 method를 설정할 수 있으며, 기본값은 'GET'이다. OPTIONS request ?
            allow_headers=["*"],  # 허용할 http header 목록을 설정할 수 있으며 Content-Type, Accept, Accept-Language, Content-Language은 항상 허용된다.

            # try, 보안강화
            # fastapi CORS allow_origins 정적 할당 # 톳시하나 틀리면 안됨.
            # allow_origins=[,
            #     # "http://localhost",  # fail
            #     # "http://localhost/",  # fail
            #     # "http://localhost:3000",# success
            #     "http://localhost:3000/service-dev-diary",
            #     # "http://127.0.0.1:3000",#
            #     "https://e-magazine-jung-hoon-parks-projects.vercel.app",
            #     # "https://e-magazine-jung-hoon-parks-projects.vercel.app/",
            #     "https://e-magazine-jung-hoon-parks-projects.vercel.app/````````````````````",
            # ],
        )

    @staticmethod
    def init_Logging_via_middleware(app):
        # 미들웨어를 통한 로깅
        # @app.middleware("http")
        # async def log_requests(request: Request, call_next):
        #     logging.debug(f"요청: {request.method} {request.url}")
        #     response = await call_next(request)
        #     logging.debug(f"응답: {response.status_code}")
        #     return response
        pass

    @staticmethod
    def init_domain_address_allowed(app):
        # 접속허용도메인 주소 제한, 이 서버의 api 를 특정 도메인에서만 호출 가능하도록 설정
        # @app.middleware("http")
        # async def domain_middleware(request: Request, call_next):
        #     allowed_domains = ["example.com", "subdomain.example.com"]
        #     client_host = request.client.host
        #     client_domain = client_host.split(":")[0]  # 도메인 추출
        #     if client_domain not in allowed_domains:
        #         raise HTTPException(status_code=403, detail="Forbidden")
        #     response = await call_next(request)
        #     return response
        pass

    @staticmethod
    def init_ip_address_allowed(app):
        # 접속허용IP 주소 제한
        # @app.middleware("http")
        # async def ip_middleware(request: Request, call_next):
        #     allowed_ips = [
        #         "127.0.0.1",
        #         "10.0.0.1",
        #     ]
        #     client_ip = request.client.host
        #     if client_ip not in allowed_ips:
        #         raise HTTPException(status_code=403, detail="Forbidden")
        #     response = await call_next(request)
        #     return response
        pass

    @staticmethod
    async def preprocess_after_request(request):
        # BusinessLogicUtil.print_as_log(f"{str(request.url)} 로 라우팅 시도 중...")
        pass

    @staticmethod
    async def preprocess_before_response_return(request, response):
        # BusinessLogicUtil.print_as_log(f"{str(request.url)} 로 라우팅 되었습니다")
        pass

    @staticmethod
    def init_and_update_json_file(json_file, objects=None):
        if objects is None:
            objects = []
        try:
            BusinessLogicUtil.make_pnx(pnx=json_file, mode="f")
            if os.path.exists(json_file):
                if BusinessLogicUtil.is_letters_cnt_zero(pnx=json_file) == True:
                    BusinessLogicUtil.write_str_to_file(pnx=json_file, txt_str="[]\n")  # 이러한 형태로 객체를 받을 수 있도록 작성해 두어야 받을 수 있음.
                else:
                    if not os.path.isfile(json_file):
                        with open(json_file, "w", encoding='utf-8') as f:
                            # json.dump(objects, f, ensure_ascii=False)  # ensure_ascii=False 는 encoding 을 그대로 유지하는 것 같다. ascii 로 변환하는게 안전할 지도 모르겠다.
                            json.dump(objects, f)  # ensure_ascii=False 는 encoding 을 그대로 유지하는 것 같다. ascii 로 변환하는게 안전할 지도 모르겠다.
                    else:
                        with open(json_file, "r", encoding='utf-8') as f:
                            # BusinessLogicUtil.print_ment_via_colorama(f"{BOOKS_FILE} 업로드 되었습니다", colorama_color=ColoramaColorUtil.LIGHTWHITE_EX)
                            objects = json.load(f)
                        return objects
        except IOError as e:
            print("파일 작업 중 오류가 발생했습니다:", str(e))

    @staticmethod
    def test_client_post_request():  # test 자동화 용도
        import requests
        import json
        url = "https://BusinessLogicUtil.store/api/volatile/items"
        url = "https://BusinessLogicUtil.store/api/db-json/items"
        url = "https://BusinessLogicUtil.store/api/db-maria/items"

        # 저장할 데이터
        data = {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "password": "password",
        }
        # 데이터를 JSON 문자열로 변환합니다.
        json_data = json.dumps(data)

        # POST 요청을 생성합니다.
        headers = {"Content-Type": "application/json"}
        response = requests.post(url, headers=headers, data=json_data)

        # 응답을 확인합니다.
        if response.status_code == 201:
            print("데이터가 성공적으로 저장되었습니다.")
        else:
            print("데이터 저장에 실패했습니다.")

    # Pydantic은 Python의 데이터 유효성 검사 및 직렬화를 위한 라이브러리,
    # BaseModel은 Pydantic에 built in 되어 있다,
    # 데이터 모델을 정의하고 유효성을 검사하며 직렬화/역직렬화를 수행하는 기능을 제공합니다
    # auto increment 하고 싶어 pydantic model 로 구현
    class Board(BaseModel):
        id: int = uuid4().hex  # 수정대기
        title: str
        content: str

        class Config:
            populate_by_name = True

    @staticmethod
    def is_board_validated(board: Board) -> bool:
        # Board(게시물)의 유효성을 검사하는 커스텀 비지니스 로직을 구현, create/update 의 경우에 사용
        if not board.title:
            return False
        if not board.content:
            return False
        return True

    class Book(BaseModel):  # BaseModel 를 상속받은 Book 은 일반적인 객체가 아니다. type 을 출력해봐도 pydantic 의 하위 객체를 상속한 것으로 보인다
        id: Optional[str] = uuid4().hex  # Optional 을 설정하면 nullable 되는 거야? # 여기서 할당을 시키면 put() 동작하며 id가 바뀌어버린다. put()에서 업데이트되도록 따로 설정했다.
        name: str
        genre: Literal["러브코메디", "러브픽션", "액션"]  # string literal validation 설정, 이 중 하나만 들어갈 수 있음
        # price: float
        price: int

    class TodoItem(BaseModel):
        id: str
        title: str
        completed: bool

    class User(BaseModel):  # 여기에 validation 해두면 docs에서 post request 시 default 값 지정해 둘 수 있음.
        id: str = uuid4().hex + TimeUtil.get_time_as_('%Y%m%d%H%M%S%f') + SecurityUtil.get_random_alphabet()  # 진짜id 는 이렇게 default 로 들어가게하고, 사용자 id 는 e-mail
        pw: str
        name: str
        date_join: str = TimeUtil.get_time_as_('%Y-%m-%d %H:%M %S%f')
        date_logout_last: str
        address_house: str
        address_e_mail: str
        number_phone: str

        @classmethod
        @field_validator('id')
        def validate_id(cls, id):
            if 53 < len(id) or 53 < len(id):
                return {"fail", "id 는 53 자리 이상 이거나 이하 일 수 없습니다"}
            return id

        @classmethod
        @field_validator('pw')
        def validate_pw(cls, pw):
            # 다시 작성
            return pw

        @classmethod
        @field_validator('name')
        def validate_name(cls, name):
            if 30 < len(name):
                return {"fail", "name 은 30 자리 이상 일 수 없습니다"}
            return name

        @classmethod  # class 간 종속 관계가 있을 때 하위 class 에 붙여 줘야하나?, cls, 파라미터와 함께? , instance를 생성하지 않고 호출 가능해?
        @field_validator('date_join')
        def validate_date_join(cls, date_join):
            # datetime.strptime(date_join, '%Y-%m-%d %H:%M %S%f')
            # 다시 작성
            return date_join

        @classmethod
        @field_validator('address_e_mail')
        def validate_address_e_mail(cls, address_e_mail):
            # 다시 작성
            return address_e_mail

    class LoginForm(BaseModel):
        id: str
        pw: str

    class JoinForm(BaseModel):  # 회원가입 유효성검사 설정
        id: str  # 필수항목
        pw: str
        pw2: str
        name: str
        pw: str
        phone_no: str
        address: str
        e_mail: str
        age: str
        birthday: str
        date_joined: Optional[str]  # nullable
        date_canceled: Optional[str]
        fax_no: Optional[str]
        business_registration_no: Optional[str]
        company_name: Optional[str]
        department: Optional[str]
        position: Optional[str]
        company_address: Optional[str]

    class jinja_data(BaseModel):  # 모든 데이터를 수집하고, Optional 로 할당.
        id: Optional[str]  # nullable
        pw: Optional[str]
        prefix_promised: Optional[str]
        random_bytes: Optional[str]
        random_str: Optional[str]
        pw2: Optional[str]
        name: Optional[str]
        pw: Optional[str]
        phone_no: Optional[str]
        address: Optional[str]
        e_mail: Optional[str]
        age: Optional[str]
        date_joined: Optional[str]
        date_canceled: Optional[str]
        fax_no: Optional[str]
        business_registration_no: Optional[str]
        company_name: Optional[str]
        department: Optional[str]
        position: Optional[str]
        company_address: Optional[str]
        birthday: Optional[str]


class UvicornUtil:
    class Settings:
        # js 의 destructon 문법처럼 py의 unpacking 을 사용하는 방법이 있으나 변수 새로 생성해야함
        # 튜플로 데이터가 들어오는 것은 , 를 어딘가 작성했을 수 있다. 이 문법적 오류는 IDE 에서 알려주지 않는다.
        protocol_type = "http"
        # protocol_type =  "https"
        # host =  "0.0.0.0"
        host = "127.0.0.1"  # localhost
        port = 8080
        url = f"{protocol_type}://{host}:{port}"


class DbTomlUtil:
    @staticmethod
    def create_db_toml():
        try:
            db_pnx = StateManagementUtil.DB_YAML
            # db_template =BusinessLogicUtil.db_template
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            if not os.path.exists(os.path.dirname(db_pnx)):
                os.makedirs(os.path.dirname(db_pnx))  # 이거 파일도 만들어지나? 테스트 해보니 안만들어짐 디렉토리만 만들어짐
            # BusinessLogicUtil.print_as_log("db 파일 존재 검사 시도")
            if not os.path.isfile(db_pnx):
                # with open(db_pnx, "w") as f2:
                #     toml.dump(db_template, f2)
                BusinessLogicUtil.make_pnx(db_pnx, mode="f")
                BusinessLogicUtil.print_cyan(f"DB를 만들었습니다 {db_pnx}")
            else:
                BusinessLogicUtil.print_cyan(f"DB가 이미존재합니다 {db_pnx}")
        except:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def read_db_toml():
        try:
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            print("DB 의 모든 자료를 가져왔습니다")
            return toml.load(StateManagementUtil.DB_YAML)
        except:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def get_db_toml_key(unique_id):
        return BusinessLogicUtil.get_str_replaced_special_characters(target=unique_id, replacement="_")

    @staticmethod
    def select_db_toml(key):
        # BusinessLogicUtil.print_as_log(f"{inspect.currentframe().f_code.co_name}()")
        try:
            key = str(key)
            db_pnx = StateManagementUtil.DB_YAML
            try:
                # return toml.load(DB_TOML)[key]
                with open(db_pnx, 'r', encoding='utf-8') as f:
                    db = toml.load(f)
                return db[key]

            except KeyError:
                print(f"DB 에 해당키가 존재하지 않습니다 {key}")
                return None
        except:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def update_db_toml(key, value):
        try:
            db_pnx = StateManagementUtil.DB_YAML
            key: str = str(key)
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            # 기존의 DB 의 데이터
            with open(db_pnx, 'r', encoding='utf-8') as f:
                db = toml.load(f)
                # BusinessLogicUtil.print_as_log("DB 업데이트 전 ")
                # BusinessLogicUtil.print_as_log(context=str(db))

            # 데이터 업데이트
            if key in db:
                db[key] = value
            else:
                # db[key] = value
                print(f"DB에 key가 없어서 업데이트 할 수 없습니다 key:{key} value:{value}")

            # TOML 파일에 데이터 쓰기
            with open(db_pnx, 'w', encoding='utf-8') as f:
                toml.dump(db, f)
                print(f"DB에 데이터가 업데이트되었습니다")

            # DB 변경 확인
            # with open(db_pnx, 'r') as f:
            #     db = toml.load(f)
            #     BusinessLogicUtil.print_as_log("DB 변경 확인")
            #     BusinessLogicUtil.print_as_log(context=str(db))
        except:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def insert_db_toml(key, value):
        try:
            key = str(key)
            db_pnx = StateManagementUtil.DB_YAML
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            db_pnx = StateManagementUtil.DB_YAML
            # 기존의 DB 의 데이터
            with open(db_pnx, 'r', encoding='utf-8') as f:
                db = toml.load(f)
                # BusinessLogicUtil.print_as_log("DB 업데이트 전 ")
                # BusinessLogicUtil.print_as_log(context=str(db))

            # 데이터 삽입
            if key in db:
                # db[key] = value
                print(f"이미 값이 존재하여 삽입할 수 없습니다 key:{key} value:{value}")
            else:
                db[key] = value

            # TOML 파일에 데이터 쓰기
            with open(db_pnx, 'w', encoding='utf-8') as f:
                toml.dump(db, f)
                print(f"DB에 데이터가 삽입되었습니다")

            # DB 변경 확인
            # with open(db_pnx, 'r') as f:
            #     db = toml.load(f)
            #     BusinessLogicUtil.print_as_log("DB 변경 확인")
            #     BusinessLogicUtil.print_as_log(context=str(db))
        except:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def back_up_db_toml():
        try:
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.compress_pnx_via_bz(StateManagementUtil.DB_YAML)
        except:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def delete_db_toml():
        try:
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.convert_as_zip_with_timestamp(StateManagementUtil.DB_YAML)
        except:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def is_accesable_local_database():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        if not os.path.exists(StateManagementUtil.DB_YAML):
            DbTomlUtil.create_db_toml()
            return False
        else:
            return True


class MySqlUtil:
    """
    mysql 에 의존하는 유틸리티 객체
    """

    class Settings:
        protocol_type = "http"
        # db_driver = "mysql+mysqlconnector" # sqlalchemy mysql driver 설정 #  mysql-connector-python 라이브러리 에 의존
        db_driver = "mysql+pymysql"  # sqlalchemy 의 mysql driver 는 여러 개 built in 되어 있다. #  pymysql 라이브러리 에 의존
        host = "127.0.0.1"
        port = 3306
        id = "root"
        pw = "admin123!"
        database_name = 'test_db'
        # database_url = rf'{protocol_type}://{host}:{port}' # database 에 바로 연결하지 않음, use DB명령어를 써야할 수있음
        uri = rf"{db_driver}://{id}:{pw}@{host}:{port}/{database_name}?charset=utf8"

    # Base 가 여기에서 설정되어야 동작
    engine = create_engine(Settings.uri)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base = declarative_base()

    @staticmethod
    def get_session():  # ?  generator 로 되어있는데..?
        db = MySqlUtil.SessionLocal()
        try:
            yield db
        finally:
            db.close()

    @staticmethod
    def get_session_local():
        db = MySqlUtil.SessionLocal()
        return db

    @staticmethod
    def execute(native_query: str):  # without sqlarchemy
        # engine = create_engine(Settings.url)
        connection = MySqlUtil.engine.connect()
        BusinessLogicUtil.print_light_white(native_query)
        result = connection.execute(sqlalchecdmy_text(native_query))
        connection.close()
        return result


class MemberUtil:
    """
    mysql / sqlalchemy / fastapi 의존하는 유틸리티 객체
    """

    class Member(MySqlUtil.Base):  # orm 설정에는 id 있음
        __tablename__ = "members"
        __table_args__ = {'extend_existing': True}
        # __table_args__ = {'extend_existing': True, 'mysql_collate': 'utf8_general_ci'} # encoding 안되면 비슷하게 방법을 알아보자  mysql 에 적용이 가능한 코드로 보인다.
        Member_id = Column(Integer, primary_key=True, autoincrement=True)
        id = Column(VARCHAR(length=30))
        name = Column(VARCHAR(length=30))
        e_mail = Column(VARCHAR(length=30))
        phone_no = Column(VARCHAR(length=13))
        address = Column(VARCHAR(length=255))
        birthday = Column(VARCHAR(length=50))
        pw = Column(VARCHAR(length=100))
        date_joined = Column(VARCHAR(length=50))
        date_canceled = Column(VARCHAR(length=50))

    class MemberBase(BaseModel):  # pydantic validator 설정에는 Member_id 없음
        name: str
        pw: str
        phone_no: str
        address: str
        e_mail: str
        age: str
        id: str
        date_joined: str
        date_canceled: str

        @staticmethod
        @field_validator('id')
        def validate_id(value):
            MemberUtil.validate_id(value)

        @staticmethod
        @field_validator('name')
        def validate_name(value):
            MemberUtil.validate_name(value)

        @staticmethod
        @field_validator('e_mail')
        def validate_e_mail(value):
            MemberUtil.validate_e_mail(value)

        @staticmethod
        @field_validator('phone_no')
        def validate_phone_no(value):
            MemberUtil.validate_phone_no(value)

        @staticmethod
        @field_validator('address')
        def validate_address(value):
            MemberUtil.validate_address(value)

        @staticmethod
        @field_validator('birthday')
        def validate_birthday(value):
            MemberUtil.validate_birthday(value)

        @staticmethod
        @field_validator('pw')
        def validate_pw(value):
            MemberUtil.validate_pw(value)

        @staticmethod
        @field_validator('date_joined')
        def validate_date_joined(value):
            MemberUtil.validate_date_joined(value)

        @staticmethod
        @field_validator('date_canceled')
        def validate_date_canceled(value):
            MemberUtil.validate_date_canceled(value)

        @staticmethod  # class 간 종속 관계가 있을 때 하위 class 에 붙여 줘야하나?, cls, 파라미터와 함께? , instance를 생성하지 않고 호출 가능해?
        @field_validator('date_join')
        def validate_date_join(value):
            MemberUtil.validate_date_join(value)
            # datetime.strptime(date_join, '%Y-%m-%d %H:%M %S%f')
            if len(value) != 18:
                raise HTTPException(status_code=400, detail="유효한 날짜가 아닙니다.")
            return value

        @staticmethod
        @field_validator('pw')
        def validate_pw(value):
            MemberUtil.validate_pw(value)
            if len(value) != MemberUtil.Member.__table__.c.pw.type.length:
                raise HTTPException(status_code=400, detail="유효한 이메일 주소가 아닙니다.")
            return value

    @staticmethod
    def get_member_validated(member):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        # Member 클래스의 필드 개수 확인
        field_count = len(MemberUtil.Member.__table__.c)
        print(rf'''field_count : {field_count}''')

        pnxs_validated = [
            {"field_en": 'id', "field_ko": "아이디", "field_validation_func": MemberUtil.validate_id, "field_length_limit": MemberUtil.Member.__table__.c.id.type.length},
            {"field_en": 'name', "field_ko": "이름", "field_validation_func": MemberUtil.validate_name, "field_length_limit": MemberUtil.Member.__table__.c.name.type.length},
            {"field_en": 'e_mail', "field_ko": "이메일", "field_validation_func": MemberUtil.validate_e_mail, "field_length_limit": MemberUtil.Member.__table__.c.e_mail.type.length},
            {"field_en": 'phone_no', "field_ko": "전화번호", "field_validation_func": MemberUtil.validate_phone_no, "field_length_limit": MemberUtil.Member.__table__.c.phone_no.type.length},
            {"field_en": 'address', "field_ko": "주소", "field_validation_func": MemberUtil.validate_address, "field_length_limit": MemberUtil.Member.__table__.c.address.type.length},
            {"field_en": 'birthday', "field_ko": "생년월일", "field_validation_func": MemberUtil.validate_birthday, "field_length_limit": MemberUtil.Member.__table__.c.birthday.type.length},
            {"field_en": 'pw', "field_ko": "비밀번호", "field_validation_func": MemberUtil.validate_pw, "field_length_limit": MemberUtil.Member.__table__.c.pw.type.length},
            {"field_en": 'date_joined', "field_ko": "가입일", "field_validation_func": MemberUtil.validate_date_joined, "field_length_limit": MemberUtil.Member.__table__.c.date_joined.type.length},
            {"field_en": 'date_canceled', "field_ko": "탈퇴일", "field_validation_func": MemberUtil.validate_date_canceled, "field_length_limit": MemberUtil.Member.__table__.c.date_canceled.type.length},
        ]
        for target in pnxs_validated:
            field_en = target["field_en"]
            field_ko = target["field_ko"]
            field_validation_func = target["field_validation_func"]
            field_length_limit = target["field_length_limit"]
            if len(member[field_en]) > target['field_length_limit']:
                raise HTTPException(status_code=400, detail=f"{field_ko}({field_en})의 길이제한은 {field_length_limit}자 이하여야 합니다.")
            else:
                field_validation_func(member[field_en])  # success, 호출할 수 없는 함수의 내부에 구현된 부분이 필요한것 이므로 내부에 구현된 것을 다른 클래스에 구현해서 참조하도록 로직 분리,
        return member

    @staticmethod
    def validate_member(member):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        MemberUtil.get_member_validated(member)

    class MemberCreate(MemberBase):
        pass

    class MemberExtendedMemberBase(MemberBase):
        name: str
        pw: str
        phone_no: str
        address: str
        e_mail: str
        birthday: str
        id: str
        date_joined: str
        date_canceled: str

        class Config:
            # orm_mode = True
            from_attributes = True

    @staticmethod
    def get_members(db: Session):
        return db.query(MemberUtil.Member).all()

    @staticmethod
    def get_member(db: Session, id: int):
        # return db.query(MemberUtil.Member).filter(MemberUtil.Member.id == id).first() # success , 그러나 타입힌팅 에러가...
        MySqlUtil.execute(f'''SELECT * FROM members where id= {id} ORDER BY date_joined LIMIT 2;''')  # LIMIT 2 로 쿼리 성능 향상 기대, 2인 이유는 id가 2개면
        # 네이티브 쿼리를 한번 더 작성한 이유는 쿼리 디버깅
        return select(MemberUtil.Member).where(MemberUtil.Member.id.in_([id]))  # try

    @staticmethod
    def insert_member(db: Session, member):
        member_ = MemberUtil.Member(**member)
        db.add(member_)
        db.flush()  # flush() 메서드 없이 바로 commit() 메서드를 호출하면, 롤백할 수 있는 포인트가 만들어지지 않습니다. (# 나중에 롤백을 수행할 수 있는 포인트가 만들어짐)
        db.commit()
        db.refresh(member_)  # 데이터베이스에 업데이트된 최신내용을 세션에 가져오는 것.
        return member_

    @staticmethod
    def update_member(db: Session, member, updated_member):
        for key, value in updated_member.model_dump().members():
            setattr(member, key, value)
        db.commit()
        db.refresh(member)
        return member

    @staticmethod
    def delete_member(db: Session, member):
        db.delete(member)
        db.commit()

    @staticmethod
    def is_member_joined_by_id(id, request):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        result = MySqlUtil.get_session_local().query(MemberUtil.Member).filter(MemberUtil.Member.id == id).limit(2)
        for member in result:
            print(f"member.name: {member.name}, member.id: {member.id}")
        member_count = result.count()
        print(rf'''member_count : {member_count}''')
        if member_count == 1:
            for member_joined in result:
                print(f'member_joined.name: {member_joined.name}  member_joined.id: {member_joined.id}')
                request.session['name'] = member_joined.name
            return True
        else:
            return False

    @staticmethod
    def is_member_joined(id, pw, request):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        # native query
        # sql injection 에 취약,
        # 위험해서, 로그인 로직에 그냥은 못 쓴다.
        # rows = MySqlUtil.execute(f'''SELECT count(*) FROM members where id="{id}" and pw="{pw}" ORDER BY date_joined LIMIT 2;''')
        # id_count = rows.fetchone()[0]
        # print(rf'id_count : {id_count}')
        # if id_count == 1:
        #     return True
        # else:
        #     return False

        # orm
        # sql injection 에 강화됨.
        result = MySqlUtil.get_session_local().query(MemberUtil.Member).filter(MemberUtil.Member.id == id, MemberUtil.Member.pw == pw).limit(2)
        for member in result:
            print(f"member.name: {member.name}, member.id: {member.id}, member.pw: {member.pw}")
        member_count = result.count()
        print(rf'''member_count : {member_count}''')
        if member_count == 1:
            return True
        else:
            return False

    @staticmethod
    def get_member_name_joined(id, pw, request):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        result = MySqlUtil.get_session_local().query(MemberUtil.Member).filter(MemberUtil.Member.id == id, MemberUtil.Member.pw == pw).limit(2)
        member_count = result.count()
        print(rf'''member_count : {member_count}''')
        if member_count == 1:
            for member in result:
                return member.name

    @staticmethod
    def validate_id(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.raise_exception_after_special_charcater_check(value, inspect.currentframe().f_code.co_name)
        return True

    @staticmethod
    def validate_name(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.raise_exception_after_special_charcater_check(value, inspect.currentframe().f_code.co_name)
        return True

    @staticmethod
    def validate_e_mail(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.raise_exception_after_special_charcater_check(value, inspect.currentframe().f_code.co_name, ignore_list=["@"])
        MemberUtil.validate_address_e_mail(value)
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, value):
            # if not address_e_mail.endswith('@kakao.com'):
            #     raise HTTPException(status_code=400, detail="유효한 카카오 이메일이 아닙니다.")
            # return address_e_mail
            raise HTTPException(status_code=400, detail=f"유효한 이메일 주소가 아닙니다. {value}")
        return value

    @staticmethod
    def validate_phone_no(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # r'^\d{3}-\d{3,4}-\d{4}$'
        # r'^\d{2}-\d{3,4}-\d{4}$' 둘다
        if not re.match(r'^\d{2,3}-\d{3,4}-\d{4}$', value):
            raise HTTPException(status_code=400, detail=f"유효한 전화번호가 아닙니다. {value}")
        return value

    @staticmethod
    def validate_address(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        return True

    @staticmethod
    def validate_birthday(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        return True

    @staticmethod
    def validate_pw(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        return True

    @staticmethod
    def validate_date_joined(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        return True

    @staticmethod
    def validate_date_canceled(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        return True

    @staticmethod
    def validate_date_join(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        return True

    @staticmethod
    def validate_address_e_mail(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        return True


class CommutationManagementUtil:
    """
    mysql / sqlalchemy / fastapi 의존하는 유틸리티 객체
    """

    class CommutationManagement(MySqlUtil.Base):
        __tablename__ = "commutation_management"
        __table_args__ = {'extend_existing': True}
        commutation_management_id = Column(Integer, primary_key=True, autoincrement=True)
        id = Column(VARCHAR(length=30))
        name = Column(VARCHAR(length=30))
        phone_no = Column(VARCHAR(length=13))
        time_to_go_to_office = Column(VARCHAR(length=100))
        time_to_leave_office = Column(VARCHAR(length=100))

    class CommutationManagementBase(BaseModel):
        id: str
        name: str
        phone_no: str
        time_to_go_to_office: str
        time_to_leave_office: str

        # @staticmethod
        # @field_validator('id')
        # def validate_id(value):
        #     CommutationManagementUtil.validate_id(value)

    @staticmethod
    def get_commutation_management_validated(commutation_management):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        # CommutationManagement 클래스의 필드 개수 확인
        field_count = len(CommutationManagementUtil.CommutationManagement.__table__.c)
        print(rf'''field_count : {field_count}''')

        pnxs_validated = [
            {"field_en": 'id', "field_ko": "아이디", "field_validation_func": CommutationManagementUtil.validate_id, "field_length_limit": CommutationManagementUtil.CommutationManagement.__table__.c.id.type.length},
            {"field_en": 'name', "field_ko": "이름", "field_validation_func": CommutationManagementUtil.validate_name, "field_length_limit": CommutationManagementUtil.CommutationManagement.__table__.c.name.type.length},
            {"field_en": 'phone_no', "field_ko": "전화번호", "field_validation_func": CommutationManagementUtil.validate_phone_no, "field_length_limit": CommutationManagementUtil.CommutationManagement.__table__.c.phone_no.type.length},
            {"field_en": 'time_to_go_to_office', "field_ko": "출근시간", "field_validation_func": CommutationManagementUtil.validate_time_to_go_to_office, "field_length_limit": CommutationManagementUtil.CommutationManagement.__table__.c.time_to_go_to_office.type.length},
            {"field_en": 'time_to_go_to_office', "field_ko": "퇴근시간", "field_validation_func": CommutationManagementUtil.validate_time_to_leave_office, "field_length_limit": CommutationManagementUtil.CommutationManagement.__table__.c.time_to_leave_office.type.length},
        ]
        for target in pnxs_validated:
            field_en = target["field_en"]
            field_ko = target["field_ko"]
            field_validation_func = target["field_validation_func"]
            field_length_limit = target["field_length_limit"]
            if len(commutation_management[field_en]) > target['field_length_limit']:
                raise HTTPException(status_code=400, detail=f"{field_ko}({field_en})의 길이제한은 {field_length_limit}자 이하여야 합니다.")
            else:
                field_validation_func(commutation_management[field_en])  # success, 호출할 수 없는 함수의 내부에 구현된 부분이 필요한것 이므로 내부에 구현된 것을 다른 클래스에 구현해서 참조하도록 로직 분리,
        return commutation_management

    @staticmethod
    def validate_commutation_management(commutation_management):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        CommutationManagementUtil.get_commutation_management_validated(commutation_management)

    class CommutationManagementCreate(CommutationManagementBase):
        pass

    class CommutationManagementExtendedCommutationManagementBase(CommutationManagementBase):
        id: str
        name: str
        phone_no: str
        time_to_go_to_office: str
        time_to_leave_office: str

        class Config:
            # orm_mode = True
            from_attributes = True

    @staticmethod
    def get_commutation_managements(db: Session):
        return db.query(CommutationManagementUtil.CommutationManagement).all()

    @staticmethod
    def get_commutation_management(db: Session, id: int):
        # return db.query(CommutationManagementUtil.CommutationManagement).filter(CommutationManagementUtil.CommutationManagement.id == id).first() # success , 그러나 타입힌팅 에러가...
        return select(CommutationManagementUtil.CommutationManagement).where(CommutationManagementUtil.CommutationManagement.id.in_([id]))  # try

    @staticmethod
    def insert_commutation_management(db: Session, commutation_management):
        commutation_management_ = CommutationManagementUtil.CommutationManagement(**commutation_management)
        db.add(commutation_management_)
        db.flush()
        db.commit()
        db.refresh(commutation_management_)
        return commutation_management_

    @staticmethod
    def update_commutation_management(db: Session, commutation_management, updated_commutation_management):
        for key, value in updated_commutation_management.model_dump().commutation_managements():
            setattr(commutation_management, key, value)
        db.commit()
        db.refresh(commutation_management)
        return commutation_management

    @staticmethod
    def validate_id(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.raise_exception_after_special_charcater_check(value, inspect.currentframe().f_code.co_name)
        return True

    @staticmethod
    def validate_name(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.raise_exception_after_special_charcater_check(value, inspect.currentframe().f_code.co_name)
        return True

    @staticmethod
    def validate_phone_no(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # r'^\d{3}-\d{3,4}-\d{4}$'
        # r'^\d{2}-\d{3,4}-\d{4}$' 둘다
        if not re.match(r'^\d{2,3}-\d{3,4}-\d{4}$', value):
            raise HTTPException(status_code=400, detail=f"유효한 전화번호가 아닙니다. {value}")
        return value

    @staticmethod
    def validate_time_to_go_to_office(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        return True

    @staticmethod
    def validate_time_to_leave_office(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        return True


class ItemsUtil:
    class Item(MySqlUtil.Base):  # orm 설정에는 id 있음
        __tablename__ = "items"
        # __table_args__ = {'extend_existing': True}  # 이옵션을 쓰면 여기에 작성된 item 대로 테이블이 다르면 새로확장이되는 거란다.
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String(30))
        # price = Column(Integer)

    class ItemBase(BaseModel):  # pydantic validator 설정에는 id 없음
        name: str

    class ItemCreate(ItemBase):
        pass

    class ItemExtendedItemBase(ItemBase):
        id: int

        class Config:
            # orm_mode = True
            from_attributes = True

    @staticmethod
    def get_items(db: Session):
        return db.query(ItemsUtil.Item).all()

    @staticmethod
    def get_item(db: Session, id: int):
        # return db.query(ItemsUtil.Item).filter(column("id") == id).first()
        # return db.query(ItemsUtil.Item).filter(ItemsUtil.Item.id == id).first() , success , 그러나 타입힌팅 에러가...
        # return select(ItemsUtil.Item).where(ItemsUtil.Item.id.in_(["id1","id2"]))
        return select(ItemsUtil.Item).where(ItemsUtil.Item.id.in_([id]))

    @staticmethod
    def create_item(db: Session, item):
        db_item = ItemsUtil.Item(**item.model_dump())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    @staticmethod
    def update_item(db: Session, item, updated_item):
        for key, value in updated_item.model_dump().items():
            setattr(item, key, value)
        db.commit()
        db.refresh(item)
        return item

    @staticmethod
    def delete_item(db: Session, item):
        db.delete(item)
        db.commit()


class FaqBoardUtil:
    """
    mysql / sqlalchemy / fastapi 의존하는 유틸리티 객체
    """

    class FaqBoard(MySqlUtil.Base):  # orm 설정에는 id 있음
        __tablename__ = "faq_boards"
        __table_args__ = {'extend_existing': True}
        # __table_args__ = {'extend_existing': True, 'mysql_collate': 'utf8_general_ci'} # encoding 안되면 비슷하게 방법을 알아보자  mysql 에 적용이 가능한 코드로 보인다.
        FaqBoard_id: str = uuid4().hex + TimeUtil.get_time_as_('%Y%m%d%H%M%S%f') + SecurityUtil.get_random_alphabet()  # table 내 unique id
        id = Column(Integer, primary_key=True, autoincrement=True)  # index 로 이용
        writer = Column(VARCHAR(length=30))
        title = Column(VARCHAR(length=30))
        contents = Column(VARCHAR(length=13))
        date_reg = Column(DateTime, nullable=False, default=datetime.now)
        del_yn = Column(VARCHAR(length=50))

    class FaqBoardBase(BaseModel):  # pydantic validator 설정에는 FaqBoard_id 없음
        id: str
        writer: str
        title: str
        contents: Optional[str]
        date_reg: str
        del_yn: str

        @staticmethod
        @field_validator('id')
        def validate_id(value):
            FaqBoardUtil.validate_id(value)

        @staticmethod
        @field_validator('writer')
        def validate_writer(value):
            FaqBoardUtil.validate_writer(value)

        @staticmethod
        @field_validator('title')
        def validate_title(value):
            FaqBoardUtil.validate_title(value)

        @staticmethod
        @field_validator('contents')
        def validate_contents(value):
            FaqBoardUtil.validate_contents(value)

        @staticmethod
        @field_validator('date_reg')
        def validate_date_reg(value):
            # datetime.strptime(date_join, '%Y-%m-%d %H:%M %S%f')
            if len(value) != 18:
                raise HTTPException(status_code=400, detail="유효한 날짜가 아닙니다.")
            FaqBoardUtil.validate_date_reg(value)

        @staticmethod
        @field_validator('del_yn')
        def validate_del_yn(value):
            FaqBoardUtil.validate_del_yn(value)

    @staticmethod
    def get_faq_board_validated(faq_board):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        # FaqBoard 클래스의 필드 개수 확인
        field_count = len(FaqBoardUtil.FaqBoard.__table__.c)
        print(rf'''field_count : {field_count}''')

        pnxs_validated = [
            {"field_en": 'id', "field_ko": "아이디", "field_validation_func": FaqBoardUtil.validate_id, "field_length_limit": FaqBoardUtil.FaqBoard.__table__.c.id.type.length},
            {"field_en": 'writer', "field_ko": "이름", "field_validation_func": FaqBoardUtil.validate_writer, "field_length_limit": FaqBoardUtil.FaqBoard.__table__.c.writer.type.length},
            {"field_en": 'title', "field_ko": "이메일", "field_validation_func": FaqBoardUtil.validate_title, "field_length_limit": FaqBoardUtil.FaqBoard.__table__.c.title.type.length},
            {"field_en": 'contents', "field_ko": "전화번호", "field_validation_func": FaqBoardUtil.validate_contents, "field_length_limit": FaqBoardUtil.FaqBoard.__table__.c.contents.type.length},
            {"field_en": 'date_reg', "field_ko": "주소", "field_validation_func": FaqBoardUtil.validate_date_reg, "field_length_limit": FaqBoardUtil.FaqBoard.__table__.c.date_reg.type.length},
            {"field_en": 'del_yn', "field_ko": "가입일", "field_validation_func": FaqBoardUtil.validate_del_yn, "field_length_limit": FaqBoardUtil.FaqBoard.__table__.c.del_yn.type.length},
        ]
        for target in pnxs_validated:
            field_en = target["field_en"]
            field_ko = target["field_ko"]
            field_validation_func = target["field_validation_func"]
            field_length_limit = target["field_length_limit"]
            if len(faq_board[field_en]) > target['field_length_limit']:
                raise HTTPException(status_code=400, detail=f"{field_ko}({field_en})의 길이제한은 {field_length_limit}자 이하여야 합니다.")
            else:
                field_validation_func(faq_board[field_en])  # success, 호출할 수 없는 함수의 내부에 구현된 부분이 필요한것 이므로 내부에 구현된 것을 다른 클래스에 구현해서 참조하도록 로직 분리,
        return faq_board

    @staticmethod
    def validate_faq_board(faq_board):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        FaqBoardUtil.get_faq_board_validated(faq_board)

    class FaqBoardCreate(FaqBoardBase):
        pass

    class FaqBoardExtendedFaqBoardBase(FaqBoardBase):
        id: str
        writer: str
        title: str
        contents: str
        date_reg: str
        del_yn: str

        class Config:
            from_attributes = True

    @staticmethod
    def get_faq_boards(db: Session):
        return db.query(FaqBoardUtil.FaqBoard).all()

    @staticmethod
    def get_faq_board(db: Session, id: int):
        # return db.query(FaqBoardUtil.FaqBoard).filter(FaqBoardUtil.FaqBoard.id == id).first() # success , 그러나 타입힌팅 에러가...
        MySqlUtil.execute(f'''SELECT * FROM faq_boards where id= {id} ORDER BY del_yn LIMIT 2;''')  # LIMIT 2 로 쿼리 성능 향상 기대, 2인 이유는 id가 2개면
        # 네이티브 쿼리를 한번 더 작성한 이유는 쿼리 디버깅
        return select(FaqBoardUtil.FaqBoard).where(FaqBoardUtil.FaqBoard.id.in_([id]))  # try

    @staticmethod
    def insert_faq_board(db: Session, faq_board):
        faq_board_ = FaqBoardUtil.FaqBoard(**faq_board)
        db.add(faq_board_)
        db.flush()  # flush() 메서드 없이 바로 commit() 메서드를 호출하면, 롤백할 수 있는 포인트가 만들어지지 않습니다. (# 나중에 롤백을 수행할 수 있는 포인트가 만들어짐)
        db.commit()
        db.refresh(faq_board_)  # 데이터베이스에 업데이트된 최신내용을 세션에 가져오는 것.
        return faq_board_

    @staticmethod
    def update_faq_board(db: Session, faq_board, updated_faq_board):
        for key, value in updated_faq_board.model_dump().faq_boards():
            setattr(faq_board, key, value)
        db.commit()
        db.refresh(faq_board)
        return faq_board

    @staticmethod
    def delete_faq_board(db: Session, faq_board):
        db.delete(faq_board)
        db.commit()

    @staticmethod
    def is_faq_board_joined_by_id(id, request):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        result = MySqlUtil.get_session_local().query(FaqBoardUtil.FaqBoard).filter(FaqBoardUtil.FaqBoard.id == id).limit(2)
        for faq_board in result:
            print(f"faq_board.name: {faq_board.name}, faq_board.id: {faq_board.id}")
        faq_board_count = result.count()
        print(rf'''faq_board_count : {faq_board_count}''')
        if faq_board_count == 1:
            for faq_board_joined in result:
                print(f'faq_board_joined.name: {faq_board_joined.name}  faq_board_joined.id: {faq_board_joined.id}')
                request.session['name'] = faq_board_joined.name
            return True
        else:
            return False

    @staticmethod
    def validate_id(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.raise_exception_after_special_charcater_check(value, inspect.currentframe().f_code.co_name)
        return True

    @staticmethod
    def validate_writer(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.raise_exception_after_special_charcater_check(value, inspect.currentframe().f_code.co_name)
        return True

    @staticmethod
    def validate_title(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.raise_exception_after_special_charcater_check(value, inspect.currentframe().f_code.co_name, ignore_list=["@"])
        FaqBoardUtil.validate_title(value)
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, value):
            # if not date_reg_title.endswith('@kakao.com'):
            #     raise HTTPException(status_code=400, detail="유효한 카카오 이메일이 아닙니다.")
            # return date_reg_title
            raise HTTPException(status_code=400, detail=f"유효한 이메일 주소가 아닙니다. {value}")
        return value

    @staticmethod
    def validate_contents(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # r'^\d{3}-\d{3,4}-\d{4}$'
        # r'^\d{2}-\d{3,4}-\d{4}$' 둘다
        if not re.match(r'^\d{2,3}-\d{3,4}-\d{4}$', value):
            raise HTTPException(status_code=400, detail=f"유효한 전화번호가 아닙니다. {value}")
        return value

    @staticmethod
    def validate_date_reg(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        return True

    @staticmethod
    def validate_del_yn(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        return True


class CustomerServiceBoardUtil:
    """
    mysql / sqlalchemy / fastapi 의존하는 유틸리티 객체
    """

    class CustomerServiceBoard(MySqlUtil.Base):  # orm 설정에는 id 있음
        __tablename__ = "customer_service_board"
        __table_args__ = {'extend_existing': True}
        # __table_args__ = {'extend_existing': True, 'mysql_collate': 'utf8_general_ci'} # encoding 안되면 비슷하게 방법을 알아보자  mysql 에 적용이 가능한 코드로 보인다.
        CustomerServiceBoard_id: str = uuid4().hex + TimeUtil.get_time_as_('%Y%m%d%H%M%S%f') + SecurityUtil.get_random_alphabet()  # table 내 unique id
        id = Column(Integer, primary_key=True, autoincrement=True)  # index 로 이용
        writer = Column(VARCHAR(length=30))
        title = Column(VARCHAR(length=30))
        contents = Column(VARCHAR(length=13))
        date_reg = Column(DateTime, nullable=False, default=datetime.now)
        del_yn = Column(VARCHAR(length=50))

    class CustomerServiceBoardBase(BaseModel):  # pydantic validator 설정에는 CustomerServiceBoard_id 없음
        id: str
        writer: str
        title: str
        contents: Optional[str]
        date_reg: str
        del_yn: str

        @staticmethod
        @field_validator('id')
        def validate_id(value):
            CustomerServiceBoardUtil.validate_id(value)

        @staticmethod
        @field_validator('writer')
        def validate_writer(value):
            CustomerServiceBoardUtil.validate_writer(value)

        @staticmethod
        @field_validator('title')
        def validate_title(value):
            CustomerServiceBoardUtil.validate_title(value)

        @staticmethod
        @field_validator('contents')
        def validate_contents(value):
            CustomerServiceBoardUtil.validate_contents(value)

        @staticmethod
        @field_validator('date_reg')
        def validate_date_reg(value):
            # datetime.strptime(date_join, '%Y-%m-%d %H:%M %S%f')
            if len(value) != 18:
                raise HTTPException(status_code=400, detail="유효한 날짜가 아닙니다.")
            CustomerServiceBoardUtil.validate_date_reg(value)

        @staticmethod
        @field_validator('del_yn')
        def validate_del_yn(value):
            CustomerServiceBoardUtil.validate_del_yn(value)

    @staticmethod
    def get_customer_service_board_validated(customer_service_board):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        # CustomerServiceBoard 클래스의 필드 개수 확인
        field_count = len(CustomerServiceBoardUtil.CustomerServiceBoard.__table__.c)
        print(rf'''field_count : {field_count}''')

        pnxs_validated = [
            {"field_en": 'id', "field_ko": "아이디", "field_validation_func": CustomerServiceBoardUtil.validate_id, "field_length_limit": CustomerServiceBoardUtil.CustomerServiceBoard.__table__.c.id.type.length},
            {"field_en": 'writer', "field_ko": "이름", "field_validation_func": CustomerServiceBoardUtil.validate_writer, "field_length_limit": CustomerServiceBoardUtil.CustomerServiceBoard.__table__.c.writer.type.length},
            {"field_en": 'title', "field_ko": "이메일", "field_validation_func": CustomerServiceBoardUtil.validate_title, "field_length_limit": CustomerServiceBoardUtil.CustomerServiceBoard.__table__.c.title.type.length},
            {"field_en": 'contents', "field_ko": "전화번호", "field_validation_func": CustomerServiceBoardUtil.validate_contents, "field_length_limit": CustomerServiceBoardUtil.CustomerServiceBoard.__table__.c.contents.type.length},
            {"field_en": 'date_reg', "field_ko": "주소", "field_validation_func": CustomerServiceBoardUtil.validate_date_reg, "field_length_limit": CustomerServiceBoardUtil.CustomerServiceBoard.__table__.c.date_reg.type.length},
            {"field_en": 'del_yn', "field_ko": "가입일", "field_validation_func": CustomerServiceBoardUtil.validate_del_yn, "field_length_limit": CustomerServiceBoardUtil.CustomerServiceBoard.__table__.c.del_yn.type.length},
        ]
        for target in pnxs_validated:
            field_en = target["field_en"]
            field_ko = target["field_ko"]
            field_validation_func = target["field_validation_func"]
            field_length_limit = target["field_length_limit"]
            if len(customer_service_board[field_en]) > target['field_length_limit']:
                raise HTTPException(status_code=400, detail=f"{field_ko}({field_en})의 길이제한은 {field_length_limit}자 이하여야 합니다.")
            else:
                field_validation_func(customer_service_board[field_en])  # success, 호출할 수 없는 함수의 내부에 구현된 부분이 필요한것 이므로 내부에 구현된 것을 다른 클래스에 구현해서 참조하도록 로직 분리,
        return customer_service_board

    @staticmethod
    def validate_customer_service_board(customer_service_board):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        CustomerServiceBoardUtil.get_customer_service_board_validated(customer_service_board)

    class CustomerServiceBoardCreate(CustomerServiceBoardBase):
        pass

    class CustomerServiceBoardExtendedCustomerServiceBoardBase(CustomerServiceBoardBase):
        id: str
        writer: str
        title: str
        contents: str
        date_reg: str
        del_yn: str

        class Config:
            from_attributes = True

    @staticmethod
    def get_customer_service_boards(db: Session):
        return db.query(CustomerServiceBoardUtil.CustomerServiceBoard).all()

    @staticmethod
    def get_customer_service_board(id: int):
        # return db.query(CustomerServiceBoardUtil.CustomerServiceBoard).filter(CustomerServiceBoardUtil.CustomerServiceBoard.id == id).first() # success , 그러나 타입힌팅 에러가...
        MySqlUtil.execute(f'''SELECT * FROM customer_service_board where id= {id} ORDER BY del_yn LIMIT 2;''')  # LIMIT 2 로 쿼리 성능 향상 기대, 2인 이유는 id가 2개면
        # 네이티브 쿼리를 한번 더 작성한 이유는 쿼리 디버깅
        db_data = MySqlUtil.get_session_local().query(CustomerServiceBoardUtil.CustomerServiceBoard).filter_by(id=id).limit(4).all()
        return db_data  # try

    @staticmethod
    def insert_customer_service_board(db: Session, customer_service_board):
        customer_service_board_ = CustomerServiceBoardUtil.CustomerServiceBoard(**customer_service_board)
        db.add(customer_service_board_)
        db.flush()  # flush() 메서드 없이 바로 commit() 메서드를 호출하면, 롤백할 수 있는 포인트가 만들어지지 않습니다. (# 나중에 롤백을 수행할 수 있는 포인트가 만들어짐)
        db.commit()
        db.refresh(customer_service_board_)  # 데이터베이스에 업데이트된 최신내용을 세션에 가져오는 것.
        return customer_service_board_

    @staticmethod
    def update_customer_service_board(db: Session, customer_service_board, updated_customer_service_board):
        for key, value in updated_customer_service_board.model_dump().customer_service_boards():
            setattr(customer_service_board, key, value)
        db.commit()
        db.refresh(customer_service_board)
        return customer_service_board

    @staticmethod
    def delete_customer_service_board(db: Session, customer_service_board):
        db.delete(customer_service_board)
        db.commit()

    @staticmethod
    def is_customer_service_board_joined_by_id(id, request):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        result = MySqlUtil.get_session_local().query(CustomerServiceBoardUtil.CustomerServiceBoard).filter(CustomerServiceBoardUtil.CustomerServiceBoard.id == id).limit(2)
        for customer_service_board in result:
            print(f"customer_service_board.name: {customer_service_board.name}, customer_service_board.id: {customer_service_board.id}")
        customer_service_board_count = result.count()
        print(rf'''customer_service_board_count : {customer_service_board_count}''')
        if customer_service_board_count == 1:
            for customer_service_board_joined in result:
                print(f'customer_service_board_joined.name: {customer_service_board_joined.name}  customer_service_board_joined.id: {customer_service_board_joined.id}')
                request.session['name'] = customer_service_board_joined.name
            return True
        else:
            return False

    @staticmethod
    def validate_id(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.raise_exception_after_special_charcater_check(value, inspect.currentframe().f_code.co_name)
        return True

    @staticmethod
    def validate_writer(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.raise_exception_after_special_charcater_check(value, inspect.currentframe().f_code.co_name)
        return True

    @staticmethod
    def validate_title(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.raise_exception_after_special_charcater_check(value, inspect.currentframe().f_code.co_name, ignore_list=["@"])
        CustomerServiceBoardUtil.validate_title(value)
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(pattern, value):
            # if not date_reg_title.endswith('@kakao.com'):
            #     raise HTTPException(status_code=400, detail="유효한 카카오 이메일이 아닙니다.")
            # return date_reg_title
            raise HTTPException(status_code=400, detail=f"유효한 이메일 주소가 아닙니다. {value}")
        return value

    @staticmethod
    def validate_contents(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # r'^\d{3}-\d{3,4}-\d{4}$'
        # r'^\d{2}-\d{3,4}-\d{4}$' 둘다
        if not re.match(r'^\d{2,3}-\d{3,4}-\d{4}$', value):
            raise HTTPException(status_code=400, detail=f"유효한 전화번호가 아닙니다. {value}")
        return value

    @staticmethod
    def validate_date_reg(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        return True

    @staticmethod
    def validate_del_yn(value):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        return True


class TextConvertMode(Enum):
    STR_TO_LIST = rf' from  test love to  "test love" '
    GREEN = 2
    BLUE = 3


class BusinessLogicError(Exception):
    def __init__(self, ment_error):
        self.ment_error = ment_error
        BusinessLogicUtil.print_light_black(self.ment_error)
        BusinessLogicUtil.print_as_gui(self.ment_error)
        super().__init__(ment_error)  # 부모 클래스의 초기화도 호출


class BusinessLogicUtil:
    def __init__(self):
        self.USER_PROFILE = os.path.expanduser("~")

    @staticmethod
    def get_tree_depth_level(file_pnx: str):
        return len(file_pnx.split("\\")) - 1

    @staticmethod
    def get_pnx(pnx):
        """디렉토리/파일 대상 테스트 성공"""
        return pnx

    @staticmethod
    def get_pn(pnx):
        """디렉토리/파일 대상 테스트 성공"""
        return rf"{os.path.dirname(pnx)}\{os.path.splitext(os.path.basename(pnx))[0]}"

    @staticmethod
    def get_nx(pnx):
        """디렉토리/파일 대상 테스트 성공"""
        return rf"{os.path.splitext(os.path.basename(pnx))[0]}{os.path.splitext(os.path.basename(pnx))[1]}"

    @staticmethod
    def get_x(pnx):
        """# . 포함해서 리턴한다 ex> .txt """
        if BusinessLogicUtil.is_file(pnx=pnx):
            return rf"{os.path.splitext(os.path.basename(pnx))[1]}"
        else:
            return ""

    @staticmethod
    def get_n(pnx):
        if BusinessLogicUtil.is_file(pnx=pnx):
            return rf"{os.path.splitext(os.path.basename(pnx))[0]}"
        else:
            return os.path.basename(pnx)

    @staticmethod
    def convert_mkv_to_wav(file_mkv):
        BusinessLogicUtil.command_to_os_like_person_as_admin(rf'ffmpeg -i "{file_mkv}" -ab 160k -ac 2 -ar 44100 -vn {BusinessLogicUtil.get_pn(file_mkv)}.wav')

    @staticmethod
    def convert_mp4_to_webm(target_pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        '''테스트 필요'''
        BusinessLogicUtil.print_cyan(f'from : {target_pnx}')
        file_edited = f'{os.path.splitext(os.path.basename(target_pnx))[0]}.webm'
        BusinessLogicUtil.print_cyan(f'to   : {file_edited}')

        path_started = os.getcwd()
        os.system("chcp 65001 >nul")
        os.system('mkdir storage >nul')
        os.chdir('storage')
        os.system(f'"{StateManagementUtil.FFMPEG_EXE}" -i "{target_pnx}" -f webm -c:v libvpx -b:v 1M -acodec libvorbis "{file_edited}" -hide_banner')
        os.chdir(path_started)

    @staticmethod
    def convert_wav_to_flac(target_pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        '''테스트 필요'''

        # 한글 인코딩 setting
        os.system("chcp 65001 >nul")

        BusinessLogicUtil.print_cyan(f'from : {target_pnx}')
        file_edited = f'{os.path.splitext(os.path.basename(target_pnx))[0]}.flac'
        BusinessLogicUtil.print_cyan(f'to   : {file_edited}')

        # ffmpeg location setting
        ffmpeg_exe = rf"{StateManagementUtil.USERPROFILE}\Desktop\`workspace\tool\LosslessCut-win-x64\resources\ffmpeg.exe"
        destination = 'storage'
        try:
            os.makedirs(destination)
        except Exception as e:
            pass
        os.chdir(destination)
        BusinessLogicUtil.print_cyan(f'"{ffmpeg_exe}" -i "{target_pnx}" -c:a flac "{file_edited}"        를 수행합니다.')
        subprocess.check_output(f'"{ffmpeg_exe}" -i "{target_pnx}" -c:a flac "{file_edited}"', shell=True)

    @staticmethod
    def convert_mp4_to_wav(target_pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        '''테스트 필요'''
        BusinessLogicUtil.print_cyan(f'from : {target_pnx}')
        file_edited = f'{os.path.splitext(os.path.basename(target_pnx))[0]}.wav'
        BusinessLogicUtil.print_cyan(f'to   : {file_edited}')

        path_started = os.getcwd()

        os.system('mkdir storage')
        os.chdir('storage')
        if os.path.splitext(os.path.basename(target_pnx))[1] == '.mp4':
            videoclip = VideoFileClip(target_pnx)
            audioclip = videoclip.audio

            # audioclip.write_audiofile(file_edited, fps= 8000 )
            audioclip.write_audiofile(file_edited, fps=44100)
            audioclip.close()
            videoclip.close()

        os.chdir(path_started)

    @staticmethod
    def convert_mp4_to_flac(target_pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        '''테스트 필요'''
        # 한글 인코딩 setting
        os.system("chcp 65001 >nul")
        BusinessLogicUtil.print_cyan(f'from : {target_pnx}')
        file_edited = f'{os.path.splitext(os.path.basename(target_pnx))[0]}.flac'
        BusinessLogicUtil.print_cyan(f'to   : {file_edited}')

        path_started = os.getcwd()

        # ffmpeg location setting
        ffmpeg_exe = rf"{StateManagementUtil.USERPROFILE}\Desktop\`workspace\tool\LosslessCut-win-x64\resources\ffmpeg.exe"
        destination = 'storage'
        try:
            os.makedirs(destination)
        except Exception as e:
            pass
        os.chdir(destination)
        BusinessLogicUtil.print_cyan(f'"{ffmpeg_exe}" -i "{target_pnx}" -c:a flac "{file_edited}"        를 수행합니다.')
        subprocess.check_output(f'"{ffmpeg_exe}" -i "{target_pnx}" -c:a flac "{file_edited}"', shell=True)

        os.chdir(path_started)

    @staticmethod
    def convert_mp3_to_flac(target_pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        '''테스트 필요'''
        os.system("chcp 65001 >nul")

        BusinessLogicUtil.print_cyan(f'from : {target_pnx}')
        file_edited = f'{os.path.splitext(os.path.basename(target_pnx))[0]}.flac'
        BusinessLogicUtil.print_cyan(f'to   : {file_edited}')

        path_started = os.getcwd()

        # ffmpeg location setting
        ffmpeg_exe = rf"{StateManagementUtil.USERPROFILE}\Desktop\`workspace\tool\LosslessCut-win-x64\resources\ffmpeg.exe"
        destination = 'storage'
        try:
            os.makedirs(destination)
        except Exception as e:
            pass
        os.chdir(destination)
        BusinessLogicUtil.print_cyan(f'"{ffmpeg_exe}" -i "{target_pnx}" -c:a flac "{file_edited}"        를 수행합니다.')
        subprocess.check_output(f'"{ffmpeg_exe}" -i "{target_pnx}" -c:a flac "{file_edited}"', shell=True)

        os.chdir(path_started)

    @staticmethod
    def convert_xls_to_xlsx(target_pnx):
        """
        2024-02-12 15:45 작성 함수 템플릿 샘플
        """
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        import pandas as pd
        new_file_xlsx = f'{BusinessLogicUtil.get_pn(target_pnx)}.xlsx'

        try:
            if ".xls" == BusinessLogicUtil.get_x(target_pnx):
                if not os.path.exists(target_pnx):
                    BusinessLogicUtil.print_red(f"{function_name}(), fail, {BusinessLogicUtil.get_x(target_pnx)} 는 처리할 수 없는 확장자입니다.")
                    return
        except CustomErrorUtil as e:
            BusinessLogicUtil.print_red(f"{function_name}(), fail, {BusinessLogicUtil.get_x(target_pnx)} 는 처리할 수 없는 확장자입니다.")
            return

        from zipfile import BadZipFile
        try:
            df = pd.read_excel(target_pnx, engine='openpyxl')  # openpyxl 에만 적용이 되는 함수.. 에러 소지 있음.
            # if not os.path.exists(new_file_xlsx):
            df.to_excel(new_file_xlsx, index=False)
        except BadZipFile as e:
            # 유효데이터만 파싱하여 데이터프레임 으로 변환 후 Excel 파일로 저장
            # read_html() 를 이용하면 손상된 파일을 열 수 ...
            BusinessLogicUtil.print_yellow(f"확장자가 {BusinessLogicUtil.get_x(target_pnx)} 손상된 파일 같습니다. 복구를 시도합니다")
            df = pd.read_html(target_pnx, encoding='utf-8')
            # BusinessLogicUtil.print_ment_blue(df)
            # BusinessLogicUtil.print_ment_blue(df[0]) # 이번 데이터 구조의 특성상, 불필요 데이터
            # BusinessLogicUtil.print_ment_blue(df[1]) # 이번 데이터 구조의 특성상, 불필요 데이터
            # BusinessLogicUtil.print_ment_blue(df[2]) # 이번 데이터 구조의 특성상, 유효 데이터 , 데이터프레임 모든컬럼
            # BusinessLogicUtil.print_ment_blue(df[2].get(0)) # 데이터프레임 첫번쨰컬럼
            # BusinessLogicUtil.print_ment_blue(df[2].get(1)) # 데이터프레임 두번쨰컬럼
            # BusinessLogicUtil.print_ment_blue(df[2].get(2)) #
            # BusinessLogicUtil.print_ment_blue(df[2].get(6)) #
            # 이번 데이터에서 필요한 데이터, # 0 ~ 6 컬럼까지 유효
            df = df[2]  # 이번 데이터 구조의 특성상, 유효 데이터
            # df_selected = df[[0, 1, 2, 3, 4, 5, 6]]
            # df_selected = df[df.columns[0:7]]
            # df_selected = df[df.columns[7:]]
            # df_selected = df[df.columns[:5]]
            # df_selected = df[df.columns[1:5]]
            df = df[df.columns[:]]  # 모든 컬럼
            # print(rf'df : {df}')
            df.to_excel(new_file_xlsx, index=False)

            # # txt 로 변환
            # file_recovery = f"{BusinessLogicUtil.get_target_as_pn(target_pnx)}.txt"
            # print(rf'''file_recovery : {file_recovery}''')
            # shutil.copy(target_pnx,file_recovery)

            # # html 로 변환하여, HTML 테이블을 데이터프레임으로 저장
            # file_recovery = f"{BusinessLogicUtil.get_target_as_pn(target_pnx)}.html"
            # print(rf'''file_recovery : {file_recovery}''')
            # shutil.copy(target_pnx,file_recovery)
            # with open(file_recovery, 'r', encoding='utf-8') as file:
            #     html_content = file.read()
            # soup = BeautifulSoup(html_content, "lxml")
            # # results = soup.find_all(href=re.compile("magnet"), id='link1') # <a class="sister" href="http://example.com/magnet" id="link1">Elsie</a>
            # # results = soup.find_all("table", class_="datatable")  # <table class="datatable">foo!</div>
            # # results = soup.find_all("body")
            # # results = soup.find_all("html")
            # tables = soup.find_all("table")
            # table_selected = tables[2]  # 3번째 테이블 선택
            # df = pd.read_html(str(table_selected))[0]
            # BusinessLogicUtil.print_ment_blue(df)

        except Exception as e:
            BusinessLogicUtil.print_red(f"{function_name}(), fail, \n {traceback.format_exc()}")
        BusinessLogicUtil.print_success(f"{function_name}(), success")

    @staticmethod
    def convert_as_zip_with_timestamp(target_pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        starting_directory = BusinessLogicUtil.get_working_directory()
        try:
            target_dirname = os.path.dirname(target_pnx)
            target_dirname_dirname = os.path.dirname(target_dirname)
            target_basename = os.path.basename(target_pnx).split(".")[0]
            target_zip = rf'$zip_{target_basename}.zip'
            target_yyyy_mm_dd_HH_MM_SS_zip = rf'{target_basename} - {TimeUtil.get_time_as_("%Y %m %d %H %M %S")}.zip'
            # BusinessLogicUtil.print_as_log(rf'# target_dirname_dirname 로 이동')
            os.chdir(target_dirname_dirname)
            # BusinessLogicUtil.print_as_log(rf'부모디렉토리로 백업')
            cmd = f'bandizip.exe c "{target_zip}" "{target_pnx}"'
            BusinessLogicUtil.command_to_os_like_person_as_admin(cmd)
            # BusinessLogicUtil.print_as_log(rf'이름변경')
            cmd = f'ren "{target_zip}" "$deleted_{target_yyyy_mm_dd_HH_MM_SS_zip}"'
            BusinessLogicUtil.command_to_os_like_person_as_admin(cmd)
            # BusinessLogicUtil.print_as_log(rf'부모디렉토리에서 백업될 디렉토리로 이동')
            cmd = f'move "$deleted_{target_yyyy_mm_dd_HH_MM_SS_zip}" "{target_dirname}"'
            BusinessLogicUtil.command_to_os_like_person_as_admin(cmd)
            # BusinessLogicUtil.print_as_log(rf'백업될 디렉토리로 이동')
            os.chdir(target_dirname)
            # BusinessLogicUtil.print_as_log("os.getcwd()")
            # BusinessLogicUtil.print_as_log(os.getcwd())
            # BusinessLogicUtil.print_as_log("원본파일삭제")
            os.remove(target_pnx)
        except:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
        finally:
            BusinessLogicUtil.print_with_underline(rf'프로젝트 디렉토리로 이동')
            os.chdir(starting_directory)

    @staticmethod
    def convert_img_to_img_blurred(img_pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        img_converted = Image.open(img_pnx).filter(ImageFilter.GaussianBlur(10))  # 가우시안 블러 적용 # 숫자크면 많이흐려짐
        img_converted.show()

    @staticmethod
    def convert_img_to_img_grey(img_pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        img_converted = Image.open(img_pnx).convert("L")
        img_converted.show()

    @staticmethod
    def convert_img_to_img_resized(img_pnx, width_px, height_px):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        img_converted = Image.open(img_pnx).resize((width_px, height_px))
        img_converted.show()

    @staticmethod
    def convert_img_to_img_cropped(img_pnx, abs_x: int, abs_y: int, width_px: int, height_px: int):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        img_converted = Image.open(img_pnx).crop((abs_x, abs_y, width_px, height_px))
        img_converted.show()

    @staticmethod
    def convert_img_to_img_rotated(img_pnx, degree: int):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        img_converted = Image.open(img_pnx).rotate(degree)
        img_converted.show()
        img_converted.save(f"{os.path.dirname(img_pnx)}   {os.path.splitext(img_pnx)[0]}_$flipped_h{os.path.splitext(img_pnx)[1]}")

    @staticmethod
    def convert_img_to_img_flipped_horizontally(img_pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        img_converted = Image.open(img_pnx).transpose(Image.FLIP_LEFT_RIGHT)
        img_converted.show()
        img_converted.save(f"{os.path.dirname(img_pnx)}   {os.path.splitext(img_pnx)[0]}_$flipped_h{os.path.splitext(img_pnx)[1]}")

    @staticmethod
    def convert_img_to_img_flipped_vertical(img_pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        img_converted = Image.open(img_pnx).transpose(Image.FLIP_TOP_BOTTOM)
        img_converted.show()
        img_converted.save(f"{os.path.dirname(img_pnx)}   {os.path.splitext(img_pnx)[0]}_$flipped_v{os.path.splitext(img_pnx)[1]}")

    @staticmethod
    def convert_img_to_img_watermarked(img_pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        from PIL import Image, ImageDraw, ImageFont

        # step2.워터마크 삽입할 이미지 불러오기
        img = Image.open('cat.jpg')
        width, height = img.size

        # step3.그림판에 이미지를 그대로 붙여넣는 느낌의 Draw() 함수
        draw = ImageDraw.Draw(img)

        # step4.삽입할 워터마크 문자
        text = "봵 워터마크"

        # step5.삽입할 문자의 폰트 설정
        font = ImageFont.truetype('/Users/sangwoo/Downloads/나눔 글꼴/나눔손글씨_펜/NanumPen.ttf', 30)

        # step6.삽입할 문자의 높이, 너비 정보 가져오기
        width_txt, height_txt = draw.textsize(text, font)  # noqa

        # step7.워터마크 위치 설정
        margin = 10
        x = width - width_txt - margin
        y = height - height_txt - margin

        # step8.텍스트 적용하기
        draw.text((x, y), text, fill='white', font=font)

        # step9.이미지 출력
        img.show()

        # step10.현재작업 경로에 완성 이미지 저장
        img.save("cat_watermakr.jpg")  # 절대경로 되는지 확인해보자.

    @staticmethod
    def kill_thread(thread_name):
        # 종료할 스레드 이름

        # 현재 실행 중인 모든 스레드 가져오기
        current_threads = threading.enumerate()

        # 종료할 스레드 찾기
        target_thread = None
        for thread in current_threads:
            if thread.name == thread_name:
                target_thread = thread
                break

        # 스레드 종료
        if target_thread:
            target_thread.join()
            print(f"{thread_name} 스레드가 종료되었습니다.")
        else:
            print(f"{thread_name} 스레드를 찾을 수 없습니다.")

    @staticmethod
    def is_file_changed(file_pnx):
        # 조건문을 반복 작성해서 기능을 분리할 수가 있었다.
        # 여기서 알게된 사실은 조건문의 구조를 반복해서 특정 기능들의 로직들을 분리할 수 있었다.
        key = DbTomlUtil.get_db_toml_key(file_pnx)

        # 기존에 측정된 파일의 줄 수 : 없으면 새로 측정된 파일의 줄 수로 대신함.
        line_cnt_from_db = DbTomlUtil.select_db_toml(key=key)
        if line_cnt_from_db is None:
            DbTomlUtil.insert_db_toml(key=key, value=BusinessLogicUtil.get_line_cnt_of_file(file_pnx))  # 50000 줄의 str 다루는 것보다 50000 개의 list 다루는 것이 속도성능에 대하여 효율적이다.
            line_cnt_from_db = DbTomlUtil.select_db_toml(key=key)
        BusinessLogicUtil.print_cyan(f"line_cnt_from_db : {line_cnt_from_db}")

        # 새로 측정된 파일의 줄 수
        line_cnt_measured = BusinessLogicUtil.get_line_cnt_of_file(file_pnx)
        BusinessLogicUtil.print_cyan(f"line_cnt_measured : {line_cnt_measured}")

        # 로직분리 새로운 시도: 기능에 따라 조건문을 여러개 만들어 보았다.
        # print_as_log() 관련된 로직 분리
        if BusinessLogicUtil.is_file_edited(file_pnx) is None:
            BusinessLogicUtil.print_with_underline("데이터베이스 타겟에 대한 key가 없어 key를 생성합니다")
        elif BusinessLogicUtil.is_file_edited(file_pnx):
            ment = f'모니터링 중 편집을 감지하였습니다.\n{os.path.basename(file_pnx)}\n 타겟백업을 시도합니다.\n 타겟에 대한 key를 toml 데이터베이스에 업데이트합니다.'
            UiUtil.pop_up_as_complete(title_="모니터링감지보고", ment=ment, auto_click_positive_btn_after_seconds=3)

        # db crud 관련된 로직 분리
        if BusinessLogicUtil.is_file_edited(file_pnx):
            DbTomlUtil.update_db_toml(key=key, value=BusinessLogicUtil.get_line_cnt_of_file(file_pnx))
        elif BusinessLogicUtil.is_file_edited(file_pnx) is None:
            DbTomlUtil.insert_db_toml(key=key, value=BusinessLogicUtil.get_line_cnt_of_file(file_pnx))
        if BusinessLogicUtil.is_file_edited(file_pnx):
            return True

    @staticmethod
    def sync_directory_remote(target_pnx):
        """이게 뭐냐면 외부망에 있는 디렉토리를 동기화 할 수 있다. 리눅스 rsync 에 의존하는 기술"""
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.speak(MentsUtil.NOT_PREPARED_YET)
        pass

    @staticmethod
    def sync_directory_local(target_pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            import os

            from dirsync import sync

            target_pnx = target_pnx
            target_pnx_new = rf"{target_pnx}_sync"
            BusinessLogicUtil.print_cyan(rf'target_pnx_new : {target_pnx_new}')

            # 기존 작업 폴더가 없는 경우
            if not os.path.exists(target_pnx_new):
                shutil.copytree(target_pnx, target_pnx_new)
            else:
                # BusinessLogicUtil.remove_target_parmanently(StateManagementUtil.DIRSYNC_LOG)
                # # 로깅 설정 및 BusinessLogicUtil.DIRSYNC_LOG 생성
                # import logging
                # logging.basicConfig(filename=StateManagementUtil.DIRSYNC_LOG, level=logging.DEBUG, filemode='w', encoding='utf-8')
                # dirsync_logger = logging.getLogger('dirsync')

                # result_sync = sync(sourcedir=target_pnx, targetdir=target_pnx_new, action='sync', verbose=True, logger=dirsync_logger) #success
                # result_sync = sync(sourcedir=target_pnx, targetdir=target_pnx_new, action="sync", options=["--purge", "--verbose", "--force"], logger=dirsync_logger)
                result_sync = sync(sourcedir=target_pnx, targetdir=target_pnx_new, action="sync", options=["--purge", "--verbose", "--force"])
                # sync(sourcedir=target_pnx_new, targetdir=target_pnx , action='sync',verbose=True , logger = dirsync_logger)  # 양방향 으로 로컬동기화폴더를 만드려면 sync() 코드를 추가하여 sync() 함수가 총 2개가 targetdir 간에 sourcedir 서로 자리바뀌어 있도록 작성
                # if result_sync:
                #     # BusinessLogicUtil.DIRSYNC_LOG 내용 가져오기
                #     if os.path.exists(StateManagementUtil.DIRSYNC_LOG):
                #         lines = BusinessLogicUtil.get_lines_of_file(StateManagementUtil.DIRSYNC_LOG)[-4:-1]
                #         lines = [sample.strip() for sample in lines]
                #         for sample in lines:
                #             # print(BusinessLogicUtil.translate_eng_to_kor_via_googletrans(sample))
                #             BusinessLogicUtil.print_ment_light_white(rf'sample : {sample}')
                #         BusinessLogicUtil.print_ment_light_white(rf'len(lines) : {len(lines)}')
                #         BusinessLogicUtil.remove_target_parmanently(StateManagementUtil.DIRSYNC_LOG)
                #         lines = [x for x in lines if x.strip("\n")]  # 리스트 요소 "" 제거,  from ["", A] to [A]       [""] to []
                #         # BusinessLogicUtil.speak_ments(f"타겟의 동기화가 성공 되었습니다", sleep_after_play=0.65, thread_join_mode=True)
                #         BusinessLogicUtil.print_ment_success("타겟동기화 성공")
                #         UiUtil.pop_up_as_complete(title_="작업성공보고", ment=f"타겟의 동기화가 성공 되었습니다\n{target_pnx_new}", auto_click_positive_btn_after_seconds=1)
                BusinessLogicUtil.print_success("타겟동기화 성공")
        except:
            BusinessLogicUtil.print_red("타겟동기화 실패")
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

        # from dirsync import sync
        # sources = [r'C:\Users\seon\Desktop\오리지널',
        #            r'C:\Users\seon\Desktop\오리지널2',
        #            r'C:\Users\seon\Desktop\오리지널3']
        # pnxs = [r'C:\Users\seon\Desktop\테스트',
        #            r'C:\Users\seon\Desktop\테스트2',
        #            r'C:\Users\seon\Desktop\테스트3']
        # total = dict(zip(sources, pnxs))
        # for source, target in total.items():
        #     sync(sourcedir=source, targetdir=target, action='sync', verbose=True, purge=True, create=True,  delete=True, update=True)  # 이것이 sync() default 파라미터들이다.
        #     sync(sourcedir=source, targetdir=target, action='sync', verbose=True, purge=True, create=True,  delete=True, update=True)  # purge=True 이면 targetdir 에 이물질 같은 파일이 있으면 삭제를 합니다, delete=False 이면 어떻게 되는거지? # verbose = True 이면 상세설명출력

        # 윈도우 디렉토리 경로를 WSL 경로로 변환
        # try:
        #     server_time = BusinessLogicUtil.get_time_as_('%Y_%m_%d_%H_%M_%S_%f')
        #     target_pnx = rf"/mnt/c/{target_pnx}" \ 에서 / 로 바꿔야한다
        #     # target_pnx_new = rf"/mnt/c/{target_pnx}_{server_time}"
        #     target_pnx_new = rf"/mnt/c/{target_pnx}_sync"
        #     command = f"rsync -avz {target_pnx} {target_pnx_new}"
        #     print(command)
        #     subprocess.call(command, shell=True)
        # except:
        #     pass

    @staticmethod
    def get_list_from_f_txt(pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            if os.path.exists(pnx):
                # with open(file_abspath, 'r', encoding="utf-8") as f:
                # with open(file_abspath, 'r', errors='ignore') as f:
                with open(pnx, 'r', encoding="utf-8", errors='ignore') as f:
                    lines = f.readlines()  # from file.ext to ["한줄","한줄","한줄"]
                    # mkr_파일 내용을 디스크에 강제로 기록
                    # os.fsync(f.fileno())
                    return lines
        except:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def remove_pnx_parmanently(pnx):
        """
        정말 로직적으로 삭제해도 상관 없는 경우가 아니면 이 함수는 쓰지 말것
        이 메소드를 사용하는 것은 데이터소실과 관계된 위험한 일이다.
        윈도우의 경우, move_target_to_trash_bin() 로 내부를 만일을 위해서 주석처리 후, 변경하였음.
        """
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        if platform.system() == 'Windows':
            try:
                if BusinessLogicUtil.validate_and_return(value=pnx) is not False:
                    os.chdir(os.path.dirname(pnx))
                    if os.path.exists(pnx):
                        if os.path.isdir(pnx):
                            # shutil.rmtree(target_pnx)
                            # if os.path.isdir(target_pnx):
                            #     BusinessLogicUtil.run_via_cmd_exe(rf'echo y | rmdir /s "{target_pnx}"')
                            BusinessLogicUtil.move_pnx_to_trash_bin(pnx)
                        elif os.path.isfile(pnx):
                            # os.remove(target_pnx)
                            # if os.path.isfile(target_pnx):
                            #     BusinessLogicUtil.run_via_cmd_exe(rf'echo y | del /f "{target_pnx}"')
                            BusinessLogicUtil.move_pnx_to_trash_bin(pnx)

                        # BusinessLogicUtil.print_cyan(f"%%%FOO%%% green {texts}", )
                        # BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
            except:
                BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

            finally:
                os.chdir(StateManagementUtil.PROJECT_DIRECTORY)
        else:
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            try:
                if BusinessLogicUtil.validate_and_return(value=pnx) is not False:
                    os.chdir(os.path.dirname(pnx))
                    if os.path.exists(pnx):
                        if os.path.isdir(pnx):
                            shutil.rmtree(pnx)
                            if os.path.isdir(pnx):
                                # BusinessLogicUtil.run_via_cmd_exe(rf'리눅스로 코드 수정대기 | rmdir /s "{target_pnx}"')
                                pass
                        elif os.path.isfile(pnx):
                            os.remove(pnx)
                            if os.path.isfile(pnx):
                                # BusinessLogicUtil.run_via_cmd_exe(rf'리눅스로 코드 수정대기 echo y | del /f "{target_pnx}"')
                                pass

            except:
                BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

            finally:
                os.chdir(StateManagementUtil.PROJECT_DIRECTORY)

    @staticmethod
    def is_directory_changed(directory_pnx):
        # 현재 디렉토리 상태
        current_directory_state = None
        previous_directory_state = None
        try:
            current_directory_state = BusinessLogicUtil.get_list_pnxs_with_mtime_without_files_to_exclude(directory_pnx=directory_pnx)  # from str to [["abspath", "mtime"]]
            current_directory_state = sorted(current_directory_state, key=lambda item: item[1],
                                             reverse=True)  # from [["abspath", "mtime"]] to [["abspath", "mtime"]] (딕셔너리를 value(mtime)를 기준으로 내림차순으로 정렬), 날짜를 제일 현재와 가까운 날짜를 선택하는 것은 날짜의 숫자가 큰 숫자에 가깝다는 이야기이다. 그러므로  큰 수부터 작은 수의 순서로 가는 내림차순으로 정렬을 해주었다(reverse=True).
            current_directory_state = DataStructureUtil.get_list_seperated_by_each_elements_in_nested_list(current_directory_state)  # from [["a","b"], ["c","d"]] to ["a", "b", "c", "d"]
            current_directory_state = DataStructureUtil.get_list_each_two_elements_joined(current_directory_state)  # from ["a", "b", "c", "d"] to ["ab", "cd"]
            current_directory_state = BusinessLogicUtil.get_list_replaced_from_list_that_have_special_characters(target=current_directory_state, replacement="")  # from [] to [] (특수문자 제거 시킨) # 이부분을 암호화 시키면 어떨까 싶은데 #딕셔너리에 있는부분을 replace
            [print(item) for item in current_directory_state[0:10]]
            print(rf'type(current_directory_state) : {type(current_directory_state)}')
            print(rf'len(current_directory_state) : {len(current_directory_state)}')
        # 이전 디렉토리 상태
        except:
            pass
        try:
            previous_directory_state = DbTomlUtil.select_db_toml(key=DbTomlUtil.get_db_toml_key(directory_pnx))
            if previous_directory_state is None:
                DbTomlUtil.insert_db_toml(key=DbTomlUtil.get_db_toml_key(directory_pnx), value=current_directory_state)  # 50000 줄의 str 다루는 것보다 50000 개의 list 다루는 것이 속도성능에 대하여 효율적이다. # DB에 [] 로 저장
                previous_directory_state = DbTomlUtil.select_db_toml(key=DbTomlUtil.get_db_toml_key(directory_pnx))
            [print(item) for item in previous_directory_state[0:10]]
            print(rf'type(previous_directory_state) : {type(previous_directory_state)}')
            print(rf'len(previous_directory_state) : {len(previous_directory_state)}')
        except:
            pass

        # 변화 감지 ( 러프, 빠름)
        # 두 디렉토리 상태 합쳐서 중복제거 해서 디렉토리 처음 상태의 절반이 나오면 중복이 없다는 생각.
        # 위의 생각은 맞는데 실제로 내가 숫자를 잘 못 파악했다.
        # set() 함수는 중복을 제거한 나머지를 리스트에 저장하는 함수이다.
        # 따라서 a != b 인 경우,  a == b 인 경우, 중복이 없는것
        # str을 줄단위로 쪼개 [str]로 리스트를 합한다.
        # try:
        #     merged_list = current_directory_state + previous_directory_state  # from [1, 2, 3] + [ x, y, z] to [1, x, 2, y, 3, z]
        #     [print(item) for item in merged_list[0:10]]
        #     print(rf'type(merged_list) : {type(merged_list)}')
        #     print(rf'len(merged_list) : {len(merged_list)}')
        #     a = len(merged_list)/2
        #     b = len(list(set(merged_list)))
        #     print(rf'a : {a}  b : {b} ')
        #     # duplicates = list(set([x for x in merged_list if merged_list.count(x) == 1])) # 중복되는 것만 추출 # 너무 느림 # 추가된파일, 삭제된 파일
        #     # print(rf'a : {a}  b : {b}   duplicates : {duplicates}')
        # except:
        #     pass
        # try:
        #     merged_list = Park4139List.get_list_added_elements_alternatively(current_directory_state, previous_directory_state)  # from [1, 2, 3] + [ x, y, z] to [1, x, 2, y, 3, z]
        #     [print(item) for item in merged_list[0:10]]
        #     print(rf'type(merged_list) : {type(merged_list)}')
        #     print(rf'len(merged_list) : {len(merged_list)}')
        #     a = len(merged_list) / 2
        #     b = len(list(set(merged_list)))
        #     print(rf'a : {a}  b : {b} ')
        #     print(rf'a : {a}  b : {b}   duplicates : {duplicates}')
        # finally:
        #     pass

        # 변화 감지 ( 디테일, 느림)
        # try:
        #     added_files = BusinessLogicUtil.get_added_files(previous_directory_state, current_directory_state)
        #     if added_files:
        #         print(f"추가된 파일 개수: {len(added_files)} 추가된 파일: {added_files}")
        #     deleted_files = BusinessLogicUtil.get_deleted_files(previous_directory_state, current_directory_state)
        #     if deleted_files:
        #         print(f"삭제된 파일 개수: {len(deleted_files)} 삭제된 파일: {deleted_files}")
        #     modified_files = BusinessLogicUtil.get_modified_files(previous_directory_state, current_directory_state)
        #     if modified_files:
        #         print(f"변경된 파일 개수: {len(modified_files)} 변경된 파일: {modified_files}")
        # except:
        #     pass

        # 변화 감지 ( 러프, 덜 느림)
        try:
            if DataStructureUtil.is_two_lists_equal(list1=current_directory_state, list2=previous_directory_state):
                print("디렉토리가 변경되지 않았습니다")
                return False
            else:
                print("디렉토리 변경이 감지되었습니다")
                DbTomlUtil.update_db_toml(key=DbTomlUtil.get_db_toml_key(directory_pnx), value=current_directory_state)
                return True
        except:
            pass

    @staticmethod
    def get_list_pnxs_with_mtime_without_files_to_exclude(directory_pnx):
        files_to_exclude = [
            StateManagementUtil.DB_YAML,
            StateManagementUtil.SUCCESS_LOG,
            StateManagementUtil.LOCAL_PKG_CACHE_FILE,
        ]
        files_of_directory = []
        for root, dirs, files in os.walk(directory_pnx):
            for file in files:
                if not file.endswith(".mp3"):  # 모든 mp3 파일을 배제합니다
                    file_path = os.path.join(root, file)
                    if file_path not in files_to_exclude:
                        # files_of_directory[rf"{file_path}"] = os.path.getmtime(file_path)
                        files_of_directory.append([file_path, os.path.getmtime(file_path)])
        return files_of_directory

    @staticmethod
    def get_added_files(previous_state, current_state):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        return DataStructureUtil.get_elements_that_list1_only_have(list1=current_state, list2=previous_state)

    @staticmethod
    def get_deleted_files(previous_state, current_state):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        return DataStructureUtil.get_elements_that_list1_only_have(list1=previous_state, list2=current_state)

    @staticmethod
    def get_modified_files(previous_state, current_state):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        return DataStructureUtil.get_different_elements(list1=current_state, list2=previous_state)

    @staticmethod
    def make_pnx(pnx, mode):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.print_as_log(string=rf'''leaf_pnx="{pnx}" %%%FOO%%%''')
        BusinessLogicUtil.print_as_log(string=rf'''mode="{mode}" %%%FOO%%%''')
        if mode == "f":
            if not os.path.exists(pnx):
                try:
                    os.makedirs(os.path.dirname(pnx))
                except:
                    BusinessLogicUtil.print_as_log(string=rf'''return %%%FOO%%%''')
                    pass
                BusinessLogicUtil.command_to_os_like_person_as_admin(rf'chcp 65001 >nul')
                BusinessLogicUtil.command_to_os_like_person_as_admin(rf'echo. > "{pnx}"')
        elif mode == "d":
            if not os.path.exists(pnx):
                os.makedirs(pnx)
        else:
            BusinessLogicUtil.print_as_log(string=rf'''return %%%FOO%%%''')
            return

    @staticmethod
    def is_empty_directory(directory_pnx, show_mode):
        function_name = inspect.currentframe().f_code.co_name
        if show_mode == True:
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        try:
            if len(os.listdir(directory_pnx)) == 0:
                return True
            else:
                return False
        except FileNotFoundError:
            if show_mode == True:
                BusinessLogicUtil.print_ment_via_colorama(ment="FileNotFoundError", colorama_color=ColoramaUtil.RED)
            pass

    @staticmethod
    def pnx_rename(src, pnx_new):
        # 이름을 변경하는 경우에 재귀적으로 바뀌어야 하는 것으로 생각되어 os.renames 를 테스트 후 적용하였다.
        # os.rename 사용 중에 directory  인 경우는 재귀적으로 변경이 안된다
        try:
            if not BusinessLogicUtil.does_pnx_exist(src=src):
                BusinessLogicUtil.print_as_log(f'''"rename 할 파일이 없습니다 {src}''', print_color='red')
                return
            if src == pnx_new:
                BusinessLogicUtil.print_as_log(f'''"현재파일명 과 바꾸려는파일명 이 같아 처리하지 않았습니다 "''', print_color='red')
                return
            if BusinessLogicUtil.does_pnx_exist(src=pnx_new):
                BusinessLogicUtil.print_as_log(f'''"dst에 중복된 파일이 있습니다. {pnx_new}"''', print_color='red')
                return

            if BusinessLogicUtil.is_file(src):
                type = "파일명"
            else:
                type = "디렉토리명"

            os.renames(src, pnx_new)
            BusinessLogicUtil.print_as_log(f'''"{src}" 를 "{pnx_new}"로 {type}을 rename 하였습니다''', print_color='blue')
        except:
            BusinessLogicUtil.print_as_log(f'''"{src}" 와 "{pnx_new}"를 rename이 되었는지 확인이 필요합니다''', print_color='red')
            BusinessLogicUtil.print_as_log(string=rf'''traceback.format_exc()="{traceback.format_exc()}" %%%FOO%%%''')

    @staticmethod
    def merge_directories(directory_pnxs: List[str]):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        target_pnx = BusinessLogicUtil.get_pnx(pnx=os.path.dirname(directory_pnxs[0]))

        # 파일명들을 나열한다.
        # 파일을 깊이 별로 나열을 하고 깊이가 깊은 것부터 시작해서 깊이가 낮은 것으로 처리해 나간다
        #

        directory_pnxs = [x for x in directory_pnxs if x.strip()]  # 리스트 요소 "" 제거,  from ["", A] to [A]    from [""] to []
        directory_pnxs = [x.strip() for x in directory_pnxs]  # 리스트 각 요소 strip(),  ["   A", "B   "] from ["A", "B"]
        directory_pnxs = [x.strip("\"") for x in directory_pnxs]  # 리스트 각 요소 strip("\""),  [""A""] from ["A"]
        directory_pnxs = [x.strip("\'") for x in directory_pnxs]  # 리스트 각 요소 strip("\'),  ["'A'""] from ["A"]

        BusinessLogicUtil.print_list_as_vertical(items_list=directory_pnxs, items_list_name="directory_pnxs_")

        if 0 == len(directory_pnxs):
            BusinessLogicUtil.speak_ment_experimental("pnx가 아무것도 입력되지 않았습니다", comma_delay=0.98)
            return
        elif 1 == len(directory_pnxs):
            BusinessLogicUtil.speak_ment_experimental("하나의 pnx로는 머지를 시도할수 없습니다, 여러개의 pnx들을 입력해주세요", comma_delay=0.98)
            return
        elif 1 < len(directory_pnxs):
            for index, directory in enumerate(directory_pnxs):
                connected_drives = []
                for drive_letter in string.ascii_uppercase:
                    drive_path = drive_letter + ":\\"
                    if os.path.exists(drive_path):
                        connected_drives.append(drive_path)
                        if directory == drive_path:
                            BusinessLogicUtil.speak_ment_experimental("입력된 pnx는 너무 광범위하여, 진행할 수 없도록 설정되어 있습니다", comma_delay=0.98)
                            break

            # BusinessLogicUtil.make_leaf_directory(StateManagementUtil.EMPTY_DIRECTORYIES)

            # indices_to_remove = []  # 제거할 인덱스를 기록할 리스트
            # for index, directory in enumerate(directoryies_):
            #     if os.path.isdir(directory):
            #         if BusinessLogicUtil.is_empty_directory(directory):
            #             BusinessLogicUtil.move_pnx_without_overwrite(target_pnx=directory, dst=StateManagementUtil.EMPTY_DIRECTORYIES)
            #             indices_to_remove.append(index)
            # for index in indices_to_remove:
            #     directoryies_.pop(index)

            # for index, directory in enumerate(directoryies_):
            #     if directory == "":
            #         BusinessLogicUtil.speak_ments("하나 이상의 pnx가 공백으로 입력되었습니다", sleep_after_play=0.65)
            #         return
            #     if not os.path.exists(directory):
            #         BusinessLogicUtil.speak_ments("하나 이상의 pnx가 존재하지 않습니다", sleep_after_play=0.65)
            #         return

            BusinessLogicUtil.print_with_underline("빈 트리 리프디렉토리별로 해체한 뒤 제거")
            files_to_move = []
            for index, directory in enumerate(directory_pnxs):
                for root, directories, files in os.walk(directory, topdown=True):
                    for file in files:
                        files_to_move.append(rf"{root}\{file}")
            [BusinessLogicUtil.print_light_white(rf'file_to_move : {file_to_move}') for file_to_move in files_to_move]
            BusinessLogicUtil.print_light_white(rf'type(files_to_move) : {type(files_to_move)}')
            BusinessLogicUtil.print_light_white(rf'len(files_to_move) : {len(files_to_move)}')
            dst = rf"{os.path.dirname(directory_pnxs[0])}\{os.path.basename(directory_pnxs[0]).replace("_$merged", "")}_$merged"
            BusinessLogicUtil.print_light_yellow(rf'dst : {dst}')
            BusinessLogicUtil.make_pnx(dst, mode="d")

            for file_to_move in files_to_move:
                BusinessLogicUtil.move_pnx_without_overwrite(src=file_to_move, dst=dst)

            # 이 함수는 캐싱문제를 해결하지 못함.
            def count_files_in_folder(folder_path):
                file_count = 0
                for _, _, files in os.walk(folder_path):
                    file_count += len(files)
                return file_count

            # 이 함수는 캐싱문제를 해결하지 못함.
            # def count_files_in_folder(folder_path):
            #     file_count = 0
            #     with os.scandir(folder_path) as entries:
            #         for entry in entries:
            #             if entry.is_file():
            #                 file_count += 1
            #     return file_count

            # 분명히 파일이 들어있는데 개수가 0개로 나오네  캐싱때문에 그럴 수 있어?
            # 운영체제 성능향상을 위한 폴더정보 캐싱으로 갱신이 안될 수 있음.
            # 폴더를 다른 위치로 이동한 후 다시 이동합니다. 이렇게 하면 파일 시스템이 폴더의 변경을 감지하고 캐시를 갱신할 수 있습니다.
            # current_path = os.getcwd()
            # os.chdir(os.path.dirname(current_path)) # 부모 디렉토리로 이동
            # os.chdir(current_path)

            # 분명히 가 틀렸다. 운영체제의 캐싱이 문제가 아닌, 로직을 잘못 만든 것이었다.
            # directory 변수를 엉뚱하게 초기화하였기 때문이다.
            # directory 를 directory_ 로 별도로 호출해서 해소하였다.

            # empty directory 리프단위로 분해하여 이동
            while True:
                directorys_to_move = []
                for index, directory in enumerate(directory_pnxs):
                    for root, directories, files in os.walk(directory, topdown=False):
                        for directory_ in directories:
                            file_count = count_files_in_folder(rf"{root}\{directory_}")
                            if file_count == 0:
                                directorys_to_move.append(rf"{root}\{directory_}")

                [BusinessLogicUtil.print_light_black(sample) for sample in directorys_to_move]
                BusinessLogicUtil.print_light_black(f'''directorys_to_move = {directorys_to_move}''')
                BusinessLogicUtil.print_light_black(rf'''type(directorys_to_move) = {type(directorys_to_move)}''')
                BusinessLogicUtil.print_light_black(rf'''len(directorys_to_move) = {len(directorys_to_move)}''')

                BusinessLogicUtil.print_light_yellow(rf'dst : {dst}')
                BusinessLogicUtil.make_pnx(dst, mode="d")

                if len(directorys_to_move) == 0:
                    break

                for directory_to_move in directorys_to_move:
                    BusinessLogicUtil.move_pnx_without_overwrite(src=directory_to_move, dst=dst)

            for directory in directory_pnxs:
                BusinessLogicUtil.gather_pnxs_empty(rf"{directory}")

            BusinessLogicUtil.print_success(rf'디렉토리 머지를 완료했습니다')

    @staticmethod
    # THIS IS BAD FUNCTION... I SHOULD CHECK TYPE, WHEN I MADE THIS
    def get_display_info():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # 디스플레이 정보 가져오기  # pyautogui.size?() 로 대체할것.
        global height, width
        from screeninfo import get_monitors
        for infos in get_monitors():
            for info in str(infos).split(','):
                if 'width=' in info.strip():
                    width = info.split('=')[1]
                elif 'height=' in info.strip():
                    height = info.split('=')[1]
        display_setting = {
            'height': int(height),  # ,(comma) 실수로 써놨는데 런타임에러 에서 발견못한 문제... 코드업데이트필요
            'width': int(width)
        }
        return display_setting

    @staticmethod
    def change_os_to_power_saving_mode():  # done
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        command = [r'C:\Windows\System32\rundll32.exe', 'powrprof.dll,SetSuspendState', 'hibernate']
        BusinessLogicUtil.command_run_via_subprocess(command=command)

    @staticmethod
    def play_wav_file(file_pnx):
        # 종료가 되버린다
        # try:
        #     import playsound
        #     playsound.playsound(file_abspath)
        # except:
        #     pass

        # 너무 느리다.
        # try:
        #     import wave
        #     import pyaudio
        #     # WAV 파일 열기
        #     with wave.open(file_abspath, 'rb') as wav:
        #         audio = pyaudio.PyAudio()
        #         # 스트림 열기
        #         stream = audio.open(format=audio.get_format_from_width(wav.getsampwidth()),
        #                             channels=wav.getnchannels(),
        #                             rate=wav.getframerate(),
        #                             output=True)
        #         # 데이터 읽기
        #         data = wav.readframes(1024)
        #
        #         # 재생
        #         while data:
        #             stream.write(data)
        #             data = wav.readframes(1024)
        #
        #         # 스트림 닫기
        #         stream.stop_stream()
        #         stream.close()
        #
        #         # PyAudio 객체 종료
        #         audio.terminate()
        #
        #     # WAV 파일 닫기
        #     # wav.close()
        # except:
        #     pass

        file_pnx = StateManagementUtil.POP_SOUND_POP_SOUND_WAV
        if BusinessLogicUtil.does_pnx_exist(src=file_pnx):
            import pyglet
            source = pyglet.media.load(file_pnx)
            source.play()
        pass

    @staticmethod
    def command_to_os_like_person_as_admin(command, show_mode=True):  # todo need refactorying
        # os.Popen 으로 print 가능하도록 할 수 있다는 것 같았는데 다른 방식으로 일단 되니까. 안되면 시도.
        # cmd = ['dir', '/b']
        # fd_popen = subprocess.Popen(cmd, stdout=subprocess.PIPE).stdout # 명령어 실행 후 반환되는 결과를 파일에 저장합니다.
        # fd_popen = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout # shell=True 옵션, cmd를 string 으로 설정
        # lines = fd_popen.read().strip().split('\n')# lines에 저장합니다.
        # fd_popen.close()# 파일을 닫습니다.
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        if not platform.system() == 'Windows':
            command = command.replace("\\", "/")
        try:
            if platform.system() == 'Windows':
                # lines = subprocess.check_output('chcp 65001 >nul', shell=True).decode('utf-8').split('\n')
                lines = subprocess.check_output(command, shell=True).decode('utf-8').split('\n')
                # lines = subprocess.check_output(command, shell=True).decode('euc-kr').split('\n')
            if show_mode == True:
                BusinessLogicUtil.print_as_log(string=rf'''command="{command}" %%%FOO%%% 1''')
            return lines
        except:
            BusinessLogicUtil.print_as_log(string=rf'''traceback.format_exc()="{traceback.format_exc()}" %%%FOO%%%''')
            # os.system(cmd)
        return None

    @staticmethod
    def run_via_explorer_exe(pnx: str, show_mode=True):  # 이거 # deprecated 시키자.
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        pnx = BusinessLogicUtil.get_pnx_preprocessed(pnx=pnx)
        pnx = rf'explorer "{pnx}"'
        # BusinessLogicUtil.print_cyan(rf'{target_pnx}')
        try:
            subprocess.check_output(pnx, shell=show_mode).decode('utf-8').split('\n')
        except UnicodeDecodeError:
            subprocess.check_output(pnx, shell=show_mode).decode('euc-kr').split('\n')
        except:
            if show_mode == True:
                BusinessLogicUtil.print_light_black(f"#{traceback.format_exc()}")

    @staticmethod
    # 프로그램 PID 출력
    def get_current_program_pid():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        pro = subprocess.check_output(
            rf'powershell (Get-WmiObject Win32_Process -Filter ProcessId=$PID).ParentProcessId', shell=True).decode(
            'utf-8')  # 실험해보니 subprocess.check_output(cmd,shell=True).decode('utf-8') 코드는 프로세스가 알아서 죽는 것 같다. 모르겠는데 " " 가 있어야 동작함
        lines = pro.split('\n')
        pids = []
        for line in lines:
            if "" != line.strip():
                pid = line
                pids.append(pid)
                BusinessLogicUtil.print_cyan(f'pid: {pid}')
        return pids

    @staticmethod
    def get_target_bite(start_path='.'):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)
        return total_size

    @staticmethod
    def get_target_megabite(target_path):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        return BusinessLogicUtil.get_target_bite(target_path.strip()) / 1024 ** 2

    @staticmethod
    def get_target_gigabite(target_path):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        return BusinessLogicUtil.get_target_bite(target_path.strip()) / 1024 ** 3

    @staticmethod
    def move_pnx_to_trash_bin(src):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        # pnx = BusinessLogicUtil.get_pnx_unix_style(pnx  =pnx)
        src = BusinessLogicUtil.get_pnx_windows_style(pnx=src)

        try:
            if BusinessLogicUtil.does_pnx_exist(src):
                send2trash.send2trash(src)
            # if BusinessLogicUtil.does_pnx_exist(pnx):
            #     shutil.move(pnx, r'C:\$Recycle.Bin') # 메타데이터가 함께 삭제 # 복원이 어려움
            BusinessLogicUtil.print_as_log(string=rf'''pnx="{src}" %%%FOO%%%''')
        except:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

        # 휴지통 열기
        # BusinessLogicUtil.run_via_cmd_exe('explorer.exe shell:RecycleBinFolder')

    @staticmethod
    def xcopy_with_overwrite(target_pnx, future_target_pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            result = BusinessLogicUtil.command_to_os_like_person_as_admin(rf'echo a | xcopy "{target_pnx}" "{future_target_pnx}" /e /h /k /y')
            if result == subprocess.CalledProcessError:
                if os.path.isfile(target_pnx):
                    BusinessLogicUtil.command_to_os_like_person_as_admin(rf'echo f | xcopy "{target_pnx}" "{future_target_pnx}" /e /h /k /y')
                else:
                    BusinessLogicUtil.command_to_os_like_person_as_admin(rf'echo d | xcopy "{target_pnx}" "{future_target_pnx}" /e /h /k /y')
        except Exception:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def xcopy_without_overwrite(target_pnx, future_target_pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            if os.path.exists(future_target_pnx):
                future_target_pnx = rf"{os.path.dirname(future_target_pnx)}\{os.path.basename(target_pnx)[0]}_{TimeUtil.get_time_as_('%Y_%m_%d_%H_%M_%S_%f')}{os.path.basename(target_pnx)[1]}"
            BusinessLogicUtil.command_to_os_like_person_as_admin(rf'echo a | xcopy "{target_pnx}" "{future_target_pnx}" /e /h /k')
            if os.path.isfile(target_pnx):
                BusinessLogicUtil.command_to_os_like_person_as_admin(rf'echo f | xcopy "{target_pnx}" "{future_target_pnx}" /e /h /k')
            else:
                BusinessLogicUtil.command_to_os_like_person_as_admin(rf'echo d | xcopy "{target_pnx}" "{future_target_pnx}" /e /h /k')
        except Exception:
            print(rf"subprocess.CalledProcessError 가 발생하여 재시도를 수행합니다 {inspect.currentframe().f_code.co_name}")
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def is_file_edited(target_pnx: str):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            key = DbTomlUtil.get_db_toml_key(target_pnx)
            db = DbTomlUtil.read_db_toml()
            line_cnt_measured = BusinessLogicUtil.get_line_cnt_of_file(target_pnx)
            if line_cnt_measured != db[key]:
                BusinessLogicUtil.print_with_underline("파일편집 감지되었습니다")
            else:
                BusinessLogicUtil.print_with_underline("파일편집 감지되지 않았습니다")
                pass
            if line_cnt_measured != db[key]:
                return True
            else:
                return False
        except KeyError:
            DbTomlUtil.insert_db_toml(key=DbTomlUtil.get_db_toml_key(target_pnx), value=BusinessLogicUtil.get_line_cnt_of_file(target_pnx))
            BusinessLogicUtil.print_with_underline("파일편집 확인 중 key 에러가 발생하였습니다")
        except Exception:  # except Exception:으로 작성하면 KeyError 를 뺀 나머지 에러처리 설정 , except: 를 작성하면 모든 에러처리 설정
            BusinessLogicUtil.print_with_underline("데이터베이스 확인 중 예상되지 않은 에러가 감지되었습니다")
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def move_pnx_without_overwrite(src, dst, debug_mode=False):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            # define
            pnx_p = os.path.dirname(src)
            spaceless_time_pattern = rf"{BusinessLogicUtil.get_time_as_('now')}"
            pnx_n = BusinessLogicUtil.get_n(src)
            pnx_x = BusinessLogicUtil.get_x(src)
            pnx_with_timestamp = rf'{pnx_p}\{re.sub(pattern=r'\d{4}_\d{2}_\d{2}_(월|화|수|목|금|토|일)_\d{2}_\d{2}_\d{2}_\d{3}', repl='', string=pnx_n)}_{spaceless_time_pattern}{random.randint(10, 99)}{pnx_x}'
            src_type = None
            if os.path.isfile(src):
                src_type = '파일'
            elif os.path.isdir(src):
                src_type = '디렉토리'
            dst_n_timestamp_x = rf'{dst}\{BusinessLogicUtil.get_nx(pnx_with_timestamp)}'

            # logging
            if debug_mode == True:
                BusinessLogicUtil.print_as_log(string=rf'''src_type="{src_type}" %%%FOO%%%''')
                BusinessLogicUtil.print_as_log(string=rf'''spaceless_time_pattern="{spaceless_time_pattern}" %%%FOO%%%''')
                BusinessLogicUtil.print_as_log(string=rf'''pnx_p="{pnx_p}" %%%FOO%%%''')
                BusinessLogicUtil.print_as_log(string=rf'''pnx_n="{pnx_n}" %%%FOO%%%''')
                BusinessLogicUtil.print_as_log(string=rf'''pnx_x="{pnx_x}" %%%FOO%%%''')
                BusinessLogicUtil.print_as_log(string=rf'''pnx_with_timestamp="{pnx_with_timestamp}" %%%FOO%%%''')
                BusinessLogicUtil.print_as_log(string=rf'''dst != os.path.dirname(pnx_with_timestamp)="{dst != os.path.dirname(pnx_with_timestamp)}" %%%FOO%%%''')
                BusinessLogicUtil.print_as_log(string=rf'''dst_n_timestamp_x="{dst_n_timestamp_x}" %%%FOO%%%''')

            if dst != os.path.dirname(pnx_with_timestamp):
                os.rename(src, pnx_with_timestamp)
                shutil.move(src=pnx_with_timestamp, dst=dst)
                BusinessLogicUtil.print_as_log(string=rf'''pnx_with_timestamp="{pnx_with_timestamp}" %%%FOO%%%''')
                BusinessLogicUtil.print_as_log(string=rf'''dst="{dst}" %%%FOO%%%''')
        except:
            BusinessLogicUtil.print_red(f"[Fail] {function_name}() {src_type} \n {traceback.format_exc()}")

    @staticmethod
    def move_without_overwrite_via_robocopy(src, dst):  # 명령어 자체가 안되는데 /mir 은 되는데 /move 안된다
        src = src
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            BusinessLogicUtil.print_with_underline(f'타겟이동 시도')
            # BusinessLogicUtil.run_via_cmd_exe(rf'robocopy "{target_pnx}" "{dst}" /MOVE')
            if os.path.exists(rf'{dst}\{os.path.dirname(src)}'):
                BusinessLogicUtil.move_pnx_to_trash_bin(src)

        except Exception:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def is_empty_tree(directory_path, show_mode):
        '''디렉토리의 내부를 순회하며 돌면서 모든 하위 디렉토리에 파일이 하나도 없는지를 판단합니다'''
        function_name = inspect.currentframe().f_code.co_name
        if show_mode == True:
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            # 디렉토리 내부의 파일과 하위 디렉토리 목록을 가져옵니다.
            contents = os.listdir(directory_path)
            # 파일이 존재하는 경우,
            for content in contents:
                # [print(rf'content : {content}') for content in contents]
                content_path = os.path.join(directory_path, content)
                if os.path.isfile(content_path):
                    if show_mode == True:
                        BusinessLogicUtil.print_light_black("빈 트리 디렉토리 아닙니다")
                    return False
            if show_mode == True:
                BusinessLogicUtil.print_light_black("빈 트리 디렉토리 있니다.")
            return True
        except FileNotFoundError:
            if show_mode == True:
                BusinessLogicUtil.print_red('FileNotFoundError')
        except OSError:
            if show_mode == True:
                BusinessLogicUtil.print_red('OSError')
        except UnboundLocalError:
            if show_mode == True:
                BusinessLogicUtil.print_red('UnboundLocalError')

    @staticmethod
    def is_leaf_directory(directory_path, show_mode=True):
        function_name = inspect.currentframe().f_code.co_name
        if show_mode == True:
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # leaf 디렉토리란, 하위 디렉토리를 소유하지 않는 말단의 디렉토리를 말합니다

        # 디렉토리 내부의 파일과 하위 디렉토리 목록을 가져옵니다.
        try:
            contents = os.listdir(directory_path)

            # 디렉토리 내에 파일이 존재하면 leaf 디렉토리가 아닙니다.
            if len(contents) > 0:
                return False

            # 디렉토리 내에 하위 디렉토리가 존재하는지 확인합니다.
            for content in contents:
                content_path = os.path.join(directory_path, content)
                if os.path.isdir(content_path):
                    return False

            # 디렉토리가 leaf 디렉토리입니다.
            return True
        except FileNotFoundError:
            if show_mode == True:
                BusinessLogicUtil.print_red(string='FileNotFoundError')
        except:
            BusinessLogicUtil.print_red(string=f'{inspect.currentframe().f_code.co_name}() 기타에러발생')

    @staticmethod
    def write_str_to_file(txt_str, pnx, mode="a", encoding='utf-8', show_mode=True):
        function_name = inspect.currentframe().f_code.co_name
        if show_mode == True:
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        with open(file=pnx, mode=mode, encoding=encoding) as file:
            file.write(txt_str)
        # BusinessLogicUtil.print_as_log(f'''{text[:23]}... {pnx} ''')
        # text =text.replace("\n", "")
        # BusinessLogicUtil.print_as_log(string=rf'''text="{text}" %%%FOO%%%''')
        # BusinessLogicUtil.print_as_log(string=rf'''pnx="{pnx}" %%%FOO%%%''')

    @staticmethod
    def write_list_to_f_txt(texts, pnx, mode="a", encoding='utf-8'):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        with open(file=pnx, mode=mode, encoding=encoding) as file:
            for text in texts:
                file.write(text + "\n")
        # BusinessLogicUtil.print_as_log(f'''{texts[0][:23]}... {pnx} ''')

    @staticmethod
    def get_cnts_of_line_of_file(file_abspath):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        with open(file_abspath, mode='r') as file:
            return sum(1 for line in file)

    @staticmethod
    def is_letters_cnt_zero(pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            with open(pnx, mode='r') as file:
                contents = file.read().strip()
                # print(rf'len(contents) : {len(contents)}')
                if len(contents) == 0:
                    return True
        except FileNotFoundError:
            print("파일을 찾을 수 없습니다.")
            return False
        except UnicodeDecodeError:
            with open(pnx, 'r', encoding='utf-8') as file:
                contents = file.read().strip()
                # print(rf'len(contents) : {len(contents)}')
                if len(contents) == 0:
                    return True
            return False
        except:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
            print("오류가 발생했습니다.")
            return False

    @staticmethod
    def is_os_windows():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # BusinessLogicUtil.print_ment_red(rf'''INFO:{StateManagementUtil.INDENTATION_PROMISED}윈도우 기반 리눅스 개발 모드를 실행시도''')
        # return False

        if platform.system() == 'Windows':
            return True
        else:
            return False

    @staticmethod
    def get_os():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        if platform.system() == 'Windows':
            return 'Windows'.lower()
        elif platform.system() == 'Linux':
            return 'Linux'.lower()
        else:
            return 'Unknown'.lower()

    @staticmethod
    def truncate_tree(directory_pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        if os.path.exists(directory_pnx):
            shutil.rmtree(directory_pnx)
        if not os.path.exists(directory_pnx):
            BusinessLogicUtil.make_pnx(directory_pnx, mode="d")

    @staticmethod
    def get_count_none_of_list(list):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # count = sum(element is None for element in list)
        Nones = list
        None_count = Nones.count(None)
        return None_count

    @staticmethod
    def get_validated(target: any):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        if target is None:
            target = "논값"
        if target == "":
            target = "공백"
        if type(target) == str:
            if BusinessLogicUtil.is_pattern_in_string(string=target, pattern=r'[^a-zA-Z0-9가-힣\s]', with_case_ignored=False):  # 특수문자 패턴 정의( 알파벳, 숫자, 한글, 공백을 제외한 모든 문자)
                target = BusinessLogicUtil.get_str_replaced_special_characters(target, "$특수문자$")
            return target
        else:
            return target

    @staticmethod
    def is_validated(target: any):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        if target is None:
            return False
        if target == "":
            return False
        if BusinessLogicUtil.is_pattern_in_string(string=target, pattern=r'[^a-zA-Z0-9가-힣\s]', with_case_ignored=False):  # 특수문자 패턴 정의( 알파벳, 숫자, 한글, 공백을 제외한 모든 문자)
            return False
        else:
            return True

    @staticmethod
    # def guide_user_input_intended_by_developer(user_input: str):
    def is_user_input_required(user_input: str):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # 수정 필요.
        user_input = user_input.strip()
        BusinessLogicUtil.print_as_log(string = rf'''user_input="{user_input}" %%%FOO%%%''')
        if BusinessLogicUtil.is_only_no(user_input):
            user_input = int(user_input)
        else:
            BusinessLogicUtil.speak_ment_experimental("you can input only number, please input only number again", comma_delay=0.98)
            return None
        return user_input

    @staticmethod
    def validate_and_return(value: str):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            BusinessLogicUtil.print_light_black(rf'[벨리데이션 테스트 결과] [value = {value}] [type(value) = {type(value)}] [len(value) = {len(value)}]')
        except:
            pass
        if value is None:
            BusinessLogicUtil.print_light_black(rf'[벨리데이션 테스트 결과] [value = None]')
            return False
        if value == "":
            BusinessLogicUtil.print_light_black(rf'[벨리데이션 테스트 결과] [value = 공백]')
            return False
        # if 전화번호만 같아 보이는지
        # if 특수문자만 같아 보이는지
        return value

    @staticmethod
    def get_age_biological(birth_day):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # 2023-1994=29(생일후)
        # 2024-1994=30(생일후)
        # 만나이 == 생물학적나이
        # 생일 전 만나이
        # 생일 후 만나이
        pass

    @staticmethod
    def get_age_korean(birth_day):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # 2023-1994=29(생일후)
        # 2024-1994=30(생일후)
        # 만나이 == 생물학적나이
        # 생일 전 만나이
        # 생일 후 만나이
        pass

    @staticmethod
    def should_i_download_youtube_as_webm_alt():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        previous_text = ""
        while True:
            input_box_text_default = clipboard.paste()
            # input_box_text_default = "https://www.youtube.com/shorts/oM6c4Zkej7Y"
            # input_box_text_default = ""
            dialog = UiUtil.CustomQdialog(string="다운로드하고 싶은 URL을 입력해주세요", btns=["입력", "입력하지 않기"], input_box_mode=True, input_box_text_default=input_box_text_default)
            dialog.exec()
            btn_text_clicked = dialog.btn_text_clicked
            BusinessLogicUtil.print_cyan(btn_text_clicked)
            if btn_text_clicked == "입력":
                url = dialog.input_box.text()
                BusinessLogicUtil.download_from_youtube_to_webm_alt(url)
            else:
                break

    @staticmethod
    def should_i_shutdown_this_computer():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            dialog = UiUtil.CustomQdialog(string="시스템을 종료할까요?", btns=["종료", "종료하지 않기"])
            dialog.exec()
            btn_text_clicked = dialog.btn_text_clicked
            BusinessLogicUtil.print_cyan(btn_text_clicked)
            if btn_text_clicked == "종료":
                BusinessLogicUtil.shutdown_this_computer()
            else:
                break

    @staticmethod
    def should_i_back_up_target():  # please_type_abspath_to_back_up
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        loop_cnt = 0
        while True:
            if loop_cnt == 0:
                previous_input = StateManagementUtil.PROJECT_PARENTS_DIRECTORY
            else:
                previous_input = clipboard.paste()
            previous_input = previous_input.strip()
            dialog = UiUtil.CustomQdialog(string="백업할 pnx를 입력하세요", btns=["입력", "입력하지 않기"], input_box_mode=True, input_box_text_default=previous_input)
            dialog.exec()
            btn_text_clicked = dialog.btn_text_clicked
            BusinessLogicUtil.print_cyan(btn_text_clicked)
            loop_cnt = + 1
            if btn_text_clicked == "입력":
                BusinessLogicUtil.compress_pnx_via_bz(dialog.input_box.text())
            else:
                break

    @staticmethod
    def should_i_start_test_core():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            dialog = UiUtil.CustomQdialog(string="테스트를 시작할까요?", btns=["시작하기", "시작하지 않기"])
            dialog.exec()
            btn_text_clicked = dialog.btn_text_clicked
            if btn_text_clicked == "시작하기":
                BusinessLogicUtil.print_cyan("아무 테스트도 정의되지 않았습니다.")
                pass
            else:
                break

    @staticmethod
    def should_i_enter_to_power_saving_mode():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        btn_text_clicked, function, dialog_input_box_text = BusinessLogicUtil.should_i_do(
            string="절전모드로 진입할까요?",
            btns=["진입", "아니,"                  " 그냥 닫아", "10분 뒤 진입", "20분 뒤 진입", "30분 뒤 진입", "1시간 뒤 진입", "진입취소해줘"],
            function=BusinessLogicUtil.change_os_to_power_saving_mode,
            auto_click_negative_btn_after_seconds=30,
            title="Undefined Title",
            return_mode=True,
        )
        BusinessLogicUtil.print_cyan(btn_text_clicked)
        if function is not None:
            if btn_text_clicked == "진입":
                function()
            if btn_text_clicked == "아니, 그냥 닫아":
                return
            elif btn_text_clicked == "10분 뒤 진입":
                UiUtil.pop_up_as_complete(title_="작업중간보고", ment="10분 뒤 절전모드 진입을 시도합니다", input_text_default="", auto_click_positive_btn_after_seconds=3)
                BusinessLogicUtil.sleep(minutes=10)
                function()
            elif btn_text_clicked == "20분 뒤 진입":
                UiUtil.pop_up_as_complete(title_="작업중간보고", ment="20분 뒤 절전모드 진입을 시도합니다", input_text_default="", auto_click_positive_btn_after_seconds=3)
                BusinessLogicUtil.sleep(minutes=20)
                function()
            elif btn_text_clicked == "30분 뒤 진입":
                UiUtil.pop_up_as_complete(title_="작업중간보고", ment="30분 뒤 절전모드 진입을 시도합니다", input_text_default="", auto_click_positive_btn_after_seconds=3)
                BusinessLogicUtil.sleep(minutes=30)
                function()
            elif btn_text_clicked == "1시간 뒤 진입":
                UiUtil.pop_up_as_complete(title_="작업중간보고", ment="1시간 뒤 절전모드 진입을 시도합니다", input_text_default="", auto_click_positive_btn_after_seconds=3)
                BusinessLogicUtil.sleep(minutes=60)
                function()
            elif btn_text_clicked == "진입취소해줘":
                BusinessLogicUtil.change_os_to_shutdown(cancel_mode=True)

    @staticmethod
    def should_i_translate_eng_to_kor():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            dialog = UiUtil.CustomQdialog(string="WRITE SOMETHING YOU WANT TO TRANSLATE", btns=["Translate this to Korean", "Don't"], input_box_mode=True)
            dialog.exec()
            btn_text_clicked = dialog.btn_text_clicked
            BusinessLogicUtil.print_cyan(btn_text_clicked)
            if btn_text_clicked == "Translate this to Korean":
                BusinessLogicUtil.translate_eng_to_kor(dialog.input_box.text())
            else:
                break

    @staticmethod
    def should_i_translate_kor_to_eng():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            dialog = UiUtil.CustomQdialog(string='번역하고 싶은 내용을 입력하세요', btns=["영어로 번역", "번역하지 않기"], input_box_mode=True)
            dialog.exec()
            btn_text_clicked = dialog.btn_text_clicked
            BusinessLogicUtil.print_cyan(btn_text_clicked)
            if btn_text_clicked == "영어로 번역":
                BusinessLogicUtil.translate_kor_to_eng(dialog.input_box.text())
            else:
                break

    @staticmethod
    def should_i_exit_this_program():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            # dialog = UiUtil.CustomQdialog(context="앱을 종료할까요?", buttons=["종료", "종료하지 않기"])
            dialog = UiUtil.CustomQdialog(string="프로그램을 종료할까요?", btns=["종료", "종료하지 않기"])
            dialog.exec()
            btn_text_clicked = dialog.btn_text_clicked
            BusinessLogicUtil.print_cyan(btn_text_clicked)
            if btn_text_clicked == "종료":
                # app.quit()
                # BusinessLogicUtil.taskkill("python.exe")
                # self.close()
                sys.exit()
                # break
            else:
                break

    @staticmethod
    def should_i_show_animation_information_from_web():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            dialog = UiUtil.CustomQdialog(string="nyaa.si 에서 검색할 내용을 입력하세요", btns=["검색", "검색하지 않기"], input_box_mode=True)
            dialog.exec()
            btn_text_clicked = dialog.btn_text_clicked
            BusinessLogicUtil.print_cyan(btn_text_clicked)
            if btn_text_clicked == "검색":
                BusinessLogicUtil.download_torrent_files_from_web_via_user_input(dialog.input_box.text())
            else:
                break

    @staticmethod
    def should_i_find_direction_via_naver_map():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            dialog = UiUtil.CustomQdialog(string="어디로 길을 찾아드릴까요?", btns=["찾아줘", "찾아주지 않아도 되"], input_box_mode=True)
            dialog.exec()
            btn_text_clicked = dialog.btn_text_clicked
            BusinessLogicUtil.print_cyan(btn_text_clicked)
            if btn_text_clicked == "찾아줘":
                BusinessLogicUtil.find_direction_via_naver_map(dialog.input_box.text())
            else:
                BusinessLogicUtil.speak_ment_experimental("네, 알겠습니다", comma_delay=0.98)
                break

    @staticmethod
    def should_i_reboot_this_computer():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            dialog = UiUtil.CustomQdialog(string='시스템을 재시작할까요?', btns=[MentsUtil.YES, MentsUtil.NO])
            dialog.exec()
            btn_text_clicked = dialog.btn_text_clicked
            BusinessLogicUtil.print_cyan(btn_text_clicked)
            if btn_text_clicked == MentsUtil.YES:
                BusinessLogicUtil.reboot_this_computer()
            else:
                break

    @staticmethod
    def ask_something_to_ai():
        previous_question = None
        if previous_question is None:
            previous_question = clipboard.paste()
        while True:
            dialog = UiUtil.CustomQdialog(string='AI 에게 할 질문을 입력하세요', btns=["질문하기", "질문하지 않기"], input_box_mode=True, input_box_text_default=previous_question)
            dialog.exec()
            btn_text_clicked = dialog.btn_text_clicked
            BusinessLogicUtil.print_cyan(btn_text_clicked)
            if btn_text_clicked == "질문하기":
                BusinessLogicUtil.ask_to_wrtn_core(dialog.input_box.text())
            else:
                break
            previous_question = dialog.input_box.text()

    @staticmethod
    def should_i_connect_to_rdp1():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            dialog = UiUtil.CustomQdialog(string='rdp1에 원격접속할까요?', btns=[MentsUtil.YES, MentsUtil.NO])
            dialog.exec()
            btn_text_clicked = dialog.btn_text_clicked
            BusinessLogicUtil.print_cyan(btn_text_clicked)
            if btn_text_clicked == MentsUtil.YES:
                # BusinessLogicUtil.run_rdp_client()
                pass
            else:
                break

    @staticmethod
    def should_i_record_macro():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            dialog = UiUtil.CustomQdialog(string="매크로 레코드를 어떻게 시작할까요?", btns=["새로 시작하기", "이어서 시작하기", "시작하지 않기"])
            dialog.exec()
            btn_text_clicked = dialog.btn_text_clicked
            if btn_text_clicked == "새로 시작하기":
                if os.path.exists(StateManagementUtil.MACRO_LOG):
                    BusinessLogicUtil.move_pnx_to_trash_bin(StateManagementUtil.MACRO_LOG)
                BusinessLogicUtil.make_pnx(StateManagementUtil.MACRO_LOG, mode="f")
                BusinessLogicUtil.run_via_explorer_exe(StateManagementUtil.MACRO_LOG)
            elif btn_text_clicked == "이어서 시작하기":
                if os.path.exists(StateManagementUtil.MACRO_LOG):
                    BusinessLogicUtil.make_pnx(StateManagementUtil.MACRO_LOG, mode="f")
                    BusinessLogicUtil.run_via_explorer_exe(StateManagementUtil.MACRO_LOG)
            elif btn_text_clicked == "시작하지 않기":
                break
            macro_window = UiUtil.MacroWindow()
            macro_window.show()
            macro_window.activateWindow()
            break

    @staticmethod
    def download_video_from_web1():
        while True:
            # BusinessLogicUtil.press("ctrl", "0")
            file_png = rf"{StateManagementUtil.PROJECT_DIRECTORY}\pkg_png\download_video_via_chrome_extensions.png"
            BusinessLogicUtil.click_center_of_img_recognized_by_mouse_left(img_pnx=file_png, loop_limit_cnt=10)

            BusinessLogicUtil.sleep(1000)

            BusinessLogicUtil.press("tab")
            BusinessLogicUtil.sleep(30)

            BusinessLogicUtil.press("enter")
            BusinessLogicUtil.sleep(30)

            BusinessLogicUtil.press("ctrl", "shift", "tab")

            BusinessLogicUtil.press("ctrl", "0")
            BusinessLogicUtil.press("ctrl", "-")
            BusinessLogicUtil.press("ctrl", "-")
            break

    @staticmethod
    def should_i_do(string: str, function: Callable = None, auto_click_negative_btn_after_seconds: int = None, auto_click_positive_btn_after_seconds: int = None, input_box_text_default="", btns=["응", "응, 닫아"], title="Undefined Title", return_mode=False, input_box_mode=False):
        # cli_mode = False 이 모드...to do...
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        file_pnx = StateManagementUtil.POP_SOUND_POP_SOUND_WAV
        if BusinessLogicUtil.does_pnx_exist(src=file_pnx):
            BusinessLogicUtil.play_wav_file(file_pnx=file_pnx)

        # QApplication 인스턴스 없으면 생성
        app_foo = None
        app = QApplication.instance()
        if app is None:
            app_foo = QApplication()

        dialog_ = UiUtil.CustomQdialog(
            title=title,
            string=string,
            btns=btns,
            input_box_mode=input_box_mode,
            input_box_text_default=input_box_text_default,
            auto_click_positive_btn_after_seconds=auto_click_positive_btn_after_seconds,
            auto_click_negative_btn_after_seconds=auto_click_negative_btn_after_seconds
        )
        dialog_.exec()
        dialog_btn_text_clicked = dialog_.btn_text_clicked
        dialog_input_box_text = None
        if not input_box_mode == False:
            if not dialog_.input_box.text() is None:
                dialog_input_box_text = dialog_.input_box.text()

        if return_mode == True:
            return (dialog_btn_text_clicked, function, dialog_input_box_text)
        elif return_mode == False:
            if dialog_btn_text_clicked == MentsUtil.YES:
                if function is not None:
                    function()
                    return

    @staticmethod
    def guide_to_check_routines():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        """
        예정된 routines 수행 다하면 보상을 주는 게임을 실행할지 묻는 함수 mkmk
        """
        # 여기서 deepcopy() 를 쓴 이유
        # 원본의 len(routines) 을 알아야 하는데
        # deepcopy 를 하지않으면 step 마다  routine: str 이 줄어든 routines: [routine] 의 len 을 참조하게 되는데
        # 이는, 의도한 초기의 routines 의 len 을 참조하는 것과 다르므로, routines_deep_copied 를 만들었다
        # 여기서는 routines 를 수행된 routine을 제거하고 routine이 제거된 routines 를 관리하는데
        # 그동안 평소 구현했던 일반적으로 리스트를 순환할때와 enumerate를 통하여 cursor 를 움직이며 동작하는 것과 달리,
        # routines: [str] 에서 routine 을 하나씩 없애도록 만들었다 .
        # step= 1, routines = [ "routine1", "routine2", "routine3" ]
        # step= 2, routines = [ "routine2", "routine3" ]
        # step= 3, routines = [ "routine3" ]
        # 코드 실험을 해보면, 첫번째 원소가 계속 빠지도록 만들었다는 것을 알수 있다. 큐 자료구조와 일부 비슷한 부분이 있는 구조이다.
        # 의도하고 만든건 아니지만. 자료구조적으로는 FIFO 가 활용된 것이다.
        # cursor 는 routines[0] 만 계속 가리키게 한다. routines[0]을 수행했다면 routines 에서 routines[0](리스트의 첫 원소)를 계속 빼어 버린다.

        # routines = StateManagementUtil.routines
        # routines_deep_copied = copy.deepcopy(routines)

        # ment = '루틴을 가이드합니다'
        # BusinessLogicUtil.speak(ment=ment)

        # BusinessLogicUtil.sleep(milliseconds=50)

        # ment: str = "\n".join(StateManagementUtil.routines)
        # BusinessLogicUtil.print_as_gui(ment=ment, auto_click_positive_btn_after_seconds=10)

        # btns = [MentsUtil.DONE, MentsUtil.I_WANT_TO_TO_DO_NEXT_TIME, MentsUtil.OK_I_WILL_DO_IT_NOW]
        # routines_left: str = "\n".join(routines)
        # ment = f"<남은 루틴목록>\n\n{routines_left}
        # '응, 아니 지금할게'

    @staticmethod
    def should_i_download_youtube_as_webm():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        text_previous_from_clipboard = None
        while True:
            if text_previous_from_clipboard != clipboard.paste():
                text_previous_from_clipboard = clipboard.paste()
            else:
                text_previous_from_clipboard = ""
            dialog = UiUtil.CustomQdialog(string="다운로드하고 싶은 URL을 입력해주세요", btns=["입력", "입력하지 않기"], input_box_mode=True, input_box_text_default=text_previous_from_clipboard)
            dialog.exec()
            if dialog.btn_text_clicked == "입력":
                BusinessLogicUtil.download_from_youtube_to_webm(urls=dialog.input_box.text())
            else:
                break

    @staticmethod
    def should_i_merge_directories():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        previous_text = ""
        while True:
            previous_text = clipboard.paste()
            dialog = UiUtil.CustomQdialog(string="머지할 pnx들을 입력하세요", btns=["입력", "입력하지 않기"], input_box_mode=True, input_box_text_default=previous_text, auto_click_negative_btn_after_seconds=10)
            dialog.exec()
            directory_pnxs = dialog.input_box.text()
            if dialog.btn_text_clicked == "입력":
                directory_pnxs = directory_pnxs.strip()
                directory_pnxs = directory_pnxs.strip("\t")
                directory_pnxs_: List[str] = directory_pnxs.split("\n")
                BusinessLogicUtil.merge_directories(directory_pnxs=directory_pnxs_)
                break
            else:
                break

    @staticmethod
    def should_i_convert_mkv_to_wav():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            dialog = UiUtil.CustomQdialog(string="convert 할 MKV파일경로를 입력하세요", btns=["입력", "입력하지 않기"], input_box_mode=True, auto_click_negative_btn_after_seconds=10)
            dialog.exec()
            btn_text_clicked = dialog.btn_text_clicked
            file_mkv = dialog.input_box.text()
            if btn_text_clicked == "입력":
                BusinessLogicUtil.convert_mkv_to_wav(file_mkv=file_mkv)
                break
            else:
                break

    @staticmethod
    def should_i_gather_empty_directory():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            dialog = UiUtil.CustomQdialog(string="빈폴더를 순회하며 수집할 pnx를 입력하세요", btns=["입력", "입력하지 않기"], input_box_mode=True)
            dialog.exec()
            btn_text_clicked = dialog.btn_text_clicked
            if btn_text_clicked == "입력":
                pnx = dialog.input_box.text()
                pnx = pnx.strip()
                pnx = pnx.replace("\"", "")
                pnx = pnx.replace("\'", "")
                connected_drives = []
                for drive_letter in string.ascii_uppercase:
                    drive_path = drive_letter + ":\\"
                    if os.path.exists(drive_path):
                        connected_drives.append(drive_path)
                        if pnx == drive_path:
                            BusinessLogicUtil.speak_ment_experimental("입력된 pnx는 너무 광범위하여 진행할 수 없도록 설정되어 있습니다", comma_delay=0.98)
                            break
                if not os.path.exists(pnx):
                    BusinessLogicUtil.speak_ment_experimental("입력된 pnx가 존재하지 않습니다", comma_delay=0.98)
                    continue
                if pnx == "":
                    continue

                BusinessLogicUtil.gather_pnxs_empty(pnx)
                BusinessLogicUtil.print_success(string=rf"pnx를 순회하며 빈폴더를 모았습니다")
                # BusinessLogicUtil.speak_ments("pnx를 순회하며 빈폴더를 약속된 폴더로 모았습니다", sleep_after_play=0.65) # 시끄러웠다,
                UiUtil.pop_up_as_complete(title_="작업성공보고", ment=f"pnx를 순회하며 빈폴더를 모았습니다", auto_click_positive_btn_after_seconds=2)
            else:
                break

    @staticmethod
    def should_i_gather_pnxs_useless():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            dialog_btn_text_clicked, function, dialog_input_box_text = BusinessLogicUtil.should_i_do(
                string="pnx를 순회하며 텍스트파일에 정의된 불필요한 파일을 약속된 pnx로 모을까요?",
                btns=["모으기", "모으지 않기"],
                function=BusinessLogicUtil.change_os_to_power_saving_mode, auto_click_negative_btn_after_seconds=30,
                title=f"{function_name}()",
                return_mode=True,
                input_box_mode=True,
            )
            if dialog_btn_text_clicked == "모으기":
                pnx = dialog_input_box_text
                pnx = pnx.strip()
                pnx = pnx.replace("\"", "")
                pnx = pnx.replace("\'", "")
                BusinessLogicUtil.print_as_log(f'''pnxs={pnx} %%%FOO%%%''')
                if pnx == "":
                    BusinessLogicUtil.print_as_log(f'''pnx가 입력되지 않았습니다 %%%FOO%%%''')
                    return
                connected_drives = []
                for drive_letter in string.ascii_uppercase:
                    drive_path = drive_letter + ":\\"
                    if os.path.exists(drive_path):
                        connected_drives.append(drive_path)
                        if pnx == drive_path:
                            BusinessLogicUtil.print_as_log(f'''입력된 pnx는 너무 광범위하여 진행할 수 없도록 설정되어 있습니다 %%%FOO%%%''')
                            return
                if not os.path.exists(pnx):
                    BusinessLogicUtil.print_as_log(f'''입력된 pnx가 존재하지 않습니다 %%%FOO%%%''')
                    return
                BusinessLogicUtil.gather_pnxs_useless(src=pnx)
            return
        except:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def should_i_gather_special_files():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        """분류되지 않은 하나의 폴더로 모음"""
        # while True:
        #     dialog = UiUtil.CustomQdialog(ment="pnx를 순회하며 특별한 파일을 약속된 폴더로 모을까요?", buttons=["모으기", "모으지 않기"], is_input_text_box=True)
        #     dialog.exec()
        #     btn_text_clicked = dialog.btn_text_clicked
        #     if btn_text_clicked == "모으기":
        #         target_pnx = dialog.input_box.text()
        #         target_pnx = target_pnx.strip()
        #         target_pnx = target_pnx.replace("\"", "")
        #         target_pnx = target_pnx.replace("\'", "")
        #         connected_drives = []
        #         for drive_letter in string.ascii_uppercase:
        #             drive_path = drive_letter + ":\\"
        #             if os.path.exists(drive_path):
        #                 connected_drives.append(drive_path)
        #                 if target_pnx == drive_path:
        #                     BusinessLogicUtil.speak_ments("입력된 pnx는 너무 광범위하여 진행할 수 없도록 설정되어 있습니다", sleep_after_play=0.65)
        #                     break
        #         if not os.path.exists(target_pnx):
        #             BusinessLogicUtil.speak_ments("입력된 pnx가 존재하지 않습니다", sleep_after_play=0.65)
        #             continue
        #         if target_pnx == "":
        #             continue
        #         special_files = [
        #             "[subplease]",
        #         ]
        #         dst = rf"D:\[noe] [8TB] [ext]\$special_files"
        #         BusinessLogicUtil.make_leaf_directory(dst)
        #         isSpoken = False
        #         if os.path.isdir(target_pnx):
        #             for root, dirs, files in os.walk(target_pnx, topdown=False):  # os.walk()는 with walking 으로 동작한다
        #                 for file in files:
        #                     file_path = os.path.join(root, file)
        #                     for special_file in special_files:
        #                         if special_file in os.path.basename(file_path):
        #                             # print(rf'file_path : {file_path}')
        #                             print(rf"special file : {file_path}")
        #                             BusinessLogicUtil.move_pnx_without_overwrite(target_pnx=file_path, dst=dst)
        #                             if isSpoken == False:
        #                                 BusinessLogicUtil.speak_ments("pnx를 순회하며 특별한 파일을 약속된 폴더로 모았습니다", sleep_after_play=0.65)
        #                                 isSpoken = True
        #     else:
        #         break
        pass

    @staticmethod
    def classify_pnx_by_special_keyword(pnx, special_keyword, with_walking):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        pnx = pnx.strip()
        pnx = pnx.replace("\"", "")
        pnx = pnx.replace("\'", "")
        BusinessLogicUtil.print_light_black(f'''pnx = {pnx}''')
        connected_drives = []
        for drive_letter in string.ascii_uppercase:
            drive_path = drive_letter + ":\\"
            if os.path.exists(drive_path):
                connected_drives.append(drive_path)
                if pnx == drive_path:
                    BusinessLogicUtil.print_as_log(string=rf'''"광범위진행제한%%%FOO%%%''')
                    return

        if not os.path.exists(pnx):
            BusinessLogicUtil.print_as_log("입력된 pnx가 존재하지 않습니다")
            return

        if pnx == "":
            BusinessLogicUtil.print_as_log(f'''"pnx == """''')
            return

        special_dirs_promised = [
            # "blahblahblah_boom_boom_boom",
        ]
        # previous_keyword = clipboard.paste()
        # if previous_keyword == pnx:
        #     previous_keyword = ""

        special_keyword = special_keyword.strip()
        if special_keyword == "":
            BusinessLogicUtil.print_as_log("special_keyword 는 ""일 수 없습니다.")
            return
        if "\n" in special_keyword:
            file_pnxs = special_keyword.split("\n")
            BusinessLogicUtil.print_as_log(string=rf'''len(file_pnxs)="{len(file_pnxs)}" %%%FOO%%%''')
        else:
            file_pnxs = [special_keyword]
            BusinessLogicUtil.print_as_log(string=rf'''file_pnxs="{file_pnxs}" %%%FOO%%%''')
        for special_keyword in file_pnxs:
            special_keyword = special_keyword.strip()
            if special_keyword != "":
                special_dirs_promised.append(special_keyword)
            pn = BusinessLogicUtil.get_pn(pnx)
            for special_pnx in special_dirs_promised:
                BusinessLogicUtil.make_pnx(rf"{StateManagementUtil.CLASSIFYING}\{special_pnx}", mode="d")
            pnxs_searched = []
            if os.path.isdir(pnx):
                if with_walking == True:
                    for root, dirs, files in os.walk(pnx, topdown=False):  # os.walk()는 with walking 으로 동작한다
                        for file in files:
                            file_abspath = os.path.join(root, file)
                            for special_keyword in special_dirs_promised:
                                if special_keyword in os.path.basename(file_abspath):
                                    pnxs_searched.append(file_abspath)
                else:
                    # todo without_waling
                    return

            BusinessLogicUtil.print_as_log(string=rf'''len(pnxs_searched)="{len(pnxs_searched)}" %%%FOO%%%''')  # 검색된 파일 개수
            dst = None
            for index, special_dir in enumerate(special_dirs_promised):
                dst = rf"{StateManagementUtil.CLASSIFYING}\{special_dirs_promised[index]}"
                for pnx_searched in pnxs_searched:
                    if special_dir in os.path.basename(pnx_searched):
                        BusinessLogicUtil.move_pnx_without_overwrite(src=pnx_searched, dst=dst)
            special_dirs_promised = []
            BusinessLogicUtil.print_as_log(string=rf'''dst="{dst}" %%%FOO%%%''')

    @staticmethod
    def should_i_classify_special_files():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        """분류된 여러 폴더로 모음"""
        is_nested_loop_broken = False
        previous_abspath = ""
        while True:
            while True:
                dialog1 = UiUtil.CustomQdialog(string="파일분류를 위해 순회할 디렉토리의 pnx를 입력해주세요", btns=["제출", "제출하지 않기"], input_box_mode=True, input_box_text_default=previous_abspath)
                dialog1.exec()

                btn_text_clicked = dialog1.btn_text_clicked
                if btn_text_clicked == "제출하지 않기":
                    is_nested_loop_broken = True
                    break
                if btn_text_clicked == "제출":
                    target_pnx = dialog1.input_box.text()
                    target_pnx = target_pnx.strip()
                    target_pnx = target_pnx.replace("\"", "")
                    target_pnx = target_pnx.replace("\'", "")
                    previous_abspath = target_pnx
                    connected_drives = []
                    for drive_letter in string.ascii_uppercase:
                        drive_path = drive_letter + ":\\"
                        if os.path.exists(drive_path):
                            connected_drives.append(drive_path)
                            if target_pnx == drive_path:
                                BusinessLogicUtil.print_as_log(string="입력된 pnx는 너무 광범위하여 진행할 수 없도록 설정되어 있습니다")
                                is_nested_loop_broken = True
                                break
                    if not os.path.exists(target_pnx):
                        # BusinessLogicUtil.speak_ment_experimental("입력된 pnx가 존재하지 않습니다", comma_delay=0.98)
                        continue
                    if target_pnx == "":
                        continue
                    special_dirs_promised = [
                        # "blahblahblah_boom_boom_boom",
                    ]
                    previous_keyword = clipboard.paste()
                    if previous_keyword == target_pnx:
                        previous_keyword = ""

                    dialog2 = UiUtil.CustomQdialog(string="분류할 파일에 포함되어 있을 키워드를 입력해주세요", btns=["제출", "제출하지 않기"], input_box_mode=True, input_box_text_default=previous_keyword)
                    dialog2.exec()
                    btn_text_clicked2 = dialog2.btn_text_clicked
                    if btn_text_clicked2 == "제출":
                        file_path = dialog2.input_box.text()
                        file_path = file_path.strip()
                        if file_path == "":
                            BusinessLogicUtil.speak_ment_experimental("입력된 pnx가 존재하지 않습니다", comma_delay=0.98)
                            break
                        if "\n" in file_path:
                            file_paths = file_path.split("\n")
                            BusinessLogicUtil.speak_ment_experimental(f"{len(file_paths)}개의 키워드들이 입력되었습니다, 파일분류를 시작합니다", comma_delay=0.98)
                        else:
                            file_paths = [file_path]
                        for file_path in file_paths:
                            file_path = file_path.strip()
                            if file_path != "":
                                special_dirs_promised.append(file_path)
                            # destination_directory_of_files_classified = StateManagementUtil.SPECIAL_DIRECTORY # e: drive 에 저장
                            dst_dir_of_files_classified = rf"{target_pnx}\`"  # 입력된 pnx에 ` 폴더를 만들어 저장
                            for special_file in special_dirs_promised:
                                BusinessLogicUtil.make_pnx(rf"{dst_dir_of_files_classified}\{special_file}", mode="d")
                            # BusinessLogicUtil.make_leaf_directory(destination_directory_of_files_classified)
                            file_abspaths_searched = []
                            if os.path.isdir(target_pnx):
                                for root, dirs, files in os.walk(target_pnx, topdown=False):  # os.walk()는 with walking 으로 동작한다
                                    for file in files:
                                        file_abspath = os.path.join(root, file)
                                        for file_path in special_dirs_promised:
                                            if file_path in os.path.basename(file_abspath):
                                                file_abspaths_searched.append(file_abspath)
                            file_abspaths_searched_for_print = "\n".join(file_abspaths_searched)  # [str] to str with 개행

                            # dialog3 = UiUtil.CustomQdialog(ment=f"<검색된 파일 목록>\n\n검색된 파일 개수 : {len(file_abspaths_searched)}\n{file_abspaths_searched_for_print}\n\n 검색된 내용대로 계속진행을 할까요?", btns=[MentsUtil.YES, MentsUtil.NO], auto_click_positive_btn_after_seconds=0)
                            # dialog3.exec()
                            # if dialog3.btn_text_clicked == MentsUtil.NO:
                            #     break
                            # if dialog3.btn_text_clicked == MentsUtil.YES:
                            #     for index, special_dir in enumerate(special_dirs_promised):
                            #         for file_abspath_searched in file_abspaths_searched:
                            #             if special_dir in os.path.basename(file_abspath_searched):
                            #                 # UiUtil.pop_up_as_complete(title="디버깅", ment=f"index : {index} \n special_dir: {special_dir}", auto_click_positive_btn_after_seconds=600)
                            #                 BusinessLogicUtil.move_pnx_without_overwrite(target_pnx=file_abspath_searched, dst=rf"{dst_dir_of_files_classified}\{special_dirs_promised[index]}")
                            # special_dirs_promised = []

                            BusinessLogicUtil.print_cyan(string=f"#검색된 파일 개수 : {len(file_abspaths_searched)}")
                            BusinessLogicUtil.print_cyan(string=f"#검색된 파일 목록 : {file_abspaths_searched_for_print}")
                            for index, special_dir in enumerate(special_dirs_promised):
                                for file_abspath_searched in file_abspaths_searched:
                                    if special_dir in os.path.basename(file_abspath_searched):
                                        # UiUtil.pop_up_as_complete(title="디버깅", ment=f"index : {index} \n special_dir: {special_dir}", auto_click_positive_btn_after_seconds=600)
                                        BusinessLogicUtil.move_pnx_without_overwrite(src=file_abspath_searched, dst=rf"{dst_dir_of_files_classified}\{special_dirs_promised[index]}")
                            special_dirs_promised = []

            if is_nested_loop_broken == True:
                break

    @staticmethod
    def do_random_schedules():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        int_random = random.randint(0, 7)
        # Park4139BusinessLogicUtil.Tts.speak(f'랜덤숫자 {int_random} 나왔습니다')
        # mkmk
        if int_random == 0:
            pass
        elif int_random == 1:
            pass
        elif int_random == 2:
            pass
        elif int_random == 3:
            pass
        elif int_random == 4:
            pass
        elif int_random == 5:
            pass
        elif int_random == 6:
            pass
        elif int_random == 7:
            pass

    @staticmethod
    def guide_to_sleep():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        countdown_limit_upper = 19
        count = countdown_limit_upper - len(StateManagementUtil.COUNTS_FOR_GUIDE_TO_SLEEP)
        if count == countdown_limit_upper:
            BusinessLogicUtil.speak_ment_experimental(ment='최대절전모드 카운트다운을 진행합니다', comma_delay=0.55, thread_join_mode=True)
        BusinessLogicUtil.speak_ment_experimental(ment=f'카운트다운 {count}', comma_delay=0.55, thread_join_mode=True)
        StateManagementUtil.COUNTS_FOR_GUIDE_TO_SLEEP.append("!")
        if count == 0:
            BusinessLogicUtil.speak('프로젝트 백업 진행', after_delay=0.55)
            BusinessLogicUtil.compress_pnx_via_bz(pnx=StateManagementUtil.PROJECT_PARENTS_DIRECTORY)
            BusinessLogicUtil.speak('최대 절전 모드 진입', after_delay=0.55)
            BusinessLogicUtil.change_os_to_power_saving_mode()
            BusinessLogicUtil.pause()

    @staticmethod
    def sleep(milliseconds=None, seconds=None, minutes=None, hours=None, show_mode=True):  # mode countdown
        # function_name = inspect.currentframe().f_code.co_name
        # if show_mode == True:
        #     BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # Nones = [milliseconds, seconds, minutes, hour]
        # None_count = Nones.count(None)
        # time_value = None
        # if None_count == 4:
        #     BusinessLogicUtil.print_light_black(string=rf"{function_name}() 함수는 {Nones} 중에 하나는 인자로 정의 되어야 합니다.")
        #     return
        # if None_count == 3:
        #     if milliseconds is not None:
        #         seconds = milliseconds / 1000
        #         if show_mode == True:
        #             BusinessLogicUtil.print_as_log(f"{function_name}(ms={milliseconds})")
        #         time_value = seconds
        #     elif seconds is not None:
        #         if show_mode == True:
        #             BusinessLogicUtil.print_as_log(f"{function_name}(seconds={seconds})")
        #         time_value = seconds
        #     elif minutes is not None:
        #         if show_mode == True:
        #             BusinessLogicUtil.print_as_log(f"{function_name}(minutes={minutes})")
        #         time_value = 60 * minutes
        #     elif hour is not None:
        #         if show_mode == True:
        #             BusinessLogicUtil.print_as_log(f"{function_name}(hours={hour})")
        #         time_value = 60 * 60 * hour
        #     # time_to_sleep 확인 후 동작
        #     if time_value is not None:
        #         if show_mode == True:
        #             BusinessLogicUtil.print_as_log(rf'''type(time_value) = "{type(time_value)}"''')
        #             BusinessLogicUtil.print_as_log(f'''time_value = {time_value}''')
        #         time.sleep(time_value)
        #     else:
        #         if show_mode == True:
        #             BusinessLogicUtil.print_as_log(f"{function_name}(): time_to_sleep가 None입니다. 동작하지 않습니다.")
        # else:
        #     BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
        function_name = inspect.currentframe().f_code.co_name
        if show_mode:
            BusinessLogicUtil.print_as_log(
                string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%'''
            )

        # 인자 유효성 검사
        time_units = {"milliseconds": milliseconds, "seconds": seconds, "minutes": minutes, "hours": hours}
        provided_units = {k: v for k, v in time_units.items() if v is not None}
        if len(provided_units) != 1:
            BusinessLogicUtil.print_light_black(
                string=f"{function_name}() 함수는 {list(time_units.keys())} 중 하나만 정의되어야 합니다."
            )
            return
        # 대기 시간 계산
        unit, value = next(iter(provided_units.items()))
        if unit == "milliseconds":
            time_value = value / 1000
        elif unit == "seconds":
            time_value = value
        elif unit == "minutes":
            time_value = value * 60
        elif unit == "hours":
            time_value = value * 3600

        if show_mode:
            BusinessLogicUtil.print_as_log(f'''"{unit}={value}"''')

        # 대기 실행
        time.sleep(time_value)

    @staticmethod
    def print_os_sys_environment_variables():
        BusinessLogicUtil.print_list_as_vertical(items_list=os.environ, items_list_name='모든 시스템 환경변수 출력')
        BusinessLogicUtil.pause()

    @staticmethod
    def get_os_sys_environment_variable(environment_variable_name: str):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        return os.environ.get(environment_variable_name)

    @staticmethod
    def add_os_sys_environment_variable(environment_variable_name: str, environment_variable_value: str):
        """시스템 환경변수 path 업데이트"""
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.print_with_underline("테스트가 필요한 함수를 적용하였습니다")
        BusinessLogicUtil.print_with_underline("기대한 결과가 나오지 않을 수 있습니다")
        BusinessLogicUtil.print_with_underline("업데이트 전 시스템 환경변수")
        for i in sys.path:
            BusinessLogicUtil.print_cyan(i)
        sys.path.insert(0, environment_variable_value)
        sys.path.append(environment_variable_value)
        BusinessLogicUtil.print_with_underline("업데이트 전 시스템 환경변수")
        for i in sys.path:
            BusinessLogicUtil.print_cyan(i)

    @staticmethod
    def get_name_space():  # name space # namespace # 파이썬 네임스페이스
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        dir()
        return dir()

    @staticmethod
    def compress_pnx_via_bz(pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            while True:
                ment = rf"백업 {pnx}"
                BusinessLogicUtil.print_light_black(f"%%%FOO%%% {ment}", )

                # 전처리
                pnx = pnx.replace("\n", "")
                pnx = pnx.replace("\"", "")

                if pnx.strip() == "":
                    BusinessLogicUtil.speak_ment_experimental(ment="백업할 대상이 입력되지 않았습니다", comma_delay=0.98)
                    break

                target_dirname = os.path.dirname(pnx)
                target_dirname_dirname = os.path.dirname(target_dirname)
                target_basename = os.path.basename(pnx).split(".")[0]
                target_zip = rf'{target_dirname}\$zip_{target_basename}.zip'
                target_yyyy_mm_dd_hh_mm_ss_zip_basename = rf'{target_basename} - {BusinessLogicUtil.get_time_as_("%Y %m %d %H %M %S")}.zip'
                BusinessLogicUtil.print_light_black(f"target_pnx : {pnx}")
                BusinessLogicUtil.print_light_black(f"target_dirname : {target_dirname}")
                BusinessLogicUtil.print_light_black(f"target_dirname_dirname : {target_dirname_dirname}")
                BusinessLogicUtil.print_light_black(f"target_basename : {target_basename}")
                BusinessLogicUtil.print_light_black(f"target_zip : {target_zip}")
                BusinessLogicUtil.print_light_black(f"target_yyyy_mm_dd_HH_MM_SS_zip_basename : {target_yyyy_mm_dd_hh_mm_ss_zip_basename}")

                cmd = f'bz.exe c "{target_zip}" "{pnx}"'
                BusinessLogicUtil.command_to_os(cmd)

                cmd = rf'ren "{target_zip}" "{target_yyyy_mm_dd_hh_mm_ss_zip_basename}"'
                BusinessLogicUtil.command_to_os(cmd)

                # 파일이 위치한 드라이브로 이동
                drives = [
                    "C",
                    "D",
                    "E",
                    "F",
                    "G",
                ]
                drive_where_target_is_located = pnx.split(":")[0].upper()
                for drive in drives:
                    if (drive_where_target_is_located == drive):
                        os.system(rf"cd {drive}:")
                try:
                    os.chdir(target_dirname)
                except:
                    BusinessLogicUtil.speak_ment_experimental(ment="경로를 이해할 수 없습니다", comma_delay=0.98)
                    os.chdir(StateManagementUtil.PROJECT_DIRECTORY)
                    break
                lines = BusinessLogicUtil.command_to_os_like_person_as_admin('dir /b /a-d *.zip')
                BusinessLogicUtil.print_magenta(rf'''len(lines) = {len(lines)}''')
                for line in lines:
                    BusinessLogicUtil.print_magenta(f'''line = {line}''')
                    if line != "":
                        if os.getcwd() != line:  # 여기 os.getcwd() 이게 들어가네... 나중에 수정하자
                            # 2023-12-04 월 12:14 SyntaxWarning: invalid escape sequence '\d'
                            # r 을 사용 Raw String(원시 문자열),  \를 모두 제거
                            # 정규식은 r 쓰면 안된다. \ 써야한다?.
                            # 2023-12-12 화 14:23 SyntaxWarning: invalid escape sequence '\d'
                            # 가상환경 재설치 후 또 문제가 나타남,
                            # pattern = 'd{4} d{2} d{2} d{2} d{2} d{2}'
                            # pattern = r'\d{4} \d{2} \d{2} \d{2} \d{2} \d{2}'
                            pattern = r'd{4} d{2} d{2} d{2} d{2} d{2}'
                            # BusinessLogicUtil.print_as_log(line)
                            if BusinessLogicUtil.is_pattern_in_string(line, pattern, show_mode=False):
                                BusinessLogicUtil.print_with_underline(f"zip 파일 목록에 대하여 {pattern} 타임스탬프 정규식 테스트를 통과했습니다")
                                # BusinessLogicUtil.print_as_log(line)
                                # 2023-12-03 일 20:03 trouble shooting 성공
                                # 백업 시 타임스탬프에 언더바 넣도록 변경했는데 regex 는 변경 하지 않아서 난 실수 있었음.
                                time_to_backed_up = re.findall(pattern, line)
                                time_to_backed_up_ = time_to_backed_up[0][0:10].replace(" ", "-") + " " + time_to_backed_up[0][11:16].replace(" ", ":") + ".00"
                                time_to_backed_up__ = datetime.strptime(str(time_to_backed_up_), '%Y-%m-%d %H:%M.%S')
                                time_current = datetime.now()
                                try:
                                    target_dirname_old = rf'{target_dirname}\pkg_zip'
                                    if not os.path.exists(target_dirname_old):
                                        os.makedirs(target_dirname_old)
                                except Exception:
                                    BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
                                    os.chdir(StateManagementUtil.PROJECT_DIRECTORY)
                                    break
                                # 지금부터 7일 이전의 파일만
                                # diff = time_to_backed_up__ - time_current
                                # if diff.days <-7:
                                # BusinessLogicUtil.print_as_log(f"line : {line}")

                                # BusinessLogicUtil.print_as_log(f"1분(60 seconds) 이전의 파일자동정리 시도...")
                                BusinessLogicUtil.print_with_underline(f"파일자동정리 시도...")
                                change_min = time_current - timedelta(seconds=60)
                                diff = time_to_backed_up__ - change_min
                                if 60 < diff.seconds:
                                    try:
                                        file_with_time_stamp_zip = os.path.abspath(line.strip())
                                        file_dirname_old_abspath = os.path.abspath(target_dirname_old)
                                        BusinessLogicUtil.print_cyan(rf'move "{file_with_time_stamp_zip}" "{file_dirname_old_abspath}"')
                                        shutil.move(file_with_time_stamp_zip, file_dirname_old_abspath)
                                    except Exception:
                                        BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
                                        os.chdir(StateManagementUtil.PROJECT_DIRECTORY)
                                        break
                os.chdir(StateManagementUtil.PROJECT_DIRECTORY)
                BusinessLogicUtil.print_cyan(f"%%%FOO%%% green {ment}", )
                break
        except:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
            os.chdir(StateManagementUtil.PROJECT_DIRECTORY)

    @staticmethod
    def upzip_pnx(pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            while True:
                # 전처리
                pnx = pnx.replace("\n", "")
                pnx = pnx.replace("\"", "")

                if pnx.strip() == "":
                    BusinessLogicUtil.speak_ment_experimental(ment="백업할 대상이 입력되지 않았습니다", comma_delay=0.98)
                    break

                pnx_dirname = os.path.dirname(pnx)
                pnx_basename = os.path.basename(pnx).split(".")[0]
                target_zip = rf'{pnx_dirname}\{pnx_basename}.zip'

                os.chdir(pnx_dirname)

                if os.path.exists(target_zip):
                    # cmd = f'bandizip.exe bx "{target_zip}"'
                    cmd = f'bz.exe x -aoa "{target_zip}"'  # x 는 경로 보존, -aoa :Overwrite All existing files without prompt
                    BusinessLogicUtil.command_to_os_like_person_as_admin(cmd)
                    if os.path.exists(pnx):
                        cmd = rf'echo y | del /f "{target_zip}"'
                        BusinessLogicUtil.command_to_os_like_person_as_admin(cmd)
                    else:
                        BusinessLogicUtil.print_red("압축해제 후 압축파일을 삭제에 실패")
                else:
                    BusinessLogicUtil.print_light_yellow("압축해제할 파일이 없었습니다")
                os.chdir(StateManagementUtil.PROJECT_DIRECTORY)
                BusinessLogicUtil.print_success("압축해제 성공")
                break
        except:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
            os.chdir(StateManagementUtil.PROJECT_DIRECTORY)

    @staticmethod
    def back_up_target_without_timestamp(target_pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            while True:
                # 전처리
                target_pnx = target_pnx.replace("\n", "")
                target_pnx = target_pnx.replace("\"", "")

                if target_pnx.strip() == "":
                    BusinessLogicUtil.speak_ment_experimental(ment="백업할 대상이 입력되지 않았습니다", comma_delay=0.98)
                    break

                target_dirname = os.path.dirname(target_pnx)
                target_dirname_dirname = os.path.dirname(target_dirname)
                target_basename = os.path.basename(target_pnx).split(".")[0]
                special_target_zip = rf'{target_dirname}\$zip_{target_basename}.zip'
                target_pnx_zip = rf'{target_dirname}\{target_basename}.zip'
                target_basename_zip = rf'{target_basename}.zip'
                BusinessLogicUtil.print_cyan(f"target_pnx : {target_pnx}")
                BusinessLogicUtil.print_cyan(f"target_dirname : {target_dirname}")
                BusinessLogicUtil.print_cyan(f"target_dirname_dirname : {target_dirname_dirname}")
                BusinessLogicUtil.print_cyan(f"target_basename : {target_basename}")
                BusinessLogicUtil.print_cyan(f"special_target_zip : {special_target_zip}")

                cmd = f'bz.exe c "{special_target_zip}" "{target_pnx}"'
                BusinessLogicUtil.command_to_os_like_person_as_admin(cmd)

                cmd = rf'ren "{special_target_zip}" "{target_basename_zip}"'
                BusinessLogicUtil.command_to_os_like_person_as_admin(cmd)

                if os.path.exists(target_pnx_zip):
                    cmd = rf'echo y | rmdir /s "{target_pnx}"'
                    BusinessLogicUtil.command_to_os_like_person_as_admin(cmd)
                else:
                    BusinessLogicUtil.print_red("압축에 실패")
                    break

                os.chdir(StateManagementUtil.PROJECT_DIRECTORY)
                BusinessLogicUtil.print_success("압축에 성공")
                break
        except:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
            os.chdir(StateManagementUtil.PROJECT_DIRECTORY)

    @staticmethod
    def monitor_target_edited_and_back_up(target_pnx: str):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            if os.path.isfile(target_pnx):
                if BusinessLogicUtil.is_file_changed(target_pnx):
                    BusinessLogicUtil.compress_pnx_via_bz(target_pnx)
            elif os.path.isdir(target_pnx):
                if BusinessLogicUtil.is_directory_changed(target_pnx):
                    BusinessLogicUtil.compress_pnx_via_bz(target_pnx)
        except:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def monitor_target_edited_and_sync(target_pnx: str):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            if os.path.isfile(target_pnx):
                if BusinessLogicUtil.is_file_changed(target_pnx):
                    BusinessLogicUtil.sync_directory_local(target_pnx)
            elif os.path.isdir(target_pnx):
                BusinessLogicUtil.sync_directory_local(target_pnx)
        except:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def print_and_open_py_pkg_global_path():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        for path in sys.path:
            BusinessLogicUtil.print_cyan(path)
            if BusinessLogicUtil.is_pattern_in_string(string=path, pattern='site-packages') == True:
                BusinessLogicUtil.print_cyan(rf'echo "{path}"')
                BusinessLogicUtil.run_via_explorer_exe(path)

    @staticmethod
    def process_kill(img_name=None, pid=None, show_mode=True):
        function_name = inspect.currentframe().f_code.co_name
        if show_mode == True:
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # function_arg_names= [param.name for param in inspect.signature(process_kill).parameters.values()] # fail
        Nones = [img_name, pid]
        None_count = Nones.count(None)
        if None_count == 2:
            BusinessLogicUtil.print_as_log(string=rf''' 이 {function_name}()의 인자는 최대 1개 까지 받을 수 있습니다. %%%FOO%%%''', print_color="red")
        if None_count == 1:
            if img_name is not None:
                img_name = img_name.replace("\'", "")
                img_name = img_name.replace("\"", "")
                BusinessLogicUtil.command_to_os(f'taskkill /f /im "{img_name}"', show_mode=show_mode)
                BusinessLogicUtil.command_to_os(f'wmic process where name="{img_name}" delete ', show_mode=show_mode)
            if pid is not None:
                # BusinessLogicUtil.command_to_os(f'taskkill /f /pid {pid}', show_mode=show_mode)
                BusinessLogicUtil.command_to_os(f'taskkill /f /pid {pid}', show_mode=show_mode)
        if None_count == 0:
            BusinessLogicUtil.print_as_log(string=rf''' 이 {function_name}()의 인자는 최소 1개의 인자가 요구됩니다. %%%FOO%%%''', print_color="red")

    # 2023-12-07 목요일 16:51 최신화 함수
    @staticmethod
    def afterpause(function):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        def wrapper(*args, **kwargs):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            function(*args, **kwargs)
            BusinessLogicUtil.pause()
            pass

        return wrapper

    @staticmethod
    def get_time_as_(pattern: str):
        return TimeUtil.get_time_as_(pattern)

    @staticmethod
    def parse_youtube_video_id(url):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        keyword_shorts = '/shorts/'
        keyword_slash = '/'
        if keyword_shorts in url:
            youtube_video_id = url.split(keyword_shorts)[1]
            youtube_video_id = youtube_video_id.split(keyword_slash)[0]
            BusinessLogicUtil.print_as_log(string=rf'''youtube_video_id="{youtube_video_id}" %%%FOO%%%''')
            return youtube_video_id
        query = urllib_parser.urlparse(url=url)
        # BusinessLogicUtil.print_as_log(query.scheme)
        # BusinessLogicUtil.print_as_log(query.netloc)
        # BusinessLogicUtil.print_as_log(query.hostname)
        # BusinessLogicUtil.print_as_log(query.port)
        # BusinessLogicUtil.print_as_log(query._replace(fragment="").geturl())
        # BusinessLogicUtil.print_as_log(query)
        # BusinessLogicUtil.print_as_log(query["v"][0])
        if query.hostname == 'youtu.be':
            BusinessLogicUtil.print_as_log(string=rf'''query.path[1:]="{query.path[1:]}" %%%FOO%%%''')
            return query.path[1:]
        if query.hostname in ('www.youtube.com', 'youtube.com'):
            if query.path == '/watch':
                p = urllib_parser.parse_qs(query.query)
                BusinessLogicUtil.print_as_log(string=rf'''p['v'][0]="{p['v'][0]}" %%%FOO%%%''')
                return p['v'][0]
            if query.path[:7] == '/embed/':
                BusinessLogicUtil.print_as_log(string=rf'''query.path.split('/')[2]="{query.path.split('/')[2]}" %%%FOO%%%''')
                return query.path.split('/')[2]
            if query.path[:3] == '/v/':
                BusinessLogicUtil.print_as_log(string=rf'''query.path.split('/')[2]="{query.path.split('/')[2]}" %%%FOO%%%''')
                return query.path.split('/')[2]

    @staticmethod
    def download_clip(url: str):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            if url.strip() == "":
                BusinessLogicUtil.print_red(rf"#다운로드할 url이 아닙니다 #{url}")
                break

            BusinessLogicUtil.print_cyan(f'#다운로드 시도할 URL #{url}')

            # 유튜브 다운로더 업데이트 # 다운로드가 안되면 주석 풀어 시도
            # os.system(rf'{StateManagementUtil.YT_DLP_CMD} -U')

            BusinessLogicUtil.print_cyan(f'#다운로드옵션 파싱시도')
            video_id = ''
            # lines = subprocess.check_output(rf'{StateManagementUtil.YT_DLP_CMD} -F {url}', shell=True).decode('utf-8').split("\n")

            cmd = rf'{StateManagementUtil.YT_DLP_CMD} -F {url}'
            lines = BusinessLogicUtil.command_to_os_like_person_as_admin(command=cmd)
            # 순서는 우선순위에 입각해 설정되었다. 순서를 바꾸어서는 안된다.

            video_ids_allowed = StateManagementUtil.VIDEO_IDS_ALLOWED
            audio_ids_allowed = StateManagementUtil.AUDIO_IDS_ALLOWED
            audio_id = ""
            for line in lines:
                if 'video only' in line or 'audio only' in line:
                    BusinessLogicUtil.print_cyan(line)
                    # video_id 설정
                    for id in video_ids_allowed:
                        if id in line:
                            video_id = id
                            if video_id.strip() == "":
                                BusinessLogicUtil.print_cyan(rf"다운로드 할 수 있는 video_id가 아닙니다 {video_id.strip()}")
                                break
                    # audio_id 설정
                    for id in audio_ids_allowed:
                        if id in line:
                            audio_id = id
                            if audio_id.strip() == "":
                                BusinessLogicUtil.print_cyan(rf"다운로드 할 수 있는 audio_id가 아닙니다 {audio_id.strip()}")
                                break
                            break

            # 다운로드 가능 옵션 ID 설정
            # if video_id not in video_ids and audio_id not in audio_ids:
            #     video_id = str(input('video option:'))
            #     audio_id = str(input('audio option:'))
            #     speak(rf'다운로드옵션이 선택되었습니다')
            #     BusinessLogicUtil.print_as_log(rf'video option: {video_id}  audio option: {audio_id}')
            #     speak(rf'video option: {video_id}  audio option: {audio_id}')
            # else:
            #     pass

            # directories = ["storage"]
            # for directory in directories:
            #     if not os.path.isdir(rf'{os.getcwd()}\{directory}'):
            #         print(rf'storage 디렉토리 생성 중...')
            #         os.makedirs(rf'{directory}')

            # 2023년 12월 12일 (화) 16:02:06
            # 다운로드의 최고 품질이 아닐 수 있다. 그래도
            # 차선책으로 두는 것이 낫겠다
            # cmd = rf'{StateManagementUtil.YT_DLP_CMD} -f best "{url}"'
            # cmd = rf'{StateManagementUtil.YT_DLP_CMD} -f {video_id}+{audio_id} {url}' # 초기에 만든 선택적인 방식
            # cmd = rf'{StateManagementUtil.YT_DLP_CMD} -f "best[ext=webm]" {url}' # 마음에 안드는 결과
            cmd = rf'{StateManagementUtil.YT_DLP_CMD} -f "bestvideo[ext=webm]+bestaudio[ext=webm]" {url}'  # 지금 가장 마음에 드는 방법
            # cmd = rf'{StateManagementUtil.YT_DLP_CMD} -f "bestvideo[ext=webm]+bestaudio[ext=webm]/best[ext=webm]/best" {url}' # 아직 시도하지 않은 방법
            if video_id == "" or audio_id == "" == 1:
                # text = "다운로드를 진행할 수 없습니다\n다운로드용 video_id 와 audio_id를 설정 후\nurl을 다시 붙여넣어 다운로드를 다시 시도하세요\n{url}"
                print("불완전한 다운로드 명령어가 감지되었습니다....")
                BusinessLogicUtil.speak_ment_experimental(ment="불완전한 다운로드 명령어가 감지되었습니다", comma_delay=0.98)
                dialog = UiUtil.CustomQdialog(string=f"에러코드[E004]\n아래의 비디오 아이디를 저장하고 에러코드를 관리자에게 문의해주세요\nvideo id: {url}", btns=["확인"], input_box_mode=True, input_box_text_default=url)
                dialog.exec()
                print(cmd)
                break

            try:
                lines = BusinessLogicUtil.command_to_os_like_person_as_admin(command=cmd)
            except:
                BusinessLogicUtil.print_magenta("except:2024-04-12 1750")
                BusinessLogicUtil.print_magenta(rf'''cmd : {cmd}''')

            PKG_DOWNLOADING = rf'{StateManagementUtil.PKG_DOWNLOADING}'

            if not os.path.exists(PKG_DOWNLOADING):
                os.makedirs(PKG_DOWNLOADING)

            print("다운로드 파일 이동 시도 중...")
            file = ""
            try:
                clip_id = BusinessLogicUtil.parse_youtube_video_id(url)
                if clip_id is None:
                    clip_id = url

                lines = os.listdir()
                for line in lines:
                    if BusinessLogicUtil.is_pattern_in_string(str(line), str(clip_id)):
                        file = line

                src = os.path.abspath(file)
                src_renamed = rf"{PKG_DOWNLOADING}\{os.path.basename(file)}"

                BusinessLogicUtil.print_cyan(f'src_renamed : {src_renamed}')
                if src == os.getcwd():  # 여기 또 os.getcwd() 있는 부분 수정하자..
                    # E001 : 실행불가능한 명령어입력 감지
                    # S001 : 다운로드 가능한 video_id 와 audio_id 를 가용목록에 추가해주세요.
                    dialog = UiUtil.CustomQdialog(string=f"에러코드[E001]\n아래의 비디오 아이디를 저장하고 에러코드를 관리자에게 문의해주세요\nvideo id: {url}", btns=["확인"], input_box_mode=True, input_box_text_default=url)
                    dialog.exec()
                    BusinessLogicUtil.print_cyan("cmd")
                    BusinessLogicUtil.print_cyan(cmd)
                    break
                # shutil.move(src, storage)
                if src != os.getcwd():  # 여기 또 os.getcwd() 있는 부분 수정하자..
                    BusinessLogicUtil.move_pnx_without_overwrite(src, src_renamed)

            except:
                BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
            print(rf'다운로드 결과 확인 중...')
            try:
                src_moved = rf'{PKG_DOWNLOADING}\{file}'
                BusinessLogicUtil.print_cyan(rf'''src_moved : {src_moved}''')

                # 재생할까요? 불필요하면 주석
                # dialog = UiUtil.CustomQdialog(ment="다운로드된 영상을 재생할까요?", btns=["재생하기", "재생하지 않기"], auto_click_negative_btn_after_seconds=10)
                # dialog = UiUtil.CustomQdialog(ment="다운로드된 영상을 재생할까요?", btns=["재생하기", "재생하지 않기"], auto_click_negative_btn_after_seconds=3600)
                # dialog.exec()
                # if dialog.btn_text_clicked == "재생하기":
                #     BusinessLogicUtil.run_pnx_via_explorer_exe(target_pnx=src_moved)

                # 무조건 재생
                BusinessLogicUtil.run_via_explorer_exe(pnx=src_moved)

                # UiUtil.pop_up_as_complete(title="작업성공보고", ment=f"다운로드가 성공되었습니다\n{src_moved}", auto_click_positive_btn_after_seconds=2) # 성공 뜨는게 귀찮아서 주석처리함,

            except Exception:
                BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

            # 다운로드 로깅 처리
            # cmd = f'echo "{url}" >> success_yt_dlp.log'
            # BusinessLogicUtil.run_via_cmd_exe(cmd=cmd)
            break

    @staticmethod
    def download_clip_as_mp4(url: str):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            if url.strip() == "":
                BusinessLogicUtil.print_cyan(rf"if url.strip() == "":")
                break

            BusinessLogicUtil.print_cyan(f'다운로드옵션 파싱시도 #{url}')
            video_id = ''
            cmd = rf'{StateManagementUtil.YT_DLP_CMD} -F {url}'
            lines = BusinessLogicUtil.command_to_os_like_person_as_admin(command=cmd)

            video_ids_allowed = StateManagementUtil.VIDEO_IDS_ALLOWED
            audio_ids_allowed = StateManagementUtil.AUDIO_IDS_ALLOWED
            audio_id = ""
            for line in lines:
                if 'video only' in line or 'audio only' in line:
                    BusinessLogicUtil.print_cyan(f"line: {line}")
                    # video_id 설정
                    for id in video_ids_allowed:
                        if id in line:
                            video_id = id
                            if video_id.strip() == "":
                                BusinessLogicUtil.print_cyan(rf"다운로드 할 수 있는 video_id가 아닙니다 {video_id.strip()}")
                                break
                    # audio_id 설정
                    for id in audio_ids_allowed:
                        if id in line:
                            audio_id = id
                            if audio_id.strip() == "":
                                BusinessLogicUtil.print_cyan(rf"다운로드 할 수 있는 audio_id가 아닙니다 {audio_id.strip()}")
                                break
                            break

            cmd = rf'{StateManagementUtil.YT_DLP_CMD} -f "bestvideo[ext=mp4]+bestaudio[ext=mp4]" {url}'  # ext=mp4 로 처리
            if video_id == "" or audio_id == "" == 1:
                # text = "다운로드를 진행할 수 없습니다\n다운로드용 video_id 와 audio_id를 설정 후\nurl을 다시 붙여넣어 다운로드를 다시 시도하세요\n{url}"
                BusinessLogicUtil.print_cyan("불완전한 다운로드 명령어가 감지되었습니다....")
                BusinessLogicUtil.speak_ment_experimental(ment="불완전한 다운로드 명령어가 감지되었습니다", comma_delay=0.98)
                dialog = UiUtil.CustomQdialog(string=f"에러코드[E004]\n아래의 비디오 아이디를 저장하고 에러코드를 관리자에게 문의해주세요\nvideo id: {url}", btns=["확인"], input_box_mode=True, input_box_text_default=url)
                dialog.exec()
                BusinessLogicUtil.print_cyan(cmd)
                break

            try:
                lines = BusinessLogicUtil.command_to_os_like_person_as_admin(command=cmd)
            except:
                BusinessLogicUtil.print_magenta("except:2024-04-12 1750")
                BusinessLogicUtil.print_magenta(rf'''cmd : {cmd}''')

            PKG_DOWNLOADING = StateManagementUtil.PKG_DOWNLOADING

            if not os.path.exists(PKG_DOWNLOADING):
                os.makedirs(PKG_DOWNLOADING)

            BusinessLogicUtil.print_cyan("다운로드 파일 이동 시도 중...")
            file = ""
            try:
                clip_id = BusinessLogicUtil.parse_youtube_video_id(url)
                if clip_id is None:
                    clip_id = url

                lines = os.listdir()
                for line in lines:
                    if BusinessLogicUtil.is_pattern_in_string(str(line), str(clip_id)):
                        file = line

                src = os.path.abspath(file)
                src_renamed = rf"{PKG_DOWNLOADING}\{os.path.basename(file)}"

                BusinessLogicUtil.print_cyan(f'src_renamed : {src_renamed}')
                if src == os.getcwd():  # 여기 또 os.getcwd() 있는 부분 수정하자..
                    dialog = UiUtil.CustomQdialog(string=f"에러코드[E001]\n아래의 비디오 아이디를 저장하고 에러코드를 관리자에게 문의해주세요\nvideo id: {url}", btns=["확인"], input_box_mode=True, input_box_text_default=url)
                    dialog.exec()
                    BusinessLogicUtil.print_cyan("cmd")
                    BusinessLogicUtil.print_cyan(cmd)
                    break
                if src != os.getcwd():  # 여기 또 os.getcwd() 있는 부분 수정하자..
                    BusinessLogicUtil.move_pnx_without_overwrite(src, src_renamed)

            except:
                BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
            BusinessLogicUtil.print_cyan(rf'다운로드 결과 확인 중...')
            try:
                src_moved = rf'{PKG_DOWNLOADING}\{file}'
                BusinessLogicUtil.print_cyan(rf'''src_moved : {src_moved}''')

                # 무조건 재생
                BusinessLogicUtil.run_via_explorer_exe(pnx=src_moved)

            except Exception:
                BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

            break

    @staticmethod
    def download_from_youtube_to_webm(urls):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            urls = str(urls).strip()
            if urls is None:
                BusinessLogicUtil.speak_ment_experimental(ment="다운로드할 대상 목록에 아무것도 입력되지 않았습니다", comma_delay=0.98)
                break
            if urls == "None":
                BusinessLogicUtil.speak_ment_experimental(ment="다운로드할 대상 목록에 이상한 것이 입력되었습니다", comma_delay=0.98)
                break

            if "\n" in urls:
                urls = urls.split("\n")
            else:
                urls = [urls]

            urls = [x for x in urls if x.strip("\n")]  # 리스트 요소 "" 제거,  from ["", A] to [A]       [""] to []
            UiUtil.pop_up_as_complete(title_="작업중간보고", ment=f"{len(urls)} 개의 url이 입력되었습니다", auto_click_positive_btn_after_seconds=1)

            try:
                urls.append(sys.argv[1])
            except IndexError:
                pass
            except Exception:
                BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
                pass

            # urls 중복제거(ordered way)
            urls_removed_duplicated_element: [str] = []
            for url in urls:
                if url not in urls_removed_duplicated_element:
                    if url is not None:
                        # if url is not "None":
                        urls_removed_duplicated_element.append(url)
            urls = urls_removed_duplicated_element
            BusinessLogicUtil.print_magenta(f'''urls : \n{urls}''')
            BusinessLogicUtil.print_magenta(rf'''type(urls) : {type(urls)}''')
            BusinessLogicUtil.print_magenta(rf'''len(urls) : {len(urls)}''')

            only_clip_id = ''
            for i in urls:
                BusinessLogicUtil.print_cyan(i)
                only_clip_id = i

            if len(urls) == 0:
                UiUtil.pop_up_as_complete(title_="작업성공보고", ment=f"다운로드할 대상이 없습니다", auto_click_positive_btn_after_seconds=5)
                # TtsUtil.speak_ments(ment="다운로드할 대상이 없습니다", sleep_after_play=0.65)
                break

            if len(urls) != 1:
                BusinessLogicUtil.speak_ment_experimental(f"{str(len(urls))}개의 다운로드 대상이 확인되었습니다", comma_delay=0.98)
            for url in urls:
                url = url.strip()  # url에 공백이 있어도 다운로드 가능하도록 설정
                if '&list=' in url:
                    BusinessLogicUtil.print_with_underline(f' clips mode')
                    clips = Playlist(url)  # 이걸로도 parsing 기능 수행 생각 중
                    BusinessLogicUtil.print_cyan(f"predicted clips cnt : {len(clips.video_urls)}")
                    BusinessLogicUtil.speak_ment_experimental(ment=f"{len(clips.video_urls)}개의 다운로드 목록이 확인되었습니다", comma_delay=0.98)
                    # os.system(f'echo "여기서부터 비디오 리스트 시작 {url}" >> success_yt_dlp.log')
                    for clip in clips.video_urls:
                        try:
                            BusinessLogicUtil.download_clip(clip)
                        except Exception:
                            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
                            continue
                    # os.system(f'echo "여기서부터 비디오 리스트 종료 {url}" >> success_yt_dlp.log')
                else:
                    if BusinessLogicUtil.parse_youtube_video_id(url) is not None:
                        BusinessLogicUtil.print_with_underline(f'{StateManagementUtil.UNDERLINE}youtube video id parsing mode')
                        try:
                            BusinessLogicUtil.download_clip(f'https://www.youtube.com/watch?v={BusinessLogicUtil.parse_youtube_video_id(url)}')
                        except Exception:
                            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
                            continue
                    else:
                        BusinessLogicUtil.print_with_underline(f'{StateManagementUtil.UNDERLINE}experimental mode with clip id only')
                        BusinessLogicUtil.download_clip_as_mp4(f'https://www.youtube.com/watch?v={only_clip_id}')
                        try:
                            BusinessLogicUtil.print_cyan(rf'''try:2024-04-12 18:04''')
                            url_parts_useless = [
                                "https://youtu.be/",
                                "https://www.youtube.com/shorts/",
                            ]
                            try:
                                for index, useless_str in enumerate(url_parts_useless):
                                    if useless_str in url:
                                        print(rf'url.split(useless_str)[1] : {url.split(useless_str)[1]}')
                                        BusinessLogicUtil.download_clip(url=url.split(useless_str)[1])
                            except Exception:
                                BusinessLogicUtil.download_clip(url)
                                BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
                        except Exception:
                            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
                        continue
            break

    @staticmethod
    def get_display_setting():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        height = ''
        width = ''
        for monitor_info in get_monitors():
            for info in str(monitor_info).split(','):
                if 'width=' in info.strip():
                    width = info.split('=')[1]
                elif 'height=' in info.strip():
                    height = info.split('=')[1]
        display_setting = {
            'height': int(height),
            'width': int(width)
        }
        return display_setting

    # deprecated method by Park4139
    # def print_police_line(police_line_ment):

    #     police_line = ''
    #     for i in range(0, 255 // len(police_line_ment)):
    #         police_line = police_line + f'{police_line_ment} '
    #     BusinessLogicUtil.print_as_log(f'{police_line.upper()}')

    @staticmethod
    def is_pattern_in_string(string, pattern, show_mode=True, with_case_ignored=True):
        # BusinessLogicUtil.print_as_log(string = rf'''string="{string}" %%%FOO%%%''')
        # BusinessLogicUtil.print_as_log(string = rf'''regex="{regex}" %%%FOO%%%''')
        function_name = inspect.currentframe().f_code.co_name
        if show_mode == True:
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        if with_case_ignored == True:
            pattern = re.compile(pattern, re.IGNORECASE)
        else:
            pattern = re.compile(pattern)
        m = pattern.search(string)
        if m:
            # BusinessLogicUtil.print_as_log("function name   here here here")
            # BusinessLogicUtil.print_as_log(rf"contents: {contents}")
            # BusinessLogicUtil.print_as_log(rf"regex: {regex}")
            # BusinessLogicUtil.print_as_log(rf"True")
            return True
        else:
            # BusinessLogicUtil.print_as_log(rf"contents: {contents}")
            # BusinessLogicUtil.print_as_log(rf"regex: {regex}")
            # BusinessLogicUtil.print_as_log(rf"False")
            return False

    @staticmethod
    # 출력의 결과는 tasklist /svc 와 유사하다.
    def print_python_process_for_killing_zombie_process():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        import psutil  # 실행중인 프로세스 및 시스템 활용 라이브러리
        for process in psutil.process_iter():
            print(rf'str(process.pid) : {str(process.pid)}')
            print(rf'process.status() : {process.status()}')
            print(rf'process.name() : {process.name()}')

    @staticmethod
    def recommand_console_color():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        colors = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        while True:
            try:
                for color_bg in colors:
                    for color_text in colors:
                        if color_bg != color_text:
                            os.system('cls')
                            for setting_key, setting_value in BusinessLogicUtil.get_display_info().items():
                                pass
                                # BusinessLogicUtil.print_as_log(f'setting_key: {setting_key}  ,setting_value: {setting_value}  ')
                            # BusinessLogicUtil.print_as_log(f"color {color_bg}{color_text}")
                            for i in range(0, 32):
                                BusinessLogicUtil.print_cyan('')
                            to_right_nbsp = ''
                            for i in range(0, 150):
                                to_right_nbsp = to_right_nbsp + ' '
                            BusinessLogicUtil.print_cyan(f"{to_right_nbsp}color {color_bg}{color_text}")
                            for i in range(0, 32):
                                BusinessLogicUtil.print_cyan('')
                            os.system(f"color {color_bg}{color_text}")
                            import clipboard
                            clipboard.copy(f'color {color_bg}{color_text}')
                            BusinessLogicUtil.pause()

            except Exception as e:
                BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
                # ctrl c 가 입력이 제대로 되지 않는 현상이 있어 ctrl c 로 콘솔을 종료하는데 불편...이는 어떻게 해결하지? 일단 코드 반응속도는 마음에 드는데...

    @staticmethod
    def make_matrix_console():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        os.system('color 0A')
        os.system('color 02')
        while True:
            lines = subprocess.check_output('dir /b /s /o /a-d', shell=True).decode('utf-8').split("\n")
            for line in lines:
                if "" != line:
                    if os.getcwd() != line:
                        BusinessLogicUtil.print_cyan(lines)
            time.sleep(60)

    @staticmethod
    # 이 메소드를 만들면서 권한을 얻는 여러가지 방법을 stack over flow 를 따라 시도해보았으나 적다한 해결책을 찾지 못함. pyautogui 로 시도 방법은 남아있으나
    # 일단은 regacy 한 방법으로 임시로 해결해두었다.
    def update_global_pkg_alba():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        local_pkg = rf"{StateManagementUtil.PROJECT_DIRECTORY}\pkg_alba"
        global_pkg = rf"C:\Python312\Lib\site-packages\pkg_alba"
        updateignore_txt = rf"{StateManagementUtil.PROJECT_DIRECTORY}\pkg_alba\updateignore.txt"
        try:
            if os.path.exists(global_pkg):
                # 삭제시도
                # shutil.rmtree(global_pkg)

                # 삭제시도
                # for file in os.scandir(global_pkg):
                # os.remove(file.path)

                # 덮어쓰기
                # src= local_pkg
                # dst =os.path.dirname(global_pkg)
                # os.system(f"echo y | copy {src} {dst}")
                # shutil.copytree(local_pkg, os.path.dirname(global_pkg))
                cmd = f'echo y | xcopy "{local_pkg}" "{global_pkg}" /k /e /h /exclude:{updateignore_txt} >nul'
                os.system(cmd)

                # 디버깅
                # Park4139BusinessLogicUtil.pause()
                BusinessLogicUtil.print_cyan(f'{cmd}')
                BusinessLogicUtil.print_cyan(f"{StateManagementUtil.UNDERLINE}")
                return "REPLACED global pkg_alba AS local_pkg"
            else:
                return "pkg_alba NOT FOUND AT GLOBAL LOCATION"

        except Exception as e:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def merge_video_and_sound(file_v_abspath, file_a_abspath):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        BusinessLogicUtil.print_with_underline(f'다운로드 디렉토리 생성')
        directories = ["storage"]
        for directory in directories:
            if not os.path.isdir(rf'./{directory}'):
                os.makedirs(rf'{directory}')

        BusinessLogicUtil.print_with_underline(rf'merge voiceless video and audio only video ')  # yotube 에서 고해상도 음성 없는 영상과 음성을 받아 하나의 영상으로 merge
        dst = StateManagementUtil.STORAGE_VIDEOES_MERGED
        paths = [os.path.abspath(dst), os.path.basename(file_v_abspath)]
        file_va = os.path.join(*paths)
        BusinessLogicUtil.print_cyan(rf'file_v_abspath : {file_v_abspath}')
        BusinessLogicUtil.print_cyan(rf'file_a_abspath : {file_a_abspath}')
        BusinessLogicUtil.print_cyan(rf'file_va : {file_va}')

        BusinessLogicUtil.print_with_underline(f'ffmpeg.exe 위치 설정')
        location_ffmpeg = rf"{StateManagementUtil.USERPROFILE}\Desktop\`workspace\tool\LosslessCut-win-x64\resources\ffmpeg.exe"
        trouble_characters = ['Ä']
        trouble_characters_alternatives = {'Ä': 'A'}
        for trouble_character in trouble_characters:
            file_v_abspath = file_v_abspath.replace(trouble_character, trouble_characters_alternatives[trouble_character])
            file_a_abspath = file_a_abspath.replace(trouble_character, trouble_characters_alternatives[trouble_character])
            file_va = file_va.replace(trouble_character, trouble_characters_alternatives[trouble_character])
            BusinessLogicUtil.print_with_underline(f'파일명 변경 시도')
            try:
                if trouble_character in file_va:
                    os.rename(file_v_abspath,
                              file_v_abspath.replace(trouble_character, trouble_characters_alternatives[trouble_character]))
                    os.rename(file_a_abspath,
                              file_a_abspath.replace(trouble_character, trouble_characters_alternatives[trouble_character]))
            except Exception as e:
                BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

        BusinessLogicUtil.print_with_underline(f' 파일머지 시도')
        try:
            BusinessLogicUtil.print_cyan(rf'echo y | "{location_ffmpeg}" -i "{file_v_abspath}" -i "{file_a_abspath}" -c copy "{file_va}"')
            lines = subprocess.check_output(
                rf'echo y | "{location_ffmpeg}" -i "{file_v_abspath}" -i "{file_a_abspath}" -c copy "{file_va}"', shell=True).decode(
                'utf-8').split("\n")
            for line in lines:
                BusinessLogicUtil.print_cyan(line)
        except Exception as e:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

        BusinessLogicUtil.print_cyan(rf'다운로드 및 merge 결과 확인 시도')
        try:
            BusinessLogicUtil.print_cyan(rf'explorer "{file_va}"')
            subprocess.check_output(rf'explorer "{file_va}"', shell=True).decode('utf-8').split("\n")
        except Exception as e:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

        BusinessLogicUtil.print_with_underline(f' 불필요 리소스 삭제 시도')
        try:
            if os.path.exists(file_va):
                subprocess.check_output(rf'echo y | del /f "{file_v_abspath}"', shell=True).decode('utf-8').split("\n")
                lines = subprocess.check_output(rf'echo y | del /f "{file_a_abspath}"', shell=True).decode('utf-8').split("\n")
                for line in lines:
                    BusinessLogicUtil.print_cyan(line)
        except Exception as e:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    # @staticmethod
    # def elapsed(function):
    #     def wrapper(*args, **kwargs):
    #         import time
    #         time_s = time.time()
    #         function(*args, **kwargs)
    #         time_e = time.time()
    #         mesured_time = time_e - time_s
    #         BusinessLogicUtil.print_as_log(f'측정시간은 {mesured_time} 입니다')
    #         BusinessLogicUtil.print_as_log(f'측정시간은 {mesured_time} 입니다')
    #     return wrapper

    @staticmethod
    def replace_with_auto_no(contents: str, unique_word: str, auto_cnt_starting_no=0):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        """

        input   = "-----1-----1----1------"
        Output  = "-----1-----2----3------"

        input
        --------
        -----1--
        ---1----
        ---1----
        --------
         ouput
        --------
        -----1--
        ---2----
        ---3----
        --------

        """
        tmp = []
        for index, element in enumerate(contents.split(unique_word)):
            if index != len(contents.split(unique_word)) - 1:
                tmp.append(element + str(auto_cnt_starting_no))
                auto_cnt_starting_no = auto_cnt_starting_no + 1
            else:
                tmp.append(element)
        lines_new_as_str = "".join(tmp)
        return lines_new_as_str

    @staticmethod
    def replace_with_auto_no_orderless(contents: str, unique_word: str, auto_cnt_starting_no=0):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # BusinessLogicUtil.print_as_log("항상 필요했던 부분인데 만들었다. 편하게 개발하자. //웹 서비스 형태로 아무때서나 접근이되면 더 좋을 것 같다.  웹 개발툴 을 만들어 보자")
        before = unique_word
        after = 0 + auto_cnt_starting_no
        contents_new = []
        # lines = contents.split("\n")
        lines = contents.strip().split("\n")  # 문제 없긴 했는데,  어떻게 되나 실험해보자 안되면 위의 코드로 주석 스와핑할것.
        for line in lines:
            # BusinessLogicUtil.print_as_log(line)
            # BusinessLogicUtil.print_as_log(before)
            # BusinessLogicUtil.print_as_log(str(after))
            after = after + 1

            line_new = re.sub(str(before), str(after), str(line))
            # BusinessLogicUtil.print_as_log(line_new)
            contents_new.append(line_new)

        # BusinessLogicUtil.print_as_log("str list to str")
        delimiter = "\n"
        contents_new_as_str = delimiter.join(contents_new)
        return contents_new_as_str

    # @staticmethod
    # def move_with_overwrite(src: str, dst: str):
    #     BusinessLogicUtil.print_as_log(f"{inspect.currentframe().f_code.co_name}()")
    #     try:
    #         # 목적지에 있는 중복타겟 삭제
    #         os.remove(dst)
    #     except FileNotFoundError as e:
    #         pass
    #     except Exception:
    #         BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
    #     try:
    #         # 목적지로 타겟 이동
    #         os.rename(src, dst)
    #     except Exception:
    #         BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def raise_error(str: str):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        raise shutil.Error(str)

    @staticmethod
    def upload_pnx_to_git(git_repository_url, commit_msg):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        while True:
            try:
                if not BusinessLogicUtil.does_directory_exist_at_present_directory(directory_name=".git"):
                    BusinessLogicUtil.print_as_log(string=rf''' %%%FOO%%%''', print_color='red')
                    command = rf'git init'
                    BusinessLogicUtil.command_to_os_like_person(command=command)

                command = rf'git status'
                lines = BusinessLogicUtil.command_to_os(cmd=command)
                str_negative = '?????????'
                if str_negative in lines:
                    BusinessLogicUtil.command_to_os_like_person(command=command)

                command = rf'git add .'
                lines = BusinessLogicUtil.command_to_os(cmd=command)
                BusinessLogicUtil.print_list_as_vertical(items_list=lines, items_list_name=rf"{command}")
                # line = BusinessLogicUtil.command_run_via_cmd(command=command, window_title_seg="cmd.exe")
                # BusinessLogicUtil.print_as_log(string = rf'''line="{line}" %%%FOO%%%''')

                command = rf'git commit -m "{commit_msg}"'
                lines = BusinessLogicUtil.command_to_os(cmd=command)
                BusinessLogicUtil.print_list_as_vertical(items_list=lines, items_list_name=rf"{command}")
                # lines = BusinessLogicUtil.command_run_via_cmd(command=command, window_title_seg="cmd.exe")
                # BusinessLogicUtil.print_as_log(string = rf'''line="{line}" %%%FOO%%%''')

                command = rf'git push -u origin main'
                lines = BusinessLogicUtil.command_to_os(cmd=command)
                BusinessLogicUtil.print_as_log(string=rf'''lines="{lines}" %%%FOO%%%''')
                # line = BusinessLogicUtil.command_run_via_cmd(command=command, window_title_seg="cmd.exe")
                # BusinessLogicUtil.print_as_log(string = rf'''line="{line}" %%%FOO%%%''')
                strings_positive = ["Everything up-to-date", "branch 'main' set up to track 'origin/main'."]
                if any(string_positive in lines for string_positive in strings_positive):
                    # 실행
                    # if not BusinessLogicUtil.is_window_open(window_title_seg="Chrome"):
                    # else:
                    command = rf'explorer "{git_repository_url}" '
                    BusinessLogicUtil.command_to_os(cmd=command)
                    BusinessLogicUtil.move_chrome_tab_by_url(url=git_repository_url)
                    BusinessLogicUtil.press("f5")
                    # just now
                    BusinessLogicUtil.print_as_log(f'''"upload success"''', print_color='blue')
                    return
            except:
                BusinessLogicUtil.print_as_log(f'''"upload error"''', print_color='red')
                break

    @staticmethod
    def save_all_drive_pnxs_to_text_file():  # 이 함수는 Everything.exe 를 대체할 파일탐색기 용도로 만들었으나 거의 필요 없을 것 같다. 관심디렉토리만 확인하는 것으로 충분해 보인다.
        """모든 파일 디렉토리에 대한 정보를 텍스트 파일로 저장하는 함수"""
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        # 윈도우냐 아니야에 따라
        # os.system('chcp 65001 >nul')
        # os.system('export LANG=en_US.UTF-8 >nul')

        opening_directory = os.getcwd()
        proper_tree_txt = rf"{StateManagementUtil.PROJECT_DIRECTORY}\pkg_all_tree\proper_tree.txt"
        all_tree_txt = rf"{StateManagementUtil.PROJECT_DIRECTORY}\pkg_all_tree\all_tree.txt"
        if not os.path.exists(os.path.dirname(all_tree_txt)):
            os.makedirs(os.path.dirname(all_tree_txt))
            # os.system(f'echo. >> "{all_tree_txt}"')
            os.system(f'echo. >> "{all_tree_txt}" >nul')
            os.system(f'echo. >> "{proper_tree_txt}" >nul')
        with open(all_tree_txt, 'w', encoding="utf-8") as f:
            f.write(" ")
        with open(proper_tree_txt, 'w', encoding="utf-8") as f:
            f.write(" ")

        drives = "foo"

        file_cnt = 0
        f = open(StateManagementUtil.PROJECT_DIRECTORY + '\\all_list.txt', 'a', encoding="utf-8")  # >>  a    > w   각각 대응됨.
        for drive in drives:
            os.chdir(drive)
            for dirpath, subdirs, files in os.walk(os.getcwd()):  # 여기 또 os.getcwd() 있는 부분 수정하자..
                for file in files:
                    file_cnt = file_cnt + 1
                    f.write(str(file_cnt) + " " + os.path.join(dirpath, file) + "\n")
        f.close()  # close() 를 사용하지 않으려면 with 문을 사용하는 방법도 있다.
        BusinessLogicUtil.print_cyan(f"{StateManagementUtil.UNDERLINE}{StateManagementUtil.UNDERLINE}all_list.txt writing e")
        BusinessLogicUtil.print_cyan(f"{StateManagementUtil.UNDERLINE}{StateManagementUtil.UNDERLINE}all_list_proper.txt rewriting s")
        texts_black = [
            rf"C:\$WinREAgent",
            rf"C:\mingw64",
            rf"C:\PerfLogs",
            rf"C:\Program Files (x86)",
            rf"C:\Program Files",
            rf"C:\ProgramData",
            rf"C:\Temp",
            rf"C:\Users\All Users",
            rf"C:\Windows\servicing",
            rf"C:\Windows\SystemResources",
            rf"C:\Windows\WinSxS",
            rf"C:\Users\Default",
            rf"C:\Users\Public",
            rf"C:\Windows.old",
            rf"C:\Windows",
            rf"C:\$Recycle.Bin",
            rf"D:\$RECYCLE.BIN",
            rf"E:\$RECYCLE.BIN",
            rf"E:\$Recycle.Bin",
            rf"F:\$RECYCLE.BIN",
            rf"{StateManagementUtil.USERPROFILE}\AppData",
        ]
        texts_white = [
            ".mkv",
        ]
        f = open(rf'{StateManagementUtil.PROJECT_DIRECTORY}\all_list.txt', 'r+', encoding="utf-8")
        f2 = open(rf'{StateManagementUtil.PROJECT_DIRECTORY}\all_list_proper.txt', 'a', encoding="utf-8")
        lines_cnt = 0
        while True:
            line = f.readline()
            if not line:
                break
            lines_cnt = lines_cnt + 1
            if any(text_black not in line for text_black in texts_black):
                # BusinessLogicUtil.print_as_log(line)
                if any(text_white in line for text_white in texts_white):
                    # BusinessLogicUtil.print_as_log(line.split("\n")[0] + " o")
                    f2.write(line.split("\n")[0] + " o " + "\n")
                    # BusinessLogicUtil.print_as_log('o')
                    pass
                else:
                    # BusinessLogicUtil.print_as_log(line.split("\n")[0] + " x")
                    # f2.write(line.split("\n")[0] + " x "+"\n")
                    # BusinessLogicUtil.print_as_log('x')
                    pass
        f.close()
        f2.close()
        BusinessLogicUtil.print_cyan(f"{StateManagementUtil.UNDERLINE}{StateManagementUtil.UNDERLINE}all_list_proper.txt rewriting e")

        BusinessLogicUtil.print_cyan(f"{StateManagementUtil.UNDERLINE}{StateManagementUtil.UNDERLINE}files opening s")
        os.chdir(os.getcwd())

        # 윈도우냐 아니냐
        os.system("chcp 65001 >nul")
        os.system('export LANG=en_US.UTF-8 >nul')

        # os.system("type all_list.txt")
        # os.system("explorer all_list.txt")
        os.system("explorer all_list_proper.txt")
        BusinessLogicUtil.print_cyan(f"{StateManagementUtil.UNDERLINE}{StateManagementUtil.UNDERLINE}files opening e")

        # os.system('del "'+os.getcwd()+'\\all_list.txt"')
        # mk("all_list.txt")
        BusinessLogicUtil.print_cyan(f"{StateManagementUtil.UNDERLINE}{StateManagementUtil.UNDERLINE}e")

    @staticmethod
    def get_line_cnt_of_file(target_pnx: str):
        try:
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            line_cnt = 0
            # 파일 변경 감지 이슈: linecache 모듈은 파일의 변경을 감지하지 못합니다.
            # 파일이 변경되었을 때에도 이전에 캐시된 내용을 반환하여 오래된 정보를 사용할 수 있습니다.
            # 실시간으로 파일의 변경을 감지해야 하는 경우에는 정확한 결과를 얻기 어려울 수 있습니다.
            # line_cnt = len(linecache.getlines(target_pnx))
            # BusinessLogicUtil.print_as_log(f'line_cnt:{line_cnt}')  캐시된 내용을 반환하기 때문에. 실시간 정보가 아니다

            # 이 코드는 실시간으로 파일의 변경을 감지 처리 되도록 수정, 단, 파일이 크면 성능저하 이슈 있을 수 있다.
            with open(target_pnx, 'r', encoding="UTF-8") as file:
                # whole_contents = file.readlines()
                # BusinessLogicUtil.print_as_log(whole_contents)
                # line_cnt = len(whole_contents)
                # line_cnt = list(en umerate(file))[-1][0] + 1
                line_cnt = file.read().count("\n") + 1
            return line_cnt
        except FileNotFoundError:
            BusinessLogicUtil.print_cyan("파일을 찾을 수 없었습니다")
            pass
        except Exception:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def back_up_by_manual(target_pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        working_directory = BusinessLogicUtil.get_working_directory()
        target_dirname = os.path.dirname(target_pnx)
        target_dirname_dirname = os.path.dirname(target_dirname)
        try:
            target_basename = os.path.basename(target_pnx).split(".")[0]
            target_zip = rf'$zip_{target_basename}.zip'
            target_yyyy_mm_dd_HH_MM_SS_zip = rf'{target_basename} - {TimeUtil.get_time_as_("%Y %m %d %H %M %S")}.zip'
            # BusinessLogicUtil.print_as_log(rf'# target_dirname_dirname 로 이동')
            os.chdir(target_dirname_dirname)
            # BusinessLogicUtil.print_as_log(rf'부모디렉토리로 백업')
            cmd = f'bandizip.exe c "{target_zip}" "{target_pnx}"'
            BusinessLogicUtil.command_to_os_like_person_as_admin(cmd)
            # BusinessLogicUtil.print_as_log(rf'이름변경')
            cmd = f'ren "{target_zip}" "{target_yyyy_mm_dd_HH_MM_SS_zip}"'
            BusinessLogicUtil.command_to_os_like_person_as_admin(cmd)
            # BusinessLogicUtil.print_as_log(rf'부모디렉토리에서 백업될 디렉토리로 이동')
            cmd = f'move "{target_yyyy_mm_dd_HH_MM_SS_zip}" "{target_dirname}"'
            BusinessLogicUtil.command_to_os_like_person_as_admin(cmd)
            # BusinessLogicUtil.print_as_log(rf'백업될 디렉토리로 이동')
            # os.chdir(target_dirname)
            os.chdir(working_directory)
            # BusinessLogicUtil.print_as_log("os.getcwd()")
            # BusinessLogicUtil.print_as_log(os.getcwd())

        except:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
        finally:
            BusinessLogicUtil.print_with_underline(rf'프로젝트 디렉토리로 이동')
            os.chdir(working_directory)

    @staticmethod
    def move_mouse(x_abs: float, y_abs: float, duration=1):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        pyautogui.moveTo(x_abs, y_abs, duration)

    @staticmethod
    def move_mouse_rel_x(x_rel: float, y_rel: float):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        pyautogui.move(x_rel, y_rel)

    @staticmethod
    def get_current_mouse_abs_info():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        coordination = pyautogui.position()
        coordination = str(coordination)
        coordination = coordination.replace("Point(x=", "")
        coordination = coordination.replace("y=", "")
        coordination = coordination.replace(")", "")
        coordination = coordination.replace(" ", "")
        x = coordination.split(",")[0]
        y = coordination.split(",")[1]
        return x, y

    @staticmethod
    def print_current_mouse_abs_info():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        x, y = BusinessLogicUtil.get_current_mouse_abs_info()
        BusinessLogicUtil.print_as_log(f'''x = "{x}"''')
        BusinessLogicUtil.print_as_log(f'''y = "{y}"''')
        BusinessLogicUtil.pause()

    @staticmethod
    def open_mouse_info():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # pyautogui.mouseInfo()

    @staticmethod
    def press(*presses: str, interval=0.0, show_mode=True):
        function_name = inspect.currentframe().f_code.co_name
        if show_mode == True:
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            key = None
            if len(presses) == 1:
                if presses == "pgup":
                    presses = "pageup"
                elif presses == "pgdn":
                    presses = "pagedown"
                for i in pyautogui.KEYBOARD_KEYS:
                    if str(i) == str(presses[0]):
                        pyautogui.press(str(presses[0]), interval=interval)
                        if show_mode == True:
                            BusinessLogicUtil.print_as_log(string = rf'''str(i)="{str(i)}" %%%FOO%%%''',print_color='blue')
                        break
                    else:
                        pass
            else:
                pyautogui.hotkey(*presses, interval=interval)
                tmp = ' + '.join(i for i in presses)
                if show_mode == True:
                    BusinessLogicUtil.print_as_log(string = rf'''tmp="{tmp}" %%%FOO%%%''', print_color='blue')
            # BusinessLogicUtil.sleep(milliseconds=100)
            break

    # @staticmethod
    # def get_400px_screenshot(miliseconds=0):

    #     """pyautogui, 마우스의 위치 주변 가로 세로 400 px  400 px 로 스크린샷 찍어서 저장하는 코드"""
    #     # 재우기
    #     BusinessLogicUtil.sleep(milliseconds=miliseconds)
    #
    #     # 현재 마우스 위치 가져오기
    #     x, y = pyautogui.position()
    #     width = 400
    #     height = 400
    #     left = x - width / 2  # height/2 일수도 있음
    #     top = y - height / 2  # 여기도 마찬가지 일수 있음
    #
    #     # 스크린샷 찍기
    #     pygui = pyautogui.screenshot(region=(left, top, width, height))
    #
    #     # 스크린샷 저장
    #     server_time = BusinessLogicUtil.get_time_as_('%Y_%m_%d_%H_%M_%S')
    #     screenshot_png = rf'{BusinessLogicUtil.PROJECT_DIRECTORY}\pkg_png\screenshot_{server_time}.png'
    #     try:
    #         os.makedirs(os.path.dirname(screenshot_png))
    #     except FileExistsError:
    #         pass
    #     pygui.save(screenshot_png)
    #     pygui.show(screenshot_png)

    @staticmethod
    def collect_img_for_autogui():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        server_time = TimeUtil.get_time_as_('%Y_%m_%d_%H_%M_%S')
        function_name_server_time_png = rf'{StateManagementUtil.PKG_PNG}\{function_name}_{server_time}.png'
        file_pnx = function_name_server_time_png
        file_p = BusinessLogicUtil.get_p(function_name_server_time_png)
        file_nx = BusinessLogicUtil.get_nx(function_name_server_time_png)
        BusinessLogicUtil.make_pnx(file_p, mode="d")
        try:
            BusinessLogicUtil.press("win", "shift", "s", interval=0.5)
            key = "ctrl+s"
            if not BusinessLogicUtil.is_keyboard_pressed_within_timeout(key_plus_key=key, timeout=60):
                raise BusinessLogicError(rf"[실패] 클릭감지타임아웃 {key}")
            BusinessLogicUtil.sleep(milliseconds=500)
            BusinessLogicUtil.sleep(milliseconds=500)
            BusinessLogicUtil.press("ctrl", "l", interval=0.5)
            BusinessLogicUtil.sleep(milliseconds=300)
            BusinessLogicUtil.copy_str_to_clipboard(string=file_p)
            BusinessLogicUtil.sleep(milliseconds=300)
            BusinessLogicUtil.press("enter")
            BusinessLogicUtil.sleep(milliseconds=300)
            BusinessLogicUtil.print_as_gui(ment="클립보드에 추천파일명을 저장해두었습니다")
            key = "left"
            if not BusinessLogicUtil.is_mouse_button_click_within_timeout(key="left", timeout=60):
                ment_error = rf"[실패] 클릭감지타임아웃 {key}"
                raise BusinessLogicError(ment_error)
            BusinessLogicUtil.write_fast(file_nx)
            BusinessLogicUtil.sleep(milliseconds=300)
            # BusinessLogicUtil.press("enter")
            BusinessLogicUtil.sleep(milliseconds=300)
            if BusinessLogicUtil.does_pnx_exist(src=file_pnx):
                command = rf"taskkill -im ScreenSketch.exe"
            BusinessLogicUtil.run_via_explorer_exe(pnx=file_p)
        except:
            traceback.print_exc(file=sys.stdout)

    @staticmethod
    def write_fast(string: str):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.sleep(milliseconds=500)
        BusinessLogicUtil.copy_and_paste_with_keeping_clipboard(string)
        BusinessLogicUtil.print_cyan(rf"{str(string)}")

    @staticmethod
    def write_like_person(string: str, interval=0.04):  # interval 낮을 수록 빠름 # cmd.exe 를 admin 으로 열면 클립보드가 막혀있음.
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        pyautogui.write(string, interval=interval)  # 한글 미지원.
        BusinessLogicUtil.print_cyan(rf"{str(string)}")

    @staticmethod
    def write(string: str, milliseconds=500):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.sleep(milliseconds=milliseconds)
        BusinessLogicUtil.copy_and_paste_with_keeping_clipboard(string)
        BusinessLogicUtil.print_cyan(rf"{str(string)}")

    @staticmethod
    def ask_to_wrtn(question: str):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            # 페이지 열기
            url = "https://wrtn.ai/"
            cmd = f'explorer  "{url}"  >nul'
            BusinessLogicUtil.command_to_os_like_person_as_admin(cmd)

            # 크롬 창 활성화
            target_pid: int = BusinessLogicUtil.get_pids_by_process_name(process_name="chrome.exe")  # chrome.exe pid 가져오기
            BusinessLogicUtil.move_window_to_front_by_pid(pid=target_pid)

            # 크롬 기본 배율로 변경
            BusinessLogicUtil.press('ctrl', '0')

            # 광고닫기 버튼 클릭
            file_png = rf"{StateManagementUtil.PROJECT_DIRECTORY}\pkg_png\ask_to_wrtn_ad_close.png"
            BusinessLogicUtil.click_center_of_img_recognized_by_mouse_left(img_pnx=file_png, loop_limit_cnt=10, is_zoom_toogle_mode=True)

            # 프롬프트 콘솔 클릭(광고 없어도 진행)
            file_png = rf"{StateManagementUtil.PROJECT_DIRECTORY}\pkg_png\ask_to_wrtn.png"
            if BusinessLogicUtil.click_center_of_img_recognized_by_mouse_left(img_pnx=file_png, loop_limit_cnt=50, is_zoom_toogle_mode=True):
                # 질문 작성 및 확인
                BusinessLogicUtil.write_fast(question)
                BusinessLogicUtil.press('enter')

            # 뤼튼 프롬프트 콘솔 최하단 이동 버튼 클릭
            break

    @staticmethod
    def find_direction_via_naver_map(destination: str):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            # 배경화면으로 나가기(옵션로직)
            # BusinessLogicUtil.press("win", "m")
            # BusinessLogicUtil.press("win", "m")
            # BusinessLogicUtil.sleep(10)

            # 페이지 열기
            # url = "https://map.naver.com/"
            url = "https://map.naver.com/p/directions"
            cmd = f'explorer  "{url}"  >nul'
            BusinessLogicUtil.command_to_os_like_person_as_admin(cmd)
            BusinessLogicUtil.sleep(300)

            # 크롬 창 활성화
            target_pid: int = BusinessLogicUtil.get_pids_by_process_name(process_name="chrome.exe")  # chrome.exe pid 가져오기
            BusinessLogicUtil.move_window_to_front_by_pid(pid=target_pid)
            BusinessLogicUtil.sleep(30)

            # 반쪽화면 생성(옵션로직)
            # BusinessLogicUtil.press("alt", "up")
            # BusinessLogicUtil.press("alt", "left")

            # 출발지 입력 클릭
            file_png = rf"{StateManagementUtil.PROJECT_DIRECTORY}\pkg_png\find_direction_via_naver_direction.png"
            BusinessLogicUtil.click_center_of_img_recognized_by_mouse_left(img_pnx=file_png, loop_limit_cnt=100, is_zoom_toogle_mode=True)
            BusinessLogicUtil.sleep(30)

            # 한가람한양아파트상가 입력
            BusinessLogicUtil.write_fast("한가람한양아파트상가")
            BusinessLogicUtil.sleep(30)
            BusinessLogicUtil.press('enter')
            BusinessLogicUtil.sleep(300)
            BusinessLogicUtil.press('tab')
            BusinessLogicUtil.sleep(30)

            # 목적지 입력
            BusinessLogicUtil.write_fast(destination)
            BusinessLogicUtil.sleep(30)
            BusinessLogicUtil.press('down')
            BusinessLogicUtil.press('enter')

            # 길찾기 클릭
            BusinessLogicUtil.press('tab')
            BusinessLogicUtil.press('tab')
            BusinessLogicUtil.press('tab')
            BusinessLogicUtil.press('enter')

            # 작업마침 알림
            BusinessLogicUtil.speak_ment_experimental(ment='길찾기가 시도되었습니다', comma_delay=0.98)
            break

    @staticmethod
    def download_torrent_files_from_web_via_user_input(btn_text_clicked):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        browser_show_mode = False
        try:
            while 1:
                # answer = "tate no"
                BusinessLogicUtil.print_as_gui(f"{btn_text_clicked} 입력되었습니다")
                BusinessLogicUtil.print_cyan(btn_text_clicked)
                special_prefixes = " ".join(["subsplease", "1080"]) + " "
                # special_prefixes = " ".join(["", "1080"]) + " "
                query = urllib.parse.quote(f"{special_prefixes}{btn_text_clicked}")
                if query == "":
                    BusinessLogicUtil.speak_ment_experimental(ment="아무것도 입력되지 않았습니다", comma_delay=0.98)
                    break
                # url = f'https://nyaa.si/?f=0&c=0_0&q={query}&p=1'
                url = f'https://nyaa.si/?f=0&c=0_0&q={query}'
                BusinessLogicUtil.print_cyan(url)

                driver = BusinessLogicUtil.get_driver_selenium(browser_show_mode=browser_show_mode)
                driver.get(url)
                BusinessLogicUtil.print_with_underline("모든 웹소스 우회 설정 확인")
                # setting_for_proxy = ""
                # setting_for_proxy = setting_for_proxy  + f"user_agent     : {driver.find_element(By.CSS_SELECTOR,'#user-agent').text}\n"
                # setting_for_proxy = setting_for_proxy  + f"plugins_length : {driver.find_element(By.CSS_SELECTOR,  '#plugins-length').text}\n"
                # setting_for_proxy = setting_for_proxy  + f"languages : {driver.find_element(By.CSS_SELECTOR, '#languages').text}\n"
                # setting_for_proxy = setting_for_proxy  + f"webgl_vendor : {driver.find_element(By.CSS_SELECTOR, '#webgl-vendor').text}\n"
                # setting_for_proxy = setting_for_proxy  + f"webgl_renderer : {driver.find_element(By.CSS_SELECTOR, '#webgl-renderer').text}\n"
                # BusinessLogicUtil.debug_as_gui(context=setting_for_proxy, is_app_instance_mode=False)

                # 필요할까?
                # driver.implicitly_wait(2)
                # driver.implicitly_wait(3)
                # driver.get_screenshot_as_file('hlah.png')

                BusinessLogicUtil.print_with_underline("페이지 소스 RAW")
                page_src = driver.page_source
                BusinessLogicUtil.print_cyan(page_src)
                # BusinessLogicUtil.debug_as_gui(context=f"\n{page_src}")
                # BusinessLogicUtil.debug_as_gui(context=f"페이지 소스 RAW:\n\n{page_src}")

                BusinessLogicUtil.print_with_underline("web parser 설정")
                # soup = BeautifulSoup(page_src, "html5lib")
                # soup = BeautifulSoup(page_src, "lxml") # 속도가 빠른 파서로 알려짐 ,     ....2024 06 29 애니 크롤링 기능 사용, 파서 인식 안되는 문제 인식...lxml 모듈 재설치해도 인식 못함.
                soup = BeautifulSoup(page_src, "html.parser")  # 파이썬 기본 파서, lxml 인식 불가로 lxml에서 html.parser 로 대체됨

                BusinessLogicUtil.print_with_underline("web src 분석시작")
                # title 가져오기
                # num = 0  # num 초기값
                # BusinessLogicUtil.print_as_log(soup.get_text())
                for i in soup.find_all(name="a"):
                    BusinessLogicUtil.print_cyan(i)

                results = []
                BusinessLogicUtil.print_with_underline("web src 분석시작2")
                lines = soup.find_all(name="a")
                for line in lines:
                    results.append(line.get('title'))
                    results.append(line.get('href'))
                    BusinessLogicUtil.print_cyan(line)
                    # pass
                BusinessLogicUtil.print_with_underline("titles")
                titles = []
                for i in results:
                    if type(i) is str:
                        if BusinessLogicUtil.is_pattern_in_string(string=str(i).strip(), pattern=btn_text_clicked):
                            if not BusinessLogicUtil.is_pattern_in_string(string=str(i).strip(), pattern="&q="):
                                if not BusinessLogicUtil.is_pattern_in_string(string=str(i).strip(), pattern="xt="):
                                    BusinessLogicUtil.print_cyan(f'{type(i)} : {i}')
                                    titles.append(i)
                BusinessLogicUtil.print_with_underline("magnets")
                magnets = []
                for i in results:
                    if type(i) is str:
                        if BusinessLogicUtil.is_pattern_in_string(string=i, pattern="magnet*", with_case_ignored=False):
                            BusinessLogicUtil.print_cyan(f'{type(i)} : {i}')
                            magnets.append(i)
                BusinessLogicUtil.print_with_underline("finally crawled result")
                for i in results:
                    if type(i) is str:
                        if BusinessLogicUtil.is_pattern_in_string(string=i, pattern="magnet*", with_case_ignored=False):
                            BusinessLogicUtil.print_cyan(f'{type(i)} : {i}')
                        if BusinessLogicUtil.is_pattern_in_string(string=str(i).strip(), pattern=btn_text_clicked):
                            if not BusinessLogicUtil.is_pattern_in_string(string=str(i).strip(), pattern="&q="):
                                if not BusinessLogicUtil.is_pattern_in_string(string=str(i).strip(), pattern="xt="):
                                    BusinessLogicUtil.print_cyan(f'{type(i)} : {i}')
                results_about_titles_and_magnets = ""
                if len(magnets) == len(titles):
                    for i in range(0, len(magnets)):
                        BusinessLogicUtil.print_cyan(f"{i}   :    {titles[i]}    :     {magnets[i]}")
                        results_about_titles_and_magnets = results_about_titles_and_magnets + f"{i}   :    {titles[i]}    :     {magnets[i]}\n"
                # dialog = CustomDialog(contents="웹 크롤링 결과를 화면에 시현할까요?", buttons=["시현하기", "시현하지 않기"])
                # dialog.exec()
                # btn_text_clicked = dialog.btn_text_clicked
                # BusinessLogicUtil.print_as_log(btn_text_clicked)
                # if btn_text_clicked == "시현하기":
                dialog = UiUtil.CustomQdialog(string=results_about_titles_and_magnets, btns=["확인"])
                dialog.exec()
                btn_text_clicked = dialog.btn_text_clicked
                BusinessLogicUtil.print_cyan(btn_text_clicked)
                if btn_text_clicked == "확인":
                    pass
                if len(magnets) == len(titles):
                    for i in range(0, len(magnets) - 1):
                        BusinessLogicUtil.print_cyan(f"{i}   :    {titles[i]}    :     {magnets[i]}")
                else:
                    ment = "크롤링 결과가 이상합니다\n크롤링한 마그넷주소의 개수와 타이틀의 개수가 일치하지 않습니다\n크롤링을 계속할까요"
                    BusinessLogicUtil.speak_ment_experimental(ment.replace("\n", " "), comma_delay=0.98)
                    dialog = UiUtil.CustomQdialog(string=ment, btns=["계속하기", "계속하지 않기"])
                    dialog.exec()
                    btn_text_clicked = dialog.btn_text_clicked
                    BusinessLogicUtil.print_cyan(btn_text_clicked)
                    if btn_text_clicked == "계속하지 않기":
                        BusinessLogicUtil.speak_ment_experimental(ment="네 계속하지 않겠습니다", comma_delay=0.98)
                        break

                while True:
                    ment = '토렌트에 추가하고 싶은 항목의 숫자인덱스를 입력하세요.\n전부를 원하시면 별(*)을 입력해주세요'
                    BusinessLogicUtil.speak_ment_experimental(ment=ment, comma_delay=0.98)
                    dialog = UiUtil.CustomQdialog(string=ment, btns=["계속하기", "그만하기", "크롤링 결과 다시보기"], input_box_mode=True, input_box_text_default="*")
                    dialog.exec()
                    btn_text_clicked = dialog.btn_text_clicked
                    text_of_from_input_box = str(dialog.input_box.text()).strip()
                    BusinessLogicUtil.print_cyan(f"text_of_input_box : {text_of_from_input_box}")
                    BusinessLogicUtil.print_cyan(f"btn_text_clicked : {btn_text_clicked}")
                    if btn_text_clicked == "그만하기":
                        BusinessLogicUtil.speak_ment_experimental(ment="네 그만하겠습니다", comma_delay=0.98)
                        break
                    elif btn_text_clicked == "크롤링 결과 다시보기":
                        dialog = UiUtil.CustomQdialog(string=results_about_titles_and_magnets, btns=["확인"])
                        dialog.exec()
                    elif btn_text_clicked == "계속하기":
                        if text_of_from_input_box.isdigit():
                            mg_num = int(text_of_from_input_box)
                            try:
                                if magnets[int(mg_num)]:
                                    BusinessLogicUtil.print_cyan(f"{StateManagementUtil.UNDERLINE}다운로드 가능한 범위의 숫자인덱스입니다")
                            except IndexError:
                                BusinessLogicUtil.speak_ment_experimental(ment="다운로드 가능한 범위의 숫자인덱스가 아닙니다", comma_delay=0.98)
                            ment = f"1건에 대한 마그넷 추가를 진행할까요?\n"  # 단건 마그넷 추가 진행
                            ment = ment + f"\n"
                            ment = ment + f"index  : {int(mg_num)}\n"
                            ment = ment + f"title  : {titles[int(mg_num)]}\n"
                            ment = ment + f"magnet : {magnets[int(mg_num)][0:30]} ...\n"
                            for i in range(0, 4):
                                ment = ment + f"\n"
                            dialog = UiUtil.CustomQdialog(string=ment, btns=["계속하기", "그만하기"])
                            dialog.exec()
                            btn_text_clicked = dialog.btn_text_clicked
                            if btn_text_clicked == "그만하기":
                                BusinessLogicUtil.speak_ment_experimental(ment="네 그만하겠습니다", comma_delay=0.98)
                                break
                            webbrowser.open(magnets[int(mg_num)])  # 토렌트 추가
                            break
                        elif text_of_from_input_box.strip() == "*":
                            ment = f"{len(magnets)}건에 대한 마그넷 추가를 진행할까요?\n"  # 복수 마그넷 추가 진행
                            for i in range(0, 4):
                                ment = ment + f"\n"
                            dialog = UiUtil.CustomQdialog(string=ment, btns=["계속하기", "그만하기"])
                            dialog.exec()
                            btn_text_clicked = dialog.btn_text_clicked
                            if btn_text_clicked == "그만하기":
                                BusinessLogicUtil.speak_ment_experimental(ment="네 그만하겠습니다", comma_delay=0.98)
                                break
                            for i in range(0, len(magnets)):
                                # BusinessLogicUtil.sleep(milliseconds=random.randint(20, 40))
                                BusinessLogicUtil.sleep(milliseconds=random.randint(10, 20))
                                # BusinessLogicUtil.sleep(milliseconds=random.randint(1,3))
                                BusinessLogicUtil.print_cyan(f"{i}  : title  {titles[i]}")
                                BusinessLogicUtil.print_cyan(f"{i}  : magnet {magnets[i]}")
                                webbrowser.open(magnets[i])  # 토렌트 추가
                            break
                        else:
                            BusinessLogicUtil.speak_ment_experimental(ment="입력하신 내용이 숫자나 별이 아닌 것 같아요", comma_delay=0.98)
                    print("break2")
                    break
                break
        except:
            traceback.print_exc(file=sys.stdout)



    @staticmethod  # move_target_recycle_bin()
    def empty_recycle_bin():  # done
        function_name = inspect.currentframe().f_code.co_name

        # logging
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.command_to_os_like_person_as_admin(rf'echo y | del C:\Users\WIN10PROPC3\AppData\Roaming\Microsoft\Windows\Recent')
        BusinessLogicUtil.command_to_os_like_person_as_admin('PowerShell.exe -NoProfile -Command Clear-RecycleBin -Confirm:$false')
        # 휴지통 삭제 (외장하드까지)
        # for %%a in (cdefghijk L mnopqrstuvwxyz) do (
        # 존재하는 경우 %%a:\$RECYCLE.BIN for /f "tokens=* usebackq" %%b in (`"dir /a:d/b %%a:\$RECYCLE.BIN\"`) do rd / q/s "%%a:\$RECYCLE.BIN\%%~b"
        # 존재하는 경우 %%a:\RECYCLER for /f "tokens=* usebackq" %%b in (`"dir /a:d/b %%a:\RECYCLER\"`) do rd /q/s "%% a:\RECYCLER\%%~b"
        # )

        # 가끔 휴지통을 열어볼까요?
        # BusinessLogicUtil.print_as_log("숨김 휴지통 열기")
        # cmd = 'explorer c:\$RECYCLE.BIN'
        # BusinessLogicUtil.run_via_cmd_exe(cmd=cmd)
        # 외장하드 숨김 휴지통 을 보여드릴까요
        # explorer c:\$RECYCLE.BIN
        # explorer d:\$RECYCLE.BIN
        # explorer e:\$RECYCLE.BIN
        # explorer f:\$RECYCLE.BIN

        # BusinessLogicUtil.speak_ment_experimental(f'휴지통을 비웠습니다', comma_delay=0.98, thread_join_mode=True)
        BusinessLogicUtil.print_as_log(f'''"휴지통을 비웠습니다"''')

    @staticmethod
    def print_as_gui(ment: str, input_text_default="", auto_click_positive_btn_after_seconds=3, btns=["확인"]):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        """
        이 함수는 특별한 사용요구사항이 있습니다
        pyside6 앱 내에서 해당 함수를 호출할때는 is_app_instance_mode 를 파라미터에 넣지 않고 쓰는 것을 default 로 디자인했습니다.
        pyside6 앱 밖에서 해당 함수를 호출할때는 is_app_instance_mode 를 True 로 설정하고 쓰십시오.

        사용 요구사항이 생기게 된 이유는 다음과 같습니다
        pyside6 는 app을 singletone으로 instance를 구현합니다. 즉, instance는 반드시 pyside6 app 내에서 하나여야 합니다.
        pyside6의 QApplication()이 앱 내/외에서도 호출이 될 수 있도록 디자인했습니다.
        앱 내에서 호출 시에는 is_app_instance_mode 파라미터를 따로 설정하지 않아도 되도록 디자인되어 있습니다.
        앱 외에서 호출 시에는 is_app_instance_mode 파라미터를 True 로 설정해야 동작하도록 디자인되어 있습니다.
        """
        # app_foo: QApplication = None
        # if is_app_instance_mode == True:
        #     app_foo: QApplication = QApplication()
        # if input_text_default == "":
        #     BusinessLogicUtil.print_as_log(f"{inspect.currentframe().f_code.co_name}()")
        #     is_input_text_box = False
        # else:
        #     is_input_text_box = True
        # dialog = UiUtil.CustomQdialog(ment=f"{context}", buttons=["확인"], is_input_box=is_input_text_box, input_box_text_default=input_text_default)
        # BusinessLogicUtil.print_as_log(f"{inspect.currentframe().f_code.co_name}()")
        # dialog.exec()
        # btn_text_clicked = dialog.btn_text_clicked
        # if btn_text_clicked == "":
        #     BusinessLogicUtil.print_ment_magenta()(f'누르신 버튼은 {btn_text_clicked} 입니다')
        # if is_app_instance_mode == True:
        #     if isinstance(app_foo, QApplication):
        #         app_foo.exec()
        # if is_app_instance_mode == True:
        #     # app_foo.quit()# QApplication 인스턴스 제거시도 : fail
        #     # app_foo.deleteLater()# QApplication 인스턴스 파괴시도 : fail
        #     # del app_foo # QApplication 인스턴스 파괴시도 : fail
        #     # app_foo = None # QApplication 인스턴스 파괴시도 : fail
        #     app_foo.shutdown()  # QApplication 인스턴스 파괴시도 : success  # 성공요인은 app.shutdown()이 호출이 되면서 메모리를 해제까지 수행해주기 때문
        #     # sys.exit()
        # # return app_foo
        try:
            return UiUtil.pop_up_as_complete(title_="디버깅결과보고", ment=ment, input_text_default=input_text_default, auto_click_positive_btn_after_seconds=auto_click_positive_btn_after_seconds, btns=btns)
        except:
            BusinessLogicUtil.print_red(traceback.print_exc())
            return None

    # @staticmethod
    # def print_as_log(string: str, is_app_instance_mode=False, input_text_default="", auto_click_positive_btn_after_seconds=3):
    #     BusinessLogicUtil.print_light_black(string)
    #     # BusinessLogicUtil.print_as_gui(ment, auto_click_positive_btn_after_seconds=1)
    #     # BusinessLogicUtil.print_as_gui(ment, auto_click_positive_btn_after_seconds=0)
    #     # BusinessLogicUtil.sleep(milliseconds=500)
    #     # BusinessLogicUtil.sleep(milliseconds=400)
    #     # BusinessLogicUtil.sleep(milliseconds=350)
    #     # BusinessLogicUtil.sleep(milliseconds=300)



    @staticmethod
    def click_mouse_left_btn(x_abs=None, y_abs=None, doubleclick_mode=False):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        if doubleclick_mode == True:
            clicks = 2
        else:
            clicks = 1
        if x_abs and y_abs:
            pyautogui.click(button='left', clicks=clicks, interval=0, x=x_abs, y=y_abs)
        else:
            pyautogui.click(button='left', clicks=clicks, interval=0)

    @staticmethod
    def click_mouse_right_btn(abs_x=None, abs_y=None):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        if abs_x and abs_y:
            pyautogui.click(button='right', clicks=1, interval=0)
        else:
            pyautogui.click(button='right', clicks=1, interval=0, x=abs_x, y=abs_y, )

    @staticmethod
    def ask_to_bard(question: str):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            cmd = f"explorer https://bard.google.com/chat  >nul"
            BusinessLogicUtil.command_to_os_like_person_as_admin(cmd)

            # 이시간은 web rendering time 대기 해주는 시간정도로 생각하고 있는데
            # 시간 성능에 대한 마지노선을 설정하는게 여간 편차가 크다.
            # web 크롤링 을 한뒤 연산하는게 훨씬 빠르겠다.
            # BusinessLogicUtil.sleep(milliseconds=3000) # 전부 성공
            # BusinessLogicUtil.sleep(milliseconds=1500) #
            BusinessLogicUtil.sleep(milliseconds=1060)
            # BusinessLogicUtil.sleep(milliseconds=1030)  # 실패있음
            # BusinessLogicUtil.sleep(milliseconds=1000)  #실패있음. 질문입력 안됨
            # BusinessLogicUtil.sleep(milliseconds=500)

            # 질문 작성 및 확인
            BusinessLogicUtil.write_fast(question)
            BusinessLogicUtil.sleep(milliseconds=30)
            BusinessLogicUtil.press('enter')
            break

    @staticmethod
    def ask_to_google(question: str):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            question_ = question.replace(" ", "+")
            cmd = f'explorer "https://www.google.com/search?q={question_}"  >nul'
            BusinessLogicUtil.command_to_os_like_person_as_admin(cmd)
            break

    @staticmethod
    def get_img_when_img_recognized_succeed(img_abspath, recognize_loop_limit_cnt=0, is_zoom_toogle_mode=False):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # BusinessLogicUtil.speak("화면 이미지 분석을 시도합니다")
        UiUtil.pop_up_as_complete(title_="화면이미지분석 시도 전 보고", ment="화면 이미지 분석을 시도합니다", auto_click_positive_btn_after_seconds=1)

        BusinessLogicUtil.press('ctrl', '0', interval=0.15)  # 이미지 분석 시 크롬 zoom 초기화(ctrl+0)

        # 고해상도/다크모드 에서 시도
        for i in range(0, 9):
            BusinessLogicUtil.press('ctrl', '+')

        chrome_zoom_step = 0

        # 루프카운트 제한 n번 default 0번 으로 설정
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        loop_cnt = 0
        # recognize_loop_limit_cnt = recognize_loop_limit_cnt
        if recognize_loop_limit_cnt == 0:
            while True:
                # 인식률 및 속도 개선 시도
                # pip install opencv-python # 이것은 고급 기능이 포함되지 않은 Python용 OpenCV의 미니 버전입니다. 우리의 목적에는 충분합니다.
                # confidence=0.7(70%)유사도를 낮춰 인식률개선시도, region 낮춰 속도개선시도, grayscale 흑백으로 판단해서 속도개선시도,
                # open cv 설치했는데 적용안되고 있음. 재부팅도 하였는 데도 안됨.
                # pycharm 에서 import 하는 부분에서 cv2 설치 시도 중에 옵션으로 opencv-python 이 있길래 설치했더니 결국 됨. 혹쉬 경로 설정 필요했나?
                # xy_infos_of_imgs = pyautogui.locateOnScreen(img_abspath, confidence=0.7, grayscale=True)
                # BusinessLogicUtil.debug_as_gui(xy_infos_of_imgs is None)
                BusinessLogicUtil.print_with_underline("화면 이미지 인식 시도 중...")
                loop_cnt = loop_cnt + 1
                try:
                    img = pyautogui.locateOnScreen(img_abspath, confidence=0.7, grayscale=True)
                    BusinessLogicUtil.print_cyan(type(img))
                    BusinessLogicUtil.print_cyan(img)
                    BusinessLogicUtil.print_cyan(img is not None)
                    if img is not None:
                        return img
                    else:
                        BusinessLogicUtil.print_with_underline(f"화면 이미지 분석 중...")
                        BusinessLogicUtil.print_cyan(img_abspath)
                        BusinessLogicUtil.sleep(milliseconds=15, show_mode=False)
                        if is_zoom_toogle_mode == True:
                            if chrome_zoom_step == 14:
                                chrome_zoom_step = 0
                            elif chrome_zoom_step < 7:
                                BusinessLogicUtil.press('ctrl', '-')
                                chrome_zoom_step = chrome_zoom_step + 1
                            elif 7 <= chrome_zoom_step:
                                BusinessLogicUtil.press('ctrl', '+')
                                chrome_zoom_step = chrome_zoom_step + 1
                except pyautogui.ImageNotFoundException:
                    BusinessLogicUtil.print_with_underline(f"{loop_cnt}번의 화면인식시도를 했지만 인식하지 못하였습니다")
                    pass
        else:
            while True:
                loop_cnt = loop_cnt + 1
                BusinessLogicUtil.print_with_underline("화면 이미지 인식 시도 중...")
                if recognize_loop_limit_cnt == loop_cnt:
                    BusinessLogicUtil.print_with_underline(f"{loop_cnt}번의 화면인식시도를 했지만 인식하지 못하였습니다")
                    return None
                try:
                    img = pyautogui.locateOnScreen(img_abspath, confidence=0.7, grayscale=True)
                    BusinessLogicUtil.print_cyan(type(img))
                    BusinessLogicUtil.print_cyan(img)
                    BusinessLogicUtil.print_cyan(img is not None)
                    if img is not None:
                        return img
                except:
                    BusinessLogicUtil.print_cyan(img_abspath)
                    BusinessLogicUtil.sleep(milliseconds=10)
                    if is_zoom_toogle_mode == True:
                        if chrome_zoom_step == 14:
                            chrome_zoom_step = 0
                        elif chrome_zoom_step < 7:
                            BusinessLogicUtil.press('ctrl', '-')
                            chrome_zoom_step = chrome_zoom_step + 1
                        elif 7 <= chrome_zoom_step:
                            BusinessLogicUtil.press('ctrl', '+')
                            chrome_zoom_step = chrome_zoom_step + 1

    @staticmethod
    def click_center_of_img_recognized_by_mouse_left(img_pnx: str, loop_limit_cnt=0, is_zoom_toogle_mode=False):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        img = BusinessLogicUtil.get_img_when_img_recognized_succeed(img_pnx, loop_limit_cnt, is_zoom_toogle_mode)
        if not img is None:
            center_x = img.left + (img.width / 2)
            center_y = img.top + (img.height / 2)
            BusinessLogicUtil.move_mouse(x_abs=center_x, y_abs=center_y)
            BusinessLogicUtil.click_mouse_left_btn(x_abs=center_x, y_abs=center_y)
            return True
        else:
            return False

    @staticmethod
    async def shoot_custom_screenshot_via_asyncio():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            try:
                timestamp = TimeUtil.get_time_as_('%Y_%m_%d_%H_%M_%S')
                PKG_IMAGE = rf'{StateManagementUtil.PKG_IMAGE}'
                positivie = "Positive"
                negative = "Negative"
                user_input = None
                hostname = BusinessLogicUtil.get_hostname()
                BusinessLogicUtil.print_as_log(string=rf'''hostname="{hostname}" %%%FOO%%%''')
                token_hostname_desktop = BusinessLogicUtil.get_token_from_text_file(token_file=rf'{StateManagementUtil.PKG_TXT}\token_hostname_desktop.txt', initial_token="")
                token_hostname_a2z = BusinessLogicUtil.get_token_from_text_file(token_file=rf'{StateManagementUtil.PKG_TXT}\token_hostname_a2z.txt', initial_token="")
                if token_hostname_a2z in hostname:
                    user_input = input("저장할 스크린샷의 키파일명을 입력하세요:")
                if token_hostname_desktop in hostname:
                    dialog_btn_text_clicked, function, dialog_input_box_text = BusinessLogicUtil.should_i_do(
                        string=rf"저장할 스크린샷의 키파일명을 입력하세요",
                        btns=[positivie, negative],
                        function=None,
                        auto_click_negative_btn_after_seconds=30,
                        title=f"{function_name}()",
                        return_mode=True,
                        input_box_mode=True,
                    )
                    if dialog_btn_text_clicked != positivie:
                        return
                    user_input = dialog_input_box_text
                user_input = user_input.strip()
                user_input = user_input.replace(" ", "_")
                file_png_nx = rf'screenshot_{user_input}_{timestamp}.png'
                file_png = rf'{PKG_IMAGE}\{file_png_nx}'

                await asyncio.sleep(2)

                # snipping tool 실행
                BusinessLogicUtil.press("win", "shift", "s", interval=0.5)

                if BusinessLogicUtil.is_keyboard_pressed_within_timeout("ctrl+s", timeout=10):
                    if not BusinessLogicUtil.does_pnx_exist(src=PKG_IMAGE):
                        BusinessLogicUtil.make_pnx(pnx=PKG_IMAGE, mode="d")
                else:
                    return

                await asyncio.sleep(1)  # miliseconds 로 하면 좋겠음.
                BusinessLogicUtil.press("ctrl", "l")
                await asyncio.sleep(1)
                BusinessLogicUtil.write_like_person(PKG_IMAGE, interval=0.015)
                await asyncio.sleep(1)
                BusinessLogicUtil.press("enter")
                await asyncio.sleep(1)
                if "DESKTOP-UGLEIND" in hostname:  # windows 11인 경우같다
                    for i in range(0, 7):
                        BusinessLogicUtil.press("tab")
                else:
                    for i in range(0, 4):
                        BusinessLogicUtil.press("tab")
                BusinessLogicUtil.write(file_png_nx)
                await asyncio.sleep(1)
                BusinessLogicUtil.press("enter")
                await asyncio.sleep(1)
                if BusinessLogicUtil.does_pnx_exist(src=file_png):
                    BusinessLogicUtil.print_as_log(string=rf'''file_png="{file_png}" %%%FOO%%%''')

                    # Snipping Tool.ink 종료
                    command = rf"taskkill -im SnippingTool.exe"
                    BusinessLogicUtil.command_to_os(cmd=command, show_mode=False, mode="a")
                    break
            except:
                traceback.print_exc(file=sys.stdout)

    @staticmethod
    def speak_that_service_is_in_preparing():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.speak_ment_experimental(ment="아직 준비되지 않은 서비스 입니다", comma_delay=0.98)

    @staticmethod
    def ask_to_wrtn_core(question):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            # 윈도우즈 모든창 최소화
            # BusinessLogicUtil.press('win', 'm')

            # wrtn에게 묻기 (chatGPT 3 기반)
            BusinessLogicUtil.ask_to_wrtn(question=question)

            # 구글에게 묻기
            # BusinessLogicUtil.ask_to_google(question=question)

            # bard에게 묻기
            # BusinessLogicUtil.ask_to_bard(question=question)

            # 크롬 최대화
            # BusinessLogicUtil.press('win', 'up')

            # 크롬 화면 적당한 배율로 변경
            BusinessLogicUtil.press('ctrl', '0')
            BusinessLogicUtil.press('ctrl', '-')
            BusinessLogicUtil.press('ctrl', '-')
            BusinessLogicUtil.press('ctrl', '-')

            # 크롬 이전 시트로 이동
            # BusinessLogicUtil.press("ctrl", "shift", "tab")

            BusinessLogicUtil.press("ctrl", "0")
            for i in range(1, 5):
                BusinessLogicUtil.press("ctrl", "-")

            # 사용자에게 질문 답변
            BusinessLogicUtil.speak_ment_experimental(ment="AI 에게 질문을 성공했습니다", comma_delay=0.98)
            break

    @staticmethod
    def is_keyboard_pressed_within_timeout(key_plus_key: str, timeout):
        # timeout 이 아니라 트리거로 ESC 눌렸을 때 종료되도록 하는 함수가 더 유용하겠다.
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        time_s = time.time()
        keys = key_plus_key.split("+")
        waiting_limit = 30
        while True:
            if all(keyboard.is_pressed(key) for key in keys):
                # 단축키 조합이 모두 눌렸을 때 실행할 코드
                BusinessLogicUtil.print_cyan(f"{keys[0]}+{keys[1]}")
                return True
            else:
                BusinessLogicUtil.print_light_black(f"{key_plus_key} 눌릴때까지 기다리고 있습니다")
                time_e = time.time()
                time_diff = time_e - time_s
                if time_diff == timeout:
                    return False
                BusinessLogicUtil.sleep(milliseconds=waiting_limit, show_mode=False)

    click_detected = False  # 클릭 감지 상태를 저장하는 클래스 변수

    @staticmethod
    def on_right_click(x, y, button, pressed):
        """마우스 클릭 이벤트 처리."""
        if pressed and button == mouse.Button.right:
            BusinessLogicUtil.click_detected = True  # 클릭 감지 상태 업데이트
            BusinessLogicUtil.print_light_black("마우스 우클릭 감지됨!")
            return False  # 마우스 왼쪽 클릭 감지되면 Listener 종료

    @staticmethod
    def on_left_click(x, y, button, pressed):
        """마우스 클릭 이벤트 처리."""
        if pressed and button == mouse.Button.left:
            BusinessLogicUtil.click_detected = True  # 클릭 감지 상태 업데이트
            BusinessLogicUtil.print_light_black("마우스 왼쪽 클릭 감지됨!")
            return False  # 마우스 왼쪽 클릭 감지되면 Listener 종료

    @staticmethod
    def is_mouse_button_click_within_timeout(key="left", timeout=10):
        """주어진 시간 이내에 마우스 클릭을 감지하는 함수."""
        if key == "left":
            listener = mouse.Listener(on_click=BusinessLogicUtil.on_left_click)
        elif key == "right":
            listener = mouse.Listener(on_click=BusinessLogicUtil.on_right_click())
        listener.start()  # Listener 시작
        listener.join(timeout)  # 주어진 시간 동안 대기
        listener.stop()  # Listener 종료

        return BusinessLogicUtil.click_detected  # 클릭 감지 여부 반환

    #
    # @staticmethod
    # def detect_mouse_click(timeout=10):
    #     import time
    #     import pyautogui
    #     import keyboard
    #     """10초 이내에 마우스 왼쪽 클릭을 감지하는 함수.
    #
    #     Args:
    #         timeout (int): 클릭 감지를 위한 대기 시간 (초).
    #
    #     Returns:
    #         bool: 클릭이 감지되면 True, 그렇지 않으면 False.
    #     """
    #     start_time = time.time()
    #     BusinessLogicUtil.print_as_gui("10초 이내에 마우스 왼쪽 클릭을 해주세요..." ,auto_click_positive_btn_after_seconds=2)
    #     while (time.time() - start_time) < timeout:
    #         if keyboard.is_pressed('left'):
    #             BusinessLogicUtil.print_as_gui("마우스 왼쪽 클릭 감지됨!")
    #             return True
    #         time.sleep(0.1)  # CPU 사용량을 줄이기 위해 잠시 대
    #     BusinessLogicUtil.print_as_gui("타임아웃! 클릭이 감지되지 않았습니다.")
    #     return False
    @staticmethod
    def translate_eng_to_kor(question: str):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            while True:
                try:
                    question = question.strip('""')
                except AttributeError:
                    break
                BusinessLogicUtil.press("win", "m")

                # 구글 번역 페이지로 이동
                url = "https://www.google.com/search?q=eng+to+kor"
                cmd = f'explorer "{url}" >nul'
                BusinessLogicUtil.command_to_os_like_person_as_admin(cmd)

                # 크롬 창 활성화
                target_pid: int = BusinessLogicUtil.get_pids_by_process_name(process_name="chrome.exe")  # chrome.exe pid 가져오기
                BusinessLogicUtil.move_window_to_front_by_pid(pid=target_pid)

                # 텍스트를 입력하세 클릭
                file_png = rf"{StateManagementUtil.PROJECT_DIRECTORY}\pkg_png\eng to kor.png"
                BusinessLogicUtil.click_center_of_img_recognized_by_mouse_left(img_pnx=file_png, is_zoom_toogle_mode=True, loop_limit_cnt=100)

                # 번역할 내용 작성
                BusinessLogicUtil.write_fast(question)

                # 글자수가 많으면 text to voice icon 이 잘려서 보이지 않음. 이는 이미지의 객체 인식이 불가능해지는데
                # 스크롤를 내려서 이미지 인식을 가능토록
                if len(question) > 45:
                    pyautogui.vscroll(-15)
                BusinessLogicUtil.sleep(30)

                # text to voice icon
                file_png = rf"{StateManagementUtil.PROJECT_DIRECTORY}\pkg_png\text to voice icon.png"
                BusinessLogicUtil.click_center_of_img_recognized_by_mouse_left(img_pnx=file_png, is_zoom_toogle_mode=True, loop_limit_cnt=100)

                # 종료
                break
        except:
            traceback.print_exc(file=sys.stdout)

    @staticmethod
    def translate_kor_to_eng(question: str):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            while True:
                try:
                    question = question.strip('""')
                except AttributeError:
                    break
                BusinessLogicUtil.press("win", "m")

                # 페이지 열기
                url = "https://www.google.com/search?q=kor+to+eng"
                cmd = f'explorer "{url}" >nul'
                BusinessLogicUtil.command_to_os_like_person_as_admin(cmd)

                # 크롬 창 활성화
                target_pid: int = BusinessLogicUtil.get_pids_by_process_name(process_name="chrome.exe")  # chrome.exe pid 가져오기
                BusinessLogicUtil.move_window_to_front_by_pid(pid=target_pid)

                # Enter Text 클릭
                file_png = rf"{StateManagementUtil.PROJECT_DIRECTORY}\pkg_png\kor to eng.png"
                BusinessLogicUtil.click_center_of_img_recognized_by_mouse_left(img_pnx=file_png, is_zoom_toogle_mode=True, loop_limit_cnt=100)

                # 번역할 내용 작성
                BusinessLogicUtil.write_fast(question)

                # 글자수가 많으면 text to voice icon 이 잘려서 보이지 않음. 이는 이미지의 객체 인식이 불가능해지는데
                # 스크롤를 내려서 이미지 인식을 가능토록
                if len(question) > 45:
                    pyautogui.vscroll(-15)
                BusinessLogicUtil.sleep(30)

                # text to voice icon
                file_png = rf"{StateManagementUtil.PROJECT_DIRECTORY}\pkg_png\text to voice icon.png"
                BusinessLogicUtil.click_center_of_img_recognized_by_mouse_left(img_pnx=file_png, is_zoom_toogle_mode=True, loop_limit_cnt=100)

                break
        except:
            traceback.print_exc(file=sys.stdout)

    @staticmethod
    def run_cmd_exe_as_admin():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            while True:
                # run.exe 관리자모드로 실행
                BusinessLogicUtil.command_to_os_like_person_as_admin('PowerShell -Command "Start-Process cmd -Verb RunAs"')

                # 네 클릭
                # file_png = rf"{StateManagementUtil.PROJECT_DIRECTORY}\pkg_png\run cmd exe.png"
                # BusinessLogicUtil.click_center_of_img_recognized_by_mouse_left(img_abspath=file_png)

                # 루프 종료
                break
        except:
            traceback.print_exc(file=sys.stdout)

    @staticmethod
    def copy_and_paste_with_keeping_clipboard(string, wsl_mode=False, show_mode=True):
        # copy & paste 기능이 끝났을 때 기존의 클립보드를 유지
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        # paste for backup
        string_bkup = BusinessLogicUtil.get_str_from_clipboard()
        BusinessLogicUtil.print_as_log(string=rf'''string_bkup="{string_bkup}" %%%FOO%%%''')

        # copy
        BusinessLogicUtil.copy(string=string)
        BusinessLogicUtil.print_as_log(string=rf'''string="{string}" %%%FOO%%%''')

        # paste
        if wsl_mode == True:
            BusinessLogicUtil.press("ctrl", "c", show_mode=show_mode)
            BusinessLogicUtil.press("ctrl", "shift", "v", show_mode=show_mode)
        else:
            BusinessLogicUtil.press("ctrl", "v", show_mode=show_mode)

        # copy for restore
        BusinessLogicUtil.copy(string=string_bkup)

    @staticmethod
    def is_void_function(func):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        """
            함수가 void 함수인지 아닌지 판단하는 함수입니다.

            Args:
              function: 함수

            Returns:
              함수가 void 함수이면 True, 아니면 False
        """
        function_code = func.__code__
        return function_code.co_argcount == 0 and function_code.co_flags & 0x20 == 0

    @staticmethod
    def get_count_args(func):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        return func.__code__.co_argcount

    @staticmethod
    def get_list_replaced_from_list_that_have_special_characters(target: [str], replacement: str):  # from [str] to [str] # 문제있어보임.
        return [re.sub(pattern=r'[^a-zA-Z0-9가-힣\s]', repl='', string=string) for string in target]

    @staticmethod
    def get_str_replaced_special_characters(target: str, replacement: str):  # str to str
        target_replaced = re.sub(pattern=r'[^a-zA-Z0-9가-힣\s]', repl=replacement, string=target)  # 정규표현식을 사용하여 특수문자(알파벳, 숫자, 한글, 공백을 제외한 모든 문자) 제거
        return target_replaced

    @staticmethod
    def speak_alt_for_emergency(contents: str):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.translate_eng_to_kor(contents)

    @staticmethod
    def get_all_pid_and_process_name():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        """모든 프로세스명 돌려주는 함수"""
        process_info = ""

        def enum_windows_callback(hwnd, _):
            # todo function_name 출력 하지 말자
            # function_name = inspect.currentframe().f_code.co_name
            # BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            import psutil  # 실행중인 프로세스 및 시스템 활용 라이브러리
            nonlocal process_info
            if win32gui.IsWindowVisible(hwnd):
                _, pid = win32process.GetWindowThreadProcessId(hwnd)
                try:
                    process = psutil.Process(pid)
                    process_name = process.name()
                    process_info += f"창 핸들: {hwnd}, pid: {pid}, process_name: {process_name}\n"
                except psutil.NoSuchProcess:
                    pass

        win32gui.EnumWindows(enum_windows_callback, None)
        return process_info

    @staticmethod
    def move_window_to_front_by_pid(pid: int, show_mode=True):
        function_name = inspect.currentframe().f_code.co_name
        if show_mode == True:
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.print_as_log(string=rf'''pid="{pid}" %%%FOO%%%''')
        import psutil  # 실행중인 프로세스 및 시스템 활용 라이브러리
        if not str(pid).isdigit():
            BusinessLogicUtil.print_as_gui(f"pid 분석결과 숫자가 아닌 것으로 판단됨 \n\n{pid}")
        pid = int(pid)
        try:
            process = psutil.Process(pid)
            if process.is_running() and process.status() != psutil.STATUS_ZOMBIE:
                hwnd = win32gui.FindWindow(None, None)  # PID를 기반으로 창 핸들을 가져옵니다.
                while hwnd:
                    _, found_pid = win32process.GetWindowThreadProcessId(hwnd)  # 창이 속한 프f로세스의 PID를 가져옵니다.
                    if found_pid == pid:
                        win32gui.SetForegroundWindow(hwnd)  # 창을 활성화합니다.
                        break
                    hwnd = win32gui.FindWindowEx(None, hwnd, None, None)
            else:
                BusinessLogicUtil.print_cyan(f"{StateManagementUtil.UNDERLINE}프로세스가 실행 중이지 않습니다.")
        except psutil.NoSuchProcess:
            BusinessLogicUtil.print_cyan(f"{StateManagementUtil.UNDERLINE}유효하지 않은 PID입니다.")
        except:
            if show_mode == True:
                BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def get_pid_by_process_name_legacy(process_name: str):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # Q.how to activate certain program window at python?
        pids: str = BusinessLogicUtil.get_all_pid_and_process_name()
        # BusinessLogicUtil.debug_as_gui(f"pids:\n\n{pids}")
        pids: list[str] = [i for i in pids.split("\n") if BusinessLogicUtil.is_pattern_in_string(string=i, pattern=process_name)]  # 프로세스명이 target_process_name 인 경우만 추출
        pids: str = pids[0].split(",")[1].replace("pid:", "").strip()  # strip() 은 특정 문자를 제거를 위해서 만들어짐. 단어를 제거하기 위해서는 replace() 가 더 적절하다고 chatGPT 는 말한다.
        target_pid = int(pids)  # 추출된 target_process_name 의 pid
        BusinessLogicUtil.print_as_gui(f"target_process_name 프로세스 정보\n\n{target_pid}")
        return target_pid

    @staticmethod
    def get_process_name_by_pid(pid):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            data = BusinessLogicUtil.command_to_os(cmd=f'tasklist | findstr "{pid}"')
            return data[0].split(" ")[0]
        except:
            return 0

    @staticmethod
    def get_pids_by_process_name(process_name: str):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            command = f"tasklist | findstr {process_name}"
            pids = BusinessLogicUtil.command_to_os(cmd=command, show_mode=False)
            # BusinessLogicUtil.debug_as_gui(f"pids:\n\n{pids}")
            cnts: [int] = []
            for i in pids:
                cnts.append(i.count(" "))  # str 내의 특정문자의 개수를 cnts에 저장
            try:
                max_cnt = max(cnts)
            except ValueError:
                BusinessLogicUtil.print_as_log(f'''"f"{process_name}에 대한 현재 실행중인 pid 가 없는 것 같습니다""''')
                break
            for i in range(0, max_cnt):  # max(cnts):  pids 요소별 가장 " " 가 많이 든 요소의 개수
                pids: [str] = [i.replace("  ", " ") for i in pids]  # 공백 제거

            pids_ = []
            for i in pids:
                if i.strip() != "\"":
                    if i.strip() != "":
                        # pids_.append(i.split(" "))  # 리스트 요소 내 "" 인 경우 제거, \" 인 경우 제거
                        pids_.append(list(map(str, i.split(" "))))  # 리스트 요소 내 "" 인 경우 제거, \" 인 경우 제거
            pids = pids_

            pid_and_size = {}
            for i in pids:
                pid_and_size[i[1]] = i[4]  # pid 와 size 를 튜플로 나눠 담았는데 이부분 생략하고 처음부터 남아 담아도 되었을 것 같은데

            pids = []
            sizes = []
            for pid, size in pid_and_size.items():
                pids.append(pid)
                sizes.append(size)

            # for pid, size in pid_and_size.items():  # 프로세스명이 중복일 때 size 가 큰 프로세스의 pid를 리턴
            #     if size == max(sizes):
            #         # BusinessLogicUtil.print_cyan(f"pid : {pid}")
            #         return int(pid)

            return pids

    @staticmethod
    def get_max_pid_by_process_name(process_name: str, show_mode=False):

        function_name = inspect.currentframe().f_code.co_name
        if show_mode == True:
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            command = f"tasklist | findstr {process_name}"
            pids = BusinessLogicUtil.command_to_os(cmd=command, show_mode=show_mode)
            # BusinessLogicUtil.debug_as_gui(f"pids:\n\n{pids}")
            cnts: [int] = []
            for i in pids:
                cnts.append(i.count(" "))  # str 내의 특정문자의 개수를 cnts에 저장
            try:
                max_cnt = max(cnts)
            except ValueError:
                BusinessLogicUtil.print_cyan(f"{process_name}에 대한 현재 실행중인 pid 가 없는 것 같습니다")
                break
            for i in range(0, max_cnt):  # max(cnts):  pids 요소별 가장 " " 가 많이 든 요소의 개수
                pids: [str] = [i.replace("  ", " ") for i in pids]  # 공백 제거

            pids_ = []
            for i in pids:
                if i.strip() != "\"":
                    if i.strip() != "":
                        # pids_.append(i.split(" "))  # 리스트 요소 내 "" 인 경우 제거, \" 인 경우 제거
                        pids_.append(list(map(str, i.split(" "))))  # 리스트 요소 내 "" 인 경우 제거, \" 인 경우 제거
            pids = pids_

            pid_and_size = {}
            for i in pids:
                pid_and_size[i[1]] = i[4]  # pid 와 size 를 튜플로 나눠 담았는데 이부분 생략하고 처음부터 남아 담아도 되었을 것 같은데

            pids = []
            sizes = []
            for pid, size in pid_and_size.items():
                pids.append(pid)
                sizes.append(size)

            for pid, size in pid_and_size.items():  # 프로세스명이 중복일 때 size 가 큰 프로세스의 pid를 리턴
                if size == max(sizes):
                    # BusinessLogicUtil.print_cyan(f"pid : {pid}")
                    return int(pid)

    @staticmethod
    def print_pid_by_process_name(pnx_process_name: str):
        BusinessLogicUtil.print_cyan(BusinessLogicUtil.get_pids_by_process_name(pnx_process_name))

    @staticmethod
    def print_today_time_info_natural():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        yyyy = TimeUtil.get_time_as_('%Y')
        MM = TimeUtil.get_time_as_('%m')
        dd = TimeUtil.get_time_as_('%d')
        HH = TimeUtil.get_time_as_('%H')
        mm = TimeUtil.get_time_as_('%M')
        week_name = BusinessLogicUtil.get_weekday_as_korean()
        BusinessLogicUtil.print_cyan(f'대한민국 표준시 기준, 현재시각 {int(yyyy)}년 {int(MM)}월 {int(dd)}일 {week_name}요일 {int(HH)}시 {int(mm)}분')
        # 이 형식의 텍스트들은 예측이 가능하다
        # 미리 하루 정도 치를 미리 만들어 두면
        # 재생하는데 지금보다 빠르게 가능할 것이다
        # 시간이 과거 인 것들은 지워 용량을 관리한다.
        # 회사 컴퓨터로 미리 재생 파일들을 만들어 둔다.

    @staticmethod
    def chrome_remote_desktop(hostname):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        function_name_txt = rf'{StateManagementUtil.PROJECT_DIRECTORY}\pkg_txt\{function_name}.txt'
        # BusinessLogicUtil.make_pnx(pnx=function_name_txt, mode="f")
        # if not BusinessLogicUtil.is_window_open(window_title=function_name_txt):
        #     BusinessLogicUtil.run_pnx_via_explorer_exe(function_name_txt, show_mode=False)

        # 페이지 열기
        # url = "https://remotedesktop.google.com/access/session/7dc038af-5992-1938-470a-8f85923ab286"
        url = 'https://remotedesktop.google.com/access'
        BusinessLogicUtil.command_to_os(cmd=f'explorer "{url}"')
        BusinessLogicUtil.print_as_log(string=rf'''url="{url}" %%%FOO%%%''')

        # 창 앞으로 이동
        window_title = "Chrome"
        window_title_seg = window_title
        BusinessLogicUtil.move_window_to_front(window_title_seg=window_title_seg)

        # chrome 창 탭 중 해당 url로 이동
        # BusinessLogicUtil.move_chrome_tab_by_url(url_to_move=url)

        # 클릭
        BusinessLogicUtil.click_string(string=hostname)

        # PIN 입력
        token_chrome_remote_pin_encoded = BusinessLogicUtil.get_token_from_text_file(token_file=rf'{StateManagementUtil.PKG_TXT}\token_chrome_remote_pin.txt', initial_token="")
        token_chrome_remote_pin = BusinessLogicUtil.decode_via_park4139(token_chrome_remote_pin_encoded)
        BusinessLogicUtil.write(token_chrome_remote_pin, milliseconds=5000)
        BusinessLogicUtil.press("enter")

    @staticmethod
    def translate_eng_to_kor_via_googletrans(text: str):  # 수정할것 update 되었다는데 googletrans 업데이트 해보자
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # from googletrans import Translator
        # translater = Translator()
        # text_translated = translater.translate([text_eng.split(".")], dest='ko')
        # for translation in text_translated:
        #     print(translation.origin, ' -> ', translation.text)
        # BusinessLogicUtil.debug_as_gui(context=text_translated, is_app_instance_mode=True)

        # from papago_translate import Translator
        # naver papago api 서비스는 2024 년 종료가 된다...
        # translator = Translator(service_urls=['translate.google.com', 'translate.google.co.kr'],user_agent='Mozilla/5.0 (Windows NT 10.0;  x64; Win64)', timeout=random.randint(0, 99) / 10)
        # tmp = translator.translate(text, src="ko", dest="en")
        # print(rf'tmp : {tmp}')
        # print(rf'type(tmp) : {type(tmp)}')
        # print(rf'len(tmp) : {len(tmp)}')
        # Park4139BusinessLogicUtil.pause()

        # 한수훈 씨가 만든 모듈 같다. 무료이다. 단, 안정성 보장은 안되며, google 로 부터 ip가 차단이 될 수 있다.
        # 단일 텍스트의 최대 글자수 제한은 15k입니다. 이거 로직으로 제한 해야 한다.
        # 약간 시간적인 트릭도 넣을 것
        # <Translated src=ko dest=en text=Good evening. pronunciation=Good evening.>
        # translator.translate('안녕하세요.', dest='ja')
        # <Translated src=ko dest=ja text=こんにちは。 pronunciation=Kon'nichiwa.>
        # translator.translate('veritas lux mea', src='la')
        # <Translated src=la dest=en text=The truth is my light pronunciation=The truth is my light>
        # 2023 12 31 01 11 현재시각기준 안된다

        # from googletrans import Translator
        # translator = Translator()
        # translator.detect('이 문장은 한글로 쓰여졌습니다.')
        # # <Detected lang=ko confidence=0.27041003>
        # translator.detect('この文章は日本語で書かれました。')
        # # <Detected lang=ja confidence=0.64889508>
        # translator.detect('This sentence is written in English.')
        # # <Detected lang=en confidence=0.22348526>
        # translator.detect('Tiu frazo estas skribita en Esperanto.')
        # # <Detected lang=eo confidence=0.10538048>

    @staticmethod
    def translate_kor_to_eng_foo(request: str):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        translator = Translator()
        text_translated = translator.translate(str(request), src='ko', dest='en')
        BusinessLogicUtil.print_as_gui(ment=text_translated, is_app_instance_mode=True)

    @staticmethod
    def keyDown(key: str):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        pyautogui.keyDown(key)

    @staticmethod
    def keyUp(key: str):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        pyautogui.keyUp(key)

    @staticmethod
    def get_font_name_for_mataplot(font_abspath):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        import matplotlib
        import matplotlib.font_manager as mataplotlig_fontmanager

        # mataplot 폰트캐시 삭제
        cache_dir = matplotlib.get_cachedir()
        for file in os.listdir(cache_dir):
            if file.endswith('.json'):
                os.remove(os.path.join(cache_dir, file))

        # local font 를 mataplot 폰트 위치로 복사
        pnx_new = rf"{os.path.dirname(matplotlib.matplotlib_fname())}\fonts\ttf\{os.path.basename(font_abspath)}"
        if not os.path.exists(pnx_new):
            BusinessLogicUtil.xcopy_with_overwrite(target_pnx=font_abspath, future_target_pnx=pnx_new)
        font_name = mataplotlig_fontmanager.FontProperties(fname=pnx_new).get_name()
        return font_name

    @staticmethod
    def get_weekday_as_korean():
        now = datetime.now()
        weekdays_korean = ['월', '화', '수', '목', '금', '토', '일']
        return weekdays_korean[now.weekday()]

    @staticmethod
    def get_weekday_as_english():
        now = datetime.now()
        weekdays_korean = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        return weekdays_korean[now.weekday()]

    @staticmethod
    def get_comprehensive_weather_information_from_web():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        browser_show_mode = False
        try:
            while 1:
                title = ""
                ment_about_naver_weather = ''
                results_about_naver_weather = ''
                results_about_nationwide_ultrafine_dust = ''
                ment_about_geo = ''
                results_about_geo = ''
                ment_about_pm_ranking = ''
                results_about_pm_ranking = ''
                async def crawl_pm_ranking():
                    function_name = inspect.currentframe().f_code.co_name
                    BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
                    driver = None
                    try:
                        driver = BusinessLogicUtil.get_driver_selenium(browser_show_mode=browser_show_mode)
                        ment = '미세먼지랭킹 웹사이트 크롤링 결과'
                        global ment_about_pm_ranking
                        ment_about_pm_ranking = ment
                        target_url = f'https://www.dustrank.com/air/air_dong_detail.php?addcode=41173103'
                        BusinessLogicUtil.print_cyan(target_url)
                        driver.get(target_url)
                        page_src = driver.page_source
                        soup = BeautifulSoup(page_src, "lxml")
                        results = soup.find_all("table", class_="datatable")  # <table class="datatable">foo!</div>
                        soup = BeautifulSoup(str(results), "lxml")
                        results = soup.find_all("table")[-1]
                        soup = BeautifulSoup(str(results), "lxml")
                        results = soup.find_all("table")[-1].text
                        results = results.split("\n")  # 리스트
                        results = [x for x in results if x.strip()]
                        results = [x for x in results if x.strip(",")]
                        head_1 = results[1]
                        head_2 = results[2]
                        pattern = r'(\d{2}-\d{2}-\d{2} \d{2}:\d{2})([가-힣]+\(\d+\))([가-힣]+\(\d+\))'  # 정규식을 () 로 부분 부분 묶으면 tuple 형태로 수집할 수 있다.
                        body = re.findall(pattern, results[3])
                        body = list(body)  # tuple to list
                        body = [list(item) for item in body]  # LIST 내 ITEM 이 TUPLE 일 때 ITEM 을 LIST 로 변환 #의도대로 잘 변했으~

                        # 리스트 요소를 3개 단위로 개행하여 str 에 저장
                        body_ = ""
                        for i in range(0, len(body), 1):
                            body_ = body_ + body[i][0] + body[i][1] + body[i][2] + "\n"
                        body = body_
                        # body = "\n".join(body) # list to str
                        results = f"{head_1}\t{head_2}\n{body}"

                        global results_about_pm_ranking
                        results_about_pm_ranking = results
                        BusinessLogicUtil.print_as_log(string = rf'''results_about_pm_ranking="{results_about_pm_ranking}" %%%FOO%%%''')
                    except:
                        BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
                        # driver.close()
                        driver.quit()

                async def crawl_nationwide_ultrafine_dust():
                    function_name = inspect.currentframe().f_code.co_name
                    BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
                    driver = BusinessLogicUtil.get_driver_selenium(browser_show_mode=browser_show_mode)

                    # # '전국초미세먼지'(bs4 way)
                    ment = '전국초미세먼지  크롤링 결과'
                    global title
                    title = ment
                    target_url = 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=전국초미세먼지'
                    BusinessLogicUtil.print_cyan(target_url)
                    driver.get(target_url)
                    page_src = driver.page_source
                    soup = BeautifulSoup(page_src, "lxml")
                    results: any
                    # results = soup.find_all("body")
                    results: ResultSet = soup.find_all("div", class_="detail_box")
                    results: str = results[0].text
                    results: str = results.replace("지역별 초미세먼지 정보", "")
                    results: str = results.replace("관측지점 현재 오전예보 오후예보", "")
                    results: str = results.replace("", "")
                    results___: [str] = results.split(" ")
                    results___: [str] = [x for x in results___ if x.strip(" ") and x.strip("") and x.strip("\"") and x.strip("\'") and x.strip("\'\'")]  # 불필요 리스트 요소 제거 ( "" , "\"", " " ...)

                    # 리스트 요소를 4개 단위로 개행하여 str 에 저장
                    results_: str = ""
                    for i in range(0, len(results___), 4):
                        if i == len(results___):
                            pass
                        results_ = f"{results_}\t{results___[i]}\t{results___[i + 1]}\t{results___[i + 2]}\t{results___[i + 3]}\n"
                    results___ = results_
                    global results_about_nationwide_ultrafine_dust
                    results_about_nationwide_ultrafine_dust = results___
                    BusinessLogicUtil.print_as_log(string = rf'''results_about_nationwide_ultrafine_dust="{results_about_nationwide_ultrafine_dust}" %%%FOO%%%''')

                async def crawl_naver_weather():
                    function_name = inspect.currentframe().f_code.co_name
                    BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
                    driver = BusinessLogicUtil.get_driver_selenium(browser_show_mode=browser_show_mode)
                    # '동안구 관양동 날씨 정보'(bs4 way)
                    ment = '네이버 동안구 관양동 날씨 크롤링 결과'

                    global ment_about_naver_weather
                    ment_about_naver_weather = ment
                    target_url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=동안구+관양동+날씨'
                    BusinessLogicUtil.print_cyan(target_url)
                    driver.get(target_url)
                    page_src = driver.page_source
                    soup = BeautifulSoup(page_src, "lxml")
                    results: ResultSet = soup.find_all("div", class_="status_wrap")
                    results: str = results[0].text
                    # 리스트 요소 변경
                    results: str = results.replace("오늘의 날씨", "오늘의날씨")
                    results: str = results.replace(" 낮아요", "낮아요")
                    results: str = results.replace(" 높아요", "높아요")
                    results: str = results.replace(" 체감", "체감온도")
                    results_refactored = results.split(" ")
                    results_refactored: [str] = [x for x in results_refactored if x.strip(" ") and x.strip("") and x.strip("\"") and x.strip("\'") and x.strip("\'\'")]  # 불필요 리스트 요소 제거 ( "" , "\"", " " ...)
                    results_refactored: [str] = [x for x in results_refactored if x.strip("현재")]  # 리스트 요소 "오늘의"
                    # 리스트 내 특정문자와 동일한 요소의 바로 뒷 요소를 가져와 딕셔너리에 저장 # 데이터의 key, value 형태가 존재하면서 순번이 key 다음 value 형태로 잘 나오는 경우 사용.
                    keys_predicted = ['온도', '체감온도', '습도', '서풍', '동풍', '남풍', '북풍', '북서풍', '미세먼지', '초미세먼지', '자외선', '일출', '오늘의날씨']
                    results_: dict = {}
                    for i in range(len(results_refactored) - 1):
                        for key_predicted in keys_predicted:
                            if results_refactored[i] == key_predicted:
                                key = results_refactored[i]
                                value = results_refactored[i + 1]
                                results_[key] = value
                    results_refactored = results_

                    # results: [str] = str(results_)  # dict to str (개행을 시키지 않은)

                    results: str = "\n".join([f"{key}: {value}" for key, value in results_refactored.items()])  # dict to str (개행을 시킨)

                    global results_about_naver_weather
                    results_about_naver_weather = results
                    BusinessLogicUtil.print_as_log(string = rf'''results_about_naver_weather="{results_about_naver_weather}" %%%FOO%%%''')

                async def crawl_geo_info():
                    function_name = inspect.currentframe().f_code.co_name
                    BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
                    # '지역 정보'(bs4 way)
                    driver = BusinessLogicUtil.get_driver_selenium(browser_show_mode=browser_show_mode)
                    ment = '지역정보 크롤링 결과'
                    global ment_about_geo
                    ment_about_geo = ment
                    # target_url = 'https://map.naver.com/p'
                    target_url = 'https://www.google.com/search?q=현재위치'
                    BusinessLogicUtil.print_cyan(target_url)
                    driver.get(target_url)
                    page_src = driver.page_source
                    soup = BeautifulSoup(page_src, "lxml")
                    results: any
                    # results = soup.find_all("body")
                    results: ResultSet = soup.find_all("span", class_="BBwThe")  # 지역정보 한글주소
                    # results: ResultSet = soup.find_all("span", class_="fMYBhe") # 지역정보 영어주소
                    results: str = results[0].text

                    global results_about_geo
                    results_about_geo = results
                    BusinessLogicUtil.print_as_log(string = rf'''results_about_geo="{results_about_geo}" %%%FOO%%%''')

                def run_async_loop1():
                    function_name = inspect.currentframe().f_code.co_name
                    BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
                    try:
                        function_name = inspect.currentframe().f_code.co_name
                        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
                        loop = asyncio.new_event_loop()
                        asyncio.set_event_loop(loop)
                        loop.run_until_complete(crawl_pm_ranking())
                    except:
                        BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

                def run_async_loop2():
                    function_name = inspect.currentframe().f_code.co_name
                    BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    loop.run_until_complete(crawl_nationwide_ultrafine_dust())

                def run_async_loop3():
                    function_name = inspect.currentframe().f_code.co_name
                    BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    loop.run_until_complete(crawl_naver_weather())

                def run_async_loop4():
                    function_name = inspect.currentframe().f_code.co_name
                    BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
                    # BusinessLogicUtil.print_as_log(f"def {inspect.currentframe().f_code.co_name}() is running...")
                    function_name = inspect.currentframe().f_code.co_name
                    BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
                    loop = asyncio.new_event_loop()
                    asyncio.set_event_loop(loop)
                    loop.run_until_complete(crawl_geo_info())

                thread1 = threading.Thread(target=run_async_loop1)
                thread1.start()

                thread2 = threading.Thread(target=run_async_loop2)
                thread2.start()

                thread3 = threading.Thread(target=run_async_loop3)
                thread3.start()

                thread4 = threading.Thread(target=run_async_loop4)
                thread4.start()

                # 모든 쓰레드 끝날때 까지 대기
                thread1.join()
                thread2.join()
                thread3.join()
                thread4.join()

                BusinessLogicUtil.speak_ment_experimental(ment='날씨에 대한 웹크롤링 및 데이터 분석이 성공되었습니다', comma_delay=0.98)
                # 함수가 break 로 끝이 나면 창들이 창을 닫아야 dialog 들이 사라지도록 dialog 를 global 처리를 해두었음.
                global dialog4
                global dialog3
                global dialog2
                global dialog1
                dialog3 = UiUtil.CustomQdialog(title=f"{ment_about_naver_weather}", string=f"{results_about_naver_weather}")
                dialog2 = UiUtil.CustomQdialog(title=f"{title}", string=f"{results_about_nationwide_ultrafine_dust}")
                dialog1 = UiUtil.CustomQdialog(title=f"{ment_about_geo}", string=f"{results_about_geo}")
                dialog4 = UiUtil.CustomQdialog(title=f"{ment_about_pm_ranking}", string=f"{results_about_pm_ranking}")
                dialog1.show()
                dialog2.show()
                dialog3.show()
                dialog4.show()
                break
        except:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def back_up_biggest_pnxs():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.print_with_underline(f"biggest_pnxs에 대한 백업을 시도합니다")
        for biggest_target in StateManagementUtil.BIGGEST_PNXS:
            BusinessLogicUtil.compress_pnx_via_bz(f'{biggest_target}')

    @staticmethod
    def back_up_smallest_pnxs():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.print_with_underline(f"smallest_pnxs에 대한 백업을 시도합니다")
        for target in StateManagementUtil.SMALLEST_PNXS:
            BusinessLogicUtil.compress_pnx_via_bz(f'{target}')

    @staticmethod
    def classify_pnxs_between_smallest_pnxs_biggest_pnxs():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.print_with_underline(f'백업할 파일들의 크기를 분류합니다.')
        pnxs = [
            rf"{StateManagementUtil.USERPROFILE}\Desktop\services\helper-from-youtube-url-to-webm",
            rf"{StateManagementUtil.USERPROFILE}\Desktop\services",
        ]
        BusinessLogicUtil.print_with_underline(f'biggest_pnxs(300 메가 초과), smallest_pnxs(300 메가 이하) 분류 시도')
        for target in pnxs:
            target_size_megabite = BusinessLogicUtil.get_target_megabite(target.strip())
            print(target_size_megabite)
            if target_size_megabite <= 300:
                StateManagementUtil.SMALLEST_PNXS.append(target.strip())

            elif 300 < target_size_megabite:
                StateManagementUtil.BIGGEST_PNXS.append(target.strip())
            else:
                BusinessLogicUtil.print_cyan(f'{target.strip()}pass')

        BusinessLogicUtil.print_with_underline(f'smallest_target 출력')
        # pnxs 에서 biggest_pnxs 과 일치하는 것을 소거 시도
        smallest_pnxs = [i for i in pnxs if i not in StateManagementUtil.BIGGEST_PNXS]
        for target in StateManagementUtil.SMALLEST_PNXS:
            print(target)

        BusinessLogicUtil.print_with_underline(f'biggest_target 출력')
        for target in StateManagementUtil.BIGGEST_PNXS:
            print(target)
        pass

    @staticmethod
    def gather_pnxs_special():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        function_name_directory = rf"{StateManagementUtil.PROJECT_DIRECTORY}\{function_name}"  # function_name_directory 에 저장
        BusinessLogicUtil.make_pnx(pnx=function_name_directory, mode="d")
        BusinessLogicUtil.run_via_explorer_exe(function_name_directory, show_mode=False)
        if not BusinessLogicUtil.is_window_open(window_title_seg=function_name):
            BusinessLogicUtil.run_via_explorer_exe(function_name_directory, show_mode=False)

        starting_directory = BusinessLogicUtil.get_working_directory()

        dst = function_name_directory
        if not os.path.exists(dst):
            return
        services = os.path.dirname(dst)
        os.chdir(services)
        storages = []
        cmd = rf'dir /b /s "{StateManagementUtil.USERPROFILE}\Downloads"'
        lines = BusinessLogicUtil.command_to_os_like_person_as_admin(cmd)
        for line in lines:
            if line.strip() != "":
                storages.append(line.strip())

        BusinessLogicUtil.print_with_underline(rf'archive_py 는 storage 목록 에서 제외')
        withouts = ['archive_py']
        for storage in storages:
            for without in withouts:
                if BusinessLogicUtil.is_pattern_in_string(string=storage, pattern=without, with_case_ignored=False):
                    storages.remove(storage)
        for storage in storages:
            print(storage)

        BusinessLogicUtil.print_with_underline(rf'이동할 storage 목록 중간점검 출력 시도')
        for storage in storages:
            print(os.path.abspath(storage))

        if not storages:
            BusinessLogicUtil.print_with_underline(rf'이동할 storage 목록 이 없어 storage 이동을 할 수 없습니다')
        else:
            BusinessLogicUtil.print_with_underline(rf'이동할 storage 목록 출력 시도')
            for storage in storages:
                print(os.path.abspath(storage))
            BusinessLogicUtil.print_with_underline(rf'목적지 생성 시도')
            if not os.path.exists(dst):
                os.makedirs(dst)
            for storage in storages:
                # print(src)
                try:
                    BusinessLogicUtil.print_with_underline(rf'storage 이동 시도')
                    BusinessLogicUtil.move_pnx_without_overwrite(storage, dst)
                except FileNotFoundError:
                    BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

                except Exception as e:
                    BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

        os.chdir(starting_directory)

    @staticmethod
    def process_kill_via_hard_coded():
        nxs = [
            # "python.exe", # 프로그램 스스로를 종료시켜는 방법
            "alsong.exe",
            "cortana.exe",
            "mysqld.exe",
            "KakaoTalk.exe",
            "OfficeClickToRun.exe",
            "TEWebP.exe",
            "TEWeb64.exe",
            "TEWebP64.exe",
            "AnySign4PC.exe",
        ]
        for nx in nxs:
            BusinessLogicUtil.process_kill(img_name=nx)

    @staticmethod
    def run_up_and_down_game():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        correct_answer: int = random.randint(1, 100)
        left_oportunity: int = 10
        ment = f"<UP AND DOWN GAME>\n\nFIND CORRECT NUMBER"
        BusinessLogicUtil.speak_ment_experimental(ment=ment, comma_delay=1.0)

        dialog_btn_text_clicked, function, dialog_input_box_text = BusinessLogicUtil.should_i_do(
            string=ment,
            btns=["START", "EXIT"],
            function=None,
            auto_click_negative_btn_after_seconds=30,
            title=f"{function_name}()",
            return_mode=True,
            input_box_mode=False,
        )
        if dialog_btn_text_clicked != "START":
            return

        user_input = None
        is_game_strated = False
        btn_text_clicked = dialog_btn_text_clicked


        if btn_text_clicked == "START":
            ment = f"START IS PRESSED, LETS START GAME"
            BusinessLogicUtil.speak_ment_experimental(ment=ment, comma_delay=0.98, thread_join_mode=True)
            while left_oportunity >= 0:
                if left_oportunity == 0:
                    ment = f"LEFT CHANCE IS {left_oportunity} \nTAKE YOUR NEXT CHANCE."
                    BusinessLogicUtil.speak_ment_experimental(ment=ment, comma_delay=0.98)

                    dialog_btn_text_clicked, function, dialog_input_box_text = BusinessLogicUtil.should_i_do(
                        string=ment,
                        btns=["EXIT"],
                        function=None,
                        auto_click_negative_btn_after_seconds=None,
                        title=f"{function_name}()",
                        return_mode=True,
                        input_box_mode=True,
                    )
                    if dialog_btn_text_clicked == "EXIT":
                        return

                    break
                elif is_game_strated == False or user_input is None:

                    ment = f"TYPE NUMBER BETWEEN 1 TO 100"
                    if user_input is None:
                        ment = rf"{ment} AGAIN"
                    BusinessLogicUtil.speak_ment_experimental(ment=ment, comma_delay=0.98)
                    dialog_btn_text_clicked, function, dialog_input_box_text = BusinessLogicUtil.should_i_do(
                        string=ment,
                        btns=["SUBMIT", "EXIT"],
                        function=None,
                        auto_click_negative_btn_after_seconds=None,
                        title=f"{function_name}()",
                        return_mode=True,
                        input_box_mode=True,
                    )
                    if dialog_btn_text_clicked == "EXIT":
                        return

                    user_input = BusinessLogicUtil.is_user_input_required(dialog_input_box_text)
                    if user_input is not None:
                        left_oportunity = left_oportunity - 1
                    is_game_strated = True
                elif user_input == correct_answer:
                    ment = f"CONGRATULATIONS\n\nYOUR NUMBER IS {correct_answer}\nTHIS IS ANSWER\n\nSEE YOU AGAIN"
                    BusinessLogicUtil.speak_ment_experimental(ment=ment, comma_delay=0.98)

                    dialog_btn_text_clicked, function, dialog_input_box_text = BusinessLogicUtil.should_i_do(
                        string=ment,
                        btns=["SUBMIT", "EXIT"],
                        function=None,
                        auto_click_negative_btn_after_seconds=None,
                        title=f"{function_name}()",
                        return_mode=True,
                        input_box_mode=True,
                    )
                    if dialog_btn_text_clicked == "EXIT":
                        return

                elif correct_answer < user_input:
                    ment = f"YOUR NUMBER IS {user_input}\n\nYOU NEED DOWN\n\nYOUR LEFT CHANCE IS {left_oportunity}"
                    BusinessLogicUtil.speak_ment_experimental(ment=ment, comma_delay=0.98)

                    dialog_btn_text_clicked, function, dialog_input_box_text = BusinessLogicUtil.should_i_do(
                        string=ment,
                        btns=["SUBMIT", "EXIT"],
                        function=None,
                        auto_click_negative_btn_after_seconds=None,
                        title=f"{function_name}()",
                        return_mode=True,
                        input_box_mode=True,
                    )
                    if dialog_btn_text_clicked == "EXIT":
                        return

                    user_input = BusinessLogicUtil.is_user_input_required(dialog_input_box_text)
                    if user_input is not None:
                        left_oportunity = left_oportunity - 1
                elif correct_answer > user_input:
                    ment = f"YOUR NUMBER IS {user_input}\n\nYOU NEED UP\n\nYOUR LEFT CHANCE IS {left_oportunity}"
                    BusinessLogicUtil.speak_ment_experimental(ment=ment, comma_delay=0.98)

                    dialog_btn_text_clicked, function, dialog_input_box_text = BusinessLogicUtil.should_i_do(
                        string=ment,
                        btns=["SUBMIT", "EXIT"],
                        function=None,
                        auto_click_negative_btn_after_seconds=None,
                        title=f"{function_name}()",
                        return_mode=True,
                        input_box_mode=True,
                    )
                    if dialog_btn_text_clicked == "EXIT":
                        return

                    user_input = BusinessLogicUtil.is_user_input_required(dialog_input_box_text)
                    if user_input is not None:
                        left_oportunity = left_oportunity - 1
        else:
            return

    @staticmethod
    def thread_run_for_console_blurred_as_scheduler(q_application: QApplication):
        async def run_scheduler(q_application):
            # schedule.every(30).minutes.do(partial(BusinessLogicUtil.speak_after_x_min, 30))
            # schedule.every().tuesday.at("15:00").do(BusinessLogicUtil.speak_today_time_info)
            # schedule.every().wednesday.at("15:00").do(BusinessLogicUtil.speak_today_time_info)
            # schedule.every().thursday.at("15:00").do(BusinessLogicUtil.speak_today_time_info)
            # schedule.every().friday.at("15:00").do(BusinessLogicUtil.speak_today_time_info)
            # schedule.every().saturday.at("15:00").do(BusinessLogicUtil.speak_today_time_info)
            # schedule.every().sunday.at("15:00").do(BusinessLogicUtil.speak_today_time_info)
            # schedule.every(1).hour.do(BusinessLogicUtil.speak_server_hh_mm)
            # schedule.every(1).day.do(BusinessLogicUtil.speak_server_hh_mm)
            # schedule.every(1).day.at("12:30").do(BusinessLogicUtil.speak_server_hh_mm)
            # while True:
            # schedule.run_pending()
            # BusinessLogicUtil.print_as_log(f"async def {inspect.currentframe().f_code.co_name}() is running...")
            # await ....sleep(1000)
            BusinessLogicUtil.run_scheduler()
            pass

        def run_async_loop(q_application):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(run_scheduler(q_application))

        thread = threading.Thread(target=partial(run_async_loop, q_application))
        thread.start()

    @staticmethod
    def thread_run_for_console_blurred_as_gui(q_application: QApplication):
        # 비동기 이벤트 함수 설정 (simple for void async processing)
        async def run_rpa_program(q_application):
            dialog = UiUtil.CustomDialog(q_application=q_application, q_wiget=UiUtil.RpaProgramMainWindow(q_application=q_application), is_app_instance_mode=True)
            # dialog = UiUtil.CustomDialog(q_application=q_application, q_wiget=UiUtil.RpaProgramMainWindow(), is_app_instance_mode=True)
            # dialog = UiUtil.CustomDialog(q_application=q_application, q_wiget=UiUtil.RpaProgramMainWindow, is_app_instance_mode=True)

        # 비동기 이벤트 루프 설정 (simple for void async processing)
        def run_async_event_loop(q_application):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(run_rpa_program(q_application))

        # 비동기 이벤트 루프 실행할 쓰레드 설정 (simple for void async processing)
        thread_for_run_scheduler = threading.Thread(target=partial(run_async_event_loop, q_application))
        thread_for_run_scheduler.start()

    @staticmethod
    def run_scheduler():
        scheduler_loop_cnt = 0
        yyyy = TimeUtil.get_time_as_('%Y')
        while True:
            # mkr_매루프마다 # 매루프 루프에한번

            yyyy_previous_loop = yyyy
            yyyy = TimeUtil.get_time_as_('%Y')
            MM = TimeUtil.get_time_as_('%m')
            dd = TimeUtil.get_time_as_('%d')
            HH = TimeUtil.get_time_as_('%H')

            # mm, ss는 이건 매 작업마다 업데이트 해줘야 한다. 수정하자
            mm = TimeUtil.get_time_as_('%M')
            ss = TimeUtil.get_time_as_('%S')
            server_time = TimeUtil.get_time_as_(rf'%Y-%m-%d %H:%M:%S')

            # .. 시간을 순간 순간 로그처럼 가져와서 동작하도록 하는 것이 좋겠다. 일단 백업하고

            if scheduler_loop_cnt == 0:
                # mkr_스케쥴러_트리거 : 첫번째루프 #첫번쨰루프에서한번 #스케쥴러 실행 시 한번만

                # 아이스 브레이킹 멘트
                ice_breaking_ments = [
                    "오늘도 좋은 하루 되세요!",
                ]
                ice_breaking_ment = BusinessLogicUtil.get_element_random(items=ice_breaking_ments)
                ment = f'작업스케쥴러의 첫번째루프가 시작되었습니다, {ice_breaking_ment}!'
                BusinessLogicUtil.speak_ment_experimental(ment=ment, comma_delay=0.98, thread_join_mode=True)

                # mkr_스케쥴러_트리거 : 콘솔블러드 프로그램 시작시에만
                # BusinessLogicUtil.run_pnxs_via_hard_coded()
                # BusinessLogicUtil.guide_to_check_routines()

                # QThread 설정
                # thread = CustomQthread(q_application=q_application)
                # thread.finished.connect(lambda: Park4139BusinessLogicUtil.Tts.speak("QThread 작업이 성공되었습니다"))
                # thread.start()

                # 프로그램 외 전역감지 단축키 이벤트 설정
                # shortcut_keys_up_promised = {
                #     # "<ctrl>+h": partial(q_wiget.toogle_rpa_window, "<ctrl>+h"),  # fail
                #     "<ctrl>+A": BusinessLogicUtil.ask_something_to_ai, # fail
                # "<ctrl>+H": BusinessLogicUtil.단축키 목록 토글, # 이거 하나만이라도 되게 만들자. # 진짜 그래도 안되면 python rpa 프로그램을 따로 하나 더 띄우게 명령어를 설정하자.
                # BusinessLogicUtil.should_i_merge_directories,
                # BusinessLogicUtil.should_i_download_youtube_as_webm,
                # }
                # keyboard_main_listener = pynput.keyboard.GlobalHotKeys(shortcut_keys_up_promised)
                # keyboard_main_listener.start()

                # 윈도우 특정시간에 부팅되도록 설정하는 방법 알려줘
                # 리눅스로 윈도우 서버 부팅하는 법

                # mkr_스케쥴러_트리거 : 하루에 1번
                # 인사
                # unique_id = "already_said_about_today_greeting"
                # already_said_about_today_greeting = DbTomlUtil.select_db_toml(key=DbTomlUtil.get_db_toml_key(unique_id=unique_id))
                # if already_said_about_today_greeting is None:
                #     DbTomlUtil.insert_db_toml(key=DbTomlUtil.get_db_toml_key(unique_id=unique_id), value=False)
                #     already_said_about_today_greeting = DbTomlUtil.select_db_toml(key=DbTomlUtil.get_db_toml_key(unique_id=unique_id))
                # if already_said_about_today_greeting == False:
                #     ment = f'오늘도 좋은 하루 되세요!'
                #     BusinessLogicUtil.speak_ment_experimental(ment=ment, comma_delay=0.98, thread_join_mode=True)
                #     BusinessLogicUtil.should_i_do(ment=ment, auto_click_positive_btn_after_seconds=100)
                #     DbTomlUtil.update_db_toml(key=DbTomlUtil.get_db_toml_key(unique_id=unique_id), value=True)  # DB_TOML 업데이트
                # if BusinessLogicUtil.is_midnight():  # 자정이면 초기화
                #     DbTomlUtil.update_db_toml(key=DbTomlUtil.get_db_toml_key(unique_id=unique_id), value=False)  # 자정에 초기화 잘되면, 리펙토링 수행하자

                # BusinessLogicUtil.should_i_do(ment="요청된 불필요한 프로그램을 종료할까요?", function=BusinessLogicUtil.taskkill_useless_programs_via_hard_coded, auto_click_negative_btn_after_seconds=5)
                # BusinessLogicUtil.should_i_do(ment="백업할 타겟들을 크기에 따라 분류를 해둘까요?", function=BusinessLogicUtil.classify_pnxs_between_smallest_pnxs_biggest_pnxs, auto_click_positive_btn_after_seconds=10)
                # BusinessLogicUtil.should_i_do(ment="백업할 타겟들을 크기에 따라 분류를 해둘까요?", function=BusinessLogicUtil.classify_pnxs_between_smallest_pnxs_biggest_pnxs, auto_click_negative_btn_after_seconds=5)

            scheduler_loop_cnt = scheduler_loop_cnt + 1  # 루프 카운트 갱신
            BusinessLogicUtil.print_light_black(f"[scheduler_loop_cnt:{scheduler_loop_cnt}] [{TimeUtil.get_time_as_('%Y-%m-%d %H:%M:%S %f')}]")

            # # mkr_스케쥴러_트리거 : 하루에 24번
            # BusinessLogicUtil.back_up_pnxs_to_deprecated_via_text_file()

            # # mkr_0시에서 24시 사이, # 분단위 스케쥴,
            # if 0 <= int(HH) <= 24 and int(ss) == 0:
            #     BusinessLogicUtil.monitor_target_edited_and_back_up(target_pnx=StateManagementUtil.PARK4139_ARCHIVE_TOML)  # seconds_performance_test_results : ['11.95sec', '26.78sec', '11.94sec', '3.7sec', '11.72sec']
            #     if int(HH) == 6 and int(mm) == 30:
            #         # BusinessLogicUtil.speak_ments(f'{int(HH)} 시 {int(mm)}분 루틴을 시작합니다', sleep_after_play=0.65, thread_join_mode=True)  # 쓰레드가 많아지니 speak() 하면서 부정확한 재생이 늘어났다. 쓰레드의 정확한 타이밍 제어가 필요한 것 같다. 급한대로 thread_join_mode 를 만들었다)
            #         # BusinessLogicUtil.speak_ments(f'아침음악을 준비합니다, 아침음악을 재생할게요', sleep_after_play=0.65, thread_join_mode=True)
            #         pass
            #     if int(HH) == 7 and int(mm) == 30:
            #         # BusinessLogicUtil.speak_ments(f'{int(HH)} 시 {int(mm)}분 루틴을 시작합니다', sleep_after_play=0.65, thread_join_mode=True)
            #         # BusinessLogicUtil.speak_ments('지금 나가지 않는다면 지각할 수 있습니다, 더이상 나가는 것을 지체하기 어렵습니다', sleep_after_play=0.65, thread_join_mode=True)
            #         pass
            #
            #     if int(HH) == 8 and int(mm) == 50:
            #         # BusinessLogicUtil.speak_ments(f'{int(HH)} 시 {int(mm)}분 루틴을 시작합니다', sleep_after_play=0.65, thread_join_mode=True)
            #         # BusinessLogicUtil.speak_ments('업무시작 10분전입니다, 업무준비를 시작하세요, 업무 전에 세수와 양치는 하셨나요', sleep_after_play=0.65, thread_join_mode=True)
            #         pass
            #
            #     if int(HH) == 9:
            #         # BusinessLogicUtil.speak_ments(f'{int(mm)}시 정각, 루틴을 시작합니다', sleep_after_play=0.65, thread_join_mode=True)
            #         # BusinessLogicUtil.speak_ments('근무시간이므로 음악을 종료합니다', sleep_after_play=0.65, thread_join_mode=True)
            #         pass
            #     if int(HH) == 11 and int(mm) == 30:
            #         # # BusinessLogicUtil.speak_ments('용량이 큰 약속된 타겟들을 백업을 수행 시도합니다', sleep_after_play=0.65, thread_join_mode=True)
            #         # BusinessLogicUtil.back_up_biggest_pnxs()
            #         # # BusinessLogicUtil.speak_ments('용량이 작은 약속된 타겟들을 백업을 수행 시도합니다', sleep_after_play=0.65, thread_join_mode=True)
            #         # BusinessLogicUtil.back_up_smallest_pnxs()
            #         # # BusinessLogicUtil.speak_ments('흩어져있는 storage 들을 한데 모으는 시도를 합니다', sleep_after_play=0.65, thread_join_mode=True)
            #         # BusinessLogicUtil.gather_storages()
            #         pass
            #     if int(HH) == 22 and int(mm) == 10:
            #         BusinessLogicUtil.speak_ment_experimental('씻으실 것을 추천드립니다, 샤워루틴을 수행하실 것을 추천드립니다', comma_delay=0.98, thread_join_mode=True)  # 샤워루틴 확인창 띄우기
            #     if int(HH) == 22 and int(mm) == 30:
            #         BusinessLogicUtil.speak_ment_experimental('건강을 위해서 지금 씻고 주무실 것을 추천드려요', comma_delay=0.98, thread_join_mode=True)
            #         BusinessLogicUtil.speak_ment_experimental('건강을 위해서 24시에 최대 절전 모드에 예약이 되었습니다', comma_delay=0.98, thread_join_mode=True)
            #     if int(HH) == 23 and int(mm) == 55:
            #         BusinessLogicUtil.speak_ment_experimental('5분 뒤 최대 절전 모드로 진입합니다', comma_delay=0.98, thread_join_mode=True)
            #     if int(HH) == 24 and int(mm) == 0:
            #         BusinessLogicUtil.speak_ment_experimental(f'자정이 되었습니다', comma_delay=0.98, thread_join_mode=True)
            #         BusinessLogicUtil.speak_ment_experimental('최대 절전 모드에 진입합니다', comma_delay=0.98, thread_join_mode=True)
            #         BusinessLogicUtil.back_up_target(target_pnx=StateManagementUtil.SERVICE_DIRECTORY)
            #         BusinessLogicUtil.enter_power_saving_mode()
            #     if int(HH) == 2 and int(mm) == 0:
            #         BusinessLogicUtil.speak('새벽 두시입니다', after_delay=0.55)
            #         BusinessLogicUtil.speak('지금부터 예약된 최대 절전 모드에 진입합니다', after_delay=1)
            #     if int(mm) % 15 == 0:
            #         # BusinessLogicUtil.speak_ments(f'15분 간격 루틴을 시작합니다', sleep_after_play=0.65, thread_join_mode=True)
            #         # BusinessLogicUtil.speak_ments(f'랜덤 스케줄을 시작합니다', sleep_after_play=0.65, thread_join_mode=True)
            #         BusinessLogicUtil.do_random_schedules()
            #         # BusinessLogicUtil.speak_ments(f'프로젝트 디렉토리 싱크를 시작합니다', sleep_after_play=0.65, thread_join_mode=True)
            #     if int(mm) % 30 == 0:
            #         # BusinessLogicUtil.speak_ments(f'30분 간격 루틴을 시작합니다', sleep_after_play=0.65, thread_join_mode=True)
            #         # BusinessLogicUtil.speak_ments(f'깃허브로 파이썬 아카이브 프로젝트 백업을 시도합니다', sleep_after_play=0.65, thread_join_mode=True)
            #         # BusinessLogicUtil.git_push_by_auto()
            #         BusinessLogicUtil.monitor_target_edited_and_sync(target_pnx=StateManagementUtil.SERVICE_DIRECTORY)  # seconds_performance_test_results : ['28.46sec', '27.53sec', '2.85sec', '2.9sec', '2.91sec']
            #     if int(mm) % 60 == 0:
            #         # BusinessLogicUtil.speak_ments(f'1시간 간격 루틴을 시작합니다', sleep_after_play=0.65, thread_join_mode=True)
            #         BusinessLogicUtil.should_i_do(ment="쓰레기통을 비울까요?", function=BusinessLogicUtil.empty_recycle_bin, auto_click_negative_btn_after_seconds=10)
            #         BusinessLogicUtil.should_i_do(ment="오늘 시간정보를 말씀드릴까요?", function=BusinessLogicUtil.speak_today_time_info, auto_click_negative_btn_after_seconds=10)
            #         BusinessLogicUtil.monitor_target_edited_and_sync(target_pnx=StateManagementUtil.SERVICE_DIRECTORY)  # seconds_performance_test_results : ['28.46sec', '27.53sec', '2.85sec', '2.9sec', '2.91sec']

            # mkr_ 23시에서 5시 사이, 30초 마다
            # if (23 <= int(HH) <= 24 or 0 <= int(HH) <= 5) and int(ss) % 30 == 0:
            #     BusinessLogicUtil.guide_to_sleep() #최대절전모드 가이드

            # mkr_특정시간에 한번
            # if BusinessLogicUtil.is_same_time(time1=server_time, time2=datetime(year=2024, month=10, day=31, hour=22, minute=27 , second=0)):
            #     # mkr
            #     if "" not in file:
            #     BusinessLogicUtil.print_as_gui(ment="약속된 시간이 되었습니다.")

            # mkr_매시간 한시간에한번
            #     랜덤미션
            #      BusinessLogicUtil.do_random_schedules()

            # mkr_매일 하루한번

            # 매년 1년에 한번 1월 1일이고 인사안했으면 인사하기 인사하고 인사했다고 기록하기
            # BusinessLogicUtil.remove_target_parmanently(StateManagementUtil.SCHECLUER_CFG)
            MM = 1
            dd = 1
            if int(MM) == 1 and int(dd) == 1:
                cfg_file = StateManagementUtil.SCHECLUER_YAML
                BusinessLogicUtil.make_pnx(cfg_file, mode="f")
                memo_done = rf'[new_year_greeting] {yyyy}_{MM}_{dd} [done]'

                # cfg_file의 내용 읽기
                lines = BusinessLogicUtil.get_list_from_f_txt(cfg_file)

                checklist = []
                if lines:  # 파일이 비어있지 않다면
                    for line in lines:
                        if memo_done in line:
                            checklist.append(line)

                # BusinessLogicUtil.print_magenta(rf'''checklist = {checklist}''')
                # BusinessLogicUtil.print_magenta(rf'''len(checklist) = {len(checklist)}''')

                if len(checklist) == 0:
                    ment = f'{yyyy} 신년입니다! 새해에는 반드시 좋은일이 가득하시길 바랄게요!!'
                    BusinessLogicUtil.print_light_black(ment)

                    # 메모를 파일에 추가 기록
                    with open(cfg_file, 'a') as file:
                        file.write(memo_done + f" [{TimeUtil.get_time_as_('%Y-%m-%d %H:%M:%S')}]\n")

            # 크리스마스 축하 인사하기
            if BusinessLogicUtil.is_christmas():
                ment = f'{yyyy}년 크리스마스입니다! 즐거운 크리스마스 되세요!'
                # unique_id = "already_said_about_christmas_today"
                # already_said_about_christmas_today = DbTomlUtil.select_db_toml(key=DbTomlUtil.get_db_toml_key(unique_id=unique_id))
                # if already_said_about_christmas_today is None:
                #     DbTomlUtil.insert_db_toml(key=DbTomlUtil.get_db_toml_key(unique_id=unique_id), value=False)
                #     already_said_about_christmas_today = DbTomlUtil.select_db_toml(key=DbTomlUtil.get_db_toml_key(unique_id=unique_id))
                # if already_said_about_christmas_today == False:
                #     print(ment)
                #     DbTomlUtil.update_db_toml(key=DbTomlUtil.get_db_toml_key(unique_id=unique_id), value=True)  # DB_TOML 업데이트
                # if BusinessLogicUtil.is_midnight():  # 자정이면 초기화
                #     DbTomlUtil.update_db_toml(key=DbTomlUtil.get_db_toml_key(unique_id=unique_id), value=False)
                BusinessLogicUtil.speak_ment_without_async_experimental_2(ment_string=ment)

            # 매월 월에한번
            #     DbTomlUtil.update_db_toml(key=DbTomlUtil.get_db_toml_key(unique_id=unique_id), value=False)

            # 1년에 한번 수행 아이디어
            # random_schedule.json 에서 leaved_max_count를 읽어온다
            # leaved_max_count=1 이면 년에 1번 수행 하도록
            # leaved_max_count=10 이면 년에 10번 수행 하도록
            # leaved_max_count=0 이면 올해에는 더이상 수행하지 않음
            # leaved_max_count 를 random_schedule_tb.toml 에 저장

            # - 1시간 뒤 시스템 종료 예약 기능
            # - 즉시 시스템 종료 시도 기능
            # - 시간 시현기능 기능(autugui 이용)
            #   ment ='pc 정밀검사를 한번 수행해주세요'
            #   print_as_log(ment)
            # - 하드코딩된 스케줄 작업 수행 기능
            # - 미세먼지 웹스크래핑 기능
            # - 초미세먼지 웹스크래핑 기능
            # - 종합날씨 웹스크래핑 기능
            # - 습도 웹스크래핑 기능
            # - 체감온도 웹스크래핑 기능
            # - 현재온도 웹스크래핑 기능
            # - 음악재생 기능
            # - 영상재생 기능

    @staticmethod
    def run_console_blurred():
        while True:
            # colorama 초기화, 이거 프로젝트의 root 근처의 상단에 설정 해두어야 함. 재호출 될때 많이엄청느려진다. root 근처에서 호출되는게 아니라, colorma 호출 직전 초기화 되도록 수정하였음.
            # init(autoreset=True)
            # init(autoreset=True)

            pyautogui.FAILSAFE = False
            q_application = QApplication(sys.argv)

            # 프로그램 코어진입 with 프로그램실행동의요청
            # dialog = UiUtil.CustomDialog(q_application=q_application, q_wiget=UiUtil.CustomQdialog(ment=f"다음의 프로젝트 디렉토리에서 자동화 프로그램이 시작됩니다\n{StateManagementUtil.PROJECT_DIRECTORY}", btns=["실행동의", "실행하지 않기"], auto_click_positive_btn_after_seconds=10), is_app_instance_mode=True)
            # if dialog.btn_text_clicked == "실행동의":
            #     print(StateManagementUtil.PROJECT_DIRECTORY)
            #     os.chdir(StateManagementUtil.PROJECT_DIRECTORY)
            #     BusinessLogicUtil.run_console_blurred_core_as_scheduler(q_application)
            # if dialog.btn_text_clicked == "실행하지 않기":
            #     sys.exit()

            # 프로그램 코어진입 without 프로그램실행동의요청
            window = UiUtil.RpaProgramMainWindow(q_application)
            q_application.exec()

            break

    @staticmethod
    def is_christmas():
        import datetime
        today = datetime.datetime.now()
        christmas = datetime.datetime(year=today.year, month=12, day=25)
        if today == christmas:
            return True
        else:
            return False

    @staticmethod
    def is_same_time(time1, time2):
        time2.strftime(rf'%Y-%m-%d %H:%M:%S')
        # print(rf'time1 : {time1} , time2 : {time2}')
        if time1 == time2:
            return True
        else:
            return False

    @staticmethod
    def is_midnight():
        import datetime
        now = datetime.datetime.now()
        if now.hour == 0 and now.minute == 0 and now.second == 0:
            return True
        else:
            return False

    @staticmethod
    def crawl_html_href(url: str):
        BusinessLogicUtil.print_ment_via_colorama(f"{StateManagementUtil.UNDERLINE}{inspect.currentframe().f_code.co_name}", colorama_color=ColoramaUtil.BLUE)
        # 최하단으로 스크롤 이동 처리를 추가로 해야함. 그렇지 않으면 기대하는 모든 영상을 크롤링 할 수 없음..귀찮..지만 처리했다.

        browser_show_mode = False

        # url 전처리
        url = url.strip()

        # driver 설정
        BusinessLogicUtil.print_ment_via_colorama(f"BusinessLogicUtil.get_driver_selenium(browser_show_mode=True) 수행 중...", colorama_color=ColoramaUtil.BLUE)
        driver = BusinessLogicUtil.get_driver_selenium(browser_show_mode=browser_show_mode)

        BusinessLogicUtil.print_ment_via_colorama(f"driver.get(target_url) 수행 중...", colorama_color=ColoramaUtil.BLUE)
        target_url = url
        driver.get(target_url)

        # 자동제어 브라우저 화면 초기 로딩 random.randint(1,n) 초만큼 명시적 대기
        n = 2
        seconds = random.randint(1, n)
        BusinessLogicUtil.print_ment_via_colorama(f"자동제어 브라우저 화면 초기 로딩 중... {seconds} seconds", colorama_color=ColoramaUtil.BLUE)
        driver.implicitly_wait(seconds)  # 처음페이지 로딩이 끝날 때까지 약 random.randint(1,n)초 대기

        # 최하단으로 자동 스크롤, 페이지 최하단에서 더이상 로딩될 dom 객체가 없을 때 까지
        BusinessLogicUtil.print_ment_via_colorama("스크롤 최하단으로 이동 중...", colorama_color=ColoramaUtil.BLUE)
        scroll_cnt = 0
        previous_scroll_h = None
        current_scroll_h = None
        scroll_maxs_monitored = []
        while True:
            if current_scroll_h is not None and previous_scroll_h is not None:
                if previous_scroll_h == current_scroll_h:
                    scroll_maxs_monitored.append(True)
                    # break

            # 로딩타이밍 제어가 어려워 추가한 코드. n번 모니터링.
            n = 6  # success
            if len(scroll_maxs_monitored) == n:
                if all(scroll_maxs_monitored) == True:  # [bool] bool list 내 요소가 모두 true 인지 확인
                    BusinessLogicUtil.print_ment_via_colorama(ment="스크롤 최하단으로 이동되었습니다", colorama_color=ColoramaUtil.BLUE)
                    break

            # previous_scroll_h 업데이트
            # previous_scroll_h = driver.execute_script("return document.body.scrollHeight")
            previous_scroll_h = driver.execute_script("return document.documentElement.scrollHeight")

            # 가능한만큼 스크롤 최하단으로 이동
            # driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.PAGE_DOWN)  # page_down 을 누르는 방법, success
            # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")# JavaScript 로 스크롤 최하단으로 이동, 네이버용 코드?
            driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")  # JavaScript 로 스크롤 최하단으로 이동, 유튜브용 코드?
            # time.sleep(2)  # 스크롤에 의한 추가적인 dom 객체 로딩 대기, 여러가지 예제를 보니, 일반적으로 2 초 정도 두는 것 같음. 2초 내에 로딩이 되지 않을 때도 있는데.
            BusinessLogicUtil.sleep(milliseconds=500, show_mode=False)  # 스크롤에 의한 추가적인 dom 객체 로딩 대기, success, 지금껏 문제 없었음.

            # previous_scroll_h = driver.execute_script("return document.body.scrollHeight")
            current_scroll_h = driver.execute_script("return document.documentElement.scrollHeight")

            scroll_cnt = scroll_cnt + 1

            BusinessLogicUtil.print_ment_via_colorama(f'{scroll_cnt}번 째 스크롤 성공 previous_scroll_h : {previous_scroll_h} current_scroll_h : {current_scroll_h}   previous_scroll_h==current_scroll_h : {previous_scroll_h == current_scroll_h}', colorama_color=ColoramaUtil.BLUE)

        page_src = driver.page_source
        soup = BeautifulSoup(page_src, "lxml")
        driver.close()

        # 모든 태그 가져오기
        # tags = soup.find_all()
        # for tag in tags:
        #     print(tag)

        # body 리소스 확인 : success
        # bodys = soup.find_all("body")
        # for body in bodys:
        #     print(f"body:{body}")

        # 이미지 태그 크롤링
        # images = soup.find_all("img")
        # for img in images:
        #     img_url = img.get("src")
        #     print("Image URL:", img_url)
        #
        # 스크립트 태그 크롤링
        # scripts = soup.find_all("script")
        # for script in scripts:
        #     script_url = script.get("src")
        #     print("Script URL:", script_url)
        #
        # # 스타일시트 크롤링
        # stylesheets = soup.find_all("link", rel="stylesheet")
        # for stylesheet in stylesheets:
        #     stylesheet_url = stylesheet.get("href")
        #     print("Stylesheet URL:", stylesheet_url)

        # 특정 태그의 class 가 "어쩌구" 인
        # div_tags = soup.find_all("div", class_="어쩌구")

        # a 태그 크롤링
        # a_tags = soup.find_all("a")
        # results = ""
        # for a_tag in a_tags:
        #     hrefs = a_tag.get("href")
        #     if hrefs is not None and hrefs != "":
        #         # print("href", hrefs)
        #         results = f"{results}{hrefs}\n"

        # 변수에 저장 via selector
        # name = soup.select('a#video-title')
        # video_url = soup.select('a#video-title')
        # view = soup.select('a#video-title')

        # name, video_url 에 저장 via tag_name and id
        name = soup.find_all("a", id="video-title")
        video_url = soup.find_all("a", id="video-title")

        # 유튜브 주소 크롤링 및 진행률 표시 via tqdm, 14 초나 걸리는데. 성능이 필요할때는 여러개의 thread 로 처리해보자.
        a_tags = soup.find_all("a")

        # success
        # BusinessLogicUtil.debug_as_gui(f"{len(a_tags)}")

        # results를 str으로 처리
        # results = ""
        # a_tags_cnt  = 0
        # with tqdm(total=total_percent,ncols = 79 , desc= "웹 크롤링 진행률") as process_bar:
        #     for a_tag in a_tags:
        #         hrefs = a_tag.get("href")
        #         if hrefs is not None and hrefs != "" and "/watch?v=" in hrefs :
        #             if hrefs not in results:
        #                 results = f"{results}{hrefs}\n"
        #                 a_tags_cnt = a_tags_cnt + 1
        #         time.sleep(0.06)
        #         process_bar.update(total_percent/len(a_tags))

        # fail
        # if process_bar.total == 90:
        #     BusinessLogicUtil.speak_ments(ment='웹 크롤링이 90퍼센트 진행되었습니다. 잠시만 기다려주세요', sleep_after_play=0.65)

        # results를 list 으로 처리, list 으로만 처리하고 str 으로 변형하는 처리를 추가했는데 3초나 빨라졌다. 항상 list 로 처리를 하자.
        results = []
        a_tags_cnt = 0
        for a_tag in a_tags:
            hrefs = a_tag.get("href")
            if hrefs is not None and hrefs != "" and "/watch?v=" in hrefs:
                if hrefs not in results:
                    results.append(hrefs)
                    a_tags_cnt = a_tags_cnt + 1
        results = DataStructureUtil.add_prefix_to_string_list(results, 'https://www.youtube.com')  # string list 의 요소마다 suffix 추가
        results = "\n".join(results)  # list to str

        # fail
        # dialog = UiUtil.CustomQdialog(title=f"크롤링결과보고", ment=f"{results}", btns=[MentsUtil.YES], auto_click_positive_btn_after_seconds="")
        # dialog.exec()

        # fail
        # UiUtil.pop_up_as_complete(title="크롤링결과보고", ment=f"{results}")

        # success
        # BusinessLogicUtil.debug_as_gui(f"{results}") # 테스트용 팝업    UiUtil 로 옮기는 게 나을 지 고민 중이다.

        # success
        # 비동기로 진행 가능
        global dialog
        dialog = UiUtil.CustomQdialog(title=f"크롤링결과보고", string=f"({a_tags_cnt}개 추출됨)\n\n{results}")
        dialog.show()

    @staticmethod
    def crawl_youtube_video_title_and_url(url: str):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        browser_show_mode = False

        # url 전처리
        url = url.strip()

        # driver 설정
        total_percent = 100
        driver = BusinessLogicUtil.get_driver_selenium(browser_show_mode=browser_show_mode)
        with tqdm(total=total_percent, ncols=79, desc="driver 설정 진행률") as process_bar:
            global title
            title = 'html  href 크롤링 결과'
            target_url = url
            driver.get(target_url)
            page_src = driver.page_source
            soup = BeautifulSoup(page_src, "lxml")
            time.sleep(0.0001)
            process_bar.update(total_percent)
        driver.close()

        # 변수에 저장 via tag_name and id
        name = soup.find_all("a", id="video-title")
        video_url = soup.find_all("a", id="video-title")

        # list 에 저장
        name_list = []
        url_list = []
        # view_list = []
        for i in range(len(name)):
            name_list.append(name[i].text.strip())
            # view_list.append(view[i].get('aria-label').split()[-1])
        for i in video_url:
            url_list.append('{}{}'.format('https://www.youtube.com', i.get('href')))

        # dict 에 저장
        # youtubeDic = {
        #     '제목': name_list,
        #     '주소': url_list,
        #     # '조회수': view_list
        # }

        # csv 에 저장
        # import pandas as pd
        # youtubeDf = pd.DataFrame(youtubeDic)
        # youtubeDf.to_csv(f'{keyword}.csv', encoding='', index=False)

        # str 에 저장
        results_list = []
        for index, url in enumerate(url_list):
            results_list.append(f"{name_list[index]}   {url_list[index]}")
        results_str = "\n".join(results_list)  # list to str

        # fail
        # dialog = UiUtil.CustomQdialog(title=f"크롤링결과보고", ment=f"{results}", btns=[MentsUtil.YES], auto_click_positive_btn_after_seconds="")
        # dialog.exec()

        # fail
        # UiUtil.pop_up_as_complete(title="크롤링결과보고", ment=f"{results}")

        # success
        # BusinessLogicUtil.debug_as_gui(f"{results}") # 테스트용 팝업    UiUtil 로 옮기는 게 나을 지 고민 중이다.

        # success
        # 비동기로 진행 가능
        global dialog
        dialog = UiUtil.CustomQdialog(title=f"크롤링결과보고", string=f"({len(url_list)}개 url 추출됨)\n\n{results_str}")
        dialog.show()

    @staticmethod
    def crawl_youtube_playlist(url: str):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        browser_show_mode = False

        # url 전처리
        url = url.strip()

        # driver 설정
        total_percent = 100
        driver = BusinessLogicUtil.get_driver_selenium(browser_show_mode=browser_show_mode)
        with tqdm(total=total_percent, ncols=79, desc="driver 설정 진행률") as process_bar:
            global title
            title = 'html  href 크롤링 결과'
            target_url = url
            driver.get(target_url)
            page_src = driver.page_source
            soup = BeautifulSoup(page_src, "lxml")
            time.sleep(0.0001)
            process_bar.update(total_percent)
        driver.close()

        # 변수에 저장 via tag_name and href
        names = soup.find_all("a", id="video-title")
        hrefs = soup.find_all("a", id="video-title")
        # hrefs = copy.deepcopy(names)

        # list 에 저장
        name_list = []
        hrefs_list = []
        # view_list = []
        for i in range(len(names)):
            name_list.append(names[i].text.strip())
            # view_list.append(view[i].get('aria-label').split()[-1])
        for i in hrefs:
            hrefs_list.append('{}{}'.format('https://www.youtube.com', i.get('href')))

        # str 에 저장
        results_list = []
        for index, url in enumerate(hrefs_list):
            # results_list.append(f"{name_list[index]}   {hrefs_list[index]}")
            results_list.append(f"{hrefs_list[index]}")  # href 만 출력
        results_str = "\n".join(results_list)  # list to str

        # fail
        # dialog = UiUtil.CustomQdialog(title=f"크롤링결과보고", ment=f"{results}", btns=[MentsUtil.YES], auto_click_positive_btn_after_seconds="")
        # dialog.exec()

        # fail
        # UiUtil.pop_up_as_complete(title="크롤링결과보고", ment=f"{results}")

        # success
        # BusinessLogicUtil.debug_as_gui(f"{results}") # 테스트용 팝업    UiUtil 로 옮기는 게 나을 지 고민 중이다.

        # success
        # 비동기로 진행 가능
        global dialog
        dialog = UiUtil.CustomQdialog(title=f"크롤링결과보고", string=f"({len(hrefs_list)}개 playlist 추출됨)\n\n{results_str}")
        dialog.show()

    @staticmethod
    def should_i_crawl_a_tag_href():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:

            url = ""

            dialog = UiUtil.CustomQdialog(string="해당 페이지의 href 를 크롤링할까요?", btns=[MentsUtil.YES, MentsUtil.NO], input_box_mode=True, input_box_text_default=url)
            dialog.exec()
            btn_text_clicked = dialog.btn_text_clicked

            if btn_text_clicked == MentsUtil.YES:
                BusinessLogicUtil.crawl_html_href(url=dialog.input_box.text())
                break
            else:
                break

    @staticmethod
    def should_i_crawl_youtube_video_title_and_url():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:

            # 테스트용
            keyword = 'blahblah'
            url = f'https://www.youtube.com/results?search_query={keyword}'

            dialog = UiUtil.CustomQdialog(string="해당 페이지의 video title, video url을 크롤링할까요?", btns=[MentsUtil.YES, MentsUtil.NO], input_box_mode=True, input_box_text_default=url)
            dialog.exec()
            btn_text_clicked = dialog.btn_text_clicked

            if btn_text_clicked == MentsUtil.YES:
                BusinessLogicUtil.crawl_youtube_video_title_and_url(url=dialog.input_box.text())
                break
            else:
                break

    @staticmethod
    def should_i_crawl_youtube_playlist():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            # 테스트용
            keyword = 'blahblah'
            url = f'https://www.youtube.com/@{keyword}/playlists'

            dialog = UiUtil.CustomQdialog(string="해당 페이지의 video title, video url을 크롤링할까요?", btns=[MentsUtil.YES, MentsUtil.NO], input_box_mode=True, input_box_text_default=url)
            dialog.exec()
            btn_text_clicked = dialog.btn_text_clicked

            if btn_text_clicked == MentsUtil.YES:
                BusinessLogicUtil.crawl_youtube_playlist(url=dialog.input_box.text())
                break
            else:
                break

    @staticmethod
    def print_json_via_jq_pkg(json_str=None, json_file=None, json_list=None):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        if platform.system() == 'Windows':
            if BusinessLogicUtil.get_count_none_of_list([json_str, json_file, json_list]) == 2:  # 2개가 NONE이면 1나는 BINDING 된것으로 판단하는 로직
                if json_str is not None:
                    # lines = BusinessLogicUtil.run_via_cmd_exe(cmd=rf'echo "{json_str}" | {StateManagementUtil.JQ_WIN64_EXE} "."') # 나오긴 하는데 한줄로 나온다
                    # lines = BusinessLogicUtil.run_via_cmd_exe(cmd=rf'echo "{json_str}" | python -mjson.tool ')# 나오긴 하는데 한줄로 나온다
                    # [BusinessLogicUtil.print_as_success(line) for line in lines]
                    json_str = json.dumps(json_str, indent=4)  # json.dumps() 함수는 JSON 데이터를 문자열로 변환하는 함수이며, indent 매개변수를 사용하여 들여쓰기를 설정하여 json 형태의 dict 를 예쁘게 출력할 수 있습니다.
                    BusinessLogicUtil.print_light_white(json_str)
                if json_file is not None:
                    lines = BusinessLogicUtil.command_to_os_like_person_as_admin(command=rf"type {json_file} | {StateManagementUtil.JQ_WIN64_EXE} ")
                    [BusinessLogicUtil.print_light_white(line) for line in lines]
                if json_list is not None:
                    lines = BusinessLogicUtil.command_to_os_like_person_as_admin(command=rf'echo "{json_list}" | "{StateManagementUtil.JQ_WIN64_EXE}" ')
                    [BusinessLogicUtil.print_light_white(line) for line in lines]
            else:
                BusinessLogicUtil.print_red(string=rf"{inspect.currentframe().f_code.co_name}() 를 사용하려면 json_str/json_file/json_list 파라미터들 중 둘 중 하나만 데이터바인딩이 되어야합니다")
        else:
            print("리눅스 시스템에서 아직 지원되지 않는 함수입니다")

    @staticmethod
    def should_i_explorer():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            dialog = UiUtil.CustomQdialog(string="해당위치의 타겟을 실행할까요?", btns=[MentsUtil.YES, MentsUtil.NO], input_box_mode=True, input_box_text_default=clipboard.paste())
            dialog.exec()
            btn_text_clicked = dialog.btn_text_clicked
            input_box_text = dialog.input_box.text()
            if btn_text_clicked == MentsUtil.YES:
                pnx = input_box_text
                command = rf"explorer {pnx}"
                BusinessLogicUtil.command_to_os(cmd=command, show_mode=False, mode="a")
                break
            else:
                break

    @staticmethod
    def should_i_sync():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # text_promised = clipboard.paste()
        text_promised = StateManagementUtil.PROJECT_PARENTS_DIRECTORY
        while True:
            dialog = UiUtil.CustomQdialog(string="해당위치의 타겟을 싱크할까요?", btns=[MentsUtil.YES, MentsUtil.NO], input_box_mode=True, input_box_text_default=text_promised)
            dialog.exec()
            btn_text_clicked = dialog.btn_text_clicked

            # dialog_input_box_text 에 데이터 저장
            dialog_input_box_text = dialog.input_box.text()

            # dialog_input_box_text 데이터 전처리
            # "  C:\projects\services  " -> "C:\projects\services"
            dialog_input_box_text = dialog_input_box_text.strip()
            # "C:\projects\services" -> C:\projects\services
            if dialog_input_box_text.startswith("\""):
                if dialog_input_box_text.endswith("\""):
                    dialog_input_box_text = dialog_input_box_text.replace("\"", "", 1)
                    # dialog_input_box_text = dialog_input_box_text[:-(len("\""))] + "${add suffix test}" # 이코드는 add suffix 만들 때 활용하자
                    dialog_input_box_text = dialog_input_box_text[:-(len("\""))] + ""

            target_pnx = dialog_input_box_text
            target_pnx_sync = rf"{target_pnx}_sync"
            target_pnx_sync_zip = rf"{target_pnx}_sync.zip"

            if btn_text_clicked == MentsUtil.YES:
                BusinessLogicUtil.sync_directory_local(target_pnx=target_pnx)
                break
            else:
                break

    @staticmethod
    def should_i_sync_V_0_0_2():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # text_promised = clipboard.paste()
        text_promised = StateManagementUtil.PROJECT_PARENTS_DIRECTORY
        while True:
            dialog = UiUtil.CustomQdialog(string="해당위치의 타겟을 싱크할까요?", btns=[MentsUtil.YES, MentsUtil.NO], input_box_mode=True, input_box_text_default=text_promised)
            dialog.exec()
            btn_text_clicked = dialog.btn_text_clicked

            # dialog_input_box_text 에 데이터 저장
            dialog_input_box_text = dialog.input_box.text()
            dialog_input_box_text = dialog_input_box_text.strip()
            if dialog_input_box_text.startswith("\""):
                if dialog_input_box_text.endswith("\""):
                    dialog_input_box_text = dialog_input_box_text.replace("\"", "", 1)
                    dialog_input_box_text = dialog_input_box_text[:-(len("\""))] + ""

            target_pnx = dialog_input_box_text
            target_pnx_sync = rf"{target_pnx}_sync"
            target_pnx_sync_zip = rf"{target_pnx}_sync.zip"

            if btn_text_clicked == MentsUtil.YES:
                BusinessLogicUtil.upzip_pnx(pnx=target_pnx_sync_zip)
                BusinessLogicUtil.sync_directory_local(target_pnx=target_pnx)
                BusinessLogicUtil.back_up_target_without_timestamp(target_pnx=target_pnx_sync)
                break
            else:
                break

    @staticmethod
    def download_video_from_web2():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        while True:
            file_png = rf"{StateManagementUtil.PROJECT_DIRECTORY}\pkg_png\download_video_via_chrome_extensions1.png"
            is_image_finded = BusinessLogicUtil.click_center_of_img_recognized_by_mouse_left(img_pnx=file_png, loop_limit_cnt=100)
            if is_image_finded:
                BusinessLogicUtil.sleep(30)
                BusinessLogicUtil.press("ctrl", "f")
                BusinessLogicUtil.press("end")
                BusinessLogicUtil.press("ctrl", "a")
                BusinessLogicUtil.press("backspace")
                BusinessLogicUtil.write_fast("save")
                BusinessLogicUtil.press("enter")
                BusinessLogicUtil.press("enter")
                BusinessLogicUtil.press("esc")
                BusinessLogicUtil.press("enter")
                file_png = rf"{StateManagementUtil.PROJECT_DIRECTORY}\pkg_png\download_video_via_chrome_extensions2.png"
                is_image_finded = BusinessLogicUtil.click_center_of_img_recognized_by_mouse_left(img_pnx=file_png, loop_limit_cnt=100)
                if is_image_finded:
                    BusinessLogicUtil.press("shift", "w")
                else:
                    BusinessLogicUtil.speak_ment_experimental(ment="이미지를 찾을 수 없어 해당 자동화 기능을 마저 진행할 수 없습니다", comma_delay=0.98)
            else:
                BusinessLogicUtil.speak_ment_experimental(ment="이미지를 찾을 수 없어 해당 자동화 기능을 마저 진행할 수 없습니다", comma_delay=0.98)
            break
        pass

    @staticmethod
    def gather_pnxs_empty(src: str, show_mode):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        dst = rf"D:\pkg_classified\pkg_empty"
        BusinessLogicUtil.make_pnx(pnx=dst, mode="d")

        if os.path.isdir(src):
            for dirpath, dirnames, filenames in os.walk(src, topdown=False):
                if not dirnames and not filenames:
                    if os.path.isdir(dirpath):
                        BusinessLogicUtil.is_empty_directory(dirpath, show_mode=show_mode)
                        BusinessLogicUtil.move_pnx_without_overwrite(src=dirpath, dst=dst)

        # 빈 트리 리프디렉토리별로 해체한 뒤 제거
        for index, directory in enumerate(src):
            if BusinessLogicUtil.is_empty_tree(directory, show_mode=False):
                for root, directories, files in os.walk(directory, topdown=True):
                    for directory in directories:
                        directory = os.path.abspath(os.path.join(root, directory))
                        if BusinessLogicUtil.is_leaf_directory(directory, show_mode=False):
                            BusinessLogicUtil.move_pnx_without_overwrite(src=directory, dst=dst)

        BusinessLogicUtil.make_pnx(pnx=dst, mode="d")
        if os.path.isdir(src):
            for dirpath, dirnames, filenames in os.walk(src, topdown=False):
                if not dirnames and not filenames:
                    if os.path.isdir(dirpath):
                        BusinessLogicUtil.is_empty_directory(dirpath, show_mode=False)
                        BusinessLogicUtil.move_pnx_without_overwrite(src=dirpath, dst=dst)

        BusinessLogicUtil.print_as_log(string=rf'''dst="{dst}" %%%FOO%%%''')

    @staticmethod
    def is_containing_special_characters(text: str, ignore_list: [str] = None):
        pattern = "[~!@#$%^&*()_+|<>?:{}]"  # , 는 제외인가?
        if ignore_list is not None:
            for exception in ignore_list:
                pattern = pattern.replace(exception, "")
        if re.search(pattern, text):
            return True

    @staticmethod
    def get_kor_from_eng(english_word: str):
        translating_dictionary = {
            "id": "아이디",
            "pw": "패스워드",
            "e mail": "이메일",
        }
        result = ""
        try:
            result = translating_dictionary[english_word]
        except:
            result = english_word
        return result

    @staticmethod
    def raise_exception_after_special_charcater_check(value, inspect_currentframe_f_code_co_name, ignore_list: [str] = None):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        if BusinessLogicUtil.is_containing_special_characters(value, ignore_list):
            word_english = inspect_currentframe_f_code_co_name
            word_english = word_english.replace('validate_', "")
            word_english = word_english.replace("_", " ")
            word_english = word_english.strip()
            word_korean = BusinessLogicUtil.get_kor_from_eng(english_word=word_english)
            ment = f"유효한 {word_korean}이(가) 아닙니다. 특수문자가 없어야 합니다 {value}"
            raise HTTPException(status_code=400, detail=ment)

    @staticmethod
    def merge_excel_files(dir_path):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            import openpyxl  # pip install openpyxl
            import os
            import pandas as pd
            from openpyxl.styles import Font, Alignment, PatternFill, Color, Border, Side

            print(rf'''dir_path : {dir_path}''')

            # xls 에서 xlsx로 변환 # openpyxl 은 xls 지원안함.  xlsx 가 더 최신기술.
            file_to_merge_ext = ".xls"
            files = [rf"{dir_path}\{file}" for file in os.listdir(dir_path) if file_to_merge_ext in BusinessLogicUtil.get_x(file)]
            for file in files:
                BusinessLogicUtil.convert_xls_to_xlsx(file)

            # 합병할 파일의 목록을 리스트에 저장
            file_to_merge_ext = ".xlsx"
            files_to_merge = [f"{dir_path}/{file}" for file in os.listdir(dir_path) if file_to_merge_ext in BusinessLogicUtil.get_x(file)]
            [print(item) for item in files_to_merge]
            print(rf'type(file_list) : {type(files_to_merge)}')
            print(rf'len(file_list) : {len(files_to_merge)}')

            # 파일합병할 작업공간 제어
            # wb_new = openpyxl.Workbook()
            # ws1 = wb_new.active
            # ws2 = wb_new.create_sheet("result")
            # files_cnt = len(files_to_merge)

            # 엑셀 병합 및 저장
            merged_file = StateManagementUtil.MERGED_EXCEL_FILE
            merged_cnt = 0
            merged_df = pd.DataFrame()
            for file_path in files_to_merge:
                # df = pd.read_excel(file_path, engine = "openpyxl")  # 엑셀 파일 읽기
                # df = pd.read_excel(file_path, engine = "openpyxl", header=0, usecols = [0, 1, 2,3])  # fail, sheet_name="Sheet1"  여러 시트가 있을 경우 시트명을 직접 입력하여 dataframe화 # usecols = [0, 2]  컬럼선택
                # df = pd.read_excel(file_path, engine = "openpyxl", header=0, usecols = [1, 2,3])  # fail,   sheet_name="Sheet1"  여러 시트가 있을 경우 시트명을 직접 입력하여 dataframe화 # usecols = [0, 2]  컬럼선택
                df = pd.read_excel(file_path, engine="openpyxl")  # success, 근데 sheet1 만 되고 sheet2 는 무시 된다.

                # 첫줄 제거
                # df = df.iloc[1:]  # 이번 데이터 구조상, 첫줄 을 제외한 나머지 데이터 선택

                # 마지막줄 제거
                # df = df.iloc[:-1]  # 이번 데이터 구조상, 마지막줄 제외한 나머지 데이터 선택

                merged_df = pd.concat([merged_df, df], ignore_index=True)  # 두 데이터프레임 병합

                merged_cnt = merged_cnt + 1

            print(rf'''merge_files_cnt : {merged_cnt + 1}''')
            print(rf'''merged_df : ''')
            print(rf'''{merged_df}''')
            print(rf'''merged_cnt : {merged_cnt}''')
            print(rf'''merged_file : {merged_file}''')
            try:
                merged_df.to_excel(merged_file)  # success
                # pd.ExcelWriter(merged_file, engine= "openpyxl") # fail, 확장자 잘못 저장했나?
                # BusinessLogicUtil.run_pnx_via_explorer_exe(merged_file)
            except PermissionError:
                BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
                BusinessLogicUtil.print_red(f"{function_name}(), fail, 엑셀파일이 열려있을 수 있습니다. 닫고 머지를 다시 시도해 주세요")
            except Exception as e:
                BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
                BusinessLogicUtil.print_red(f"{function_name}(), fail, \n {traceback.format_exc()}")
            BusinessLogicUtil.print_cyan(f"mkr_ment", )
        except:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def download_youtube_list(via_text_file=True):
        function_name = inspect.currentframe().f_code.co_name
        function_name_txt = rf'{StateManagementUtil.PROJECT_DIRECTORY}\pkg_txt\{function_name}.txt'
        BusinessLogicUtil.make_pnx(pnx=function_name_txt, mode="f")
        if not BusinessLogicUtil.is_window_open(window_title_seg=function_name):
            BusinessLogicUtil.command_to_os(cmd=rf"explorer {function_name_txt}", show_mode=False)

        if via_text_file == True:
            urls = BusinessLogicUtil.get_list_from_f_txt(pnx=function_name_txt)
        else:
            urls = BusinessLogicUtil.get_list_via_user_input(ment=rf"다운로드할 유튜브 리스트를 \n 단위로 입력하세요", function_name=function_name)

        urls = BusinessLogicUtil.get_list_removed_element_preprocessed(items_list=urls)
        BusinessLogicUtil.print_list_as_vertical(items_list=urls, items_list_name="urls")
        BusinessLogicUtil.print_light_black(rf'''len(urls) = "{len(urls)}"''')
        if len(urls) == 0:
            return
        from urllib.parse import quote
        from pytube import Playlist
        string_playlist_positive = 'list='
        for url in urls:
            if string_playlist_positive in url:
                encoded_url = quote(url, safe=':/?&=')
                playlist = Playlist(encoded_url)
                BusinessLogicUtil.print_as_log(string = rf'''playlist="{playlist}" %%%FOO%%%''')
                BusinessLogicUtil.print_as_log(string = rf'''playlist.title="{playlist.title}" %%%FOO%%%''')
                BusinessLogicUtil.print_as_log(string = rf'''len(playlist.video_urls)="{len(playlist.video_urls)}" %%%FOO%%%''')
                for index, video in enumerate(playlist.videos, start=1):
                    BusinessLogicUtil.print_as_log(string = rf'''video.watch_url="{video.watch_url}" %%%FOO%%%''')
                    BusinessLogicUtil.download_youtube(video.watch_url, function_name_txt)
            else:
                BusinessLogicUtil.download_youtube(url, function_name_txt)

    @staticmethod
    def organize_duplicated_hashed_texts_via_user_input():
        pyautogui.FAILSAFE = False
        q_application = QApplication(sys.argv)
        while True:
            # input_box_text_default = ""
            input_box_text_default = "##2025 #2024 #2024 #2024 #2024 #2027 #2025 #hacks#2024 #hacks#2024 #hacks#2024 #hacks#2024 #hacks#2024 #hacks#2024 #hacks #스프레이부스 RC making #압축봉활용 #ORGANIZER #과탄산소다 #커스텀 #diy #DIY #청소 #2027 10 42 스프레이부스 #가구커스텀 #2024 Drawing #2025 건축 #건축커스텀"
            texts = input_box_text_default.split("#")
            texts_removed_duplication: [str] = []
            dialog = UiUtil.CustomQdialog(string="정리정돈하고 싶은 텍스트를 입력해주세요", btns=["진행", "종료"], input_box_mode=True, input_box_text_default=input_box_text_default)
            dialog.exec()
            btn_text_clicked = dialog.btn_text_clicked
            BusinessLogicUtil.print_cyan(btn_text_clicked)
            if btn_text_clicked == "진행":
                user_input = dialog.input_box.text()
                texts = user_input.split("#")
                hashtag_as_year = f'{TimeUtil.get_time_as_("%Y")} '
                texts = [item.replace("##", "#") for item in texts]  # mkr_replace_list_element_each
                texts = [hashtag_as_year] + texts  # mkr_add_element_to_list_as_front_element
                texts = [x for x in texts if x is not None]
                texts = BusinessLogicUtil.get_list_striped_element(items_list=texts)  # mkr_strip_list_element_each
                texts = [item for item in texts if item and item.strip()]  # mkr_remove_list_element_as_""
                for text in texts:
                    if text not in texts_removed_duplication:
                        if text is not None:
                            texts_removed_duplication.append(text)
                texts = texts_removed_duplication
                texts_contained_no = [text for text in texts if any(char.isdigit() for char in text)]
                # texts_contained_no = sorted(texts_contained_no, reverse=False)  # mkr_sort_list_element_by_accend_order
                texts_contained_no = sorted(texts_contained_no, reverse=True)  # mkr_sort_list_element_by_decent_order
                texts_not_contained_no = [text for text in texts if text not in texts_contained_no]
                texts = texts_contained_no + texts_not_contained_no  # 숫자있는 요소를 앞쪽에 배열
                texts = ["#" + item for item in texts]  # mkr_add_prefix_to_list_element_each
                texts = " ".join(texts)  # mkr_convert_from_list_to_str
                BusinessLogicUtil.print_magenta(f'''texts = {texts}''')
                clipboard.copy(texts)
                dialog = UiUtil.CustomQdialog(string=f"클립보드로 붙여넣기 되었습니다", btns=["닫기"], auto_click_positive_btn_after_seconds=0)
                dialog.exec()
                sys.exit()
            elif btn_text_clicked == "종료":
                sys.exit()

    @staticmethod
    def merge_silent_mp3_and_ment_mp3_and_ment__mp3_via_ffmepeg(ment_mp3, ment__mp3):
        """
        앞부분 소리가 들리지 않는 현상
        전체 소리가 다 들려야 하는데
        앞부분의 단어가 들리지 않은채로 소리가 들린다.
        음악파일의 앞부분에 빈소리를 추가
        ffmpeg를 이용하여 silent.mp3(1초간 소리가 없는 mp3 파일)을 소리를 재생해야할 mp3 파일의 앞부분에 합쳐서 재생
        """
        silent_mp3 = StateManagementUtil.SILENT_MP3
        if not os.path.exists(silent_mp3):
            BusinessLogicUtil.print_as_gui("사일런트 mp3 파일이 없습니다")
            sys.exit()
        if not os.path.exists(ment_mp3):
            cmd = rf'echo y | "ffmpeg" -i "concat:{os.path.abspath(silent_mp3)}|{os.path.abspath(ment__mp3)}" -acodec copy -metadata "title=Some Song" "{os.path.abspath(ment_mp3)}" -map_metadata 0:-1  >nul 2>&1'
            BusinessLogicUtil.command_to_os_like_person_as_admin(cmd)

    @staticmethod
    def speak_ment_without_async_experimental_2(ment_string, delay=1.00):
        '''
        이 함수를 많이 쓸 수록 프로그램이 느려진다, 왜냐하면 말하는 속도 < 처리 속도
        '''

        # 음소거 모드
        # BusinessLogicUtil.print_ment_light_yellow("음소거 모드를 실행중입니다")
        # ment = "`"

        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')  # noqa , pycharm 에서 개별검사 억제설정 via noqa
        ment_string = str(ment_string)
        ment_string = ment_string.strip()
        BusinessLogicUtil.print_as_log(string = rf'''ment_string="{ment_string}" %%%FOO%%%''', print_color='blue')
        if BusinessLogicUtil.is_containing_special_characters_with_thread(text=ment_string):
            ment_string = BusinessLogicUtil.remove_special_characters(text=ment_string)
        if ment_string == "":
            return None
        try:
            while True:
                ments = []
                if "," in ment_string:  # , 를 넣으면 나누어 읽도록 업데이트
                    ments = ment_string.split(",")
                    for ment_string in ments:
                        BusinessLogicUtil.speak_ment_experimental(ment=ment_string, comma_delay=0.98)
                    break
                if type(ment_string) == str:
                    # while BusinessLogicUtil.is_speak_as_async_running:
                    #     BusinessLogicUtil.print_as_log(f"def {inspect.currentframe().f_code.co_name}() 에 대한 다른 쓰레드를 기다리는 중입니다")
                    #     pass
                    # BusinessLogicUtil.is_speak_as_async_running = True # 쓰레드상태 사용 중으로 업데이트

                    cache_mp3 = rf'{StateManagementUtil.PROJECT_DIRECTORY}\pkg_mp3'
                    BusinessLogicUtil.make_pnx(pnx=cache_mp3, mode="d")

                    # "ment 전처리, 윈도우 경로명에 들어가면 안되는 문자들 공백으로 대체"
                    ment_string = BusinessLogicUtil.get_str_replaced_special_characters(target=ment_string, replacement=" ")
                    ment_string = ment_string.replace("\n", " ")

                    # 파일 없으면 생성
                    ment__mp3 = rf'{cache_mp3}\{ment_string}_.mp3'
                    ment_mp3 = rf'{cache_mp3}\{ment_string}.mp3'
                    if not os.path.exists(ment_mp3):
                        if not os.path.exists(ment__mp3):
                            from gtts import gTTS
                            if "special_characters" in BusinessLogicUtil.what_does_this_consist_of(text=ment_string):
                                gtts = gTTS(text=ment_string, lang='ko')
                                gtts.save(ment__mp3)
                            elif "kor" in BusinessLogicUtil.what_does_this_consist_of(text=ment_string):
                                gtts = gTTS(text=ment_string, lang='ko')
                                gtts.save(ment__mp3)
                            elif "eng" in BusinessLogicUtil.what_does_this_consist_of(text=ment_string):
                                gtts = gTTS(text=ment_string, lang='en')
                                gtts.save(ment__mp3)
                            elif "jpn" in BusinessLogicUtil.what_does_this_consist_of(text=ment_string):
                                gtts = gTTS(text=ment_string, lang='ja')
                                gtts.save(ment__mp3)
                            else:
                                gtts = gTTS(text=ment_string, lang='ko')
                                gtts.save(ment__mp3)

                    try:
                        BusinessLogicUtil.merge_silent_mp3_and_ment_mp3_and_ment__mp3_via_ffmepeg(ment_mp3, ment__mp3)
                    except Exception:
                        BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

                    try:
                        # 자꾸 프로세스 세션을 빼앗기 때문에 불편한 코드
                        # os.system(rf'start /b cmd /c call "{ment_mp3}" >nul 2>&1')

                        # 프로세스 세션을 빼앗지 않고 mp3재생하는 다른 방법
                        # playsound.playsound(os.path.abspath(ment_mp3))

                        # BusinessLogicUtil.print_as_log(rf'프로세스 세션을 빼앗지 않고 mp3재생')
                        ment_mp3 = os.path.abspath(ment_mp3)
                        try:
                            # 재생
                            import pyglet
                            source = pyglet.media.load(ment_mp3)
                            # pyglet_player = BusinessLogicUtil.pyglet_player
                            # pyglet_player.queue(source)
                            source.play()  # 웃긴다 이거 이렇게는 재생이 된다.

                            length_of_mp3 = BusinessLogicUtil.get_length_of_mp3(ment_mp3)
                            # time.sleep(length_of_mp3 * 0.65)
                            # time.sleep(length_of_mp3 * 0.75)
                            # time.sleep(length_of_mp3 * 0.85)
                            # time.sleep(length_of_mp3 * 0.95)
                            # time.sleep(length_of_mp3 * 1.05)
                            # time.sleep(length_of_mp3 * 1.00)
                            time.sleep(length_of_mp3 * delay)

                            return length_of_mp3
                            # BusinessLogicUtil.is_speak_as_async_running = False # 쓰레드상태 사용종료로 업데이트
                        except FileNotFoundError:
                            BusinessLogicUtil.print_cyan(f"{ment_mp3} 재생할 파일이 없습니다")
                        except:
                            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
                            break

                        BusinessLogicUtil.print_with_underline("before_mp3_length_used_in_speak_as_async 업데이트")
                        length_of_mp3 = round(float(BusinessLogicUtil.get_length_of_mp3(ment_mp3)), 1)
                        BusinessLogicUtil.previous_mp3_length_used_in_speak_as_async = length_of_mp3

                    except Exception:
                        BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

                    # BusinessLogicUtil.print_as_log(rf'불필요 파일 삭제')
                    os.system(f'echo y | del /f "{ment__mp3}" >nul 2>&1')

                    # BusinessLogicUtil.print_as_log(rf'중간로깅')
                    BusinessLogicUtil.print_as_log(string=f"TTS 재생시도")
                break
        except Exception:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def speak_today_info_as_korean():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        yyyy = TimeUtil.get_time_as_('%Y')
        MM = TimeUtil.get_time_as_('%m')
        dd = TimeUtil.get_time_as_('%d')

        BusinessLogicUtil.speak_ment_without_async_experimental_2(ment_string=f'{int(yyyy)}년 {int(MM)}월 {int(dd)}일', delay=0.95)


    @staticmethod
    def back_up_pnx(src, dst):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        if not BusinessLogicUtil.does_pnx_exist(src=src):
            BusinessLogicUtil.print_as_log(string=rf''' %%%FOO%%%''', print_color="red")
            return

        # 용량을 확인하고 부족하면 95프로 이면 휴지통을 비울것을 가이드 하고
        # 하면안될것 같다고 이야기해줘

        # 압축
        BusinessLogicUtil.compress_pnx(src=src, dst=dst)

    @staticmethod
    def back_up_pnxs_to_deprecated_via_hard_code():  # deprecat 시키던 중복코드 제거해보자
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        pnxs_raw = rf"""
                F:\park4139\park4139_memo.toml
                F:\park4139\park4139_shell_start_up.bat
        """
        pnxs = []
        for pnx in pnxs_raw.split("\n"):
            if not pnx.strip() == "":
                pnxs.append(pnx.strip())
        # print(rf'''len(pnxs) : {len(pnxs)}''')
        # print(pnxs)
        for pnx in pnxs:
            # print(target)
            dst = rf"{StateManagementUtil.DOWNLOADS}\archived"
            BusinessLogicUtil.back_up_pnx(src=pnx, dst=dst)

    @staticmethod
    def back_up_pnxs_via_function_name_txt(dst):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        function_name_txt = rf'{StateManagementUtil.PROJECT_DIRECTORY}\pkg_txt\{function_name}.txt'
        BusinessLogicUtil.make_pnx(pnx=StateManagementUtil.PKG_TXT, mode="d")
        BusinessLogicUtil.make_pnx(pnx=function_name_txt, mode="f")
        # BusinessLogicUtil.run_pnx_via_explorer_exe(function_name_txt)
        texts = BusinessLogicUtil.get_list_from_f_txt(pnx=function_name_txt)
        texts = BusinessLogicUtil.get_list_removed_element_duplicated(items_list=texts)
        texts = BusinessLogicUtil.get_list_striped_element(items_list=texts)
        for text in texts:
            BusinessLogicUtil.back_up_pnx(src=text, dst=dst)

    @staticmethod
    def hold_console():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        os.system("cmd /k")

    @staticmethod
    def run_powershell_exe_as_admin():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # BusinessLogicUtil.command_to_os('PowerShell -Command "Start-Process powershell"')
        BusinessLogicUtil.command_to_os('powershell -Command "Start-Process powershell -Verb RunAs"')
        window_title_seg = "관리자: Windows PowerShell"
        while True:
            if not BusinessLogicUtil.is_front_window_title(window_title_seg=window_title_seg):
                BusinessLogicUtil.move_window_to_front(window_title_seg=window_title_seg)
            if BusinessLogicUtil.is_front_window_title(window_title_seg=window_title_seg):
                break
        # BusinessLogicUtil.window_move_to_front_via_win32gui(window_title_seg=window_title_seg)

    @staticmethod
    def chcp_65001(show_mode=True):
        function_name = inspect.currentframe().f_code.co_name
        if show_mode == True:
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        os.system("chcp 65001 >nul")

    @staticmethod
    def run_ubuntu_via_wsl(wsl_linux_version, window_title_seg):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        # command = f'wsl -d {wsl_linux_version} --exec exit'
        # BusinessLogicUtil.command_to_os(command)

        command = f'start cmd /k "wsl -d {wsl_linux_version}"'
        BusinessLogicUtil.command_to_os(cmd=command, mode='a')

        timeout = 20
        start_time = time.time()
        while True:
            BusinessLogicUtil.print_as_log(string=time.time() - start_time)
            if time.time() - start_time > timeout:
                break
            if BusinessLogicUtil.is_window_open(window_title_seg=window_title_seg):
                break
            time.sleep(0.5)

        timeout = 5
        start_time = time.time()
        while True:
            BusinessLogicUtil.print_as_log(string=time.time() - start_time)
            if time.time() - start_time > timeout:
                break
            if BusinessLogicUtil.is_front_window_title(window_title_seg=window_title_seg):
                break
            else:
                BusinessLogicUtil.move_window_to_front(window_title_seg=window_title_seg)
            time.sleep(0.5)
            break

        # cd

        # clear

    @staticmethod
    def change_os_to_shutdown(seconds=None, miliseconds=None, mins=None, restart_mode=False, cancel_mode=False):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        modes = [restart_mode, cancel_mode]
        false_count = modes.count(False)

        Nones = [seconds, miliseconds, mins]
        None_count = Nones.count(None)

        if false_count == 2 and None_count == 3:
            BusinessLogicUtil.print_light_black(f"이 함수의 최소인자의 수는 1개 입니다")
            return

        if false_count < 2:
            if restart_mode == True:
                function_name = inspect.currentframe().f_code.co_name
                BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
                command = f'shutdown.exe /r'
                BusinessLogicUtil.command_to_os(command)
                return

            if cancel_mode == True:
                command = f'shutdown.exe /a'
                BusinessLogicUtil.command_to_os(command)
                return
        else:

            if None_count != 2:
                # BusinessLogicUtil.print_light_black(f'''None_count = {None_count}''')
                BusinessLogicUtil.print_light_black(f"이 함수는 시간단위에 대한인자를 1개의 인자만 받도록 만들어졌습니다")
                return

            # sys_shutdown(seconds = x)
            # sys_shutdown(mins = x)
            if miliseconds is not None:
                seconds = miliseconds
            elif mins is not None:
                seconds = mins * 60

            command = f'shutdown.exe /s /t {seconds}'
            BusinessLogicUtil.command_to_os(command)

    @staticmethod
    def shutdown_pnx(process_name):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # command = f'taskkill /im {app_image_name} /f"'
        command = f'taskkill /f /im {process_name}"'
        BusinessLogicUtil.command_to_os(command)
        # command = f'wmic process where name="{app_image_name}" delete'
        # BusinessLogicUtil.run_via_subprocess(command)

    @staticmethod
    def rerun_pnx(my_name):  # 종료용이름 시작용이름 이 다름 따로 수집해서 코딩 필요
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.shutdown_pnx(process_name=(my_name))
        BusinessLogicUtil.sleep(milliseconds=200)  # 최적화 테스트 필요
        cmd = rf'start "{my_name}"'
        BusinessLogicUtil.command_to_os(cmd=cmd, mode="a")

    @staticmethod
    def mstsc(ip=None, port=3389):
        # 내부망에서 유동ip일때 ip대신 hostname 추천
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # command = f'mstsc /v:{ip}:{port} /admin /w:640 /h:350 /multimon /NoConsentPrompt'
        # command = f'mstsc /admin /w:960 /h:540 /v:{ip}:{port} /multimon /NoConsentPrompt'
        # command = f'mstsc /admin /w:960 /h:540 /v:{ip}:{port} /multimon /NoConsentPrompt'
        # command = f'mstsc /admin /w:960 /h:1080 /v:{ip}:{port} /multimon /NoConsentPrompt'
        command = f'mstsc /v:{ip}:{port} /admin /w:1024 /h:768 /multimon '
        BusinessLogicUtil.command_to_os(command, mode='a')

    @staticmethod
    def ssh(wsl_linux_version, wsl_window_title_seg, users, ip, port=22, pw="", exit_mode=True):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        wsl_command = f'ssh-keygen -t rsa -b 4096 -C "{users}{ip}{port}"'
        BusinessLogicUtil.run_command_run_via_wsl_exe(wsl_command=wsl_command, wsl_linux_version=wsl_linux_version, wsl_window_title_seg=wsl_window_title_seg, exit_mode=exit_mode)

        for i in range(0, 3):
            BusinessLogicUtil.press("enter")
            BusinessLogicUtil.sleep(milliseconds=200)

        wsl_command = f'ssh-copy-id -p {port} "{users}@{ip}"'
        BusinessLogicUtil.run_command_run_via_wsl_exe(wsl_command=wsl_command, wsl_linux_version=wsl_linux_version, wsl_window_title_seg=wsl_window_title_seg, exit_mode=exit_mode)

        wsl_command = f'ssh {users}@{ip} -p {port} '
        BusinessLogicUtil.run_command_run_via_wsl_exe(wsl_command=wsl_command, wsl_linux_version=wsl_linux_version, wsl_window_title_seg=wsl_window_title_seg, exit_mode=exit_mode)

        BusinessLogicUtil.command_to_wsl_os_like_person('clear', wsl_linux_version=wsl_linux_version, wsl_window_title_seg=wsl_window_title_seg)

    # @staticmethod
    # def ():
    #     BusinessLogicUtil.print_as_log(f"{inspect.currentframe().f_code.co_name}()")
    #     command = f'start cmd /k "wsl -d Ubuntu-22.04"'
    #     BusinessLogicUtil.run_via_subprocess(command) #success
    #

    # @staticmethod
    # def ():
    #     BusinessLogicUtil.print_as_log(f"{inspect.currentframe().f_code.co_name}()")
    #     command = f'start cmd /k "wsl -d Ubuntu-22.04"'
    #     BusinessLogicUtil.run_via_subprocess(command) #success
    #

    # @staticmethod
    # def ():
    #     BusinessLogicUtil.print_as_log(f"{inspect.currentframe().f_code.co_name}()")
    #     command = f'start cmd /k "wsl -d Ubuntu-22.04"'
    #     BusinessLogicUtil.run_via_subprocess(command) #success
    #

    # @staticmethod
    # def ():
    #     BusinessLogicUtil.print_as_log(f"{inspect.currentframe().f_code.co_name}()")
    #     command = f'start cmd /k "wsl -d Ubuntu-22.04"'
    #     BusinessLogicUtil.run_via_subprocess(command) #success
    #

    # @staticmethod
    # def ():
    #     BusinessLogicUtil.print_as_log(f"{inspect.currentframe().f_code.co_name}()")
    #     command = f'start cmd /k "wsl -d Ubuntu-22.04"'
    #     BusinessLogicUtil.run_via_subprocess(command) #success
    #

    # @staticmethod
    # def ():
    #     BusinessLogicUtil.print_as_log(f"{inspect.currentframe().f_code.co_name}()")
    #     command = f'start cmd /k "wsl -d Ubuntu-22.04"'
    #     BusinessLogicUtil.run_via_subprocess(command) #success
    #

    @staticmethod
    def run_park4139_release_server(port):
        """
        park4139 release server
        FTP 서버
        HTTP 서버
        """
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        py_pnx = rf'{StateManagementUtil.PROJECT_DIRECTORY}\park4139_{function_name}.py'
        if not BusinessLogicUtil.does_pnx_exist(src=py_pnx):
            return

        if BusinessLogicUtil.is_window_open(window_title_seg=py_pnx):
            BusinessLogicUtil.close_windows_duplicated()
            BusinessLogicUtil.move_window_to_front(window_title_seg=py_pnx)
            return

        server_ip = "localhost"
        BusinessLogicUtil.print_as_log(f'''server_ip = {server_ip}''')
        BusinessLogicUtil.print_as_log(f'''server_port = {port}''')

        # bat_pnx = rf'{StateManagementUtil.USERPROFILE}\Downloads\jung_hoon_park\plain\park4139_http_server_run.bat'
        # cmd = rf'start cmd.exe /k "{bat_pnx}"'

        cmd = rf'start cmd.exe /k python "{py_pnx}"'
        BusinessLogicUtil.command_to_os(cmd=cmd, mode="a")
        # BusinessLogicUtil.print_as_log(f'''"{cmd} [Negative]"''')

        url = rf'http://{server_ip}:{port}'
        cmd = rf" explorer {url}/"
        BusinessLogicUtil.command_to_os(cmd=cmd, mode="a")
        BusinessLogicUtil.close_chrome_tab_duplicated()
        BusinessLogicUtil.move_chrome_tab_by_url(url=url)

        cmd = rf' netstat -ano | find "{port}" '
        BusinessLogicUtil.command_to_os(cmd=cmd, mode="a")

    @staticmethod
    def cd(target_pnx):
        import os
        os.chdir(target_pnx)
        current_directory = os.getcwd()
        # BusinessLogicUtil.print_light_black(f"{current_directory}")

    @staticmethod
    def pwd():
        import os
        current_directory = os.getcwd()
        BusinessLogicUtil.print_light_black(f"{current_directory}")
        return current_directory

    @staticmethod
    def build_console_blurred():
        import os

        helper = BusinessLogicUtil()
        hp = helper

        CURRENT_DIRECTORY = hp.pwd()
        PROJECT_NAME = "console_blurred"
        USER_PROFILE = hp.USER_PROFILE
        DESKTOP_ABSPATH = os.path.join(USER_PROFILE, "Desktop")
        # SERVICE_ABSPATH = os.path.join(USER_PROFILE, "Desktop", "services")
        # PROJECT_ABSPATH = os.path.join(SERVICE_ABSPATH, PROJECT_NAME)
        # PROJECT_DIRECTORY = PROJECT_ABSPATH
        PROJECT_ABSPATH = hp.pwd()

        # 프로젝트 디렉토리로 이동
        hp.cd(PROJECT_ABSPATH)

        # 현재디렉토리에 "venv" 디렉토리 있는 경우
        directory_name_to_find = "venv"
        if hp.does_directory_exist_at_present_directory(directory_name=directory_name_to_find):
            hp.print_light_black(f"{directory_name_to_find} 디렉토리가 있습니다")

            # 현재디렉토리의 불필요한 타겟들을 삭제
            BusinessLogicUtil.remove_pnxs_related_to_console_blurred_build()

            # pip 업그레이드
            commands = ["python", "-m", "pip", "install", "--upgrade", "pip"]
            BusinessLogicUtil.command_run_via_subprocess(commands)

            # pip 업그레이드
            commands = ["pip", "install", "pyinstaller", "--upgrade"]
            BusinessLogicUtil.command_run_via_subprocess(commands)

            # OP 용 build
            commands = ["python", "-m", "PyInstaller", "-i", rf".\pkg_png\icon.PNG", "console_blurred.py"]
            BusinessLogicUtil.command_run_via_subprocess(commands)

            # Dev 용 build
            # echo d | xcopy ".\pkg_yaml" ".\dist\console_blurred\_internal\pkg_yaml" /e /h /k /y
            # echo d | xcopy ".\pkg_log" ".\dist\console_blurred\_internal\pkg_log" /e /h /k /y
            # echo d | xcopy ".\pkg_mp3" ".\dist\console_blurred\_internal\pkg_mp3" /e /h /k /y
            # echo d | xcopy ".\pkg_png" ".\dist\console_blurred\_internal\pkg_png" /e /h /k /y
            # echo d | xcopy ".\pkg_tools" ".\dist\console_blurred\_internal\pkg_tools" /e /h /k /y
            # echo d | xcopy ".\pkg_txt" ".\dist\console_blurred\_internal\pkg_txt" /e /h /k /y
            # echo d | xcopy ".\pkg_yt_dlp" ".\dist\console_blurred\_internal\pkg_yt_dlp" /e /h /k /y
            # echo d | xcopy ".\pkg_png" ".\dist\console_blurred\_internal\pkg_png" /e /h /k /y
            # echo d | xcopy ".\pkg_sound" ".\dist\console_blurred\_internal\pkg_sound" /e /h /k /y
            # echo d | xcopy ".\pkg_alba" ".\dist\console_blurred\_internal\pkg_alba" /e /h /k /y
            # echo d | xcopy ".\pkg_font" ".\dist\console_blurred\_internal\pkg_font" /e /h /k /y
            # echo d | xcopy ".\pkg_json" ".\dist\console_blurred\_internal\pkg_json" /e /h /k /y
            # echo d | xcopy ".\pkg_work_for_music" ".\dist\console_blurred\_internal\pkg_work_for_music" /e /h /k /y

            # 가상환경을 활성화하고, 그 후에 파이썬 스크립트 실행
            # venv_path = "path_to_your_virtualenv\\Scripts\\activate.bat"
            # subprocess.call(f"cmd /k {venv_path} && python your_script.py", shell=True)

            # park4139_temp.py 생성
            # script_path = 'park4139_temp.py'
            # venv_python = r'.\venv\Scripts\python.exe'
            # with open(script_path, 'w') as f:
            #     # 실행할 스크립트 내용
            #     f.write('print(1)')
            #
            # # park4139_temp.py 실행 (Python venv 가상환경에서)
            # subprocess.run([venv_python, script_path])
            #
            # # park4139_temp.py 삭제
            # os.remove(script_path)

        else:
            hp.print_light_black(f"{directory_name_to_find} 디렉토리가 없습니다")

    @staticmethod
    def get_nxs_without_walking(mode=None, directory_pnx=None):
        import os

        if directory_pnx is None:
            directory_pnx = os.getcwd()  # 현재 작업 디렉토리로 설정

        # 절대경로로 변환
        directory_pnx = os.path.abspath(directory_pnx)

        # 리스트로 결과를 받기 위한 변수
        files = []
        directories = []

        # os.scandir() 사용하여 더 빠르게 항목 탐색
        try:
            with os.scandir(directory_pnx) as it:
                for entry in it:
                    if entry.is_dir():  # 디렉토리일 경우
                        directories.append(entry.name)  # 디렉토리 이름 추가
                    elif entry.is_file():  # 파일일 경우
                        files.append(entry.name)  # 파일 이름 추가
        except FileNotFoundError:
            print(f"디렉토리 '{directory_pnx}'을 찾을 수 없습니다.")
            return []

        # 원하는 mode에 따라 파일, 디렉토리, 혹은 둘 다 반환
        if mode == "f":
            return files
        elif mode == "d":
            return directories
        else:
            return files + directories

    @staticmethod
    def get_pnxs_without_walking(mode=None, directory_pnx=None):
        import os
        if directory_pnx is None:
            directory_pnx = os.getcwd()

        # 절대경로로 변환
        directory_pnx = os.path.abspath(directory_pnx)

        items = os.listdir(directory_pnx)
        files = []
        directories = []

        for item in items:
            item_path = os.path.join(directory_pnx, item)  # 절대경로로 결합
            if os.path.isdir(item_path):
                directories.append(item_path)  # 디렉토리의 절대경로 추가
            else:
                files.append(item_path)  # 파일의 절대경로 추가

        # 원하는 mode에 따라 결과 반환
        if mode == "f":
            pnxs = files
        elif mode == "d":
            pnxs = directories
        else:
            pnxs = files + directories
        return pnxs

    @staticmethod
    def get_pnxs_with_walking(mode=None, directory_pnx=None):
        import os

        if directory_pnx is None:
            directory_pnx = os.getcwd()

        files = []
        directories = []

        for file_p, dir_nx, file_nxs in os.walk(directory_pnx):
            file_pnx = os.path.abspath(file_p)
            directories.append(file_pnx)

            for file_nx in file_nxs:
                item_pnx = os.path.abspath(os.path.join(file_p, file_nx))
                files.append(item_pnx)

            # 하위 디렉토리 탐색을 원하지 않는 경우
            if mode == "d":  # 디렉토리만 원하면 아래 항목에서 멈춤
                del dir_nx[:]

        # 원하는 mode에 따라 결과 반환
        if mode == "f":
            pnxs = files
        elif mode == "d":
            pnxs = directories
        else:
            pnxs = files + directories

        # 출력제한
        print_limit = 100000000
        if len(files) <= print_limit:
            # BusinessLogicUtil.print_light_black(f'''files = {files}''')
            # BusinessLogicUtil.print_light_black(f'''directories = {directories}''')
            pass

        return pnxs

    @staticmethod
    def get_nxs_with_walking(mode=None, directory_pnx=None):
        import os

        if directory_pnx is None:
            directory_pnx = os.getcwd()  # 기본 디렉토리 경로를 현재 작업 디렉토리로 설정

        files = []
        directories = []

        # os.walk를 사용하여 디렉토리 트리 전체를 탐색
        for file_p, dir_nx, file_nx in os.walk(directory_pnx):
            if mode == "f":
                files.extend(file_nx)  # 파일만 추가
            elif mode == "d":
                directories.append(os.path.basename(file_p))  # 디렉토리명만 추가
            else:
                # 디렉토리명과 파일명 둘 다 필요한 경우
                directories.append(os.path.basename(file_p))
                files.extend(file_nx)  # 파일명만 추가

        # mode에 따라 결과 반환
        if mode == "f":
            return files
        elif mode == "d":
            return directories
        return files + directories

    @staticmethod
    def is_directory(target_pnx):
        if os.path.isdir(target_pnx):
            return True
        else:
            return False

    @staticmethod
    def is_file(pnx):
        if os.path.isdir(pnx):
            return False
        else:
            return True

    @staticmethod
    def get_pnxs_include_text_from_items(items, text):
        pnxs = []
        for item in items:
            if text in item:
                pnxs.append(item)
        return pnxs

    @staticmethod
    def does_directory_exist_at_present_directory(directory_name: str):
        pnxs = BusinessLogicUtil.get_pnxs_without_walking(mode="d")
        for pnx in pnxs:
            if BusinessLogicUtil.get_nx(pnx) == directory_name:
                return True
        return False

    @staticmethod
    def get_directory_at_present_directory(directory_name_to_find: str):
        pnxs = BusinessLogicUtil.get_pnxs_without_walking(mode="d")
        pnxs = BusinessLogicUtil.get_pnxs_include_text_from_items(items=pnxs, text=directory_name_to_find)
        for item in pnxs:
            if item.split("\\")[0] == directory_name_to_find:
                # return True
                return item
        return None

    @staticmethod
    def print_and_get_text_converted(text: str, convert_mode=0):
        """
        # str to str

        param str
        return str
        """
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        def convert_mode_1(text):
            text_converted = text
            while (True):
                if "  " in text:
                    text_converted = text.replace("  ", " ")
                else:
                    break
            text_converted = text_converted.replace(" ", "\",\"")
            text_converted = f"\"{text_converted}\""
            text_converted = f"[{text_converted}]"
            BusinessLogicUtil.print_magenta(f'''{inspect.currentframe().f_code.co_name} = {text_converted}''')
            return text_converted

        def convert_mode_2(text):
            text_converted = text
            while (True):
                if "  " in text:
                    text_converted = text.replace("  ", " ")
                else:
                    break
            text_converted = text_converted.replace(" ", "\",\"")
            text_converted = text_converted.replace("\"\"", "\"")
            text_converted = f"\"{text_converted}\""
            text_converted = f"[{text_converted}]"
            BusinessLogicUtil.print_magenta(f'''{inspect.currentframe().f_code.co_name} = {text_converted}''')
            return text_converted

        def convert_mode_3(text):
            text = text.replace("  ", " ")
            text_converted = text.replace(" ", ",")
            BusinessLogicUtil.print_magenta(f'''{inspect.currentframe().f_code.co_name} = {text_converted}''')
            return text_converted

        def convert_mode_4(text):
            texts = text.split(" ")
            texts = BusinessLogicUtil.get_list_striped_element(items_list=texts)
            text_converted = text
            BusinessLogicUtil.print_magenta(f'''{inspect.currentframe().f_code.co_name} = {text_converted}''')
            return text_converted

        def convert_mode_x(text):
            text_converted = text
            if "  " in text:
                text_converted = text.replace("  ", " ")
            text_converted = text.replace(" ", "\",\"")
            text_converted = f"\"{text_converted}\""
            text_converted = f"[{text_converted}]"
            BusinessLogicUtil.print_magenta(f'''{inspect.currentframe().f_code.co_name} = {text_converted}''')
            return text_converted

        def convert_mode_0(text):
            convert_mode_1(text)
            convert_mode_2(text)
            convert_mode_3(text)
            convert_mode_4(text)
            convert_mode_x(text)

        if convert_mode == 0:
            convert_mode_0(text)
            return None

        elif convert_mode == 1:
            return convert_mode_1(text)
        elif convert_mode == 2:
            return convert_mode_2(text)
        else:
            return None

    @staticmethod
    def command_run_via_subprocess(command, show_mode=True):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.print_light_black(f"%%%FOO%%% {command}", )
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            texts = command
            texts = " ".join(texts)
            BusinessLogicUtil.print_light_black(f"[result.stdout] {result.stdout}", )
            if show_mode == False:
                BusinessLogicUtil.print_cyan(f"%%%FOO%%% green {texts}", )
        except:
            if show_mode == False:
                BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
            pass

    @staticmethod
    def remove_pnx(pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # 타겟있으면 무조건 영구 삭제
        # 타겟없으면 넘어감
        if BusinessLogicUtil.does_pnx_exist(pnx):
            if BusinessLogicUtil.is_file(pnx):
                command = rf'echo y | del /f "{pnx}"'
            else:
                command = rf'echo y | rmdir /s "{pnx}"'
            BusinessLogicUtil.command_to_os(command)

    @staticmethod
    def does_pnx_exist(src, show_mode=True):
        function_name = inspect.currentframe().f_code.co_name
        if show_mode == False:
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        if os.path.exists(src):
            return True
        else:
            return False

    @staticmethod
    def is_target_type_list(target):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        if isinstance(target, list):
            return True
        else:
            return False

    @staticmethod
    def is_target_type_str(target):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        if isinstance(target, str):
            return True
        else:
            return False

    @staticmethod
    def run_console_blurred_exe():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # console_blurred.exe 실행
        commands = rf".\dist\console_blurred\console_blurred.exe"
        BusinessLogicUtil.command_to_os(commands)

    @staticmethod
    def remove_pnxs_related_to_console_blurred_build():  # done
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # 현재디렉토리의 불필요한 타겟들을 삭제
        items_useless = [
            r".\console_blurred.exe",
            r".\build",
            r".\dist",
            r".\_internal",
            r".\dist.zip",
            r".\console_blurred.spec",
        ]
        for item in items_useless:
            # BusinessLogicUtil.remove_target(target_pnx=item)
            BusinessLogicUtil.remove_pnx_parmanently(pnx=item)

    @staticmethod
    def decompress_pnx_via_zip(pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # command = rf'bz.exe x "{pnx}"'  # 화면에 창이 안뜨는 모드
        # BusinessLogicUtil.command_to_os(command=command)
        pnx_p = BusinessLogicUtil.get_p(pnx=pnx)
        if pnx_p is None:
            pnx_p = os.path.dirname(pnx)
        pnx_p = BusinessLogicUtil.get_pnx_unix_style(pnx=pnx_p)
        pnx = BusinessLogicUtil.get_pnx_unix_style(pnx=pnx)
        with zipfile.ZipFile(pnx, 'r') as zip_ref:
            if not os.path.exists(pnx_p):
                os.makedirs(pnx_p)
            zip_ref.extractall(pnx_p)
            BusinessLogicUtil.print_as_log(string=rf'''pnx_p="{pnx_p}" %%%FOO%%%''')

    @staticmethod
    def get_parents_process_pid():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        command = rf'powershell (Get-WmiObject Win32_Process -Filter ProcessId=$PID).ParentProcessId'
        lines = BusinessLogicUtil.command_to_os_like_person_as_admin(command=command, show_mode=False)
        lines = BusinessLogicUtil.get_list_replaced_element_from_str_to_str(item_list=lines, from_str="\r", to_str="")
        return lines[0]

    @staticmethod
    def print_parents_process_pid():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        os.system(rf'powershell (Get-WmiObject Win32_Process -Filter ProcessId=$PID).ParentProcessId')

    @staticmethod
    def is_containing_kor(text):
        pattern = "[ㄱ-ㅎ가-힣]"
        if re.search(pattern, text):
            return True
        else:
            return False

    @staticmethod
    def is_containing_special_characters_with_thread(text: str):
        # 비동기 처리 설정 ( advanced  )
        nature_numbers = [n for n in range(1, 101)]  # from 1 to 100
        work_quantity = len(text)
        n = 4  # thread_cnt # interval_cnt
        d = work_quantity // n  # interval_size
        r = work_quantity % n
        start_1 = 0
        end_1 = d - 1
        starts = [start_1 + (n - 1) * d for n in nature_numbers[:n]]  # 등차수열 공식
        ends = [end_1 + (n - 1) * d for n in nature_numbers[:n]]
        remained_start = ends[-1] + 1
        remained_end = work_quantity

        # print(rf'nature_numbers : {nature_numbers}')  # 원소의 길이의 합이 11넘어가면 1에서 3까지만 표기 ... 의로 표시 그리고 마지막에서 3번째에서 마지막에서 0번째까지 표기 cut_list_proper_for_pretty()
        # print(rf'work_quantity : {work_quantity}')
        # print(rf'n : {n}')
        # print(rf'd : {d}')
        # print(rf'r : {r}')
        # print(rf'start_1 : {start_1}')
        # print(rf'end_1 : {end_1}')
        # print(rf'starts : {starts}')
        # print(rf'ends : {ends}')
        # print(rf'remained_start : {remained_start}')
        # print(rf'remained_end : {remained_end}')

        # 비동기 이벤트 함수 설정 ( advanced  )
        async def is_containing_special_characters(start_index: int, end_index: int, text: str):
            pattern = "[~!@#$%^&*()_+|<>?:{}]"  # , 는 제외인가?
            if re.search(pattern, text[start_index:end_index]):
                # print(f"쓰레드 {start_index}에서 {end_index}까지 작업 성공 True return")
                result_list.append(True)
                # return True
            else:
                result_list.append(False)
                # print(f"쓰레드 {start_index}에서 {end_index}까지 작업 성공 False return")
                # return False

        # 비동기 이벤트 루프 설정
        def run_async_event_loop(start_index: int, end_index: int, text: str):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(is_containing_special_characters(start_index, end_index, text))

        # 스레드 객체를 저장할 리스트 생성
        threads = []

        # 각 스레드의 결과를 저장할 리스트
        # result_list = [None] * work_quantity
        result_list = []

        # 주작업 처리용 쓰레드
        for n in range(0, n):
            start_index = starts[n]
            end_index = ends[n]
            thread = threading.Thread(target=run_async_event_loop, args=(start_index, end_index, text))
            thread.start()
            threads.append(thread)

        # 남은 작업 처리용 쓰레드
        if remained_end <= work_quantity:
            start_index = remained_start
            end_index = remained_end
            thread = threading.Thread(target=run_async_event_loop, args=(start_index, end_index, text))
            thread.start()
            threads.append(thread)
        else:
            start_index = remained_start
            end_index = start_index  # end_index 를 start_index 로 하면 될 것 같은데 테스트필요하다.
            thread = threading.Thread(target=run_async_event_loop, args=(start_index, end_index, text))
            thread.start()
            threads.append(thread)

        # 모든 스레드의 작업이 종료될 때까지 대기
        for thread in threads:
            thread.join()

        # 먼저 종료된 스레드가 있는지 확인하고, 나머지 스레드 중지
        # for thread in threads:
        #     if not thread.is_alive():
        #         for other_thread in threads:
        #             if other_thread != thread:
        #                 other_thread.cancel()
        #         break

        # 바뀐 부분만 결과만 출력, 전체는 abspaths_and_mtimes 에 반영됨
        # print(rf'result_list : {result_list}')
        # print(rf'type(result_list) : {type(result_list)}')
        # print(rf'len(result_list) : {len(result_list)}')

        if all(result_list):
            # print("쓰레드 작업결과 result_list의 모든 요소가 True이므로 True를 반환합니다")
            return True
        else:
            # print("쓰레드 작업결과 result_list에 False인 요소가 있어 False를 반환합니다")
            pass

    @staticmethod
    def is_containing_jpn(text):
        # pattern = r"^[\p{Script=Hiragana}\p{Script=Katakana}\p{Script=Han}ー〜・]+$"
        # pattern = r"^\P{Script=Hiragana}\P{Script=Katakana}\P{Script=Han}ー〜・]+$"
        # pattern = r"^[\p{Script=Hiragana}\p{Script=Katakana}\p{Script=Han}ー〜・]+$"
        # pattern = r"^[^\p{Script=Hiragana}^\p{Script=Katakana}^\p{Script=Han}ー〜・]+$"
        # pattern = r"^[^\p{Script=Hiragana}^\p{Script=Katakana}^\p{Script=Han}ー〜・]+$"
        pattern = r"^[^\u3040-\u309F\u30A0-\u30FF\u4E00-\u9FFFー〜・]+$"
        if re.search(pattern, text, flags=re.U):
            return True
        else:
            return False

    @staticmethod
    def is_containing_eng(text):
        pattern = "[a-zA-Z]"
        if re.search(pattern, text):
            return True
        else:
            return False

    @staticmethod
    def is_containing_number(text):
        pattern = "[0-9]"
        if re.search(pattern, text):
            return True
        else:
            return False

    @staticmethod
    def is_only_no(text):
        pattern = "^[0-9]+$"
        if re.search(pattern, text):
            return True
        else:
            return False

    @staticmethod
    def is_only_speacial_characters(text):
        pattern = "^[~!@#$%^&*()_+|<>?:{}]+$"
        if re.search(pattern, text):
            return True
        else:
            return False

    @staticmethod
    def is_only_eng_and_kor_and_no_and_speacial_characters(text):
        pattern = "^[ㄱ-ㅎ가-힣0-9a-zA-Z~!@#$%^&*()_+|<>?:{}]+$"
        if re.search(pattern, text):
            return True
        else:
            return False

    @staticmethod
    def is_only_eng_and_no_and_speacial_characters(text):
        pattern = "^[0-9a-zA-Z~!@#$%^&*()_+|<>?:{}]+$"
        if re.search(pattern, text):
            return True
        else:
            return False

    @staticmethod
    def is_only_eng_and_speacial_characters(text):
        pattern = "^[a-zA-Z~!@#$%^&*()_+|<>?:{}]+$"
        if re.search(pattern, text):
            return True
        else:
            return False

    @staticmethod
    def is_only_eng_and_no(text):
        pattern = "^[0-9a-zA-Z]+$"
        if re.search(pattern, text):
            return True
        else:
            return False

    @staticmethod
    def is_only_eng(text):
        pattern = "^[a-zA-Z]+$"
        if re.search(pattern, text):
            return True
        else:
            return False

    @staticmethod
    def is_eng_or_kor_ja(text: str):
        """
        한글처리 :
            한영숫특 :
            한숫특 :
            한숫
            한특
            숫특
            특
            숫
        영어처리 :
            영숫특
            영특
            영숫
            영
        일어처리 :
        빠진거있나? 일단 여기까지

        문자구성 판별기가 필요하다
            return "eng, kor, jap, special_characters ", ... 이런식 > what_does_this_consist_of() 를 만들었다.
        """
        if BusinessLogicUtil.is_only_speacial_characters(text=text):
            return "ko"
        elif BusinessLogicUtil.is_only_no(text=text):
            return "ko"
        elif BusinessLogicUtil.is_containing_kor(text=text):
            return "ko"
        if BusinessLogicUtil.is_only_eng_and_no_and_speacial_characters(text=text):
            return "en"
        elif BusinessLogicUtil.is_only_eng_and_speacial_characters(text=text):
            return "en"
        elif BusinessLogicUtil.is_only_eng_and_no(text=text):
            return "en"
        elif BusinessLogicUtil.is_only_eng(text=text):
            return "en"
        else:
            return "ko"

    @staticmethod
    def what_does_this_consist_of(text: str):
        result = []
        if BusinessLogicUtil.is_containing_kor(text=text):
            result.append("kor")
        if BusinessLogicUtil.is_containing_eng(text=text):
            result.append("eng")
        if BusinessLogicUtil.is_containing_number(text=text):
            result.append("number")
        if BusinessLogicUtil.is_containing_special_characters_with_thread(text=text):
            result.append("special_characters")
        if BusinessLogicUtil.is_containing_jpn(text=text):
            result.append("jpn")
        # BusinessLogicUtil.print_magenta(rf'text : {text}   result : {result}')
        return result

    @staticmethod
    def get_length_of_mp3(target_pnx: str):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            audio = MP3(target_pnx)
            return audio.info.length
        except mutagen.MutagenError:
            # BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}") # gtts 모듈 불능? mutagen 모듈 불능? license 찾아보자 으로 어쩔수 없다.
            return
        except Exception:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def loop_run_for_speak_as_async_deprecated(ment):
        async def speak_as_async(ment):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            # pyglet_player 가 play() 하고 있으면 before_mp3_length_used_in_speak_as_async 만큼 대기
            BusinessLogicUtil.print_cyan(rf'before_mp3_length_used_in_speak_as_async 만큼 재생 대기')

            # BusinessLogicUtil.pyglet_player 을 del 을 한 경우:
            # BusinessLogicUtil.pyglet_player 에 대한 참조가 불가능해진다. 다른 참조법을 적용해보자. 시도해보니 BusinessLogicUtil.pyglet_player 는 더이상 쓸 수가 없다.
            # 재활용해야하는 BusinessLogicUtil.pyglet_player는 더이상 쓸 수 없어졌다.
            if StateManagementUtil.PYGLET_PLAYER is None:
                import pyglet
                StateManagementUtil.PYGLET_PLAYER = pyglet.media.Player()
            # if hasattr(Park4139, 'pyglet_player') and BusinessLogicUtil.pyglet_player is None:
            #     # BusinessLogicUtil.pyglet_player가 None인 경우
            #     BusinessLogicUtil.pyglet_player = pyglet.media.Player()
            #     pass
            if StateManagementUtil.PYGLET_PLAYER is not None:
                if StateManagementUtil.PYGLET_PLAYER.playing == True:
                    length_of_mp3 = BusinessLogicUtil.previous_mp3_length_used_in_speak_as_async
                    time.sleep(length_of_mp3 * 0.65)  # 이렇면 소리가 겹치지 않는 장점이 있으나, 실제로 일을 미리하고 나중에 보고하는 단점이 있다
                    # asyncio.sleep(length_of_mp3 * 0.65) # 이렇면 실제로 일을 하자마자 보고하는 장점이 있으나, 소리가 겹치는 않는 단점이 있다
                    # time.sleep(length_of_mp3 * 0.75)
                    # time.sleep(length_of_mp3 * 0.85)
                    # time.sleep(length_of_mp3 * 0.95)
                    # time.sleep(length_of_mp3 * 1.05)
                    # time.sleep(length_of_mp3 * 1.00)
            try:
                while True:
                    if type(ment) == str:
                        # while BusinessLogicUtil.is_speak_as_async_running:
                        #     BusinessLogicUtil.print_as_log(f"def {inspect.currentframe().f_code.co_name}() 에 대한 다른 쓰레드를 기다리는 중입니다")
                        #     pass
                        # BusinessLogicUtil.is_speak_as_async_running = True # 쓰레드상태 사용 중으로 업데이트

                        cache_sound = rf'{StateManagementUtil.PROJECT_DIRECTORY}\pkg_sound'
                        BusinessLogicUtil.make_pnx(pnx=cache_sound, mode="d")

                        # BusinessLogicUtil.print_ment_magenta("ment 전처리, 윈도우 경로명에 들어가면 안되는 문자들 공백으로 대체")
                        ment = BusinessLogicUtil.get_str_replaced_special_characters(target=ment, replacement=" ")
                        ment = ment.replace("\n", " ")

                        # BusinessLogicUtil.print_ment_magenta(rf'파일 없으면 생성')
                        ment__mp3 = rf'{cache_sound}\{ment}_.mp3'
                        ment_mp3 = rf'{cache_sound}\{ment}.mp3'
                        if not os.path.exists(ment_mp3):
                            if not os.path.exists(ment__mp3):
                                from gtts import gTTS
                                if "special_characters" in BusinessLogicUtil.what_does_this_consist_of(text=ment):
                                    gtts = gTTS(text=ment, lang='ko')
                                    gtts.save(ment__mp3)
                                elif "kor" in BusinessLogicUtil.what_does_this_consist_of(text=ment):
                                    gtts = gTTS(text=ment, lang='ko')
                                    gtts.save(ment__mp3)
                                elif "eng" in BusinessLogicUtil.what_does_this_consist_of(text=ment):
                                    gtts = gTTS(text=ment, lang='en')
                                    gtts.save(ment__mp3)
                                elif "jpn" in BusinessLogicUtil.what_does_this_consist_of(text=ment):
                                    gtts = gTTS(text=ment, lang='ja')
                                    gtts.save(ment__mp3)
                                else:
                                    gtts = gTTS(text=ment, lang='ko')
                                    gtts.save(ment__mp3)

                        try:
                            BusinessLogicUtil.merge_silent_mp3_and_ment_mp3_and_ment__mp3_via_ffmepeg(ment_mp3, ment__mp3)
                        except Exception:
                            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

                        try:
                            # 자꾸 프로세스 세션을 빼앗기 때문에 불편한 코드
                            # os.system(rf'start /b cmd /c call "{ment_mp3}" >nul 2>&1')

                            # 프로세스 세션을 빼앗지 않고 mp3재생하는 다른 방법
                            # playsound.playsound(os.path.abspath(ment_mp3))

                            # BusinessLogicUtil.print_as_log(rf'프로세스 세션을 빼앗지 않고 mp3재생')
                            ment_mp3 = os.path.abspath(ment_mp3)

                            try:
                                # 재생
                                # pyglet_player = BusinessLogicUtil.pyglet_player

                                pyglet_player = pyglet.media.Player()
                                source = pyglet.media.load(ment_mp3)
                                # BusinessLogicUtil.multiprocessed_source_play = source
                                pyglet_player.queue(source)

                                # 재생추적

                                # 재생 중인 사운드 리소스를 추적하는 이벤트 핸들러 함수
                                def on_player_eos():
                                    player = pyglet.media.Player()
                                    playing_sounds.remove(player)

                                pyglet_player.push_handlers(on_eos=on_player_eos)
                                # pyglet_player.play()  # 이거 재생 안되는데, 이게 공식문서에 나온 방식인데, media 객채 생성 순서가 문제였나 보다.이젠 된다
                                pyglet_player.play()
                                source.play()  # 웃긴다 이거 이렇게는 재생이 된다.
                                playing_sounds = StateManagementUtil.PLAYING_SOUNDS
                                playing_sounds.append(pyglet_player)
                                # 사운드 재생을 시작할 때마다 이벤트 핸들러를 등록하여 playing_sounds 리스트에 추가

                                # FAIL
                                # import  multiprocessing
                                # BusinessLogicUtil.multiprocessed_source_play = multiprocessing.Process(target= source.play , args=None)
                                # BusinessLogicUtil.multiprocessed_source_play.start()

                                if StateManagementUtil.PYGLET_PLAYER.playing == False:
                                    StateManagementUtil.PYGLET_PLAYER = None
                                    BusinessLogicUtil.previous_mp3_length_used_in_speak_as_async = 0

                                # BusinessLogicUtil.is_speak_as_async_running = False # 쓰레드상태 사용종료로 업데이트
                            except FileNotFoundError:
                                BusinessLogicUtil.print_cyan(f"{ment_mp3} 재생할 파일이 없습니다")
                            except:
                                BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
                                return

                            BusinessLogicUtil.print_with_underline("before_mp3_length_used_in_speak_as_async 업데이트")
                            length_of_mp3 = round(float(BusinessLogicUtil.get_length_of_mp3(ment_mp3)), 1)
                            BusinessLogicUtil.previous_mp3_length_used_in_speak_as_async = length_of_mp3

                        except Exception:
                            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

                        # BusinessLogicUtil.print_as_log(rf'불필요 파일 삭제')
                        os.system(f'echo y | del /f "{ment__mp3}" >nul 2>&1')

                        # BusinessLogicUtil.print_as_log(rf'중간로깅')
                        BusinessLogicUtil.print_as_log(string=f"TTS 재생시도")
                        return
                    return
            except Exception:
                BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(speak_as_async(ment))

    @staticmethod
    def speak_ment_experimental(ment, comma_delay=1.00, thread_join_mode=False):
        if platform.system() == 'Windows':
            # if thread_for_speak_as_async is not None:
            #     # 이전에 생성된 쓰레드가 있다면 종료
            #     thread_for_speak_as_async.join()

            # 이미 실행 중인 speak()관련 쓰레드가 있다면 종료시킴
            # if threading.Event() is not None:
            #     global exit_event
            #     exit_event = threading.Event()
            # else:
            #     exit_event.set()
            #     exit_event.clear()  # 종료 이벤트 객체 초기화

            # pyglet을 실행하는 스레드 종료
            # BusinessLogicUtil.kill_thread(thread_name="thread_for_speak")
            # BusinessLogicUtil.kill_thread(thread_name="thread_for_run_loop_for_speak_as_async")

            # 재생 중인 사운드 리소스를 중지하는 함수
            def stop_all_sounds():
                playing_sounds = StateManagementUtil.PLAYING_SOUNDS
                for player in playing_sounds:
                    player.pause()  # 또는 player.stop()

            stop_all_sounds()
            if StateManagementUtil.PYGLET_PLAYER is not None:
                # if BusinessLogicUtil.pyglet_player.playing == True:
                # pyglet.app.exit()
                # BusinessLogicUtil.pyglet_player.delete()
                # BusinessLogicUtil.pyglet_player = None
                # BusinessLogicUtil.pyglet_player.pause()
                # pyglet.app.platform_event_loop.pause()
                # BusinessLogicUtil.pyglet_player.pause()
                # BusinessLogicUtil.pyglet_player.delete()

                # BusinessLogicUtil.pyglet_player 을 del 을 한 경우. 의도한대로 pyglet 의 play() 동작은 중지가 되는데.
                # BusinessLogicUtil.pyglet_player 에 대한 참조가 불가능해진다. 다른 참조법을 적용해보자. 시도해보니 BusinessLogicUtil.pyglet_player 는 더이상 쓸 수가 없다.
                # 재활용해야하는 BusinessLogicUtil.pyglet_player는 더이상 쓸 수 없어졌다.
                # del BusinessLogicUtil.pyglet_player
                # 혹시 몰라서 tmp 변수에 참조시켜서 del 시도 해보았는데, BusinessLogicUtil.pyglet_player에 대해 참조는 가능해 보인다.
                # tmp = BusinessLogicUtil.pyglet_player
                # del tmp
                # del 쓰는 것을 포기하자

                # TBD
                # sound = pyglet.resource.media('sound.wav')
                # sound.stop()
                pass
            else:
                import pyglet
                StateManagementUtil.PYGLET_PLAYER = pyglet.media.Player()
                if StateManagementUtil.PYGLET_PLAYER.playing == True:
                    StateManagementUtil.PYGLET_PLAYER.pause()
                    # BusinessLogicUtil.pyglet_player.delete()
                    # del BusinessLogicUtil.pyglet_player
                    # tmp = BusinessLogicUtil.pyglet_player
        else:
            BusinessLogicUtil.print_cyan(string=f"{inspect.currentframe().f_code.co_name}() 는 리눅스 환경에서 테스트가 필요합니다.")

        # 비동기 이벤트 함수 설정 (simple for void async processing)
        async def process_thread_speak(ment):
            # while not exit_event.is_set(): # 쓰레드 이벤트 제어
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            ment = str(ment)
            ment = ment.strip()
            if ment == "":
                return None
            if BusinessLogicUtil.is_containing_special_characters_with_thread(text=ment):
                ment = BusinessLogicUtil.remove_special_characters(text=ment)
            while True:
                ments = [x.strip() for x in ment.replace(".", ",").split(",")]  # from "abc,abc.abc,abc." to ["abc","abc","abc","abc"] # , or . 를 넣으면 나누어 읽도록 업데이트
                ments = [x for x in ments if x.strip()]  # 리스트 요소 "" 제거,  from ["", A] to [A]
                # [print(item) for item in ments ]
                # print(rf'ments : {ments}')
                # print(rf'type(ments) : {type(ments)}')
                # print(rf'len(ments) : {len(ments)}')
                for ment in ments:
                    # Park4139BusinessLogicUtil.Tts.speak(ment)
                    # thread = threading.Thread(target=partial(Park4139BusinessLogicUtil.Tts.run_loop_for_speak_as_async, ment), name ="thread_for_run_loop_for_speak_as_async")
                    # thread.start()
                    # if thread.is_alive():
                    #     thread.join()
                    BusinessLogicUtil.speak_ment_without_async_experimental_2(ment, delay=comma_delay)
                    pass
                return None

        # 비동기 이벤트 루프 설정 (simple for void async processing)
        def process_thread_loop(ment):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(process_thread_speak(ment))

        # 비동기 이벤트 루프 실행할 쓰레드 설정 (simple for void async processing)
        thread = threading.Thread(target=partial(process_thread_loop, ment), name="thread_for_speak")  # Q: 왜 thread.name 의 case 는 다른거야 ?  wrtn: 네, 스레드의 이름은 일반적으로 대소문자를 구분하지 않습니다.
        thread.start()
        if thread_join_mode == True:
            thread.join()

    @staticmethod
    def speak(string, after_delay=1.00):  # 많이 쓸 수록 프로그램이 느려진다
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        string = str(string)
        string = string.strip()
        if BusinessLogicUtil.is_containing_special_characters(text=string):
            string = BusinessLogicUtil.remove_special_characters(text=string)
        if string == "":
            return None
        try:
            while True:
                ments = []
                if "," in string:  # , 를 넣으면 나누어 읽도록 업데이트
                    ments = string.split(",")
                    for string in ments:
                        BusinessLogicUtil.speak_ment_experimental(ment=string, comma_delay=0.98)
                    break
                if type(string) == str:
                    cache_mp3 = rf'{StateManagementUtil.PROJECT_DIRECTORY}\pkg_mp3'
                    BusinessLogicUtil.make_pnx(pnx=cache_mp3, mode="d")

                    # "ment 전처리, 윈도우 경로명에 들어가면 안되는 문자들 공백으로 대체"
                    string = BusinessLogicUtil.get_str_replaced_special_characters(target=string, replacement=" ")
                    string = string.replace("\n", " ")

                    # 파일 없으면 생성
                    ment__mp3 = rf'{cache_mp3}\{string}_.mp3'
                    ment_mp3 = rf'{cache_mp3}\{string}.mp3'
                    if not os.path.exists(ment_mp3):
                        if not os.path.exists(ment__mp3):
                            from gtts import gTTS
                            if "special_characters" in BusinessLogicUtil.what_does_this_consist_of(text=string):
                                gtts = gTTS(text=string, lang='ko')
                                gtts.save(ment__mp3)
                            elif "kor" in BusinessLogicUtil.what_does_this_consist_of(text=string):
                                gtts = gTTS(text=string, lang='ko')
                                gtts.save(ment__mp3)
                            elif "eng" in BusinessLogicUtil.what_does_this_consist_of(text=string):
                                gtts = gTTS(text=string, lang='en')
                                gtts.save(ment__mp3)
                            elif "jpn" in BusinessLogicUtil.what_does_this_consist_of(text=string):
                                gtts = gTTS(text=string, lang='ja')
                                gtts.save(ment__mp3)
                            else:
                                gtts = gTTS(text=string, lang='ko')
                                gtts.save(ment__mp3)
                    try:
                        silent_mp3 = StateManagementUtil.SILENT_MP3
                        if not os.path.exists(silent_mp3):
                            BusinessLogicUtil.print_as_log("사일런트 mp3 파일이 없습니다")
                            break
                        if not os.path.exists(ment_mp3):
                            cmd = rf'echo y | "ffmpeg" -i "concat:{os.path.abspath(silent_mp3)}|{os.path.abspath(ment__mp3)}" -acodec copy -metadata "title=Some Song" "{os.path.abspath(ment_mp3)}" -map_metadata 0:-1  >nul 2>&1'
                            BusinessLogicUtil.command_to_os_like_person_as_admin(cmd)
                    except Exception:
                        BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
                    try:
                        ment_mp3 = os.path.abspath(ment_mp3)
                        try:
                            import pyglet
                            source = pyglet.media.load(ment_mp3)
                            source.play()

                            length_of_mp3 = BusinessLogicUtil.get_length_of_mp3(ment_mp3)
                            time.sleep(length_of_mp3 * after_delay)
                            return length_of_mp3
                        except FileNotFoundError:
                            BusinessLogicUtil.print_as_log(f"{ment_mp3} 재생할 파일이 없습니다")
                        except:
                            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
                            break
                        BusinessLogicUtil.print_with_underline("before_mp3_length_used_in_speak_as_async 업데이트")
                        length_of_mp3 = round(float(BusinessLogicUtil.get_length_of_mp3(ment_mp3)), 1)
                        BusinessLogicUtil.previous_mp3_length_used_in_speak_as_async = length_of_mp3
                    except Exception:
                        BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

                    os.system(f'echo y | del /f "{ment__mp3}" >nul 2>&1')
                    BusinessLogicUtil.print_as_log(string=f"TTS 재생시도")
                break
        except Exception:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def remove_special_characters(text):
        # pattern = r"[^\w\s]" #  \s(whitespace characters = [" ", "\t", "\n", ".", "\n", "_" ])      # space = " " #공백
        # pattern = r"[^\w.,]" # \w(알파벳, 숫자, 밑줄 문자)와 "." 그리고 ","를 제외한 모든문자를 선택, \t, \n, _ 도 삭제되는 설정
        pattern = r"[~!@#$%^&*()_+|<>?:{}]"
        return re.sub(pattern, "", text)




    @staticmethod
    def print_with_underline(ment):
        BusinessLogicUtil.print_light_black(f'{StateManagementUtil.UNDERLINE}{ment}')
        return f'{StateManagementUtil.UNDERLINE}{ment}'

    @staticmethod
    # def print_ment_via_colorama(ment, color:Union[ColoramaColorUtil.GREEN, ColoramaColorUtil.RED]):
    def print_ment_via_colorama(ment, colorama_color: Enum):
        # colorama 초기화
        # init(autoreset=True)  # 색상전이를 막을 수 있음, 최적화를 한다면 연산되어 콘솔에 출력되는 것을 모두 중단처리. StateManagementUtil.is_op_mode == True 에서 동작하도록 하는 것도 방법이다.
        # 혹시나 싶었는데 console_blurred 에서 팝업 기능과 충돌이 되는 것으로 보인다.

        # colorama_color 값에 해당하는 Fore 값으로 매핑, 리펙토리 후
        colorama_to_fore = {
            ColoramaUtil.BLACK: Fore.BLACK,
            ColoramaUtil.RED: Fore.RED,
            ColoramaUtil.GREEN: Fore.GREEN,
            ColoramaUtil.YELLOW: Fore.YELLOW,
            ColoramaUtil.BLUE: Fore.BLUE,
            ColoramaUtil.MAGENTA: Fore.MAGENTA,
            ColoramaUtil.CYAN: Fore.CYAN,
            ColoramaUtil.WHITE: Fore.WHITE,
            ColoramaUtil.RESET: Fore.RESET,
            ColoramaUtil.LIGHTBLACK_EX: Fore.LIGHTBLACK_EX,
            ColoramaUtil.LIGHTRED_EX: Fore.LIGHTRED_EX,
            ColoramaUtil.LIGHTGREEN_EX: Fore.LIGHTGREEN_EX,
            ColoramaUtil.LIGHTYELLOW_EX: Fore.LIGHTYELLOW_EX,
            ColoramaUtil.LIGHTBLUE_EX: Fore.LIGHTBLUE_EX,
            ColoramaUtil.LIGHTMAGENTA_EX: Fore.LIGHTMAGENTA_EX,
            ColoramaUtil.LIGHTCYAN_EX: Fore.LIGHTCYAN_EX,
            ColoramaUtil.LIGHTWHITE_EX: Fore.LIGHTWHITE_EX
        }
        colorama_color = colorama_to_fore.get(colorama_color, Fore.RESET)
        print(f"{colorama_color}{ment}")
        # colorama_color = colorama_to_fore.get(ColoramaUtil.LIGHTBLACK_EX, Fore.RESET)
        # print(f"{colorama_color}")

    @staticmethod
    def print_red(string):
        BusinessLogicUtil.print_ment_via_colorama(string, colorama_color=ColoramaUtil.RED)

    @staticmethod
    def print_success(string):
        BusinessLogicUtil.print_ment_via_colorama(string, colorama_color=ColoramaUtil.LIGHTGREEN_EX)

    @staticmethod
    def print_magenta(string):
        BusinessLogicUtil.print_ment_via_colorama(string, colorama_color=ColoramaUtil.LIGHTMAGENTA_EX)

    @staticmethod
    def print_light_white(string):
        BusinessLogicUtil.print_ment_via_colorama(string, colorama_color=ColoramaUtil.LIGHTWHITE_EX)

    @staticmethod
    def print_light_yellow(string):
        BusinessLogicUtil.print_ment_via_colorama(string, colorama_color=ColoramaUtil.LIGHTYELLOW_EX)

    @staticmethod
    def print_yellow(string):
        BusinessLogicUtil.print_ment_via_colorama(string, colorama_color=ColoramaUtil.YELLOW)

    @staticmethod
    def print_blue(string):
        BusinessLogicUtil.print_ment_via_colorama(string, colorama_color=ColoramaUtil.BLUE)

    @staticmethod
    def print_light_blue(string):
        BusinessLogicUtil.print_ment_via_colorama(string, colorama_color=ColoramaUtil.LIGHTBLUE_EX)

    @staticmethod
    def print_green(string):
        BusinessLogicUtil.print_ment_via_colorama(string, colorama_color=ColoramaUtil.LIGHTGREEN_EX)

    @staticmethod
    def print_light_black(string):
        BusinessLogicUtil.print_ment_via_colorama(string, colorama_color=ColoramaUtil.LIGHTBLACK_EX)

    @staticmethod
    def print_cyan(string):
        BusinessLogicUtil.print_ment_via_colorama(string, colorama_color=ColoramaUtil.CYAN)

    @staticmethod
    def pause():
        # 디버깅을 시작할 지점
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        # 창 앞으로 이동
        pnx_process_name = "pycharm64.exe"
        # pids = BusinessLogicUtil.get_pids_by_process_name(process_name=pnx_process_name)
        pid = BusinessLogicUtil.get_max_pid_by_process_name(process_name=pnx_process_name, show_mode=False)
        # BusinessLogicUtil.print_as_log(string = rf'''pid="{pid}" %%%FOO%%%''')
        BusinessLogicUtil.move_window_to_front_by_pid(pid=pid, show_mode=False)
        # BusinessLogicUtil.window_move_to_front(window_title_seg=window_title_seg, show_mode=False)

        # sys.exit() #
        # os.system('pause >nul') # windows 환경(파이썬 가상환경 기반)
        pdb.set_trace()  # 파이썬 환경
        # BusinessLogicUtil.print_today_time_info_natural()

    @staticmethod
    def make_project_tree_for_park4139():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        leaf_directorys = [
            StateManagementUtil.PKG_DPL
        ]
        for item in leaf_directorys:
            BusinessLogicUtil.make_pnx(pnx=item, mode="d")
        leaf_files = [
            # ...
        ]
        for item in leaf_files:
            BusinessLogicUtil.make_pnx(pnx=item, mode="f")

    @staticmethod
    def run_pnxs_via_text_file():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        function_name_txt = rf'{StateManagementUtil.PROJECT_DIRECTORY}\pkg_txt\{function_name}.txt'
        BusinessLogicUtil.make_pnx(pnx=function_name_txt, mode="f")
        BusinessLogicUtil.print_magenta(rf'''function_name_txt = {function_name_txt}''')
        BusinessLogicUtil.run_via_explorer_exe(function_name_txt)
        texts = BusinessLogicUtil.get_list_from_f_txt(pnx=function_name_txt)
        # texts = texts.split("\n")
        texts = BusinessLogicUtil.get_list_striped_element(items_list=texts)
        texts_removed_duplication: [str] = []
        for text in texts:  # mkr_remove_duplication
            if text not in texts_removed_duplication:
                if text is not None:
                    texts_removed_duplication.append(text)
        texts = texts_removed_duplication
        for text in texts:
            BusinessLogicUtil.run_via_explorer_exe(text)
        BusinessLogicUtil.print_as_log(string=rf'''texts="{texts}" %%%FOO%%%''')

    @staticmethod
    def get_list_removed_element_duplicated_and_none(items, show_mode=True):
        function_name = inspect.currentframe().f_code.co_name
        if show_mode == False:
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        items = BusinessLogicUtil.get_list_removed_element_duplicated(items)
        items = BusinessLogicUtil.get_list_removed_element_none(items)
        return items

    @staticmethod
    def get_list_removed_element_preprocessed(items_list, show_mode=True):
        function_name = inspect.currentframe().f_code.co_name
        if show_mode == False:
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        if items_list is None:
            return None
        items_list = BusinessLogicUtil.get_list_removed_element_duplicated(items_list, show_mode=show_mode)
        items_list = BusinessLogicUtil.get_list_removed_element_none(items_list, show_mode=show_mode)
        items_list = BusinessLogicUtil.get_list_removed_element_empty(items_list, show_mode=show_mode)
        items_list = BusinessLogicUtil.get_list_replaced_element_from_str_to_str(items_list, "\n", "", show_mode=show_mode)
        items_list = BusinessLogicUtil.get_list_striped_element(items_list, show_mode=show_mode)
        return items_list

    @staticmethod
    def get_list_removed_element_duplicated(items_list, show_mode=True):
        function_name = inspect.currentframe().f_code.co_name
        if show_mode == False:
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        items_removed_duplication: [str] = []
        for item in items_list:
            if item not in items_removed_duplication:
                # if item is not None:
                items_removed_duplication.append(item)
        items_list = items_removed_duplication
        return items_list

    @staticmethod
    def get_list_removed_element_none(items, show_mode=True):
        function_name = inspect.currentframe().f_code.co_name
        if show_mode == False:
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        if items is not None:
            return [x for x in items if x is not None]
        return None

    # @staticmethod
    # def get_last_digit(string, show_mode=True):
    #     function_name = inspect.currentframe().f_code.co_name
    #     if show_mode == False:
    #         BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
    #     # match = re.search(r'\d$', string) # 숫자 1자리를 지우는 코드
    #     match = re.search(r'\d{1,2}\b$', string.strip())  # 숫자 1자리 또는 2자리를 지우는 코드
    #     if match:
    #         return match.group(0)
    #     return "00"  # 숫자를 찾지 못한 경우 기본값 "00" 반환

    @staticmethod
    def get_last_digit(string, show_mode=True):
        function_name = inspect.currentframe().f_code.co_name
        if show_mode == False:
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        match = re.search(r'\d+\b$', string.strip())  # 끝에 위치한 모든 연속된 숫자를 찾음
        if match:
            return match.group(0)  # 매칭된 숫자 반환
        return "00"  # 숫자를 찾지 못한 경우 기본값 "00" 반환

    @staticmethod
    def get_str_removed_last_digit(string, show_mode=True):
        function_name = inspect.currentframe().f_code.co_name
        if show_mode == False:
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        return re.sub(r'\d+\s*$', '', string)



    @staticmethod
    def download_torrent_magnets_from_torrentqq(title_to_search=None, driver=None, via_txt_f=None): #mkr.
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        browser_show_mode = True
        try:
            function_name_txt = rf'{StateManagementUtil.PROJECT_DIRECTORY}\pkg_txt\{function_name}.txt'
            function_name_back_up_txt = rf'{StateManagementUtil.PROJECT_DIRECTORY}\pkg_txt\{function_name}.txt.bkp'


            if title_to_search is None and via_txt_f is None:
                BusinessLogicUtil.print_as_log(f'''"string_to_search 와 via_text_file 둘 중 하나는 설정을 해야합니다"''', print_color='red')
                return
            if title_to_search is not None and via_txt_f is not None:
                BusinessLogicUtil.print_as_log(f'''"string_to_search 와 via_text_file 둘 중 하나만 설정을 해야합니다"''', print_color='red')
                return

            # 텍스트 백업
            BusinessLogicUtil.print_as_log(f'''"%%%FOO%%%"''', print_color='green')
            list_to_search = BusinessLogicUtil.get_list_from_f_txt(pnx=function_name_txt)
            list_to_search = BusinessLogicUtil.get_list_striped_element(items_list=list_to_search)
            BusinessLogicUtil.make_pnx(pnx=function_name_back_up_txt, mode="f")
            # BusinessLogicUtil.run_pnx_via_explorer_exe(function_name_back_up_txt, show_mode=False)
            with open(function_name_back_up_txt, 'a', encoding='utf-8') as file:
                file.write(f"{StateManagementUtil.UNDERLINE}\n")
                for text in list_to_search:
                    file.write(text + "\n")
            # BusinessLogicUtil.run_pnx_via_explorer_exe(function_name_back_up_txt, print_mode=False)


            list_to_search = []
            if title_to_search != None:
                list_to_search.append(title_to_search)
                list_to_search = BusinessLogicUtil.get_list_removed_element_contain_string(items=list_to_search, string="#")  # ignore line
                BusinessLogicUtil.print_as_log(string=rf'''texts="{list_to_search}" %%%FOO%%%''')
                BusinessLogicUtil.print_as_log(string=rf'''len(texts)="{len(list_to_search)}" %%%FOO%%%''')
            elif via_txt_f == True:
                BusinessLogicUtil.make_pnx(pnx=function_name_txt, mode="f")
                BusinessLogicUtil.run_via_explorer_exe(function_name_txt, show_mode=False)
                list_to_search = BusinessLogicUtil.get_list_from_f_txt(pnx=function_name_txt)
                list_to_search = BusinessLogicUtil.get_list_striped_element(items_list=list_to_search)
                list_to_search = BusinessLogicUtil.get_list_removed_element_duplicated(items_list=list_to_search)
                list_to_search = BusinessLogicUtil.get_list_removed_element_contain_string(items=list_to_search, string="#")  # ignore line
                BusinessLogicUtil.print_as_log(string=rf'''list_to_search="{list_to_search}" %%%FOO%%%''')
                BusinessLogicUtil.print_as_log(string=rf'''len(list_to_search)="{len(list_to_search)}" %%%FOO%%%''')

            # 셀레니움 웹드라이버 로딩
            from selenium.webdriver.support.ui import WebDriverWait
            from selenium.webdriver.support import expected_conditions as EC
            from selenium.webdriver.common.by import By
            from selenium import webdriver
            from selenium.webdriver.chrome.service import Service
            from selenium.webdriver.chrome.options import Options
            if driver is None:
                driver = BusinessLogicUtil.get_driver_selenium(browser_show_mode=browser_show_mode)
            # driver.set_window_size(500, 1000)
            # driver.execute_script("window.scrollTo(200, 300);") 스크롤
            # driver.execute_script("alert('hello selenium!!!');")
            # driver.find_element(By.CSS_SELECTOR, "#q").send_keys("셀레니움") #문자열 입력
            # driver.find_element(By.CSS_SELECTOR, '.inner_search > .ico_pctop.btn_search').click() #검색버튼 클릭
            # driver.quit()

            # CAPTCHA 확인
            # WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'captcha-id')))  # CAPTCHA 요소 ID로 변경
            # print("CAPTCHA가 나타났습니다. 사용자가 해결하세요.")
            # 사용자가 CAPTCHA를 해결할 수 있도록 대기
            # input("CAPTCHA를 해결한 후 Enter를 눌러 계속 진행하세요.")

            items = list_to_search
            for item in items:
                BusinessLogicUtil.print_as_log(f"{StateManagementUtil.UNDERLINE}")
                search_keyword = item
                BusinessLogicUtil.print_as_log(string = rf'''search_keyword="{search_keyword}" %%%FOO%%%''')
                query = BusinessLogicUtil.get_encoded_url(search_keyword)
                if query == "":
                    BusinessLogicUtil.print_as_log(f"[실패] {search_keyword} 아무것도 입력되지 않았습니다")
                else:
                    # 페이지 출력
                    url = f'https://torrentqq340.com/search?q={query}'
                    BusinessLogicUtil.print_as_log(f'''url  = {url}''')
                    url = BusinessLogicUtil.get_decoded_url(url)
                    BusinessLogicUtil.print_as_log(f'''url  = {url}''')
                    driver.get(url)

                    # 페이지 정적웹소스 다운로드 대기
                    BusinessLogicUtil.sleep(milliseconds=random.randint(a=222, b=1333))


                    # 정상탭이동
                    try_cnt_limit =22
                    try_cnt = 0
                    tab_title_negative = "잠시만 기다리십시오"
                    while True:
                        if BusinessLogicUtil.does_normal_tab_exist(driver_selenium=driver, tab_title_negative=tab_title_negative):
                            window_required = driver.current_window_handle  # 현재 창 핸들 저장
                            driver.switch_to.window(window_required)
                            BusinessLogicUtil.print_as_log(f"%%%FOO%%% green 정상탭이동")
                            break
                        try_cnt +=1
                        if try_cnt == try_cnt_limit:
                            driver = BusinessLogicUtil.get_driver_selenium(browser_show_mode=browser_show_mode)
                            BusinessLogicUtil.close_tabs_except_current_tab_via_selenium(driver)
                            driver.get(url)
                            BusinessLogicUtil.sleep(milliseconds=random.randint(a=222, b=1333))
                            try_cnt = 0

                        # 새탭복사
                        BusinessLogicUtil.copy_tab_like_pserson()
                        # BusinessLogicUtil.open_tab_via_selenium(driver, url)
                        BusinessLogicUtil.sleep(milliseconds=random.randint(a=222, b=1333))


                        # 체크박스 클릭
                        BusinessLogicUtil.move_window_to_front(window_title_seg=tab_title_negative)  # 창을 맨앞으로 가져오기
                        # BusinessLogicUtil.sleep(milliseconds=random.randint(a=544, b=655))
                        BusinessLogicUtil.sleep(milliseconds=random.randint(a=22, b=222))
                        img = rf'{StateManagementUtil.PKG_PNG}\collect_img_for_autogui_2024_11_03_19_41_12.png'
                        BusinessLogicUtil.click_img_via_autogui(img, x_cal=-15)
                        BusinessLogicUtil.print_as_log(f"%%%FOO%%% green 체크박스 클릭")


                    # 나머지탭을 닫는다
                    BusinessLogicUtil.close_tabs_except_current_tab_via_selenium(driver)

                    # 정적웹소스 다운로드
                    BusinessLogicUtil.sleep(milliseconds=random.randint(a=2222, b=4333))  # 정적웹소스 다운로드 대기
                    page_src = driver.page_source
                    soup = BeautifulSoup(page_src, "html.parser")  # web parser 설정

                    hrefs = []
                    titles = []
                    links = []
                    lines = soup.find_all(name="a")
                    for line in lines:
                        title = line.get('title')
                        href = line.get('href')
                        titles.append(title)
                        hrefs.append(href)
                        if title and href:  # 둘 다 존재할 때만 리스트에 추가
                            links.append((title, href))
                    hrefs = BusinessLogicUtil.get_list_removed_element_preprocessed(hrefs)
                    titles = BusinessLogicUtil.get_list_removed_element_preprocessed(titles)
                    keywords_required = search_keyword.split(" ")

                    # logging
                    # BusinessLogicUtil.print_as_log(string = rf'''page_src="{page_src}" %%%FOO%%%''')
                    # BusinessLogicUtil.print_as_log(f'''soup.get_text()={soup.get_text()} %%%FOO%%% 데이터파싱''')
                    # BusinessLogicUtil.print_as_log(rf'''len(hrefs) = {len(hrefs)}''')
                    # BusinessLogicUtil.print_as_log(rf'''len(titles) = {len(titles)}''')
                    # BusinessLogicUtil.print_as_log(string=rf'''len(links)="{len(links)}" %%%FOO%%%''')
                    # BusinessLogicUtil.print_list_as_vertical(links, 'links')
                    # BusinessLogicUtil.print_as_log(f'''search_keyword = {search_keyword}''')
                    # BusinessLogicUtil.print_as_log(f'''keywords_required={keywords_required} %%%FOO%%% 매칭키워드생성''')

                    # 매칭키워드에 매칭하는 링크추출
                    links_requried = []
                    for title, href in links:
                        if BusinessLogicUtil.check_str_inclusion_all_texts(text_str=title, texts_list=keywords_required):
                            BusinessLogicUtil.print_as_log(f'''title = {title}  href = {href}''')
                            links_requried.append((title, href))

                    # 상세페이지이동
                    for title, href in links_requried:
                        original_window = driver.current_window_handle  # 원래 탭 저장
                        BusinessLogicUtil.open_tab_via_selenium(driver, href)
                        new_window = [window for window in driver.window_handles if window != original_window][0]
                        if not BusinessLogicUtil.check_str_inclusion_all_texts(text_str=driver.title, texts_list=keywords_required):
                            BusinessLogicUtil.print_as_log(f'''"%%%FOO%%%"''', print_color='red')
                            return
                        driver.switch_to.window(new_window)  # 새 탭으로 가기
                        BusinessLogicUtil.close_tabs_except_current_tab_via_selenium(driver)  # 나머지 탭 닫기
                        # break
                    BusinessLogicUtil.print_as_log(f'''"%%%FOO%%%"''', print_color='green')

                    # 정적웹소스
                    BusinessLogicUtil.sleep(milliseconds=random.randint(a=2222, b=4333))  # 정적웹소스 다운로드 대기
                    page_src = driver.page_source
                    BusinessLogicUtil.print_as_log(f'''len(page_src)={len(page_src)} %%%FOO%%% 상세페이지HTML다운로드''')

                    # web parser
                    soup = BeautifulSoup(page_src, "html.parser")
                    soup_get_text =soup.get_text()
                    BusinessLogicUtil.print_as_log(string = rf'''soup_get_text="{soup_get_text}" %%%FOO%%%''')
                    string_negative ='잠시만 기다리십시오…torrentqq'
                    if  string_negative in soup_get_text:
                        break
                    BusinessLogicUtil.print_as_log(string = rf'''len(soup_get_text)="{len(soup_get_text)}" %%%FOO%%%''')
                    hrefs = []
                    titles = []
                    links = []
                    onclicks = []
                    classes = []
                    inner_texts = []
                    lines = soup.find_all(name="a")
                    BusinessLogicUtil.print_as_log(string=rf'''lines="{lines}" %%%FOO%%%''')
                    BusinessLogicUtil.print_as_log(string=rf'''len(lines)="{len(lines)}" %%%FOO%%%''')
                    for line in lines:
                        title = line.get('title')
                        href = line.get('href')
                        onclick = line.get('onclick')
                        a_class = line.get('class')
                        inner_text = line.get_text(strip=True)
                        titles.append(title)
                        hrefs.append(href)
                        onclicks.append(onclick)
                        classes.append(a_class)
                        inner_texts.append(inner_text)
                        if a_class is not None and "btn-magnet" in a_class and onclick:  # 둘 다 존재할 때만 리스트에 추가
                            links.append((inner_text, a_class, onclick))
                    search_keyword_without_useless = search_keyword.strip()
                    keywords_required = search_keyword_without_useless.split(" ")

                    # logging
                    BusinessLogicUtil.print_as_log(string=rf'''links="{links}" %%%FOO%%%''')
                    BusinessLogicUtil.print_as_log(f'''len(links)={len(links)} %%%FOO%%% 상세페이지 a 태그 inner_text class onclick 속성 파싱''')
                    BusinessLogicUtil.print_as_log(f'''search_keyword={search_keyword} %%%FOO%%%''')
                    BusinessLogicUtil.print_as_log(f'''search_keyword_without_useless={search_keyword_without_useless} %%%FOO%%%''')
                    BusinessLogicUtil.print_as_log(f'''keywords_required={keywords_required} %%%FOO%%% 상세페이지 매칭키워드생성''')

                    for inner_text, a_class, onclick in links:
                        BusinessLogicUtil.print_as_log(f'''links={links} %%%FOO%%%''')
                        BusinessLogicUtil.print_as_log(rf"""all(keyword in inner_text for keyword in keywords_required) = {all(keyword in inner_text for keyword in keywords_required)}""")
                        url = driver.current_url
                        base_url = BusinessLogicUtil.get_base_url(url)
                        onclick = onclick
                        magnet_path = re.search(r"'(.+?)'", onclick)
                        if magnet_path:
                            BusinessLogicUtil.print_as_log(f'''magnet_path = {magnet_path}''')
                            magnet_link = f"{magnet_path.group(1)}"
                            magnet_link = f"{magnet_link.replace("//", "/")}"
                            magnet_link = f"{base_url}{magnet_link}"
                            BusinessLogicUtil.print_as_log(f'''magnet_link = {magnet_link}''')

                            # 마그넷 다운로드 ver 1.0.2
                            # webbrowser.open(magnet_link)

                            # 마그넷 다운로드 ver 1.0.1
                            BusinessLogicUtil.run_via_explorer_exe(magnet_link, show_mode=False)

                            # 마그넷 다운로드 ver 1.0.2
                            # command = f'explorer  "{magnet_link}"'
                            # BusinessLogicUtil.command_to_os(command=command, show_mode=False, mode='a' )
                            # BusinessLogicUtil.command_to_os(cmd=command, show_mode=False)

                            # 다운로드 받은 기존텍스트 기록제거
                            txts = BusinessLogicUtil.get_list_from_f_txt(pnx=function_name_txt)
                            txt_without_prefix = search_keyword.strip()
                            txt_without_prefix = txt_without_prefix.strip()
                            txts_updated = BusinessLogicUtil.get_list_striped_element(items_list=txts)
                            txts_updated = BusinessLogicUtil.get_list_removed_element_duplicated(items_list=txts_updated)
                            txts_updated = [txt for txt in txts_updated if txt_without_prefix not in txt]
                            txts_updated = BusinessLogicUtil.get_list_removed_element_empty(items_list=txts_updated)
                            BusinessLogicUtil.write_list_to_f_txt(pnx=function_name_txt, texts=txts_updated, mode="w")
                            BusinessLogicUtil.print_as_log(f'''texts_updated={txts_updated} %%%FOO%%%''')

                            # 다운로드 받을 다음텍스트 추가 #.torrent 파일이 없는 경우
                            text_before = search_keyword.strip()
                            new_number = str(str(int(BusinessLogicUtil.get_last_digit(text_before)) + 1).zfill(2)).strip()
                            text_removed_success_and_last_digit = BusinessLogicUtil.get_str_removed_last_digit(text_before).strip()
                            if title_to_search is None:
                                ment = f"{text_removed_success_and_last_digit}{new_number}"
                            else:
                                ment     = f"{text_removed_success_and_last_digit}"
                            BusinessLogicUtil.write_str_to_file(pnx=function_name_txt, txt_str=f"{ment}\n", mode="a", show_mode=False)  # mkr_텍스트 추가

                            # 부수적으로 열린 탭닫기
                            # URL을 포함하는 탭을 찾아 닫는 함수
                            BusinessLogicUtil.refresh_chrome_tab(url_to_close=magnet_link)
                            BusinessLogicUtil.close_chrome_tab(url_to_close=magnet_link)

                        else:
                            BusinessLogicUtil.print_as_log("마그넷 경로를 찾을 수 없습니다.")
                        break



        except:
            traceback.print_exc(file=sys.stdout)

    @staticmethod
    def check_str_inclusion_all_texts(text_str, texts_list):
        if all(keyword in text_str for keyword in texts_list):
            return True
        else:
            return False

    @staticmethod
    def get_encoded_url(string):
        return urllib.parse.quote(f"{string}")

    @staticmethod
    def get_decoded_url(string):
        return urllib.parse.unquote(string)

    @staticmethod
    def copy_str_to_clipboard(string):
        clipboard.copy(string)

    @staticmethod
    def sum_via_text_file():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        function_name_txt = rf'{StateManagementUtil.PROJECT_DIRECTORY}\pkg_txt\{function_name}.txt'
        BusinessLogicUtil.make_pnx(pnx=function_name_txt, mode="f")
        BusinessLogicUtil.run_via_explorer_exe(function_name_txt)

        texts = BusinessLogicUtil.get_list_from_f_txt(pnx=function_name_txt)
        # texts = texts.split("\n")
        texts = BusinessLogicUtil.get_list_striped_element(items_list=texts)
        total = 0
        for text in texts:
            if text is not None:
                total += int(text.strip())
        [BusinessLogicUtil.print_light_black(item) for item in texts]
        BusinessLogicUtil.print_as_log(f'''len(texts)={len(texts)}''')
        BusinessLogicUtil.print_as_log(f'''total={total}''')

    @staticmethod
    def get_p(pnx):
        return rf"{os.path.dirname(pnx)}"

    @staticmethod
    def close_tabs_except_current_tab_via_selenium(driver):
        # 현재 탭 핸들 저장
        current_window = driver.current_window_handle

        # 모든 탭 확인
        for window in driver.window_handles:
            if window != current_window:  # 현재 탭 제외
                driver.switch_to.window(window)
                # BusinessLogicUtil.press("ctrl", "w", interval=0.15)
                driver.close()  # 탭 닫기
                time.sleep(0.1)
            #     BusinessLogicUtil.sleep(milliseconds=random.randint(a=22, b=2222))
            # BusinessLogicUtil.sleep(milliseconds=random.randint(a=22, b=2222))

        # 원래 탭으로 돌아가기
        driver.switch_to.window(current_window)
        BusinessLogicUtil.print_as_log(f"%%%FOO%%% green 나머지탭닫기")

    @staticmethod
    def click_img_via_autogui(img, x_cal=0, y_cal=0):
        # confidence=0.7(70%)유사도를 낮춰 인식률개선시도, region 낮춰 속도개선시도, grayscale 흑백으로 판단해서 속도개선시도,

        # 이미지중앙좌표 클릭
        img_finding_loop_cnt = 0
        img_finding_loop_cnt_limit = 10
        while True:
            img_finding_loop_cnt = img_finding_loop_cnt + 1
            try:
                x, y = pyautogui.locateCenterOnScreen(image=img, confidence=0.7, grayscale=True)
            except pyautogui.ImageNotFoundException:
                BusinessLogicUtil.print_as_log(rf"[실패] 이미지찾기")
                break
            if x is not None and y is not None:
                x_cal = x_cal
                y_cal = y_cal
                x = x - x_cal
                y = y - y_cal

                # 마우스위치 기록
                initial_position = pyautogui.position()

                duration = 1
                BusinessLogicUtil.move_mouse(x_abs=x, y_abs=y, duration=duration)
                pyautogui.click()

                # 마우스위치 원복
                x, y = initial_position
                duration = 0
                BusinessLogicUtil.move_mouse(x_abs=x, y_abs=y, duration=duration)
                BusinessLogicUtil.print_as_log(rf"%%%FOO%%% green 이미지중앙좌표클릭 ({x}, {y})")
                break

            BusinessLogicUtil.print_as_log(rf"[실패] 이미지중앙좌표클릭")
            if img_finding_loop_cnt == img_finding_loop_cnt_limit:
                BusinessLogicUtil.print_as_log(rf"[실패] 이미지중앙좌표클릭")
                break

    @staticmethod
    def open_tab_via_selenium(driver, url):
        driver.execute_script(rf"window.open('{url}', '_blank');")
        # driver.get(f"{url}")
        # new_window = [window for window in driver.window_handles if window != original_window][0] # 새 탭의 모든 핸들을 가져옴

    @staticmethod
    def copy_tab_like_pserson():
        BusinessLogicUtil.press("ctrl", "l", interval=0.15)
        BusinessLogicUtil.sleep(milliseconds=random.randint(a=12, b=23))
        BusinessLogicUtil.press("alt", "shift", "enter", interval=0.15)
        # BusinessLogicUtil.print_as_log(f"%%%FOO%%% green 새탭복사")

    @staticmethod
    def get_base_url(url):
        from urllib.parse import urlparse
        parsed_url = urlparse(url)
        base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"
        return base_url

    @staticmethod
    def print_list_as_vertical(items_list, items_list_name='Undefined'):
        for name, value in locals().items():
            if value == items_list:
                BusinessLogicUtil.print_light_black(f'''{items_list_name}=[''')
        [BusinessLogicUtil.print_light_black(f"    rf'{item}',") for item in items_list]
        BusinessLogicUtil.print_light_black(f"""]\n""")

    @staticmethod
    def print_list_as_horizontal(items, items_name):
        for name, value in locals().items():
            if value == items:
                BusinessLogicUtil.print_light_black(f'''{items_name}={value}''')

    # @staticmethod
    # def pnxs_classify_to_pkg_extensions_via_hard_coded():
    #
    #     pnx = rf'D:\#기타\pkg_files'
    #
    #     # target_pnx가 유효한 디렉토리인지 확인
    #     if BusinessLogicUtil.is_file(pnx=pnx):
    #         BusinessLogicUtil.print_light_black(f"{pnx} 는 정리할 수 있는 디렉토리가 아닙니다")
    #         return
    #
    #     # 파일과 디렉토리 get
    #     texts_to_exclude = [
    #         StateManagementUtil.DB_YAML,
    #         StateManagementUtil.SUCCESS_LOG,
    #         StateManagementUtil.LOCAL_PKG_CACHE_FILE,
    #     ]
    #     dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_without_walking(pnx=pnx, texts_to_exclude=texts_to_exclude)
    #     # dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_with_walking(pnx=pnx, texts_to_exclude= texts_to_exclude)
    #
    #     # 파일 처리
    #     for file_pnx in file_pnxs:
    #         file_pnx = file_pnx[0]
    #         file_p = BusinessLogicUtil.get_p(file_pnx)
    #         file_x = BusinessLogicUtil.get_x(file_pnx).replace(".", "")
    #         pkg_ext = rf"{file_p}\pkg_{file_x}"
    #         BusinessLogicUtil.make_pnx(pkg_ext, mode="d")
    #         BusinessLogicUtil.move_pnx_without_overwrite(src=file_pnx, dst=pkg_ext)
    #         BusinessLogicUtil.print_as_log(string=rf'''file_pnx="{file_pnx}" %%%FOO%%%''')
    #
    #     # 디렉토리 처리
    #     # for dir_pnx in dir_pnxs:
    #     #     dir_pnx = dir_pnx[0]
    #     #     dir_p = BusinessLogicUtil.get_p(dir_pnx)
    #     #     pkg_ext = rf"{dir_p}\pkg_directory"
    #     #     BusinessLogicUtil.make_pnx(pkg_ext, target_mode="d")
    #     #     BusinessLogicUtil.move_pnx_without_overwrite(pnx=dir_pnx, dst=pkg_ext)
    #     #     BusinessLogicUtil.print_as_log(string = rf'''dir_pnx="{dir_pnx}" %%%FOO%%%''')

    @staticmethod
    def get_current_file_name():
        CURRENT_FILE = os.path.basename(__file__)
        return CURRENT_FILE

    @staticmethod
    def print_class_field_and_value(class_name):  # print 보다는 get 으로 바꾸는게 좋겠다.
        command_usage_explanations = []
        command_usage_explanations.append(title)
        command_usage_explanations.append('\n')
        command_usage_explanations.append('<예시> : python console_blurred.py <mode_option>')
        command_usage_explanations.append('\n')
        longest_field = max(vars(class_name), key=len)  # mkr_get_longest_field_name
        longest_value = vars(class_name)[longest_field]  # mkr_get_longest_field_value
        for key, value in class_name.__dict__.items():  # mkr_get_field_name_and_field_value
            if not key.startswith('__'):  # 내장 속성 제외
                command_usage_explanations.append(f"{key}{" " * (len(longest_field) - len(key))}: {value}")
        command_usage_explanations.append('\n')
        for command_usage_explanation in command_usage_explanations:
            BusinessLogicUtil.print_light_black(string=command_usage_explanation)
        command_usage_explanations.append('\n')

    @staticmethod
    def get_current_directory_name():
        texts_removed_duplicated_element = []
        CURRENT_DIRECTORY = BusinessLogicUtil.command_to_os_like_person_as_admin(rf'echo %cd%', show_mode=False)
        for text in CURRENT_DIRECTORY:  # remove_duplication
            if text not in texts_removed_duplicated_element:
                if text is not None:
                    texts_removed_duplicated_element.append(text)
        CURRENT_DIRECTORY = texts_removed_duplicated_element
        CURRENT_DIRECTORY = [item.strip() for item in CURRENT_DIRECTORY]  # strip_list_element_each
        CURRENT_DIRECTORY = [item for item in CURRENT_DIRECTORY if item and item.strip()]
        CURRENT_DIRECTORY = " ".join(CURRENT_DIRECTORY)  # convert_from_list_to_str
        return CURRENT_DIRECTORY

    @staticmethod
    def classify_pnxs_to_pn_dir(src):
        # BusinessLogicUtil.run_pnx_via_explorer_exe(target_pnx,show_mode=False)
        for filename in os.listdir(src):
            pnx_item = os.path.join(src, filename)
            if os.path.isfile(pnx_item):
                BusinessLogicUtil.print_light_black(f'''pnx_item = {pnx_item}''')
                file_name_directory_pnx = os.path.join(src, filename)
                file_name_directory_pn = BusinessLogicUtil.get_pn(file_name_directory_pnx)

                if not os.path.exists(file_name_directory_pn):
                    os.makedirs(file_name_directory_pn)

                # shutil.move(pnx_item, file_name_directory_pn) # 중복있으면 에러로 처리됨
                BusinessLogicUtil.move_pnx_without_overwrite(src=pnx_item, dst=file_name_directory_pn)  # 중복있으면 timestamp를 붙여 이동됨

    @staticmethod
    def get_windows_opened():
        # return BusinessLogicUtil.get_windows_opened_via_psutil()
        # return BusinessLogicUtil.get_windows_opened_via_pygetwindow()
        return BusinessLogicUtil.get_windows_opened_via_win32gui()

    @staticmethod
    def get_windows_opened_via_win32gui():
        window_titles = []

        def enum_windows_callback(hwnd, lparam):
            if win32gui.IsWindowVisible(hwnd):
                # 창의 제목을 가져와서 리스트에 추가
                window_title = win32gui.GetWindowText(hwnd)
                if window_title:  # 제목이 비어있지 않은 창만 추가
                    window_titles.append(window_title)

        win32gui.EnumWindows(enum_windows_callback, None)
        return window_titles

    # @staticmethod
    # def get_windows_opened_via_psutil():
    #     import psutil
    #     process_names = []
    #     for proc in psutil.process_iter(['pid', 'name']):
    #         try:
    #             process_names.append(proc.info['name'])  # proc.info 없는데?
    #         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
    #             pass
    #     return process_names

    @staticmethod
    def get_windows_opened_via_pygetwindow():
        windows = pygetwindow.getAllTitles()
        return windows

    @staticmethod
    def is_window_open(window_title_seg, show_mode=True):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        windows_titles_opened = BusinessLogicUtil.get_windows_opened()
        for windows_title_opened in windows_titles_opened:
            # BusinessLogicUtil.print_light_black(f'''windows_title_opened = {windows_title_opened}''')
            if window_title_seg in windows_title_opened:
                if show_mode == True:
                    BusinessLogicUtil.print_as_log(f'''"{windows_title_opened}" 창이 열려 있습니다''')
                return True
        if show_mode == True:
            BusinessLogicUtil.print_as_log(f'''"{window_title_seg}" 창이 닫혀 있습니다''')
        return False

    @staticmethod
    def is_window_open_via_pygetwindow(window_title):
        windows = pygetwindow.getAllTitles()  # 모든 열린 창들의 제목을 가져옴
        return window_title in windows  # 특정 창이 열려 있는지 확인

    @staticmethod
    def is_window_open_via_win32gui(window_title):
        import win32gui
        def enum_windows_callback(hwnd, lparam):
            if win32gui.IsWindowVisible(hwnd):
                # 창의 제목을 확인
                if window_title in win32gui.GetWindowText(hwnd):
                    # BusinessLogicUtil.print_as_log(f'''"{win32gui.GetWindowText(hwnd)}"''')
                    lparam.append(hwnd)

        # 열린 창들을 확인
        hwnd_list = []
        win32gui.EnumWindows(enum_windows_callback, hwnd_list)

        # 특정 창이 열려 있는지 확인
        return any(window_title in win32gui.GetWindowText(hwnd) for hwnd in hwnd_list)

    @staticmethod
    def window_close_by_title(window_title):
        BusinessLogicUtil.close_window_by_title_via_wind32con(window_title)

    @staticmethod
    def close_window_by_title_via_wind32con(window_title):
        import win32con
        def enum_windows_callback(hwnd, lparam):
            try:
                if win32gui.IsWindowVisible(hwnd):
                    current_window_title = win32gui.GetWindowText(hwnd)
                    if current_window_title == window_title:
                        win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
                        print(f'창 "{window_title}"을(를) 닫았습니다.')
                        return False  # 창을 찾았으면 더 이상 탐색하지 않음
            except Exception as e:
                print(f"오류 발생: {traceback.format_exc()}")
            return True  # 계속 탐색

        try:
            # 모든 창을 탐색하여 해당 제목을 찾음
            win32gui.EnumWindows(enum_windows_callback, None)
        except Exception as e:
            print(f"EnumWindows 호출 중 오류 발생: {traceback.format_exc()}")

    @staticmethod
    def open_window_by_pnx(pnx):
        BusinessLogicUtil.run_via_explorer_exe(pnx, show_mode=False)

    @staticmethod
    def move_window_to_front(window_title_seg, show_mode=True):
        if show_mode == True:
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            def enum_windows_callback(hwnd, lparam):
                function_name = inspect.currentframe().f_code.co_name
                # todo 출력하지말자
                # BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
                if win32gui.IsWindowVisible(hwnd):
                    current_window_title = win32gui.GetWindowText(hwnd)
                    if window_title_seg.lower() in current_window_title.lower():
                        # 창을 전면에 표시하려면 먼저 ShowWindow 호출 후 SetForegroundWindow 호출
                        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # 최소화된 창 복원
                        time.sleep(0.2)  # 창 복원 후 잠시 대기
                        # SetForegroundWindow를 재시도
                        try:
                            win32gui.SetForegroundWindow(hwnd)  # 창을 제일 앞으로 가져옴
                            BusinessLogicUtil.print_as_log(f'''"f'"{window_title_seg}" 창을 제일 앞으로 이동시켰습니다.'"''')
                        except Exception as e:
                            BusinessLogicUtil.print_as_log(f'''"f"SetForegroundWindow 호출 재시도 Error: {str(e)}""''')
                            time.sleep(0.2)  # 잠시 대기 후 재시도
                            win32gui.SetForegroundWindow(hwnd)  # 재시도
                        return False  # 더 이상 검색하지 않음
                return True  # 계속 검색

            try:
                win32gui.EnumWindows(enum_windows_callback, None)
            except pywintypes.error:
                BusinessLogicUtil.print_as_log(f"pywintypes.error 는 pass")
        except Exception as e:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def get_window_titles():
        window_titles = []
        try:
            def enum_windows_callback(hwnd, lparam):
                if win32gui.IsWindowVisible(hwnd):
                    current_window_title = win32gui.GetWindowText(hwnd)
                    if current_window_title:  # 제목이 비어 있지 않은 경우에만 추가
                        window_titles.append(current_window_title)
                return True  # 계속해서 다른 창들도 검색

            # 모든 윈도우를 열거하여 창 제목을 window_titles 리스트에 추가
            win32gui.EnumWindows(enum_windows_callback, None)

        except Exception as e:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

        return window_titles

    @staticmethod
    def print_and_speak(string, print_color='blue',after_delay=1.00):
        BusinessLogicUtil.print_as_log(string=string, print_color=print_color)
        BusinessLogicUtil.speak(string=string, after_delay=after_delay)

    @staticmethod
    def classify_pnxs_to_special_keyword_dir(pnx, with_walking):
        special_keywords = [  # special_keywords는 텍스트의 길이가 길수록 분류가 잘될 확률이 높다
            # _______________________________________ mkr_예능
            "서진이네",
            "심야괴담회",
            "텐트 밖은 유럽",
            "삼시세끼 Light",
            "텐트 밖은 유럽 로맨틱 이탈리아",
            # "김병만의_정글의_법칙",
            # "강식당",
            # "_________",
            # _______________________________________ mkr_드라마
            "정년이",
            # _______________________________________ mkr_영화
            "베테랑2",
            "더 킬러스",
            "Venom The Last Dance, 2024",
            "칸다하르",
            # "영화",
            # "로멘틱 영화 Love My Scent 2023",
            "Love.Lies.Bleeding.2024",
            "문경.2024",
            # _______________________________________ mkr_애니
            "Hananoi-kun to Koi no Yamai",
            "Kaii to Otome to Kamikakushi",
            "모노노케 우중망령",
            "Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka S5",
            "Re Zero kara Hajimeru Isekai Seikatsu",
            "Dragon Ball Daima",
            "Sword Art Online Alternative - Gun Gale Online S2",
            "Haikyuu",
            "Crayon.Shinchan",
            "Ao no Exorcist",
            "One Piece",
            "Hime-sama Goumon no Jikan Desu",
            "Seirei Gensouki S2",
            "Isekai Shoukan wa Nidome Desu",
            "Amagami-san Chi no Enmusubi",
            "Highspeed Etoile",
            "Dandadan",
            "Hananoi-kun to Koi no Yamai",
            # "리제로",
            # "Osomatsu-san The Movie",
            # "kami otoko",
            # # _______________________________________ mkr_패션 #스타일링
            # "머리"
            # # _______________________________________ mkr_요리
            "백종원",
            # # _______________________________________ mkr_셀럽
            "오바마",
            # # _______________________________________ mkr_음악
            # "세로라이브",
            # # _______________________________________ mkr_게임
            # "오락실_고전",
            # # _______________________________________ mkr_정리
            # "세탁",
            # "청소",
            "데스크 테리어",
            "데스크 테리어",
            # # _______________________________________ mkr_영어
            # "쉐도우스피킹",
        ]
        for item in special_keywords:
            BusinessLogicUtil.classify_pnx_by_special_keyword(pnx=pnx, special_keyword=item, with_walking=with_walking)

    @staticmethod
    def get_sub_pnxs_with_walking(src, texts_to_exclude=[]):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        dir_pnxs = []
        file_pnxs = []
        # 모든 하위 검색
        for root, dirs, files in os.walk(src):
            for dir in dirs:
                item_pnx = os.path.join(root, dir)
                if os.path.isdir(item_pnx):
                    for text_to_exclude in texts_to_exclude:
                        if text_to_exclude in item_pnx:
                            break  # 폴더 경로에 제외할 문자열이 있으면 추가하지 않음
                    else:
                        dir_pnxs.append([item_pnx, os.path.getmtime(item_pnx)])

            for file in files:
                item_pnx = os.path.join(root, file)
                for text_to_exclude in texts_to_exclude:
                    if text_to_exclude in item_pnx:
                        break  # 파일 경로에 제외할 문자열이 있으면 추가하지 않음
                else:
                    file_pnxs.append([item_pnx, os.path.getmtime(item_pnx)])

        return dir_pnxs, file_pnxs

    @staticmethod
    def get_sub_pnxs_without_walking(pnx, texts_to_exclude=[]):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        dir_pnxs = []
        file_pnxs = []

        # 현재 디렉토리만 순회
        for item in os.listdir(pnx):
            item_pnx = os.path.join(pnx, item)
            # 폴더인 경우
            if os.path.isdir(item_pnx):
                for text_to_exclude in texts_to_exclude:
                    if text_to_exclude in item_pnx:
                        break  # 폴더 경로에 제외할 문자열이 있으면 추가하지 않음
                else:
                    dir_pnxs.append([item_pnx, os.path.getmtime(item_pnx)])

            # 파일인 경우
            if os.path.isfile(item_pnx):
                for text_to_exclude in texts_to_exclude:
                    if text_to_exclude in item_pnx:
                        break  # 파일 경로에 제외할 문자열이 있으면 추가하지 않음
                else:
                    # 파일 경로에 제외할 문자열이 없다면 file_pnxs에 추가
                    # BusinessLogicUtil.print_as_log(string=rf'''item_pnx       ="{item_pnx}" %%%FOO%%%''')
                    # BusinessLogicUtil.print_as_log(string=rf'''text_to_exclude="{text_to_exclude}" %%%FOO%%%''')
                    file_pnxs.append([item_pnx, os.path.getmtime(item_pnx)])

        # BusinessLogicUtil.print_list_as_vertical(texts=dir_pnxs, list_name='dir_pnxs')
        # BusinessLogicUtil.print_list_as_vertical(texts=file_pnxs, list_name='file_pnxs')

        return dir_pnxs, file_pnxs

    @staticmethod
    def rename_pnxs(pnxs, debug_mode=False):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        for pnx in pnxs:
            try:
                if debug_mode == True:
                    BusinessLogicUtil.print_as_log(string=rf'''pnx[0]="{pnx[0]}" %%%FOO%%%''')
                    BusinessLogicUtil.print_as_log(string=rf'''pnx[1]="{pnx[1]}" %%%FOO%%%''')
                BusinessLogicUtil.pnx_rename(src=pnx[0], pnx_new=pnx[1])
            except:
                BusinessLogicUtil.print_as_log(f"{traceback.format_exc()}")

    @staticmethod
    def rename_pnxs_from_keywords_to_keyword_new(src, mode, with_walking, debug_mode=False):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        texts_to_exclude = [
            StateManagementUtil.DB_YAML,
            StateManagementUtil.SUCCESS_LOG,
            StateManagementUtil.LOCAL_PKG_CACHE_FILE,
        ]

        dir_pnxs = None
        file_pnxs = None
        if with_walking == True:
            dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_with_walking(src=src, texts_to_exclude=texts_to_exclude)
        else:
            dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_without_walking(pnx=src, texts_to_exclude=texts_to_exclude)

        if mode == "f":
            pnxs = file_pnxs
        elif mode == "d":
            pnxs = dir_pnxs
        else:
            BusinessLogicUtil.print_as_log(string=rf'''"return" %%%FOO%%%''')
            return

        # 특정문자열 변경
        # pnxs에 "System Volume Information" 있으면 제외
        keywords_remove_pnxs_unnecessary = [
            "System Volume Information",
            "$RECYCLE.BIN",
        ]
        keywords = [
            # '_.. ', # 이렇게 . 으로 끝나는 것 안된다.
            # '"', # 이렇게 한글자 는 매우 유의해야한다.

            # from x to ''
            ('[jhp##]', ''),
            ('[시작문자]', ''),
            ('[끝문자]', ''),
            ('[중복문자]', ''),

            # from x to '_'
            ('RARBG', '_'),
            ('H264-3Li', '_'),
            ('_.UHD_.x264', '_'),
            ('_.x264-ORBS[rarbg]', '_'),
            ('_.NF_DDP5.1.x264-AO', '_'),
            ('.x264.DTS-WAF', '_'),
            ('.PORTUGUESE_VXT', '_'),
            ('_.x264-CM', '_'),
            ('_x265-', '_'),
            ('.ORIGINAL.UNRATED.CUT', '_'),
            ('_x265-', '_'),
            ('_-LCHD', '_'),
            ('[5.1]', '_'),
            (' dvdscr whd ', '_'),
            ('dvdrip', '_'),
            ('_H264.AAC', '_'),
            ('.iNTERNAL_-XME', '_'),
            ('10bit.HDR.DV_.8CH.x265.HEVC-PSA', '_'),
            ('.KOR.', '[한국]'),
            ('.KOR.FHDRip.H264.AAC-RTM', '_'),
            ('.10bit_6CH.x265.HEVC-PSA', '_'),
            ('_.NF_DDP5.1.x264-NTG', '_'),
            ('_.DTS-SWTYBLZ', '_'),
            ('_.H264.AAC-VXT', '_'),
            ('(_10bit Tigole)', '_'),
            ('WEB-DL.XviD.AC3-FGT', '_'),
            ('_.H264.AAC-VXT', '_'),
            ('.Remux.DTS-HD.5.1', '_'),
            ('.10bit_6CH.x265.HEVC-PSA', '_'),
            ('.AAC.5.1', '_'),
            ('AAC.5.1-POOP', '_'),
            ('_DD5.1', '_'),
            ('_.AAC-Hon3y', '_'),
            ('.NF_DD5.1.x264-SiGMA', '_'),
            ('_HEVC_EAC3 5.1 Silence', '_'),
            ('.1080p_H265.AAC-RGB', '_'),
            ('_H265.AAC-RGB', '_'),
            ('.DUBBED.', '_'),
            ('.1080p_x265-VXT', '_'),
            ('ENSUBBED', '_'),
            ('1080p_.x264', '_'),
            ('1080p _ x264', '_'),
            (' _ _ ', '_'),
            ('[YTS.AM]', '_'),
            ('.2018.1080p', '[2018]'),
            ('.2018.', '[2018]'),
            ('.x265-VXT', '_'),
            ('.x265-', '_'),
            ('_.bit_.ch.x_psa_', '_'),
            ('BluRay', '_'),
            ('_x264-', '_'),
            ('x264-SPARKS', '_'),
            ('BluRay_HEVC_HDR AAC 7.1 Tigole', '_'),
            ('pkg_movie_horor', '[호러영화]'),
            ('pkg_movie_image', '[영화이미지]'),
            ('pkg_movie_korean', '[한국영화]'),
            ('pkg_movie_marvel_and_dc', '[marvel dc]'),
            ('pkg_movie_space', '[우주영화]'),
            ('pkg_sound', '[영화사운드]'),
            ('x264-HANDJOB', '_'),
            (' x265 ', '_'),
            (' HEVC ', '_'),
            (' 10bit ', '_'),
            (' EAC3 5.1 ', '_'),
            ('WEBRip.x264-RARBG', '_'),
            ('WEB-DL.DD5.1.H264-FGT', '_'),
            ('KORSUB', '_'), ('DTS-FGT', '_'),
            ('BluRay.x265-RARBG', '_'),
            ('#_movie_ #', '_'),
            ('[FOXM.TO]', '_'), ('[WEBRip]', '_'), ('[YTS.MX]', '_'), ('[720p]', '_'), ('[1080p]', '_'),
            ('[BluRay]', '_'), ('DTS-JYK', '_'), ('RARBG', '_'), ('BRRip', '_'),
            ('.SPANISH.', '_'), ('.WEBRip.', '_'), ('-RARBG', '_'), ('[BLURAY]', '_'),
            ('.BluRay.x265-RARBG', '_'), ('BluRay.H264.AAC-RARBG', '_'), ('KORSUB.WEBRip.H264.AAC', '_'),
            ('.KOR.HDTC.H264.AAC_', '_'),
            ('y2meta.com', '_'),
            ('[YTS.AG]', '_'),
            ('[4K] _ [5.1]', '_'),
            ('.WEB.AMZ_.AVC.DD5.1.x264-PANAM', '_'),

            # from x to y
            ('[중복문자][중복문자][중복문자]', '[중복문자]'),
            ('[중복문자][중복문자]', '[중복문자]'),
            (' 720p ', '[720p]'),
            ('The.', 'The '),  # The.mp3 라면 The mp3 가 되어 버려 문제가 될 우려가 됨
            ('movie_ ', '영화'),
            ('.kra mvi ', '[한국영화]'),
            ('.kra mvi,', '[한국영화]'),
            ('포드 v 페라리', 'ford v ferrari'),
            ('1080p', '[1080p]'),
            ('PMC 더 벙커 Take Point', '더 벙커[한국영화]'),
            ('.CHINESE.', '[중국]'),
            ('.JAPANESE.', '[일본]'),
            ('공포_movie', '[공포영화]'),
            ('_movie_', '_영화_'),
            ('[한국_movie_]', '[한국영화]'),
            ('[공포_movie_]', '[공포영화]'),
            ('kra mvi, ', '[한국영화]'),
            ('#일본_movie_', '[일본영화]'),
            # ('www.btranking.top - 최초배포', 'www.btranking.top - 최초배포.url'), # . 이 파일명에 2개 있는 경우에 이동되지 않는데, 이동되도록 처리시도
            # ('www.btranking.top - 최초배포.url.url', 'www.btranking.top - 최초배포.url'),# . 이 파일명에 2개 있는 경우에 이동되지 않는데, 이동되도록 처리시도
            # ('[TGx]Downloaded from torrentgalaxy.to .txt', '[TGx]Downloaded from torrentgalaxy_to .txt'),# . 이 파일명에 2개 있는 경우에 이동되지 않는데, 이동되도록 처리시도
            ('베놈 라스트 댄스', 'Venom The Last Dance'),
            ('Jeongnyeon The Star is Born', '정년이'),
            ('정년이.정년이', '정년이'),
            ('Mungyeong.More.than.Roads', '문경'),
            ('#2023 #', '[PARK]'),
            ('#2025 #', '[PARK]'),
            ('#2024 #', '[PARK]'),
            ('#2024 ', '[PARK]'),
            ('#영화  ', '[PARK]'),
            ('#예능 ', '[PARK]'),
            ('#[PARK]', '[PARK]'),
            ('바운디', ' Vaundy'),
            ('mkr_', '[PARK]'),
            ('#노래 #', '[PARK]'),
            ('_tvN_', '_'),
            ('[Utaite_ sound ]', '[utaite]'),
            ('[Piano_Music]', '[piano]'),
            ('순수음성', '[순수음성]'),
            ('``', '[PARK]'),
            ('[PARK]음악[PARK]', '[PARK]'),
            ('[PARK]', ' [PARK] '),
            ('[PARK]', ' '),
            ('. ', '_'),
            ('.___', '_'), ('._', '_'),
            ('     ', ' '), ('    ', ' '), ('   ', ' '), ('  ', ' '),
            ('______', '_'), ('_____', '_'), ('____', '_'), ('___', '_'), ('__', '_'),
            ('2024.720p.WEBRip.H264.AAC', '[PARK]'),
            ('`marvel `hero`', '[movie_marvel]'),
            ('로키 시즌2', 'Loki 2'),
            ('왓 이프', 'what if'),
            # ('영화', '_movie_'),
            # ('다큐멘터리', ' documentary '),
            # ('드라마', ' drama '),
            # ('게임', ' game '),
            # ('요리', ' cooking '),
            ('사진', '이미지'),
            ('이미지', '이미지'),
            ('그림', '이미지'),
            ('스샷', '이미지'),
            ('[우주_영화_]', '[우주영화]'),
            ('[일본_영화_]', '[일본영화]'),
            ('#일본 _movie', '[일본영화]'),
            ('[한국_영화_]', '[한국영화]'),
            ('Harry_Potter', 'Harry Potter'),
            ('music', ' sound '),
            ('sing', ' sound '),
            ('song', ' sound '),
            ('애니', ' animation '),
            ('``눈물', ' [눈물] '),
            ('언리얼 엔진', ' unreal engine '),
            ('언리얼엔진', ' unreal engine '),
            ('언리얼5', ' unreal engine 5'),
            ('언리얼 5', ' unreal engine 5'),
            ('緑黄色社会', '녹황색시사회'),
            ('[SubsPlease] ', '_'),
            ('_kra_', '[korea]'),
            ('_jpn_', '[japan]'),
            ('``음악``', ' sound '),
            ('[고음질]', '_'),
            ('【 ', '['),
            ('】 ', ']'),
            ('【 ', '['),
            ('】 ', ']'),
            ('( ', '['),
            ('『 ', '['),
            ('」 ', ']'),
            ('《 ', '['),
            ('》 ', ']'),
            # 일본어 & 로마자소리 맵핑
            # 순서가 요음 먼저 맵핑해야함
            # 히라가나 요음
            ("きゃ", "kya"), ("きゅ", "kyu"), ("きょ", "kyo"), ("しゃ", "sha"), ("しゅ", "shu"), ("しょ", "sho"), ("ちゃ", "cha"), ("ちゅ", "chu"), ("ちょ", "cho"), ("にゃ", "nya"), ("にゅ", "nyu"), ("にょ", "nyo"), ("ひゃ", "hya"), ("ひゅ", "hyu"), ("ひょ", "hyo"), ("みゃ", "mya"), ("みゅ", "myu"),
            ("みょ", "myo"), ("りゃ", "rya"), ("りゅ", "ryu"), ("りょ", "ryo"), ("ぎゃ", "gya"),
            ("ぎゅ", "gyu"), ("ぎょ", "gyo"), ("じゃ", "ja"), ("じゅ", "ju"), ("じょ", "jo"), ("びゃ", "bya"), ("びゅ", "byu"), ("びょ", "byo"), ("ぴゃ", "pya"), ("ぴゅ", "pyu"), ("ぴょ", "pyo"),
            # 히라가나 모음 # k행  s행  t행  n행  h행  m행  y행  r행  w행
            ("あ", "a"), ("い", "i"), ("う", "u"), ("え", "e"), ("お", "o"), ("か", "ka"), ("き", "ki"), ("く", "ku"), ("け", "ke"), ("こ", "ko"), ("さ", "sa"), ("し", "shi"), ("す", "su"), ("せ", "se"), ("そ", "so"), ("た", "ta"), ("ち", "chi"), ("つ", "tsu"), ("て", "te"), ("と", "to"),
            ("な", "na"), ("に", "ni"), ("ぬ", "nu"), ("ね", "ne"), ("の", "no"), ("は", "ha"), ("ひ", "hi"),
            ("ふ", "fu"), ("へ", "he"), ("ほ", "ho"), ("ま", "ma"), ("み", "mi"), ("む", "mu"), ("め", "me"), ("も", "mo"), ("や", "ya"), ("ゆ", "yu"), ("よ", "yo"), ("ら", "ra"), ("り", "ri"), ("る", "ru"), ("れ", "re"), ("ろ", "ro"), ("わ", "wa"), ("を", "wo"),
            ("ん", "n"),  # 히라가나 특수
            # 가타가나 요음
            ("キャ", "kya"), ("キュ", "kyu"), ("キョ", "kyo"), ("シャ", "sha"), ("シュ", "shu"), ("ショ", "sho"), ("チャ", "cha"), ("チュ", "chu"), ("チョ", "cho"), ("ニャ", "nya"), ("ニュ", "nyu"), ("ニョ", "nyo"), ("ヒャ", "hya"), ("ヒュ", "hyu"), ("ヒョ", "hyo"), ("ミャ", "mya"), ("ミュ", "myu"),
            ("ミョ", "myo"), ("リャ", "rya"), ("リュ", "ryu"), ("リョ", "ryo"), ("ギャ", "gya"),
            ("ギュ", "gyu"), ("ギョ", "gyo"), ("ジャ", "ja"), ("ジュ", "ju"), ("ジョ", "jo"), ("ビャ", "bya"), ("ビュ", "byu"), ("ビョ", "byo"), ("ピャ", "pya"), ("ピュ", "pyu"), ("ピョ", "pyo"), ('ア', 'a'), ('イ', 'i'), ('ウ', 'u'), ('エ', 'e'), ('オ', 'o'), ('カ', 'ka'), ('キ', 'ki'),
            ('ク', 'ku'), ('ケ', 'ke'), ('コ', 'ko'), ('サ', 'sa'), ('シ', 'shi'), ('ス', 'su'), ('セ', 'se'),
            ('ソ', 'so'), ('タ', 'ta'), ('チ', 'chi'), ('ツ', 'tsu'), ('テ', 'te'), ('ト', 'to'), ('ナ', 'na'), ('ニ', 'ni'), ('ヌ', 'nu'), ('ネ', 'ne'), ('ノ', 'no'), ('ハ', 'ha'), ('ヒ', 'hi'), ('フ', 'fu'), ('ヘ', 'he'), ('ホ', 'ho'), ('マ', 'ma'), ('ミ', 'mi'), ('ム', 'mu'), ('メ', 'me'),
            ('モ', 'mo'), ('ヤ', 'ya'), ('ユ', 'yu'), ('ヨ', 'yo'), ('ラ', 'ra'), ('リ', 'ri'), ('ル', 'ru'),
            ('レ', 're'), ('ロ', 'ro'), ('ワ', 'wa'), ('ヲ', 'wo'), ('ン', 'n'),
            ("ン", "n"),  # 가타가나 특수
            # 간자체
            ("𝐘", "Y"), ("𝐱", "x"), ("𝐖", "W"), ("𝐑", "R"), ("𝐫", "r"), ("P", "P"), ("𝐨", "o"), ("𝐧", "n"), ("𝐦", "m"), ("𝐥", "l"), ("𝐤", "k"), ("𝐠", "g"), ("𝐟", "f"), ("𝐞", "e"), ("𝐃", "D"), ("𝐁", "B"), ("𝐀", "A"), ('𝐲', 'y'), ('𝐕', 'V'), ('𝐮', 'u'), ('𝐭', 't'), ('ｔ', 't'), ('𝐒', 'S'), ('𝐬', 's'),
            ('𝐏', 'P'), ('𝐨', 'o'), ('ｏ', 'o'), ('𝐧', 'n'), ('ｌ', 'l'), ('ｋ', 'k'), ('𝐢', 'i'), ('i', 'i'),
            ('ｅ', 'e'), ('𝐝', 'd'), ('𝐜', 'c'), ('ｃ', 'c'), ('𝐚', 'a'),
            # 특수문자
            ('🌕', '_'), ('🔥', '_'), ('🗡️', '_'), ('💜', '_'), ('🎤', '_'), ('☆️', '_'), ('★', '_'), ('🛸', '_'), ('🚬', '_'), ('🚪', '_'), ('🚨', '_'), ('🚘', '_'), ('🙆', '_'), ('😭', '_'), ('😥', '_'), ('😢', '_'), ('😈', '_'), ('😆', '_'), ('😅', '_'), ('🧖', '_'), ('🧐', '_'), ('🦝', '_'), ('🥺', '_'),
            ('🥩', '_'), ('🥜', '_'), ('🤸', '_'), ('🤴', '_'), ('🤫', '_'), ('🤡', '_'), ('🤘', '_'), ('🤗', '_'), ('🤔', '_'),
            ('🤓', '_'), ('🖐', '_'), ('🔹', '_'), ('🔮', '_'), ('🔍', '_'), ('📚', '_'), ('📁', '_'), ('💻', '_'), ('💸', '_'), ('💪', '_'), ('💥', '_'), ('💡', '_'), ('💛', '_'), ('💚', '_'), ('💙', '_'), ('💖', '_'), ('💔', '_'), ('💎', '_'), ('💍', '_'), ('💁', '_'), ('👹', '_'), ('👭', '_'), ('👗', '_'), ('👖', '_'),
            ('👍', '_'), ('👌', '_'), ('👋', '_'), ('👊', '_'), ('👄', '_'), ('🐶', '_'), ('🐠', '_'), ('🐟', '_'),
            ('🏻', '_'), ('🏡', '_'), ('🎩', '_'), ('🎧', '_'), ('🎉', '_'), ('🍰', '_'), ('🍭', '_'), ('🍜', '_'), ('🍒', '_'), ('🍃', '_'), ('🍂', '_'), ('🌺', '_'), ('🌹', '_'), ('🌸', '_'), ('🌷', '_'), ('🌡', '_'), ('🌟', '_'), ('🌞', '_'), ('🌙', '_'), ('🌎', '_'), ('🌈', '_'), ('⭐', '_'), ('⧸', '_'), ('➡', '_'),
            ('❤', '_'), ('❗', '_'), ('❕', '_'), ('❓', '_'), ('❌', '_'), ('✿', '_'), ('✨', '_'), ('✧', '_'),
            ('✦', '_'), ('✔', '_'), ('✅', '_'), ('🇹', '_'), ('🇷', '_'), ('🇰', '_'), ('🇮', '_'), ('⚡', '_'), ('♬', '_'), ('♪', '_'), ('♩', '_'), ('♨', '_'), ('📝', '_'), ('🌱', '_'),
            ('｜', '_'),
            # 일본어 간자체 일부 맵핑 # 공부용 #아는 것만 추가 #같은문자 다른소리 처리 어떻게하지?
            ("日", "日(nichi)"), ("人", "人(jin)"), ("本", "本(hon)"), ("大", "大(dai)"), ("中", "中(chuu)"), ("小", "小(shou)"), ("山", "山(yama)"), ("川", "川(kawa)"), ("田", "田(ta)"), ("水", "水(sui)"), ("火", "火(ka)"), ("木", "木(moku)"), ("金", "金(kin)"), ("土", "土(do)"), ("空", "空(kuu)"),
            ("天", "天(ten)"), ("海", "海(umi)"), ("心", "心(shin)"), ("愛", "愛(ai)"), ("学", "学(gaku)"),
            ("生", "生(sei)"), ("車", "車(sha)"), ("電", "電(den)"), ("語", "語(go)"), ("書", "書(sho)"), ("読", "読(doku)"), ("見", "見(ken)"), ("聞", "聞(bun)"), ("花", "花(hana)"), ("風", "風(kaze)"),

            (']_[', ']['),
            ('_.. ', '_'),
            ('.._ ', '_'),
            ('._ ', '_'),
            ('[$TIMESTAMP]', '_'),
            (' e end hdtv once ', '_E_'),
            ('.E.p_NEXT_', '_E_'),
            (' e end hdtv once ', '_E_'),
            ('hhd800.com@', '_'),
            ('티비플', '[티비플]'),
            ('re제로', ' re zero '),
            ('리제로', ' re zero '),
            ('미스터 션샤인', ' 미스터션샤인'),
            ('야나기나기', ' Nagi Yanagi'),
            ('피아노_음악', '[piano]'),
            ('「', '['),
            ('】', ']'),
            ('」', ']'),
            ('【', '['),
            ('／', ' '),
            ('│', ' '),
            ('이어폰 필수', '이어폰필수'),
            ('우타이테', 'utaite'),
            ('이어폰필수', '_'),
            ('편곡ver ', '_'),
            ('볼빨간 사춘기', '볼빨간사춘기'),
            ('cover.鹿乃', '_'),
            ('#s #', '_'),
            ('[Leopard-Raws]', '_'),
            ('메이플', '메이플스토리'),
            ('스토리스토리', '스토리'),
            ('짐___캐리', '짐 캐리'),
            ('짐_캐리', '짐 캐리'),
            ('[jhp##]', '_'),
            ('케이tv', '_'),
            ('한글자막', '_'),
            ('1080P', '1080p'),
            ('1080p.H264-F1RST', '_'),
            ('[Moozzi2]', '_'),
            # ('[[', '['),
            # (']]', ']'),
            # ('_)_)', '))'),
            ('►', '_'),
            ('♫', '_'),
            # '후회안합니다', '환영합니다', '합니다', '시작합니다', '소개합니다', '복잡합니다', '만들어야합니다', '공개합니다', '감사합니다',
            # '[퓨전_음악]', '[ENG]', '[TM_sound]', '[치유정화]', '[울적해져요]', '[nightcore]', '[MV]', '[쇼! 음악중심]', '[쇼!_음악중심]', '[이어폰_소름]', '[이어폰_필수]', '[이어폰챙겻죠]', '[한국어 자막]', '[너무좋다]', '[소름 돋아요]', '[자작곡]', '[수정본]', '[TV]', '[CD]',
            # 'Yang HeeEun', '판타스틱 듀오', '집중력 향상을 위한', '임금님랭킹2기오프닝', 'Fantastic Duo', '모던민요',
            # "(ENG_SUB)"
            # # 'playlist',
            # # 'LIVE',
            # '핫클립',
            # '_., ', '_._ ',
            # ' _ ', ' - ', '[_]', '___',
            # '__', '  ',
            # # "'",
            # '|', '「️', '」️', '【', '】',
            # # '+', '&',
        ]
        for keyword_removed in keywords_remove_pnxs_unnecessary:
            pnxs = [item for item in pnxs if keyword_removed not in item[0]]  # remove_element_to_have_"keywords_remove_dirs_unnecessary"
        # BusinessLogicUtil.print_list_as_vertical(items_list=dir_pnxs, items_name="dir_pnxs")
        # BusinessLogicUtil.print_list_as_vertical(items_list=file_pnxs, items_name="file_pnxs")
        pnxs_and_pnxs_new = []
        for item in pnxs:
            item_pnx = item[0]
            item_pnx_new = item_pnx  # item_pnx_로 초기화
            for keyword, keyword_new in keywords:
                item_p = BusinessLogicUtil.get_p(pnx=item_pnx_new)
                item_nx = BusinessLogicUtil.get_nx(pnx=item_pnx_new)
                item_nx_new = item_nx.replace(keyword, keyword_new)  # 누적하여 교체
                item_pnx_new = rf"{item_p}\{item_nx_new}"
            # BusinessLogicUtil.print_as_log(string = rf'''item_pnx="{item_pnx}" %%%FOO%%%''')
            # BusinessLogicUtil.print_as_log(string = rf'''item_pnx_new="{item_pnx_new}" %%%FOO%%%''')
            if item_pnx != item_pnx_new:  # item_pnx_와 item_pnx_new가 다르면 추가
                pnxs_and_pnxs_new.append([item_pnx, item_pnx_new])

        # 확인
        BusinessLogicUtil.print_list_as_vertical(items_list=pnxs_and_pnxs_new, items_list_name="바꿀 대상")
        BusinessLogicUtil.print_as_log(string=rf'''len(pnxs_and_pnxs_new)="{len(pnxs_and_pnxs_new)}" %%%FOO%%%''')

        # 적용
        BusinessLogicUtil.rename_pnxs(pnxs=pnxs_and_pnxs_new, debug_mode=debug_mode)

    @staticmethod
    def rename_pnxs_from_pattern_once_to_pattern_new(src, pattern, mode, pattern_new, with_walking):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.print_as_log(string=rf'''pattern="{pattern}" %%%FOO%%%''')
        BusinessLogicUtil.print_as_log(string=rf'''pattern_new="{pattern_new}" %%%FOO%%%''')

        texts_to_exclude = [
            StateManagementUtil.DB_YAML,
            StateManagementUtil.SUCCESS_LOG,
            StateManagementUtil.LOCAL_PKG_CACHE_FILE,
        ]

        if with_walking == True:
            dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_with_walking(src=src, texts_to_exclude=texts_to_exclude)
        else:
            dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_without_walking(pnx=src, texts_to_exclude=texts_to_exclude)

        if mode == "f":
            pnxs = file_pnxs
        elif mode == "d":
            pnxs = dir_pnxs
        else:
            BusinessLogicUtil.print_as_log(string=rf'''"return" %%%FOO%%%''')
            return
        BusinessLogicUtil.print_as_log(string=rf'''pnxs="{pnxs}" %%%FOO%%%''')
        # BusinessLogicUtil.print_list_as_vertical(items_list=pnxs, items_list_name="pnxs %%%FOO%%%")

        # 한 번들어간 패턴
        pnxs_reg_checked = []
        item_p = None
        item_nx = None
        item_pnx = None
        item_nx_new = None
        for item in pnxs:
            item_p = BusinessLogicUtil.get_p(item[0])
            item_nx = BusinessLogicUtil.get_nx(item[0])
            item_pnx = BusinessLogicUtil.get_pnx(item[0])
            if re.search(pattern, item_nx):
                # if re.match(pattern, item_nx):
                pnxs_reg_checked.append(item)
        BusinessLogicUtil.print_as_log(string=rf'''pnxs_reg_checked="{pnxs_reg_checked}" %%%FOO%%%''')
        # BusinessLogicUtil.print_list_as_vertical(items_list=pnxs_reg_checked, items_list_name="pnxs_reg_checked")

        pnxs_and_pnxs_new = []
        for item in pnxs_reg_checked:
            item_p = BusinessLogicUtil.get_p(item[0])
            item_nx = BusinessLogicUtil.get_nx(item[0])
            item_nx_new = re.sub(pattern, pattern_new, item_nx)

            # logging
            BusinessLogicUtil.print_as_log(string=rf'''item_nx_new="{item_nx_new}" %%%FOO%%%''')

            item_pnx_new = rf"{item_p}\{item_nx_new}"
            pnxs_and_pnxs_new.append([item[0], item_pnx_new])

        # logging
        BusinessLogicUtil.print_as_log(string=rf'''item_p="{item_p}" %%%FOO%%%''')
        BusinessLogicUtil.print_as_log(string=rf'''item_nx="{item_nx}" %%%FOO%%%''')
        BusinessLogicUtil.print_as_log(string=rf'''item_nx_new="{item_nx_new}" %%%FOO%%%''')

        # 확인
        # BusinessLogicUtil.print_list_as_vertical(items_list=pnxs_and_pnxs_new, items_list_name="바꿀 대상")
        # BusinessLogicUtil.print_as_log(string=rf'''len(pnxs_and_pnxs_new)="{len(pnxs_and_pnxs_new)}" %%%FOO%%%''')

        # 적용
        BusinessLogicUtil.rename_pnxs(pnxs=pnxs_and_pnxs_new)

    @staticmethod
    def rename_pnxs_from_pattern_twice_to_pattern_new(pnx, pattern, mode, with_walking, pattern_new="_"):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        BusinessLogicUtil.print_as_log(string=rf'''pattern="{pattern}" %%%FOO%%%''')
        BusinessLogicUtil.print_as_log(string=rf'''pattern_new="{pattern_new}" %%%FOO%%%''')

        texts_to_exclude = [
            StateManagementUtil.DB_YAML,
            StateManagementUtil.SUCCESS_LOG,
            StateManagementUtil.LOCAL_PKG_CACHE_FILE,
        ]

        if with_walking == True:
            dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_with_walking(src=pnx, texts_to_exclude=texts_to_exclude)
        else:
            dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_without_walking(pnx=pnx, texts_to_exclude=texts_to_exclude)

        if mode == "f":
            pnxs = file_pnxs
        elif mode == "d":
            pnxs = dir_pnxs
        else:
            BusinessLogicUtil.print_as_log(string=rf'''"return" %%%FOO%%%''')
            return

        # 두 번들어간 패턴
        pnxs_reg_checked = []
        item_new = None
        for item in pnxs:
            item_p = BusinessLogicUtil.get_p(item[0])
            item_nx = BusinessLogicUtil.get_nx(item[0])
            item_pnx = BusinessLogicUtil.get_pnx(item[0])
            if len(re.findall(pattern, item[0])) >= 2:
                # if re.match(pattern, item_nx):
                pnxs_reg_checked.append(item)
        BusinessLogicUtil.print_list_as_vertical(items_list=pnxs_reg_checked, items_list_name="pnxs_reg_checked")
        # BusinessLogicUtil.pause()

        pnxs_and_pnxs_new = []
        for item in pnxs_reg_checked:
            item_p = BusinessLogicUtil.get_p(item[0])
            item_nx = BusinessLogicUtil.get_nx(item[0])
            item_nx_new = re.sub(pattern, pattern_new, item_nx)
            if BusinessLogicUtil.is_file(item[0]):
                item_pnx_new = rf"{item_p}\{item_nx_new}"
            else:
                item_pnx_new = rf"{item_p}\{item_nx_new}"
            pnxs_and_pnxs_new.append([item[0], item_pnx_new])

        # 확인
        BusinessLogicUtil.print_list_as_vertical(items_list=pnxs_and_pnxs_new, items_list_name="바꿀 대상")
        BusinessLogicUtil.print_as_log(string=rf'''len(pnxs_and_pnxs_new)="{len(pnxs_and_pnxs_new)}" %%%FOO%%%''')

        # 적용
        BusinessLogicUtil.rename_pnxs(pnxs=pnxs_and_pnxs_new)

    @staticmethod
    def print_from_pnxs_to_semantic_words(pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        texts_to_exclude = [
            StateManagementUtil.DB_YAML,
            StateManagementUtil.SUCCESS_LOG,
            StateManagementUtil.LOCAL_PKG_CACHE_FILE,
        ]

        # dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_without_walking(pnx=item_pnx, texts_to_exclude=texts_to_exclude)
        dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_with_walking(src=pnx, texts_to_exclude=texts_to_exclude)

        # pnxs = dir_pnxs
        pnxs = file_pnxs

        # 수십개의 파일 경로에서 2개 이상의 한글로 구성된 의미론적인 단어를 추출
        special_korean_words = []

        def extract_korean_words(pnx):
            pattern = r'[가-힣]{2,}'  # 한글만 추출하는 정규식
            korean_words = re.findall(pattern=pattern, string=pnx)  # 2개 이상 한글 문자로 이루어진 단어를 찾음
            return korean_words

        for item in pnxs:
            item_pnx = item[0]
            korean_words = extract_korean_words(item_pnx)
            special_korean_words = special_korean_words + korean_words
        word_count = Counter(special_korean_words)
        BusinessLogicUtil.print_as_log(string=rf'''word_count="{word_count}" %%%FOO%%%''')

    @staticmethod
    def pnxs_rename_from_________to_______2______via_hard_coded():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        # pnx = rf"D:\#기타\pkg_dirs"
        # pnx = rf"D:\#기타\pkg_files"
        pnx = rf"D:\#기타"
        pnx = rf"D:\#기타\pkg_files\pkg_mp4"

        texts_to_exclude = [
            StateManagementUtil.DB_YAML,
            StateManagementUtil.SUCCESS_LOG,
            StateManagementUtil.LOCAL_PKG_CACHE_FILE,
        ]

        # dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_without_walking(pnx=item_pnx, texts_to_exclude=texts_to_exclude)
        dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_with_walking(src=pnx, texts_to_exclude=texts_to_exclude)

        # pnxs = dir_pnxs
        pnxs = file_pnxs

        # todo pattern 변수 그 유사함수에서 참조해서 가져오기
        #
        # # pattern 대체 timestamp 를 붙이기
        # pnxs_and_pnxs_new = []
        # for item in pnxs:
        #     pattern_new = ''
        #     item_without_reg = re.sub(pattern, pattern_new, item[0]) # 날짜/시간 패턴을 모두 제거
        #     item_pn=BusinessLogicUtil.get_pn(item_without_reg)
        #     item_x=BusinessLogicUtil.get_x(item_without_reg)
        #     timestamp = BusinessLogicUtil.get_time_as_("now")
        #     item_new = ""
        #     if BusinessLogicUtil.is_file(item[0]):
        #         item_new = f"{item_pn}_{timestamp}.{item_x}"
        #     else:
        #         item_new = f"{item_pn}_{timestamp}{item_x}"
        #     pnxs_and_pnxs_new.append([item[0], item_new])
        #
        # # 확인
        # BusinessLogicUtil.print_list_as_vertical(items_list=pnxs_and_pnxs_new, items_name="바꿀 대상")
        # BusinessLogicUtil.print_as_log(string=rf'''len(pnxs_and_pnxs_new)="{len(pnxs_and_pnxs_new)}" %%%FOO%%%''')
        #
        # # 적용
        # BusinessLogicUtil.rename_pnxs(pnxs=pnxs_and_pnxs_new)

    @staticmethod
    def pnxs_move_pattern_via_hard_coded():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        # pnx = rf"D:\#기타\pkg_dirs"
        # pnx = rf"D:\#기타\pkg_files"
        pnx = rf"D:\#기타"
        pnx = rf"D:\#기타\pkg_files\pkg_mp4"

        texts_to_exclude = [
            StateManagementUtil.DB_YAML,
            StateManagementUtil.SUCCESS_LOG,
            StateManagementUtil.LOCAL_PKG_CACHE_FILE,
        ]

        # dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_without_walking(pnx=item_pnx, texts_to_exclude=texts_to_exclude)
        dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_with_walking(src=pnx, texts_to_exclude=texts_to_exclude)

        # pnxs = dir_pnxs
        pnxs = file_pnxs

        # pattern 대체 timestamp 를 붙이기
        # pnxs_and_pnxs_new = []
        # for item in pnxs:
        #     pattern_new = ''
        #     item_without_reg = re.sub(pattern, pattern_new, item[0]) # 날짜/시간 패턴을 모두 제거
        #     item_pn=BusinessLogicUtil.get_pn(item_without_reg)
        #     item_x=BusinessLogicUtil.get_x(item_without_reg)
        #     timestamp = BusinessLogicUtil.get_time_as_("now")
        #     item_new = ""
        #     if BusinessLogicUtil.is_file(item[0]):
        #         item_new = f"{item_pn}_{timestamp}.{item_x}"
        #     else:
        #         item_new = f"{item_pn}_{timestamp}{item_x}"
        #     pnxs_and_pnxs_new.append([item[0], item_new])

        # [문자열] 패턴은 파일명의 맨앞이나 뒤로 이동
        pnxs_and_pnxs_new = []
        for item in pnxs:
            item_pnx = item[0]
            pattern = r'(\[.*?\])'
            # item_pnx_new = BusinessLogicUtil.get_str_moved_pattern_to_front(pattern=pattern, item_pnx=item_pnx)
            item_pnx_new = BusinessLogicUtil.get_str_moved_pattern_to_rear(pattern=pattern, item_pnx=item_pnx)
            if item_pnx != item_pnx_new:  # item_pnx item_pnx_new가 다르면 추가
                pnxs_and_pnxs_new.append([item_pnx, item_pnx_new])

        # 확인
        BusinessLogicUtil.print_list_as_vertical(items_list=pnxs_and_pnxs_new, items_list_name="바꿀 대상")
        BusinessLogicUtil.print_as_log(string=rf'''len(pnxs_and_pnxs_new)="{len(pnxs_and_pnxs_new)}" %%%FOO%%%''')

        # 적용
        BusinessLogicUtil.rename_pnxs(pnxs=pnxs_and_pnxs_new)

    @staticmethod
    def pnxs_merge_via_text_file():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        function_name_txt = rf'{StateManagementUtil.PROJECT_DIRECTORY}\pkg_txt\{function_name}.txt'
        BusinessLogicUtil.make_pnx(pnx=function_name_txt, mode="f")
        # if not BusinessLogicUtil.is_window_open(window_title=function_name_txt):
        #     BusinessLogicUtil.run_pnx_via_explorer_exe(function_name_txt, show_mode=False)
        pnxs = BusinessLogicUtil.get_list_from_f_txt(pnx=function_name_txt)
        BusinessLogicUtil.merge_directories(directory_pnxs=pnxs)

    @staticmethod
    def gather_pnxs_useless(src, debug_mode=False):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        BusinessLogicUtil.print_as_log(string=rf'''debug_mode="{debug_mode}" %%%FOO%%%''')

        dst = rf"D:\pkg_classified\pkg_useless"
        BusinessLogicUtil.make_pnx(pnx=dst, mode="d")

        try:
            BusinessLogicUtil.chdir(dst=src)

            # string_clipboard_bkp = clipboard.paste()

            # useless_files 수집
            # useless_files = []
            useless_files = set()
            is_target_moved_done = False
            useless_file_names_txt = StateManagementUtil.USELESS_FILE_NAMES_TXT
            files_list = BusinessLogicUtil.get_list_from_f_txt(useless_file_names_txt)
            # BusinessLogicUtil.run_pnx_via_explorer_exe(pnx=useless_file_names_txt, show_mode=False)

            for file_name in files_list:
                file_name = file_name.strip()
                file_name = file_name.strip("\n")
                # BusinessLogicUtil.command_to_os(command=f'dir /b /s "{file_name}" | clip.exe')
                file_sub_pnx_list = BusinessLogicUtil.command_to_os(cmd=f'dir /b /s "{file_name}"')
                if debug_mode == True:
                    BusinessLogicUtil.print_as_log(string=rf'''file_sub_pnx_list="{file_sub_pnx_list}" %%%FOO%%%''')
                for file_sub_pnx in file_sub_pnx_list:
                    if BusinessLogicUtil.does_pnx_exist(src=file_sub_pnx, show_mode=False):
                        # file_sub_pnx_set = BusinessLogicUtil.get_set_from_list(items_list=file_sub_pnx)
                        # useless_files = useless_files | file_sub_pnx_set
                        useless_files.add(file_sub_pnx)
                if debug_mode == True:
                    BusinessLogicUtil.print_as_log(string=rf'''useless_files="{useless_files}" %%%FOO%%%''')

            os.chdir(StateManagementUtil.PROJECT_DIRECTORY)

            if len(useless_files) == 0:
                BusinessLogicUtil.print_as_log(string=rf'''len(useless_files)="{len(useless_files)}" %%%FOO%%%''')
                return
            else:
                if debug_mode == True:
                    BusinessLogicUtil.print_as_log(string=rf'''useless_files="{useless_files}" %%%FOO%%%''')
                for useless_file in useless_files:
                    BusinessLogicUtil.move_pnx_without_overwrite(src=useless_file, dst=dst)  # todo fix:외장드라이브에서는 안되는듯
                    # BusinessLogicUtil.move_pnx_to_trash_bin(src=useless_file)

        except:
            BusinessLogicUtil.print_as_log(f"{traceback.format_exc()}")

        BusinessLogicUtil.print_as_log(string=rf'''dst="{dst}" %%%FOO%%%''')

        # try:
        #     useless_files = []
        #     isSpoken = False
        #     lines = BusinessLogicUtil.get_lines_of_file(BusinessLogicUtil.USELESS_FILES)
        #     os.chdir(directory_pnx)
        #     for file_name in lines:
        #         file_name = file_name.strip()
        #         file_name = file_name.strip("\n")
        #         useless_files.append(file_name)
        #     dst = rf"D:\[noe] [8TB] [ext]\$useless_directories"
        #     BusinessLogicUtil.make_leaf_directory(dst)
        #     # os.chmod(file_path, 0o777) # 0o777 소유자만 7의 권한부여, 나머지는 권한 없앰 # 777 누구나
        #     os.chmod(directory_pnx, 0o777)
        #     os.chmod(dst, 0o777)
        #     BusinessLogicUtil.make_leaf_directory(dst)
        #     if os.path.isdir(directory_pnx):
        #         for root, dirs, files in os.walk(directory_pnx, topdown=False):  # os.walk()는 with walking 으로 동작한다
        #             for file in files:
        #                 file_path = os.path.join(root, file)
        #                 for useless_file in useless_files:
        #                     if useless_file in os.path.basename(useless_file):
        #                         print(rf"useless file : {file_path}")
        #                         os.chmod(file_path, 777)
        #                         BusinessLogicUtil.move_without_overwrite(src=file_path, dst=dst)
        #                         if isSpoken == False:
        #                             TtsUtil.speak_ments("pnx를 순회하며 약속된 불필요한 파일을 약속된 폴더로 모았습니다", sleep_after_play=0.65)
        #                             isSpoken = True
        # except:
        #     BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def should_i_make_directory_for_a2z_with_timestamp():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            work_name = None
            pnx = None
            dialog_btn_text_clicked = None
            function = None
            dialog_input_box_text = None

            dialog_btn_text_clicked, function, dialog_input_box_text = BusinessLogicUtil.should_i_do(
                string="업무용 타임스템프 파일을 만들까요?",
                btns=["생성", "그만두기"],
                function=None,
                auto_click_negative_btn_after_seconds=30,
                title=f"{function_name}()",
                return_mode=True,
                input_box_mode=False,
            )
            if dialog_btn_text_clicked != "생성":
                return

            dialog_btn_text_clicked, function, dialog_input_box_text = BusinessLogicUtil.should_i_do(
                string="업무명을 입력해주세요",
                btns=["입력", "그만두기"],
                function=None,
                auto_click_negative_btn_after_seconds=30,
                title=f"{function_name}()",
                return_mode=True,
                input_box_mode=True,
            )
            if dialog_btn_text_clicked != "입력":
                return
            work_name = dialog_input_box_text
            work_name = work_name.strip()
            work_name = work_name.replace("\"", "")
            BusinessLogicUtil.print_as_log(f'''work_names={work_name} %%%FOO%%%''')
            if work_name == "":
                BusinessLogicUtil.print_as_log(f'''work_name가 입력되지 않았습니다 %%%FOO%%%''')
                return

            dialog_btn_text_clicked, function, dialog_input_box_text = BusinessLogicUtil.should_i_do(
                string="어느 경로에 만들까요?",
                btns=["입력", "그만두기"],
                function=None,
                auto_click_negative_btn_after_seconds=30,
                title=f"{function_name}()",
                return_mode=True,
                input_box_mode=True,
            )
            if dialog_btn_text_clicked != "입력":
                return
            pnx = dialog_input_box_text
            pnx = BusinessLogicUtil.get_pnx_preprocessed(pnx)
            if BusinessLogicUtil.is_wired_pnx(pnx):
                return
            BusinessLogicUtil.print_as_log(string=rf'''pnx="{pnx}" %%%FOO%%%''')
            BusinessLogicUtil.print_as_log(string=rf'''work_name="{work_name}" %%%FOO%%%''')
            timestamp = BusinessLogicUtil.get_time_as_("yyyy MM dd (weekday) HH mm")
            pnx_new = rf"{pnx}\{timestamp} {work_name}"
            BusinessLogicUtil.print_as_log(string=rf'''pnx_new="{pnx_new}" %%%FOO%%%''')
            BusinessLogicUtil.make_pnx(pnx=pnx_new, mode="d")
            BusinessLogicUtil.run_via_explorer_exe(pnx=pnx_new, show_mode=False)
            return
        except:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def get_working_directory():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        return os.getcwd()

    @staticmethod
    def is_wired_pnx(pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # wired 이상한 pnx 인지 확인
        # required 가 나은 것 같은데
        BusinessLogicUtil.print_as_log(f'''pnx={pnx} %%%FOO%%%''')
        if pnx == "":
            BusinessLogicUtil.print_as_log(f'''pnx가 입력되지 않았습니다 %%%FOO%%%''')
            return True
        connected_drives = []
        for drive_letter in string.ascii_uppercase:
            drive_path = drive_letter + ":\\"
            if os.path.exists(drive_path):
                connected_drives.append(drive_path)
                if pnx == drive_path:
                    BusinessLogicUtil.print_as_log(f'''입력된 pnx는 너무 광범위하여 진행할 수 없도록 설정되어 있습니다 %%%FOO%%%''')
                    return True
        if not os.path.exists(pnx):
            BusinessLogicUtil.print_as_log(f'''입력된 pnx가 존재하지 않습니다 %%%FOO%%%''')
            return True

    @staticmethod
    def get_pnx_preprocessed(pnx):  # todo deprecated
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        pnx = str(pnx)
        pnx = pnx.strip()
        if platform.system() == 'Windows':
            pnx = pnx.replace("\"", "")
            pnx = pnx.replace("\'", "")
            pnx = pnx.replace("/", "\\")
        if platform.system() == 'Linux':
            pnx = pnx.replace("\\", "//")

        return pnx

    @staticmethod
    def print_as_log(string, print_color=""):
        # function_name = inspect.currentframe().f_code.co_name
        # BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        if print_color == "grey":
            BusinessLogicUtil.print_light_black(f'''[{BusinessLogicUtil.get_time_as_('now')}] {string}''')
        elif print_color == "red":
            BusinessLogicUtil.print_red(f'''[{BusinessLogicUtil.get_time_as_('now')}] {string}''')
        elif print_color == "yellow":
            BusinessLogicUtil.print_light_yellow(f'''[{BusinessLogicUtil.get_time_as_('now')}] {string}''')
        elif print_color == "blue":
            BusinessLogicUtil.print_light_blue(f'''[{BusinessLogicUtil.get_time_as_('now')}] {string}''')
        elif print_color == "green":
            BusinessLogicUtil.print_green(f'''[{BusinessLogicUtil.get_time_as_('now')}] {string}''')
        elif print_color == "white":
            BusinessLogicUtil.print_light_white(f'''[{BusinessLogicUtil.get_time_as_('now')}] {string}''')
        else:
            BusinessLogicUtil.print_light_black(f'''[{BusinessLogicUtil.get_time_as_('now')}] {string}''')

    # @staticmethod
    # def pnxs_classify_by_pkg_files_and_pkg_dirs_via_hard_coded():
    #     function_name = inspect.currentframe().f_code.co_name
    #     BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
    #
    #     pnx = rf"{StateManagementUtil.USERPROFILE}\Downloads\pkg_classifying"
    #
    #     # target_pnx가 유효한 디렉토리인지 확인
    #     if BusinessLogicUtil.is_file(pnx=pnx):
    #         BusinessLogicUtil.print_light_black(f"{pnx} 는 정리할 수 있는 디렉토리가 아닙니다")
    #         return
    #
    #     texts_to_exclude = [
    #         rf'D:\pkg_classifying\Thumbs',
    #         rf'D:\pkg_classifying\desktop',
    #     ]
    #     BusinessLogicUtil.print_list_as_vertical(items_list=texts_to_exclude, items_list_name='texts_to_exclude')
    #
    #     dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_without_walking(pnx=pnx, texts_to_exclude=texts_to_exclude)
    #     # dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_with_walking(pnx=working_directory, texts_to_exclude= texts_to_exclude)
    #
    #     # 파일 정리
    #     pkg_files = rf'{pnx}\pkg_files'
    #     BusinessLogicUtil.make_pnx(pnx=pkg_files, mode="d")
    #     for file_pnx in file_pnxs:
    #         # pkg_ 디렉토리로 이동
    #         if "pkg_" not in str(file_pnx):
    #             # BusinessLogicUtil.print_as_log(string = rf'''file_pnx[0]="{file_pnx[0]}" %%%FOO%%%''')
    #             BusinessLogicUtil.move_pnx_without_overwrite(src=file_pnx[0], dst=pkg_files)
    #             pass
    #
    #     # 디렉토리 정리
    #     pkg_dirs = rf'{pnx}\pkg_dirs'
    #     BusinessLogicUtil.make_pnx(pnx=pkg_dirs, mode="d")
    #     for dir_pnx in dir_pnxs:
    #         # pkg_ 디렉토리로 이동
    #         if "pkg_" not in str(dir_pnx):
    #             # BusinessLogicUtil.print_as_log(string = rf'''dir_pnx[0]="{dir_pnx[0]}" %%%FOO%%%''')
    #             BusinessLogicUtil.move_pnx_without_overwrite(src=dir_pnx[0], dst=pkg_dirs)
    #             pass

    @staticmethod
    def get_list_removed_element_empty(items_list, show_mode=True):
        function_name = inspect.currentframe().f_code.co_name
        if show_mode == False:
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        return [item for item in items_list if item and item.strip()]

    @staticmethod
    def get_list_removed_element_contain_string(items, string):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        return [item for item in items if string not in item]

    @staticmethod
    def get_list_replaced_element_from_str_to_str(item_list, from_str, to_str, show_mode=True):
        function_name = inspect.currentframe().f_code.co_name
        if show_mode == False:
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        return [text.replace(from_str, to_str) for text in item_list]

    @staticmethod
    def get_list_striped_element(items_list, show_mode=True):
        function_name = inspect.currentframe().f_code.co_name
        if show_mode == False:
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        return [item.strip() for item in items_list]

    @staticmethod
    def download_youtube(url, function_name_txt):  # youtube_playlist_url 이건 따로 처리하도록. 하자
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            video_id = None
            audio_id = None
            youtube_video_id = BusinessLogicUtil.parse_youtube_video_id(url=url)
            url = f'https://www.youtube.com/watch?v={youtube_video_id}'
            dst = rf'{StateManagementUtil.CLASSIFYING}'
            BusinessLogicUtil.make_pnx(pnx=dst, mode='d')
            BusinessLogicUtil.chdir(dst=dst)
            lines = os.listdir()
            for line in lines:
                file = line
                if BusinessLogicUtil.is_pattern_in_string(file, youtube_video_id, show_mode = False):
                    BusinessLogicUtil.print_as_log(f'''"{youtube_video_id} 는 이미 있습니다. 다운로드하지 않습니다."''', print_color = 'green')
                    BusinessLogicUtil.command_to_os(cmd=f'echo \n{url}_[SUCCESS] {file} >> "{function_name_txt}"')
                    items_list = BusinessLogicUtil.get_list_from_f_txt(pnx=function_name_txt)
                    items_list = BusinessLogicUtil.get_list_removed_element_duplicated(items_list=items_list)
                    items_list = BusinessLogicUtil.get_list_removed_element_empty(items_list=items_list)
                    BusinessLogicUtil.write_list_to_f_txt(texts=items_list, pnx=function_name_txt, mode='w')
                    return
            try:
                BusinessLogicUtil.print_light_black(f"%%%FOO%%% 다운로드옵션 파싱")
                cmd = rf'{StateManagementUtil.YT_DLP_CMD} -F {url}'
                lines = BusinessLogicUtil.command_to_os_like_person_as_admin(command=cmd)
                video_ids_allowed = StateManagementUtil.VIDEO_IDS_ALLOWED
                audio_ids_allowed = StateManagementUtil.AUDIO_IDS_ALLOWED
                audio_ids = []
                video_ids = []
                # BusinessLogicUtil.print_list_as_vertical(items_list=lines, items_name="다운로드옵션")
                video_id = max(
                    [id for line in lines if 'video only' in line for id in video_ids_allowed if line.split(" ")[0].strip() == id.strip()],
                    key=int, default=None
                )
                audio_id = min(
                    [id for line in lines if 'audio only' in line for id in audio_ids_allowed if line.split(" ")[0].strip() == id.strip()],
                    key=int, default=None
                )
                if video_id == "" or audio_id == "" == 1:
                    BusinessLogicUtil.print_as_log(f'''"불완전한 비디오 아이디 또는 오디오 아이디로 다운로드를 진행할 수 없습니다"''')
                    return
                # BusinessLogicUtil.print_as_log(string=rf'''video_ids="{video_ids}" %%%FOO%%%''')
                # BusinessLogicUtil.print_as_log(string=rf'''audio_ids="{audio_ids}" %%%FOO%%%''')
                # BusinessLogicUtil.print_as_log(string=rf'''video_id="{video_id}" %%%FOO%%%''')
                # BusinessLogicUtil.print_as_log(string=rf'''audio_id="{audio_id}" %%%FOO%%%''')
            except Exception:
                BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

            # 다운로드
            PKG_DOWNLOADING = StateManagementUtil.PKG_DOWNLOADING
            file = None
            src = None
            BusinessLogicUtil.make_pnx(pnx=PKG_DOWNLOADING, mode='d')
            BusinessLogicUtil.chdir(dst=dst)
            cmd = rf'{StateManagementUtil.YT_DLP_CMD} -f {video_id}+{audio_id} {url}'
            try:
                BusinessLogicUtil.command_to_os(cmd=cmd)
            except:
                return
            try:
                youtube_video_id = BusinessLogicUtil.parse_youtube_video_id(url)
                if youtube_video_id is None:
                    youtube_video_id = url
                lines = os.listdir()
                for line in lines:
                    if BusinessLogicUtil.is_pattern_in_string(str(line), str(youtube_video_id)):
                        file = line
                        src = os.path.abspath(file)
                        if BusinessLogicUtil.does_pnx_exist(src=src, show_mode=False):
                            items_list = BusinessLogicUtil.get_list_from_f_txt(pnx= function_name_txt)
                            for item in items_list:
                                if url.strip() in item.strip():
                                    items_list.remove(url)
                            items_list = BusinessLogicUtil.get_list_removed_element_duplicated(items_list=items_list)
                            BusinessLogicUtil.write_list_to_f_txt(texts=items_list, pnx=function_name_txt, mode='w')
                            BusinessLogicUtil.command_to_os(cmd=f'echo {url}_[SUCCESS] {file} >> "{function_name_txt}"')
                            BusinessLogicUtil.print_as_log(f'''src = "{src}"''')
                            BusinessLogicUtil.print_as_log(f'''dst = "{dst}"''')
                if src is None:
                    return
                # BusinessLogicUtil.print_light_black(f'''"다운로드 가능한 video_id 와 audio_id 를 가용목록에 추가해주세요"''')
                BusinessLogicUtil.move_pnx_without_overwrite(src, dst)
            except:
                BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
                BusinessLogicUtil.print_as_log(f"""%%%FOO%%%""")
                return

            BusinessLogicUtil.print_as_log(string=rf'''video_new="{dst}\{file}" %%%FOO%%%''')
            # BusinessLogicUtil.run_pnx_via_cmd_exe(command=rf'explorer "{dst}\{file}"', show_mode=False)
        except Exception:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def get_window_title(window_title_seg):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        window_titles = BusinessLogicUtil.get_window_titles()
        for window_title in window_titles:
            if window_title_seg in window_title:
                return window_title

    @staticmethod
    def minimize_all_windows_callback(hwnd, lparam):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # 창이 보이는 상태일 때만 최소화
        if win32gui.IsWindowVisible(hwnd):
            win32gui.ShowWindow(hwnd, win32con.SW_MINIMIZE)  # 창을 최소화
            print(f"창 {win32gui.GetWindowText(hwnd)}를 최소화했습니다.")

    @staticmethod
    def restore_all_windows():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        def enum_windows_callback(hwnd, lparam):
            # function_name = inspect.currentframe().f_code.co_name
            # BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            if win32gui.IsWindowVisible(hwnd):
                window_title = win32gui.GetWindowText(hwnd)
                # # 예시: 시스템 창이나 보안 프로그램을 제외하는 조건
                # if "System" in window_title or "Security" in window_title:
                #     print(f"시스템 창 또는 보안 프로그램을 건너뛰는 중: {window_title}")
                #     return  # 건너뛰기
                try:
                    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
                    win32gui.SetWindowPos(hwnd, win32con.HWND_TOP, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)
                    print(f"창 {win32gui.GetWindowText(hwnd)}를 복원했습니다.")
                except Exception as e:
                    print(f"Error while processing window {hwnd}: {str(e)}")
                    pass

        win32gui.EnumWindows(enum_windows_callback, None)

    @staticmethod
    def minimize_all_windows():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # 모든 열린 창을 순회하며 최소화
        win32gui.EnumWindows(BusinessLogicUtil.minimize_all_windows_callback, None)

    @staticmethod
    def get_text_dragged(show_mode=True):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # 클립보드 백업
        clipboard_current_contents = clipboard.paste()

        # 드래그된것 클립보드에 저장
        BusinessLogicUtil.press("ctrl", "c")

        # 클립보드에서 변수에 저장
        text_dragged = clipboard.paste()

        if show_mode == True:
            BusinessLogicUtil.print_as_log(string=rf'''text_dragged="{text_dragged}" %%%FOO%%%''')

        # 클립보드 복원
        clipboard.copy(clipboard_current_contents)

        return text_dragged

    @staticmethod
    def close_chrome_tab(url_to_close):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        window_titles = BusinessLogicUtil.get_window_titles()
        loop_limit = 50
        for window_title_seg in window_titles:
            if "chrome".lower() in window_title_seg.lower():
                BusinessLogicUtil.print_as_log(string=rf'''window_title="{window_title_seg}" %%%FOO%%%''')
                loop_cnt = 0
                while True:
                    BusinessLogicUtil.move_window_to_front(window_title_seg=window_title_seg)
                    if loop_cnt == loop_limit:
                        break
                    loop_cnt = loop_cnt + 1
                    BusinessLogicUtil.sleep(milliseconds=15, show_mode=False)
                    BusinessLogicUtil.press("ctrl", "l")
                    BusinessLogicUtil.sleep(milliseconds=15, show_mode=False)
                    url_dragged = BusinessLogicUtil.get_text_dragged(show_mode=False)
                    if url_dragged == url_to_close:
                        BusinessLogicUtil.print_as_log(string=rf'''url_to_close="{url_to_close}" %%%FOO%%%''')
                        BusinessLogicUtil.print_as_log(string=rf'''url_dragged="{url_dragged}" %%%FOO%%%''')
                        BusinessLogicUtil.press("ctrl", "w")
                        # BusinessLogicUtil.restore_all_windows()
                        return

    @staticmethod
    def refresh_chrome_tab(url_to_close):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # BusinessLogicUtil.minimize_all_windows()
        # window_title_seg = BusinessLogicUtil.get_window_title(window_title_seg="Chrome")
        window_titles = BusinessLogicUtil.get_window_titles()
        import time

        timeout_seconds = 10
        start_time = time.time()
        for window_title_seg in window_titles:
            if "chrome".lower() in window_title_seg.lower():
                if timeout_seconds == 50:
                    BusinessLogicUtil.print_as_log(string=rf'''window_title="{window_title_seg}" %%%FOO%%%''')
                while True:
                    elapsed_time = time.time() - start_time
                    if elapsed_time > timeout_seconds:
                        break
                    BusinessLogicUtil.move_window_to_front(window_title_seg=window_title_seg, show_mode=False)
                    BusinessLogicUtil.sleep(milliseconds=15, show_mode=False)
                    BusinessLogicUtil.press("ctrl", "l")
                    BusinessLogicUtil.sleep(milliseconds=15, show_mode=False)
                    url_dragged = BusinessLogicUtil.get_text_dragged(show_mode=False)
                    if url_dragged == url_to_close:
                        BusinessLogicUtil.print_as_log(string=rf'''url_to_close="{url_to_close}" %%%FOO%%%''')
                        BusinessLogicUtil.print_as_log(string=rf'''url_dragged="{url_dragged}" %%%FOO%%%''')
                        BusinessLogicUtil.press("f5")
                        # BusinessLogicUtil.restore_all_windows()
                        return

    @staticmethod
    def move_chrome_tab_by_url(url):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.minimize_all_windows()
        window_title_seg = BusinessLogicUtil.get_window_title(window_title_seg="Chrome")
        window_titles = BusinessLogicUtil.get_window_titles()
        for window_title in window_titles:
            if "Chrome".lower() in window_title.lower():
                BusinessLogicUtil.move_window_to_front(window_title_seg=window_title)
                loop_limit = 30
                loop_cnt = 0
                while True:
                    if loop_cnt == loop_limit:
                        return
                    loop_cnt = loop_cnt + 1
                    BusinessLogicUtil.sleep(milliseconds=15, show_mode=False)
                    BusinessLogicUtil.press("ctrl", "l")
                    BusinessLogicUtil.sleep(milliseconds=15, show_mode=False)
                    url_dragged = BusinessLogicUtil.get_text_dragged(show_mode=False)
                    if url_dragged == url:
                        BusinessLogicUtil.print_light_black(f'''url_to_move = "{url}"''')
                        BusinessLogicUtil.print_light_black(f'''url_dragged = "{url_dragged}"''')
                        break
                    pass

    @staticmethod
    def does_normal_tab_exist(driver_selenium, tab_title_negative):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        for window in driver_selenium.window_handles:  # 모든 탭 이동
            driver_selenium.switch_to.window(window)  # 각 탭으로 전환
            BusinessLogicUtil.sleep(milliseconds=random.randint(22, 2222))
            if tab_title_negative not in driver_selenium.title:  # 탭 제목 확인
                return True
        return False

    @staticmethod
    def classify_pnxs_to_pkg_document(pnx, without_walking=True):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # target_pnx가 유효한 디렉토리인지 확인
        if BusinessLogicUtil.is_file(pnx=pnx):
            BusinessLogicUtil.print_light_black(f"{pnx} 는 정리할 수 있는 디렉토리가 아닙니다")
            return

        # 파일과 디렉토리 get
        texts_to_exclude = [
            StateManagementUtil.DB_YAML,
            StateManagementUtil.SUCCESS_LOG,
            StateManagementUtil.LOCAL_PKG_CACHE_FILE,
        ]
        if without_walking == False:
            dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_with_walking(src=pnx, texts_to_exclude=texts_to_exclude)
        else:
            dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_without_walking(pnx=pnx, texts_to_exclude=texts_to_exclude)

        # 파일 처리
        x_allowed = [".txt", '.ximind', '.pdf', '.xls']
        x_allowed = x_allowed + BusinessLogicUtil.get_list_replaced_element_from_str_to_upper_case(items_list=x_allowed)
        pnx = BusinessLogicUtil.get_pn(pnx)
        dst = rf"{pnx}\pkg_document"
        for file_pnx in file_pnxs:
            file_pnx = file_pnx[0]
            file_p = BusinessLogicUtil.get_p(file_pnx)
            file_x = BusinessLogicUtil.get_x(file_pnx).replace(".", "")  # 확장자에서 점(.) 제거
            if file_x in [ext.replace(".", "") for ext in x_allowed]:  # x_allowed의 확장자와 비교
                BusinessLogicUtil.make_pnx(dst, mode="d")
                BusinessLogicUtil.move_pnx_without_overwrite(src=file_pnx, dst=dst)
                BusinessLogicUtil.print_as_log(string=rf'''file_pnx="{file_pnx}" %%%FOO%%%''')
        BusinessLogicUtil.print_as_log(string=rf'''dst="{dst}" %%%FOO%%%''')

    @staticmethod
    def classify_pnxs_to_pkg_image(pnx, without_walking=True):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        # target_pnx가 유효한 디렉토리인지 확인
        if BusinessLogicUtil.is_file(pnx=pnx):
            BusinessLogicUtil.print_light_black(f"{pnx} 는 정리할 수 있는 디렉토리가 아닙니다")
            return

        # 파일과 디렉토리 get
        texts_to_exclude = [
            StateManagementUtil.DB_YAML,
            StateManagementUtil.SUCCESS_LOG,
            StateManagementUtil.LOCAL_PKG_CACHE_FILE,
        ]
        if without_walking == False:
            dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_with_walking(src=pnx, texts_to_exclude=texts_to_exclude)
        else:
            dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_without_walking(pnx=pnx, texts_to_exclude=texts_to_exclude)

        # 파일 처리
        x_allowed = [".png", '.jpg', '.jpeg', '.jfif', '.webp']
        x_allowed = x_allowed + BusinessLogicUtil.get_list_replaced_element_from_str_to_upper_case(items_list=x_allowed)
        pnx = BusinessLogicUtil.get_pn(pnx)
        dst = rf"{pnx}\pkg_image"
        for file_pnx in file_pnxs:
            file_pnx = file_pnx[0]
            file_p = BusinessLogicUtil.get_p(file_pnx)
            file_x = BusinessLogicUtil.get_x(file_pnx).replace(".", "")  # 확장자에서 점(.) 제거
            if file_x in [ext.replace(".", "") for ext in x_allowed]:  # x_allowed의 확장자와 비교
                BusinessLogicUtil.make_pnx(dst, mode="d")
                BusinessLogicUtil.move_pnx_without_overwrite(src=file_pnx, dst=dst)
                BusinessLogicUtil.print_as_log(string=rf'''file_pnx="{file_pnx}" %%%FOO%%%''')
        BusinessLogicUtil.print_as_log(string=rf'''dst="{dst}" %%%FOO%%%''')

    @staticmethod
    def classify_pnxs_to_pkg_video(pnx, without_walking=True):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        # target_pnx가 유효한 디렉토리인지 확인
        if BusinessLogicUtil.is_file(pnx=pnx):
            BusinessLogicUtil.print_light_black(f"{pnx} 는 정리할 수 있는 디렉토리가 아닙니다")
            return

        # 파일과 디렉토리 get
        texts_to_exclude = [
            StateManagementUtil.DB_YAML,
            StateManagementUtil.SUCCESS_LOG,
            StateManagementUtil.LOCAL_PKG_CACHE_FILE,
        ]
        if without_walking == False:
            dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_with_walking(src=pnx, texts_to_exclude=texts_to_exclude)
        else:
            dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_without_walking(pnx=pnx, texts_to_exclude=texts_to_exclude)

        # 파일 처리
        x_allowed = [".mp4", '.avi', '.mkv', '.webm', '.mpg', '.flv', '.wmv']
        x_allowed = x_allowed + BusinessLogicUtil.get_list_replaced_element_from_str_to_upper_case(items_list=x_allowed)
        pnx = BusinessLogicUtil.get_pn(pnx)
        dst = rf"{pnx}\pkg_video"
        file_pnx = None
        for file_pnx in file_pnxs:
            file_pnx = file_pnx[0]
            file_p = BusinessLogicUtil.get_p(file_pnx)
            file_x = BusinessLogicUtil.get_x(file_pnx).replace(".", "")  # 확장자에서 점(.) 제거
            if file_x in [ext.replace(".", "") for ext in x_allowed]:  # x_allowed의 확장자와 비교
                BusinessLogicUtil.make_pnx(pnx=dst, mode="d")
                BusinessLogicUtil.move_pnx_without_overwrite(src=file_pnx, dst=dst)
                BusinessLogicUtil.print_as_log(string=rf'''file_pnx="{file_pnx}" %%%FOO%%%''')
        BusinessLogicUtil.print_as_log(string=rf'''dst="{dst}" %%%FOO%%%''')

    @staticmethod
    def classify_pnxs_to_pkg_soundtrack(pnx, without_walking=True):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # 유효디렉토리 확인
        if BusinessLogicUtil.is_file(pnx=pnx):
            BusinessLogicUtil.print_light_black(f"{pnx} 는 정리할 수 있는 디렉토리가 아닙니다")
            return

        # 파일과 디렉토리 get
        texts_to_exclude = [
            StateManagementUtil.DB_YAML,
            StateManagementUtil.SUCCESS_LOG,
            StateManagementUtil.LOCAL_PKG_CACHE_FILE,
        ]
        if without_walking == False:
            dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_with_walking(src=pnx, texts_to_exclude=texts_to_exclude)
        else:
            dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_without_walking(pnx=pnx, texts_to_exclude=texts_to_exclude)

        # 파일 처리
        x_allowed = [".mp3", '.flac', '.wav']
        x_allowed = x_allowed + BusinessLogicUtil.get_list_replaced_element_from_str_to_upper_case(items_list=x_allowed)
        pnx = BusinessLogicUtil.get_pn(pnx)
        dst = rf"{pnx}\pkg_soundtrack"
        for file_pnx in file_pnxs:
            file_pnx = file_pnx[0]
            file_p = BusinessLogicUtil.get_p(file_pnx)
            file_x = BusinessLogicUtil.get_x(file_pnx).replace(".", "")  # 확장자에서 점(.) 제거
            if file_x in [ext.replace(".", "") for ext in x_allowed]:  # x_allowed의 확장자와 비교
                BusinessLogicUtil.make_pnx(dst, mode="d")
                BusinessLogicUtil.move_pnx_without_overwrite(src=file_pnx, dst=dst)
                BusinessLogicUtil.print_as_log(string=rf'''file_pnx="{file_pnx}" %%%FOO%%%''')
        BusinessLogicUtil.print_as_log(string=rf'''dst="{dst}" %%%FOO%%%''')

    @staticmethod
    def classify_pnxs_to_pkg_compressed(src, without_walking=True):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # 디렉토리 유효성 확인
        if BusinessLogicUtil.is_file(pnx=src):
            BusinessLogicUtil.print_light_black(f"{src} %%%FOO%%%")
            return

        # 파일과 디렉토리 get
        texts_to_exclude = [
            StateManagementUtil.DB_YAML,
            StateManagementUtil.SUCCESS_LOG,
            StateManagementUtil.LOCAL_PKG_CACHE_FILE,
        ]

        if without_walking == False:
            dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_with_walking(src=src, texts_to_exclude=texts_to_exclude)
        else:
            dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_without_walking(pnx=src, texts_to_exclude=texts_to_exclude)

        # 파일 처리
        x_allowed = [".zip", '.tar']
        x_allowed = x_allowed + BusinessLogicUtil.get_list_replaced_element_from_str_to_upper_case(items_list=x_allowed)
        src = BusinessLogicUtil.get_pn(src)
        dst = rf"{src}\pkg_compressed"
        for file_pnx in file_pnxs:
            file_pnx = file_pnx[0]
            file_p = BusinessLogicUtil.get_p(file_pnx)
            file_x = BusinessLogicUtil.get_x(file_pnx).replace(".", "")  # 확장자에서 점(.) 제거
            if file_x in [ext.replace(".", "") for ext in x_allowed]:  # x_allowed의 확장자와 비교
                BusinessLogicUtil.make_pnx(dst, mode="d")
                BusinessLogicUtil.move_pnx_without_overwrite(src=file_pnx, dst=dst)
                BusinessLogicUtil.print_as_log(string=rf'''file_new="{file_pnx}" %%%FOO%%%''')
        BusinessLogicUtil.print_as_log(string=rf'''dst="{dst}" %%%FOO%%%''')

    @staticmethod
    def get_str_moved_pattern_to_front(pattern, item_pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        match = re.search(pattern=pattern, string=item_pnx)
        n = BusinessLogicUtil.get_n(item_pnx)
        p = BusinessLogicUtil.get_p(item_pnx)
        x = BusinessLogicUtil.get_x(item_pnx)
        if match:
            pattern = match.group(1)
            item_pnx_new = rf"{p}\{pattern}_{n.replace(pattern, '')}{x}"
            return item_pnx_new
        else:
            # 패턴이 없으면 원래 파일명 반환
            return item_pnx

    @staticmethod
    def get_str_moved_pattern_to_rear(pattern, item_pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        match = re.search(pattern=pattern, string=item_pnx)
        n = BusinessLogicUtil.get_n(item_pnx)
        p = BusinessLogicUtil.get_p(item_pnx)
        x = BusinessLogicUtil.get_x(item_pnx)
        if match:
            pattern = match.group(1)
            item_pnx_new = rf"{p}\{n.replace(pattern, '')}_{pattern}{x}"
            return item_pnx_new
        else:
            # 패턴이 없으면 원래 파일명 반환
            return item_pnx

    @staticmethod
    def print_sub_pnxs(src):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        texts_to_exclude = [
            StateManagementUtil.DB_YAML,
            StateManagementUtil.SUCCESS_LOG,
            StateManagementUtil.LOCAL_PKG_CACHE_FILE,
        ]

        # dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_without_walking(pnx=item_pnx, texts_to_exclude=texts_to_exclude)
        dir_pnxs, file_pnxs = BusinessLogicUtil.get_sub_pnxs_with_walking(src=src, texts_to_exclude=texts_to_exclude)

        pnxs = dir_pnxs + file_pnxs

        # 확인
        BusinessLogicUtil.print_list_as_vertical(items_list=pnxs, items_list_name="바꿀 대상")
        BusinessLogicUtil.print_as_log(string=rf'''len(pnxs)="{len(pnxs)}" %%%FOO%%%''')

    @staticmethod
    def save_all_drive_pnxs_to_text_file2():  # 루프 수정필요 # 이 함수는 거의 필요 없을 것 같다. 관심디렉토리만 확인하는 것으로 충분해 보인다.
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        function_name_txt = rf'{StateManagementUtil.PROJECT_DIRECTORY}\pkg_txt\{function_name}.txt'
        BusinessLogicUtil.make_pnx(pnx=function_name_txt, mode="item")
        # if not BusinessLogicUtil.is_window_open(window_title=function_name_txt):
        #     BusinessLogicUtil.run_pnx_via_explorer_exe(function_name_txt, show_mode=False)
        import os

        # 1. 특정 경로를 제외할 텍스트 파일에서 경로 읽어오기
        def load_pnxs_exclude(file_path):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            exclude_paths = set()
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    for line in file:
                        exclude_paths.add(line.strip())
            except PermissionError as e:
                print(f"PermissionError: {e}. Check if the item is accessible and you have the right permissions.")
            except Exception as e:
                print(f"Error opening item {file_path}: {e}")
            return exclude_paths

        # 2. 모든 드라이브에서 파일 목록 가져오기
        def get_drives_connected():
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            drives = []
            for letter in string.ascii_uppercase:
                drive = f"{letter}:\\"
                if os.path.exists(drive):
                    drives.append(drive)
            BusinessLogicUtil.print_as_log(string=rf'''drives="{drives}" %%%FOO%%%''')
            return drives

        # 3. 드라이브에서 파일 검색하고 처리하기
        def list_files_in_drives(exclude_paths_txt):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            exclude_paths = load_pnxs_exclude(exclude_paths_txt)
            drives = get_drives_connected()
            cnt = 0
            pnxs = []
            limit = 10000
            cnt_files = limit
            cnt_txt_files = 0
            temp = set()
            # 모든 드라이브에서 파일 탐색
            for drive in drives:
                BusinessLogicUtil.print_as_log(string=rf'''drive="{drive}" %%%FOO%%%''')
                for foldername, subfolders, filenames in os.walk(drive):
                    for filename in filenames:
                        file_pnx = os.path.join(foldername, filename)
                        # BusinessLogicUtil.print_as_log(string = rf'''file_pnx="{file_pnx}" %%%FOO%%%''')
                        cnt_files = cnt_files - 1
                        pnxs.append(file_pnx)
                        if cnt_files == 0:
                            # BusinessLogicUtil.print_as_log(string = rf'''file_pnx="{file_pnx}" %%%FOO%%%''')
                            cnt_files = limit
                            cnt_txt_files = cnt_txt_files + 1
                            # BusinessLogicUtil.print_as_log(string = rf'''cnt_txt_files="{cnt_txt_files}" %%%FOO%%%''')
                            output_pnx_txt_before = rf"{StateManagementUtil.PKG_TXT}\{function_name}_{cnt_txt_files - 1}.txt"
                            temp = BusinessLogicUtil.get_list_from_f_txt(pnx=output_pnx_txt_before)
                            if None != temp:
                                if 0 == len(temp):
                                    cnt_txt_files = cnt_txt_files - 1

                            output_pnx_txt = rf"{StateManagementUtil.PKG_TXT}\{function_name}_{cnt_txt_files}.txt"
                            # BusinessLogicUtil.print_as_log(string = rf'''output_pnx_txt="{output_pnx_txt}" %%%FOO%%%''')
                            # if any(exclude_path in file_pnx for exclude_path in exclude_paths):
                            #     continue
                            with open(output_pnx_txt, 'w', encoding='utf-8') as f:
                                for pnx in pnxs:
                                    cnt = cnt + 1
                                    # temp.add(rf"{pnx.split("\\")[0]}\{pnx.split("\\")[1]}")
                                    # print(temp)
                                    for exclude_path in exclude_paths:
                                        if exclude_path in pnx:
                                            break
                                    else:
                                        if not pnx.strip() == "":
                                            f.write(f'{pnx}\n')
                                            BusinessLogicUtil.print_as_log(string=rf'''cnt="{cnt}" pnxs="{pnx}" output_pnx_txt="{output_pnx_txt}" %%%FOO%%%''')
                                        else:
                                            BusinessLogicUtil.print_light_black(f'''없다''')
            BusinessLogicUtil.print_as_log(string=rf'''temp="{temp}" %%%FOO%%%''')

        # 실행
        exclude_paths_txt = rf'{StateManagementUtil.PKG_TXT}\{function_name}_exclude_paths.txt'
        BusinessLogicUtil.make_pnx(pnx=exclude_paths_txt, mode='item')
        list_files_in_drives(exclude_paths_txt)

    @staticmethod
    def get_element_random(items):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        return random.choice(items)

    @staticmethod
    def make_pnxs_interested_to_text_file_x(pnxs_interested=None, string_exclude=None):
        # todo 파일 내용 초기화 되어야 한다.
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        # pnxs_interested = []
        if pnxs_interested is None:
            pnxs_interested = [
                rf'{StateManagementUtil.USERPROFILE}\Downloads',
                rf'{StateManagementUtil.USERPROFILE}\AppData\Roaming\bittorrent',

                rf'D:\\',
                rf'E:\\',
                rf'F:\\',
            ]
        if string_exclude is None:
            string_exclude = [
                rf'{StateManagementUtil.USERPROFILE}\Downloads\jung_hoon_park\docker_image_maker\venv',
                rf'{StateManagementUtil.USERPROFILE}\Downloads\jung_hoon_park\test_flutter(모바일 프론트 엔드 용도)\ios',
                rf'{StateManagementUtil.USERPROFILE}\Downloads\jung_hoon_park\test_flutter(모바일 프론트 엔드 용도)\macos',
                rf'{StateManagementUtil.USERPROFILE}\Downloads\jung_hoon_park\test_flutter(모바일 프론트 엔드 용도)\windows',
                rf'{StateManagementUtil.USERPROFILE}\Downloads\jung_hoon_park\test_flutter(모바일 프론트 엔드 용도)\web',
                rf'{StateManagementUtil.USERPROFILE}\Downloads\jung_hoon_park\test_flutter(모바일 프론트 엔드 용도)\linux',
                rf'{StateManagementUtil.USERPROFILE}\Downloads\jung_hoon_park\test_flutter(모바일 프론트 엔드 용도)\lib',
                rf'{StateManagementUtil.USERPROFILE}\Downloads\jung_hoon_park\test_flutter(모바일 프론트 엔드 용도)\build',
                rf'{StateManagementUtil.USERPROFILE}\Downloads\jung_hoon_park\test_flutter(모바일 프론트 엔드 용도)\asset',
                rf'{StateManagementUtil.USERPROFILE}\Downloads\jung_hoon_park\test_flutter(모바일 프론트 엔드 용도)\android',

                rf'D:\$RECYCLE.BIN',
                rf'D:\System Volume Information',

                rf'E:\$RECYCLE.BIN',
                rf'E:\System Volume Information',

                rf'F:\$RECYCLE.BIN',
                rf'F:\System Volume Information',

                rf'deprecated',
                rf'archived',
                rf'.git',
                rf'.idea',
                rf'venv',
                rf'node_modules',
                rf'test_flutter',
                rf'pkg_font',
                rf'telegram memo export by static web',
                rf'docker_image_maker',
                rf'e-magazine',
                rf'netlify-web',
            ]
        pnxs_processed = []
        file_cnt = 0
        write_cnt = 0
        write_cnt_limit = 1000000
        for pnx_interested in pnxs_interested:
            pnxs_with_walking = BusinessLogicUtil.get_pnxs_with_walking(directory_pnx=pnx_interested, mode="f")

            # 'pnxs_exclude'를 set으로 변경하여 'in' 연산을 최적화
            function_name_file_cnt_txt = None
            for pnx_with_walking in pnxs_with_walking:
                # 빠른 'in' 연산을 위해 set으로 변환된 pnxs_exclude 활용
                if any(pnx_exclude in pnx_with_walking for pnx_exclude in string_exclude):
                    continue  # 'pnx_exclude'에 포함되면 건너뛰기
                # 'exclude' 목록에 포함되지 않으면 'pnxs_processed'에 추가
                pnxs_processed.append(pnx_with_walking)
                BusinessLogicUtil.print_as_log(string=rf'''len(pnxs_processed)="{len(pnxs_processed)}" %%%FOO%%%''')
                if write_cnt == write_cnt_limit % 2 == 0:
                    file_cnt = file_cnt + 1
                    BusinessLogicUtil.print_list_as_vertical(items_list=pnxs_processed, items_list_name="pnxs_processed")
                    # function_name_file_cnt_txt = rf"{StateManagementUtil.PKG_TXT}\{function_name}_{file_cnt}.txt"
                    # BusinessLogicUtil.write_list_to_file(texts=pnxs_processed, pnx=function_name_file_cnt_txt, mode="w")
                function_name_file_cnt_txt = rf"{StateManagementUtil.PKG_TXT}\{function_name}_{file_cnt}.txt"
                BusinessLogicUtil.print_as_log(string=rf'''write_cnt="{write_cnt}" %%%FOO%%%''')
                BusinessLogicUtil.write_str_to_file(txt_str=f"{pnx_with_walking}\n", pnx=function_name_file_cnt_txt, mode="a", show_mode=False)
                write_cnt = write_cnt + 1
                if write_cnt == write_cnt_limit % 2 == 0:
                    window_title = rf"{function_name}_{file_cnt}"
                    # if not BusinessLogicUtil.is_window_open(window_title_seg=window_title):
                    #     BusinessLogicUtil.open_window_by_pnx(pnx=function_name_file_cnt_txt)

    @staticmethod
    def make_pnxs_interested_to_text_file(pnxs_interested=None, string_exclude=None):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        # pnxs_interested = []
        if pnxs_interested is None:
            pnxs_interested = [
                rf'{StateManagementUtil.USERPROFILE}\Downloads',
                rf'{StateManagementUtil.USERPROFILE}\AppData\Roaming\bittorrent',

                rf'D:\\',
                rf'E:\\',
                rf'F:\\',
            ]
        # pnxs_exclude = []
        if pnxs_interested is None:
            string_exclude = [
                rf'{StateManagementUtil.USERPROFILE}\Downloads\jung_hoon_park\docker_image_maker\venv',
                rf'{StateManagementUtil.USERPROFILE}\Downloads\jung_hoon_park\test_flutter(모바일 프론트 엔드 용도)\ios',
                rf'{StateManagementUtil.USERPROFILE}\Downloads\jung_hoon_park\test_flutter(모바일 프론트 엔드 용도)\macos',
                rf'{StateManagementUtil.USERPROFILE}\Downloads\jung_hoon_park\test_flutter(모바일 프론트 엔드 용도)\windows',
                rf'{StateManagementUtil.USERPROFILE}\Downloads\jung_hoon_park\test_flutter(모바일 프론트 엔드 용도)\web',
                rf'{StateManagementUtil.USERPROFILE}\Downloads\jung_hoon_park\test_flutter(모바일 프론트 엔드 용도)\linux',
                rf'{StateManagementUtil.USERPROFILE}\Downloads\jung_hoon_park\test_flutter(모바일 프론트 엔드 용도)\lib',
                rf'{StateManagementUtil.USERPROFILE}\Downloads\jung_hoon_park\test_flutter(모바일 프론트 엔드 용도)\build',
                rf'{StateManagementUtil.USERPROFILE}\Downloads\jung_hoon_park\test_flutter(모바일 프론트 엔드 용도)\asset',
                rf'{StateManagementUtil.USERPROFILE}\Downloads\jung_hoon_park\test_flutter(모바일 프론트 엔드 용도)\android',

                rf'D:\$RECYCLE.BIN',
                rf'D:\System Volume Information',

                rf'E:\$RECYCLE.BIN',
                rf'E:\System Volume Information',

                rf'F:\$RECYCLE.BIN',
                rf'F:\System Volume Information',

                rf'deprecated',
                rf'archived',
                rf'.git',
                rf'.idea',
                rf'venv',
                rf'node_modules',
                rf'test_flutter',
                rf'pkg_font',
                rf'telegram memo export by static web',
                rf'docker_image_maker',
                rf'e-magazine',
                rf'netlify-web',
            ]

        pnxs_processed = []
        function_name_txt = rf"{StateManagementUtil.PKG_TXT}\{function_name}.txt"
        BusinessLogicUtil.write_str_to_file(txt_str=f"", pnx=function_name_txt, mode="w")  # 내용 초기화
        for pnx_interested in pnxs_interested:
            pnxs_with_walking = BusinessLogicUtil.get_pnxs_with_walking(directory_pnx=pnx_interested, mode="f")
            for pnx_with_walking in pnxs_with_walking:
                if any(pnx_exclude in pnx_with_walking for pnx_exclude in string_exclude):
                    continue
                pnxs_processed.append(pnx_with_walking)
                BusinessLogicUtil.write_str_to_file(txt_str=f"{pnx_with_walking}\n", pnx=function_name_txt, mode="a")

    @staticmethod
    def get_screenshot():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # 화면 캡처 (PyAutoGUI를 사용)
        screenshot = pyautogui.screenshot()
        # PIL 이미지를 OpenCV 이미지로 변환
        open_cv_image = np.array(screenshot)
        # RGB → BGR 색상 변환 (OpenCV는 BGR 형식 사용)
        open_cv_image = cv2.cvtColor(open_cv_image, cv2.COLOR_RGB2BGR)
        return open_cv_image

    @staticmethod
    def get_extreact_texts_from_image_via_easyocr(image):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # EasyOCR 객체 생성
        reader = easyocr.Reader(['en', 'ko'])  # 영어와 한글을 동시에 처리하려면 'en', 'ko' 지정
        result = reader.readtext(image)
        return result

    @staticmethod
    def is_str_in_text(string, text):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        if string.lower() in text.lower():
            return True
        return False

    @staticmethod
    def is_str_on_screen(string):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # 화면 캡처
        screenshot = BusinessLogicUtil.get_screenshot()

        # OCR을 통해 텍스트 추출
        extreact_texts = BusinessLogicUtil.get_extreact_texts_from_image_via_easyocr(screenshot)
        text_extracted = " ".join([r[1] for r in extreact_texts])

        if BusinessLogicUtil.is_str_in_text(string=string, text=text_extracted):
            return True
        else:
            return False

    @staticmethod
    def get_all_text_with_coordinates_via_easy_ocr(image):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # EasyOCR 객체 생성
        reader = easyocr.Reader(['en', 'ko'])  # 영어와 한글을 동시에 처리하려면 'en', 'ko' 지정
        results = reader.readtext(image)

        # 추출된 텍스트와 위치 반환
        text_with_coordinates = [(result[1], result[0]) for result in results]
        return text_with_coordinates

    @staticmethod
    def get_coordinates_bounding_box(image, string):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # EasyOCR로 텍스트 및 위치 추출
        reader = easyocr.Reader(['en', 'ko'])  # 영어와 한글을 동시에 처리하려면 'en', 'ko' 지정
        results = reader.readtext(image)

        # 추출된 텍스트와 위치 반환
        for result in results:
            text = result[1]  # result[1]은 텍스트
            if string.lower() in text.lower():
                coord_bounding_box = result[0]  # result[0]은 바운딩 박스 좌표
                return coord_bounding_box
        print(f"{string}에 대한 바운딩 박스가 화면에 없습니다. ")

    @staticmethod
    def get_center_of_bounding_box(bounding_box):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        """
        바운딩 박스 좌표를 받아서, 그 중심 좌표를 반환하는 함수.

        :param bounding_box: 바운딩 박스 좌표 [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
        :return: 중심 좌표 (x, y)
        """
        # 네 점의 x, y 좌표를 각각 합산
        if bounding_box is None:
            return None
        x_coords = [point[0] for point in bounding_box]
        y_coords = [point[1] for point in bounding_box]

        # x, y 평균값을 구하여 중심 좌표 계산
        center_x = sum(x_coords) / 4
        center_y = sum(y_coords) / 4

        return center_x, center_y

    @staticmethod
    def get_text_coordinates_via_easy_ocr(string):  # 한글인식 잘 안되는 듯하다
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # 화면 캡처
        screenshot = BusinessLogicUtil.get_screenshot()

        # EsayOCR을 통해 모든텍스트 바운딩박스좌표 추출
        # coordinates_bounding_box = BusinessLogicUtil.get_all_text_with_coordinates_via_easy_ocr(screenshot)
        # BusinessLogicUtil.print_list_as_vertical(items_list=coordinates_bounding_box, items_name="coordinates_bounding_box")

        # EsayOCR을 통해 특정텍스트 바운딩박스좌표 추출
        coordinates_bounding_box = BusinessLogicUtil.get_coordinates_bounding_box(image=screenshot, string=string)
        # BusinessLogicUtil.print_list_as_vertical(items_list=coordinates_bounding_box, items_name="coordinates_bounding_box")

        # 중심 좌표 구하기
        if BusinessLogicUtil.get_center_of_bounding_box(coordinates_bounding_box) is not None:
            center_x, center_y = BusinessLogicUtil.get_center_of_bounding_box(coordinates_bounding_box)
            # BusinessLogicUtil.print_as_log(string = rf'''center_x="{center_x}" %%%FOO%%%''')
            # BusinessLogicUtil.print_as_log(string = rf'''center_y="{center_y}" %%%FOO%%%''')
            BusinessLogicUtil.print_light_black(f'''"text_coordinates = ({center_x}, {center_y})"''')
            return center_x, center_y
        return None

    @staticmethod
    def reconnect_to_qcy_h3_anc_headset_via_bluetooth():  # toogle_to_qcy_h3_anc_headset_via_bluetooth 이게 더 작명이 나은것..
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # Bluetooth 설정창 띄우기
        cmd = 'start ms-settings:bluetooth'
        BusinessLogicUtil.command_to_os_like_person_as_admin(command=cmd, show_mode=False)
        window_title_seg = "설정"
        timeout = 10
        start_time = time.time()
        while True:
            if not BusinessLogicUtil.is_window_open(window_title_seg=window_title_seg):
                BusinessLogicUtil.move_window_to_front(window_title_seg=window_title_seg)
            else:
                break
            BusinessLogicUtil.print_as_log(string=time.time() - start_time)
            if time.time() - start_time > timeout:
                break
            time.sleep(0.5)

        # string 더블 클릭
        BusinessLogicUtil.click_string(string="QCY H3 ANC HEADSET", doubleclick_mode=True)

        # string 더블 클릭
        asyncio.run(BusinessLogicUtil.shoot_custom_screenshot_via_asyncio())
        # BusinessLogicUtil.click_img_via_autogui()

        # string 더블 클릭
        # BusinessLogicUtil.click_string(string="연결", doubleclick_mode=True)
        pass

    # @staticmethod
    # def close_chrome_tab_duplicated():
    #     function_name = inspect.currentframe().f_code.co_name
    #     BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
    #     # BusinessLogicUtil.minimize_all_windows()
    #     # window_title_seg = BusinessLogicUtil.get_window_title(window_title_seg="Chrome")
    #
    #     window_title = "Chrome"
    #     BusinessLogicUtil.move_window_to_front(window_title_seg=window_title, show_mode=False)
    #
    #     chrome_tab_urls_duplicated = []
    #     chrome_tab_urls_processed = []  # 이미 처리된 URL을 저장하는 리스트
    #     chrome_tab_urls_len_before = 0
    #     loop_limit = 10
    #     loop_out_cnt = 0
    #
    #     while True:
    #         BusinessLogicUtil.print_as_log(string=rf'''loop_out_cnt="{loop_out_cnt}" %%%FOO%%%''')
    #         BusinessLogicUtil.print_as_log(string=rf'''loop_limit="{loop_limit}" %%%FOO%%%''')
    #
    #         # 탭을 전환하고 URL을 가져옵니다.
    #         BusinessLogicUtil.press("ctrl", "l")
    #         BusinessLogicUtil.sleep(milliseconds=5)
    #         url_dragged = BusinessLogicUtil.get_text_dragged(show_mode=False)
    #
    #         # 다시 탭을 전환하고 URL을 가져옵니다.
    #         BusinessLogicUtil.press("ctrl", "tab")
    #         BusinessLogicUtil.sleep(milliseconds=5)
    #         BusinessLogicUtil.press("ctrl", "l")
    #         BusinessLogicUtil.sleep(milliseconds=5)
    #         url_dragged_new = BusinessLogicUtil.get_text_dragged()
    #         BusinessLogicUtil.print_as_log(string=rf'''url_dragged="{url_dragged}" %%%FOO%%%''')
    #         BusinessLogicUtil.print_as_log(string=rf'''url_dragged_new="{url_dragged_new}" %%%FOO%%%''')
    #
    #         # URL이 동일한지 확인하여 중복된 URL인지 체크
    #         if url_dragged == url_dragged_new:
    #             # if url_dragged not in chrome_tab_urls_duplicated:
    #             #     chrome_tab_urls_duplicated.append(url_dragged)
    #             #     BusinessLogicUtil.print_as_log(string=rf'''Added duplicate URL: "{url_dragged}" %%%FOO%%%''')
    #
    #             # 중복된 URL의 탭을 닫음
    #             BusinessLogicUtil.press("ctrl", "w")
    #             loop_out_cnt -= 1
    #         loop_out_cnt += 1
    #
    #         # 처리된 URL을 `chrome_tab_urls_processed`에 추가
    #         chrome_tab_urls_processed.append(url_dragged)
    #         BusinessLogicUtil.print_as_log(string=rf'''chrome_tab_urls_processed="{chrome_tab_urls_processed}" %%%FOO%%%''')
    #
    #         # 중복된 탭을 모두 제거했으면 종료
    #         if loop_out_cnt == loop_limit:
    #             # BusinessLogicUtil.get_list_removed_element_duplicated(chrome_tab_urls_processed)
    #             BusinessLogicUtil.print_as_log(string=rf'''Counter(chrome_tab_urls_processed)="{Counter(chrome_tab_urls_processed)}" %%%FOO%%%''')
    #             # if loop_out_cnt >= loop_limit:
    #             #     BusinessLogicUtil.print_as_log(string=rf'''중복된 탭을 모두 제거 %%%FOO%%%''')
    #             #     break  # 더 이상 중복된 탭이 없으므로 종료
    #             return
    @staticmethod
    def close_chrome_tab_duplicated():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        chrome_tab_urls_processed = []  # 이미 처리된 URL을 저장하는 리스트
        loop_limit = 10
        loop_out_cnt = 0

        while True:
            window_title = "Chrome"
            if BusinessLogicUtil.is_window_open(window_title_seg=window_title):
                BusinessLogicUtil.move_window_to_front(window_title_seg=window_title, show_mode=False)

            BusinessLogicUtil.print_as_log(string=rf'''loop_out_cnt="{loop_out_cnt}" %%%FOO%%%''')
            BusinessLogicUtil.print_as_log(string=rf'''loop_limit="{loop_limit}" %%%FOO%%%''')

            # 탭을 전환하고 URL을 가져옵니다.
            BusinessLogicUtil.press("ctrl", "l")
            BusinessLogicUtil.sleep(milliseconds=5)
            url_dragged = BusinessLogicUtil.get_text_dragged(show_mode=False)

            # 중복 여부 확인
            if url_dragged in chrome_tab_urls_processed:
                BusinessLogicUtil.print_as_log(string=rf'''URL already processed: "{url_dragged}" %%%FOO%%%''')
                BusinessLogicUtil.press("ctrl", "tab")  # 다음 탭으로 이동
                loop_out_cnt += 1
                if loop_out_cnt >= loop_limit:
                    break
                continue

            # 다음 탭으로 전환 후 URL 가져오기
            BusinessLogicUtil.press("ctrl", "tab")
            BusinessLogicUtil.sleep(milliseconds=5)
            BusinessLogicUtil.press("ctrl", "l")
            BusinessLogicUtil.sleep(milliseconds=5)
            url_dragged_new = BusinessLogicUtil.get_text_dragged()

            BusinessLogicUtil.print_as_log(string=rf'''url_dragged="{url_dragged}" %%%FOO%%%''')
            BusinessLogicUtil.print_as_log(string=rf'''url_dragged_new="{url_dragged_new}" %%%FOO%%%''')

            # 중복된 URL이면 탭 닫기
            if url_dragged == url_dragged_new:
                BusinessLogicUtil.print_as_log(string=rf'''Closing duplicate tab for URL: "{url_dragged}" %%%FOO%%%''')
                BusinessLogicUtil.press("ctrl", "w")  # 탭 닫기
                continue

            # 처리된 URL을 리스트에 추가
            chrome_tab_urls_processed.append(url_dragged)
            BusinessLogicUtil.print_as_log(string=rf'''chrome_tab_urls_processed="{chrome_tab_urls_processed}" %%%FOO%%%''')

            # 최대 반복 횟수 초과 시 종료
            loop_out_cnt += 1
            if loop_out_cnt >= loop_limit:
                break

    @staticmethod
    def get_list_element_duplicated(items_list):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        items_duplicated = []
        seen = set()  # 이미 본 요소를 추적할 집합
        for item in items_list:
            if item in seen and item not in items_duplicated:
                items_duplicated.append(item)
            else:
                seen.add(item)
        return items_duplicated

    @staticmethod
    def decode_via_park4139(text_encoded):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        text_encoded = text_encoded.replace("2", "8")
        text_encoded = text_encoded.replace("3", "7")
        text_encoded = text_encoded.replace("4", "6")
        text_encoded = text_encoded.replace("6", "4")
        text_encoded = text_encoded.replace("7", "3")
        text_encoded = text_encoded.replace("8", "2")
        return text_encoded

    @staticmethod
    def encode_via_park4139(text_plain):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        text_plain = text_plain.replace("8", "2")
        text_plain = text_plain.replace("7", "3")
        text_plain = text_plain.replace("6", "4")
        text_plain = text_plain.replace("4", "6")
        text_plain = text_plain.replace("3", "7")
        text_plain = text_plain.replace("2", "8")
        return text_plain

    @staticmethod
    def replace_text_B_and_text_C_interchangeably_at_text_A_by_using_(____text_A, ____text_B, ____text_C, _____and):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        foo_foo = "{{kono foo wa sekai de uituna mono ni motomo chikai desu}}"
        text_special = "{{no}}"
        text_B_cnt = ____text_A.count(____text_B)
        foo_list = []
        foo_str = ""
        foo_cmt = 0
        if ____text_C == "":
            ____text_A = ____text_A.replace(____text_B, ____text_C)
        elif text_special in ____text_C:
            print("text_A 에서 " + ____text_B + " 를 총" + str(text_B_cnt) + "개 발견하였습니다")
            foo_list = ____text_A.split(____text_B)
            if ____text_B in ____text_C:
                foo_cmt = 0
                for j in foo_list:
                    if j == foo_list[-1]:
                        pass
                    else:
                        foo_str = foo_str + j + ____text_C.split(text_special)[0] + str(foo_cmt)
                    foo_cmt = foo_cmt + 1
                ____text_A = ""
                ____text_A = foo_str
            else:
                foo_cmt = 0
                for j in foo_list:
                    if j == foo_list[-1]:
                        pass
                    else:
                        foo_str = foo_str + j + ____text_C.split(text_special)[0] + str(foo_cmt)
                    foo_cmt = foo_cmt + 1
                ____text_A = ""
                ____text_A = foo_str
        else:
            ____text_A = ____text_A.replace(____text_C, foo_foo)
            ____text_A = ____text_A.replace(____text_B, ____text_C)
            ____text_A = ____text_A.replace(foo_foo, ____text_B)

    @staticmethod
    def act_via_interchangeable_triangle_model_by_using_(____text_A, ____text_B, ____text_C, _____and):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        foo_foo = "{{kono foo wa sekai de uituna mono ni motomo chikai desu}}"
        if ____text_C == "":
            ____text_A = ____text_A.replace(____text_B, ____text_C)
        else:
            ____text_A = ____text_A.replace(____text_C, foo_foo)
            ____text_A = ____text_A.replace(____text_B, ____text_C)
            ____text_A = ____text_A.replace(foo_foo, ____text_B)

    @staticmethod
    def print_built_in_info(thing_curious):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.print_as_log(f"{inspect.currentframe().f_code.co_name} {str(thing_curious.__code__.co_varnames)}")
        print("_______________________________________________________________ " + str() + "(" + str(thing_curious) + ") s")
        BusinessLogicUtil.print_as_log("print(inspect.getsource(thing_curious))")
        print(inspect.getsource(thing_curious))
        BusinessLogicUtil.print_as_log("for i in inspect.getmembers(thing_curious_):")
        for i in inspect.getmembers(thing_curious):
            print(i)
        BusinessLogicUtil.print_as_log("print(help(thing_curious))")
        print(help(thing_curious))
        BusinessLogicUtil.print_as_log("[x for x in dir(thing_curious) if '__' not in x]")
        foo = [x for x in dir(thing_curious) if '__' not in x]
        # dir() 함수는 값 없이 지정된 객체의 모든 속성과 메서드를 반환합니다 .
        # 이 함수는 모든 속성과 메서드를 반환하며, 모든 개체에 대한 기본값인 내장 속성도 반환합니다.
        BusinessLogicUtil.print_as_log("[x for x in dir(thing_curious) if '__' not in x]")

    @staticmethod
    def print_function_info(thing_curious):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.print_as_log(f"{inspect.currentframe().f_code.co_name} {str(thing_curious.__code__.co_varnames)}")
        print(help(thing_curious))
        BusinessLogicUtil.print_as_log(f'# of the Arguments : {thing_curious.__code__.co_argcount}')
        # BusinessLogicUtil.print_as_log(f'Name of the Arguments : {thing_curious.__code__.co_varnames}')
        print("┌>print via getsource s")
        print(inspect.getsource(thing_curious))
        print("└>print via getsource e")

    @staticmethod
    def print_event_info_(event, thing_curious):
        """
            jhp_debugger.print_event_info_(event)
            # └>call sample
        """
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        print(str(event))
        # print(event.type())
        # if type(thing_curious)==str:
        #     print('{{mkr}}')
        # if type(thing_curious)==list:
        #     print(thing_curious[str(event.type())])
        # if type(thing_curious) == tuple:
        #     print('{{mkr}}')
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

    @staticmethod
    def find_pnxs_interested_from_text_file_x(including_texts=[], exclude_texts=[], except_extensions=[], including_extensions=[]):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        # 디렉토리 내의 모든 파일 리스트 가져오기
        # directory = "."  # 현재 디렉토리에서 확인
        directory = StateManagementUtil.PKG_TXT
        # directory = BusinessLogicUtil.get_pnx_preprocessed(pnx=directory)
        # pattern = rf"{re.escape(directory)}\update_pnxs_interested_to_text_file_\d\.txt$"
        # pattern = rf"{re.escape(directory)}\\update_pnxs_interested_to_text_file_\d\.txt$"
        pattern = rf"^update_pnxs_interested_to_text_file_\d\.txt$"
        BusinessLogicUtil.print_as_log(string=rf'''pattern="{pattern}" %%%FOO%%%''')
        files_in_directory = os.listdir(directory)
        BusinessLogicUtil.print_list_as_vertical(items_list=files_in_directory, items_list_name="files_in_directory")
        files_nxs_matched = [file for file in files_in_directory if re.match(pattern, file)]
        pnxs_required = []
        if files_nxs_matched:
            BusinessLogicUtil.print_as_log(string=rf'''files_matched="{files_nxs_matched}" %%%FOO%%%''')
            for files_nx_matched in files_nxs_matched:
                pnx = rf"{directory}\{files_nx_matched}"
                BusinessLogicUtil.print_as_log(string=rf'''pnx="{pnx}" %%%FOO%%%''')
                lines = BusinessLogicUtil.get_list_from_f_txt(pnx=pnx)
                for line in lines:
                    if not including_texts == []:
                        if any(text in line for text in including_texts):
                            pnxs_required.append(line)
                    else:
                        pnxs_required.append(line)
            pnxs_required = BusinessLogicUtil.get_list_replaced_element_from_str_to_str(item_list=pnxs_required, from_str="\n", to_str="")
            # BusinessLogicUtil.print_list_as_vertical(items_list = pnxs_required, items_name="pnxs_required")
        else:
            print("정규식 패턴에 맞는 파일이 존재하지 않습니다.")

        pnxs_excluded = []
        for pnx in pnxs_required:
            # texts_to_exclude의 어떠한 요소도 포함되지 않은 경우만 추가
            if not any(exclude_text in pnx for exclude_text in exclude_texts):  # 배제할 확장자 체크
                file_extension = os.path.splitext(pnx)[1]
                if file_extension not in except_extensions:  # 제외할 확장자 체크
                    if not including_extensions == []:
                        if any(file_extension == ext for ext in including_extensions):  # 반드시 포함할 확장자 체크
                            pnxs_excluded.append(pnx)
                    else:
                        pnxs_excluded.append(pnx)
        BusinessLogicUtil.print_list_as_vertical(items_list=pnxs_excluded, items_list_name="pnxs_excluded")
        return pnxs_excluded

    @staticmethod
    def get_list_interested_from_list(item_list, string_list_include=[], string_list_exclude=[], except_extensions=[], extension_list_include=[], string_list_include_any=[]):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        pnxs_included = []
        for item in item_list:
            if not string_list_include == []:
                if any(text in item for text in string_list_include):
                    pnxs_included.append(item)
            else:
                pnxs_included.append(item)
        pnxs_included = BusinessLogicUtil.get_list_replaced_element_from_str_to_str(item_list=pnxs_included, from_str="\n", to_str="")
        # BusinessLogicUtil.print_list_as_vertical(items_list = pnxs_included, items_list_name='pnxs_included')

        pnxs_excluded = []
        for pnx in pnxs_included:
            # texts_to_exclude의 어떠한 요소도 포함되지 않은 경우만 추가
            if not any(exclude_text in pnx for exclude_text in string_list_exclude):  # 배제할 확장자 체크
                file_extension = os.path.splitext(pnx)[1]
                if file_extension not in except_extensions:  # 제외할 확장자 체크
                    if not extension_list_include == []:
                        if any(file_extension == ext for ext in extension_list_include):  # 반드시 포함할 확장자 체크
                            pnxs_excluded.append(pnx)
                    else:
                        pnxs_excluded.append(pnx)
        # BusinessLogicUtil.print_list_as_vertical(items_list=pnxs_excluded, items_list_name="pnxs_excluded")

        pnxs_required = []
        if not string_list_include_any == []:
            for item in pnxs_excluded:
                if any(include in item for include in string_list_include_any):
                    pnxs_required.append(item)
        else:
            pnxs_required = pnxs_excluded
        return pnxs_required

    @staticmethod
    def ask_to_chat_gpt(question):
        # 페이지 열기
        url = "https://chatgpt.com/"
        BusinessLogicUtil.command_to_os(cmd=f'explorer "{url}"')
        print(rf"{url} 을 띄웠습니다")

        # 창 앞으로 이동
        window_title = "Chrome"
        window_title_seg = window_title,
        BusinessLogicUtil.move_window_to_front(window_title_seg=window_title_seg)

        # chrome 창 탭 중 해당 url로 이동
        BusinessLogicUtil.move_chrome_tab_by_url(url=url)

        # text_string 클릭
        # text_string = "로그아웃 유지"
        # text_coordinates = BusinessLogicUtil.get_text_coordinates_via_easy_ocr(string=text_string)
        # # text_coordinates = (692.0, 1047.5)
        # if not text_coordinates:
        #     print(rf"Text not found. {text_string}")
        #     return
        # x_abs, y_abs = text_coordinates
        # BusinessLogicUtil.move_mouse(x_abs=x_abs, y_abs=y_abs)
        # BusinessLogicUtil.click_mouse_left_btn(x_abs=x_abs, y_abs=y_abs)
        # print(rf"{text_string}")

        # 스크린샷 프로그램 실행
        # BusinessLogicUtil.collect_img_for_autogui()
        # asyncio.run(BusinessLogicUtil.shoot_custom_screenshot())

        # 이미지 바운딩박스 찾아 가운데 센터 클릭 ...
        file_png = rf"{StateManagementUtil.PROJECT_DIRECTORY}\pkg_image\screenshot_로그아웃_유지_2024_11_19_02_54_14.png"
        # BusinessLogicUtil.click_center_of_img_recognized_by_mouse_left(img_abspath=file_png, loop_limit_cnt=10, is_zoom_toogle_mode=False)
        # 인식률 및 속도 개선 시도
        # pip install opencv-python # 이것은 고급 기능이 포함되지 않은 Python용 OpenCV의 미니 버전입니다. 우리의 목적에는 충분합니다.
        # confidence=0.7(70%)유사도를 낮춰 인식률개선시도, region 낮춰 속도개선시도, grayscale 흑백으로 판단해서 속도개선시도,
        # open cv 설치했는데 적용안되고 있음. 재부팅도 하였는 데도 안됨.
        # pycharm 에서 import 하는 부분에서 cv2 설치 시도 중에 옵션으로 opencv-python 이 있길래 설치했더니 결국 됨. 혹쉬 경로 설정 필요했나?
        # xy_infos_of_imgs = pyautogui.locateOnScreen(img_abspath, confidence=0.7, grayscale=True)
        # BusinessLogicUtil.debug_as_gui(xy_infos_of_imgs is None)
        img = pyautogui.locateOnScreen(file_png, confidence=0.7, grayscale=True)

        # # 프롬프트 콘솔 클릭(광고 없어도 진행)
        # file_png = rf"{StateManagementUtil.PROJECT_DIRECTORY}\pkg_png\ask_to_wrtn.png"
        # if BusinessLogicUtil.click_center_of_img_recognized_by_mouse_left(img_abspath=file_png, recognize_loop_limit_cnt=50, is_zoom_toogle_mode=True):
        #     # 질문 작성 및 확인
        #     BusinessLogicUtil.write_fast(question)
        #     BusinessLogicUtil.press('enter')

        # 뤼튼 프롬프트 콘솔 최하단 이동 버튼 클릭
        pass

    # @staticmethod
    # def command_run(command, show_mode=True, mode=""):
    #     function_name = inspect.currentframe().f_code.co_name
    #     BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
    #     BusinessLogicUtil.print_as_log(string=rf'''command="{command}" %%%FOO%%%''')
    #     if mode == "async":  # 비동기처리
    #         BusinessLogicUtil.print_as_log(string=rf'''mode="{mode}" %%%FOO%%%''')
    #         subprocess.Popen(command, shell=True, encoding='utf-8')
    #         # subprocess.Popen(command, shell=True, universal_newlines=True)
    #         return
    #     try:  # 동기처리
    #         # stdout_lines = []
    #         # stderr_lines = []
    #         # # process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, universal_newlines=True)
    #         # # process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, universal_newlines=True)
    #         # # process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    #         # # process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='euc-kr')
    #         # # process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
    #         # # process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8', errors='ignore')
    #         # process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, universal_newlines=True)
    #         # # process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, universal_newlines=True, errors='ignore')
    #         #
    #         # for line in process.stdout:
    #         #     stdout_lines.append(line.strip())
    #         # for line in process.stderr:
    #         #     stderr_lines.append(line.strip())
    #
    #         stdout_lines = []
    #         stderr_lines = []
    #         process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    #         stdout_data, stderr_data = process.communicate()
    #
    #         # Detect encoding using chardet
    #         detected_encoding = chardet.detect(stdout_data)
    #         encoding = detected_encoding['encoding'] if detected_encoding['encoding'] else 'utf-8'
    #
    #         # Decode using the detected encoding or default to 'utf-8' if None
    #         stdout_text = stdout_data.decode(encoding, errors='ignore')
    #         stderr_text = stderr_data.decode(encoding, errors='ignore')
    #
    #         # Split lines for stdout and stderr
    #         stdout_lines = stdout_text.splitlines()
    #         stderr_lines = stderr_text.splitlines()
    #
    #         process.wait()  # 프로세스가 끝날 때까지 기다리기
    #         for line in stdout_lines:
    #             BusinessLogicUtil.print_light_black(line)
    #         for line in stderr_lines:
    #             BusinessLogicUtil.print_red(line)
    #         return stdout_lines
    #     except:
    #         if show_mode == True:
    #             BusinessLogicUtil.print_light_black(string=rf'''"{traceback.format_exc()}" %%%FOO%%%''')
    #         pass

    @staticmethod
    def command_to_os(cmd: str, show_mode=True, mode=""):
        # 인코딩 문제가 좀처럼 해결이 안되서 만든 방법,
        # 별 문제 없으면 command_run() 을 command_to_os() 로 대체
        function_name = inspect.currentframe().f_code.co_name
        if show_mode == True:
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.print_as_log(string=rf'''command="{cmd}" %%%FOO%%%''')
            if mode == "a":
                BusinessLogicUtil.print_as_log(string=rf'''mode="{mode}" %%%FOO%%%''')
        try:
            if mode == "a": # async
                subprocess.Popen(cmd, shell=True, encoding='utf-8')
                # subprocess.Popen(command, shell=True, universal_newlines=True)
                return
            else: # 동기처리
                stdout_lines = []

                # 클립보드 백업
                clipboard_current_contents = clipboard.paste()

                # os.system(rf"{command} | clip")

                # with subprocess.Popen(rf"{command} | clip", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True, encoding='utf-8') as proc:
                #     stdout, stderr = proc.communicate()  # stdout과 stderr 캡처
                #     if show_mode == True:
                #         if stdout:
                #             # 출력 처리 (바이너리로 읽고, 유니코드로 변환)
                #             print("stdout:", stdout)
                #         if stderr:
                #             print("stderr:", stderr)
                #     proc.wait()

                with subprocess.Popen(rf"{cmd} | clip", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) as proc:
                    stdout, stderr = proc.communicate()  # 클립보드 필요 없이 시도해불 수 있겠음.
                    if show_mode == True:
                        if stdout:
                            # 출력 처리 (바이너리로 읽고, 유니코드로 변환)
                            # stdout = stdout.decode('utf-8', errors='replace')
                            stdout = stdout.decode('cp949', errors='replace')
                            # stdout = stdout.decode('euc-kr', errors='replace')
                            BusinessLogicUtil.print_as_log(string=rf'''stdout="{stdout}" %%%FOO%%%''')
                        if stderr:
                            # stderr = stderr.decode('utf-8', errors='replace')
                            stderr = stderr.decode('cp949', errors='replace')
                            # stderr = stderr.decode('euc-kr', errors='replace')
                            stderr = stderr.replace('\n', '___')
                            BusinessLogicUtil.print_as_log(string=rf'''stderr="{stderr}" %%%FOO%%%''')
                    proc.wait()

                strings = clipboard.paste()

                stdout_list = strings.splitlines()

                # 클립보드 복원
                clipboard.copy(clipboard_current_contents)

                if show_mode == True:
                    for stdout_line in stdout_list:
                        BusinessLogicUtil.print_light_black(stdout_line)

                return stdout_list
                # return strings
        except:
            BusinessLogicUtil.print_light_black(string=rf'''"{traceback.format_exc()}" %%%FOO%%%''')

    @staticmethod
    def get_found_pnxs_interested_from_text_file(including_texts=[], exclude_texts=[], except_extensions=[], including_extensions=[]):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        return BusinessLogicUtil.find_pnxs_interested_from_text_file_x(including_texts=including_texts, exclude_texts=exclude_texts, except_extensions=except_extensions, including_extensions=including_extensions)

    @staticmethod
    def get_list_sorted_element(item_list, mode="asc"):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        """
         주어진 리스트를 오름차순 또는 내림차순으로 정렬하여 반환하는 함수.

         :param input_list: 정렬할 리스트
         :param mode: 정렬 순서. "asc"는 오름차순, "desc"는 내림차순 (기본값은 "asc")
         :return: 정렬된 리스트
         """
        if mode == "asc":
            return sorted(item_list)  # 오름차순 정렬
        elif mode == "desc":
            return sorted(item_list, reverse=True)  # 내림차순 정렬
        else:
            raise ValueError("Invalid order. Use 'asc' or 'desc'.")

    @staticmethod
    def get_list_replaced_element_from_pattern_to_patternless(items, pattern):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        return [re.sub(pattern, "", item) for item in items]

    @staticmethod
    def get_str_replaced_from_pattern_to_patternless(string, pattern):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        return re.sub(pattern, "", string)

    @staticmethod
    def get_two_list_splited_pattern_and_patternless(items, pattern):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        pnx_list_required_pattern = []
        pnx_list_required_patternless = []

        for item in items:
            match = re.match(pattern, item)  # 정규식에 맞는 부분 찾기
            if match:
                pnx_list_required_pattern.append(match.group(1))  # magnet 부분
                pnx_list_required_patternless.append(match.group(2))  # 파일명 부분

        return pnx_list_required_pattern, pnx_list_required_patternless

    @staticmethod
    def here():
        # 이 함수는 1개의 호출만 허용
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.print_cyan("Here!")
        BusinessLogicUtil.pause()  # todo 필요하면 주석

    @staticmethod
    def get_hostname():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        lines = BusinessLogicUtil.command_to_os_like_person_as_admin('hostname')
        for line in lines:
            line = line.strip()
            return line

    @staticmethod
    def flash_jetson_nano():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        # wsl_linux_version= "Ubuntu-18.04"
        wsl_linux_version = "Ubuntu-22.04"
        # wsl_linux_version= "Ubuntu-24.04"
        linux_pw = BusinessLogicUtil.get_token_from_text_file(token_file=rf'{StateManagementUtil.PKG_TXT}\token_linux_pw.txt', initial_token="")
        linux_id = BusinessLogicUtil.get_token_from_text_file(token_file=rf'{StateManagementUtil.PKG_TXT}\token_linux_id.txt', initial_token="")
        wsl_working_directory = BusinessLogicUtil.get_working_directory()
        wsl_windows_title_seg = f"{linux_id}@{StateManagementUtil.HOSTNAME}"

        # windows_title_seg = rf"관리자: C:\WINDOWS\system32\cmd.exe"
        # command = rf"wsl -d {wsl_linux_version} lsusb"
        # BusinessLogicUtil.command_run_via_cmd(window_title_seg=windows_title_seg, command=command)

    @staticmethod
    def set_up_jetson_nano_dev_environment():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # winget # fail # windows 11 부터 시도해보자. 10 지원 끝난듯.
        # winget 윈도우에서 마소 공식 패키지 매니저
        # winget --version
        # winget search Google Chrome
        # winget install Google.Chrome --silent
        # winget install Microsoft.VisualStudio --silent

        # choco # fail
        # console_title = "choco install"
        # BusinessLogicUtil.run_powershell_as_admin()
        # BusinessLogicUtil.write_like_person(string=rf"$host.ui.RawUI.WindowTitle = '{console_title}'  ", interval=0.005)
        # BusinessLogicUtil.press("enter")
        # BusinessLogicUtil.write_like_person(string=rf"$Host.UI.RawUI.BufferSize = New-Object Management.Automation.Host.Size(1000, 1000) ", interval=0.005)
        # BusinessLogicUtil.press("enter")
        # BusinessLogicUtil.write_like_person(string=rf"$Host.UI.RawUI.WindowSize = New-Object Management.Automation.Host.Size(1000, 1000)  ", interval=0.005)
        # BusinessLogicUtil.press("enter")
        # BusinessLogicUtil.write_like_person(string=rf" Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.SecurityProtocolType]::Tls12; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1')) ", interval=0.005)
        # BusinessLogicUtil.press("enter")
        # choco search usbipd-win
        # choco list #설치된 패키지 확인

        # usbipd
        # BusinessLogicUtil.chdir(pnx = StateManagementUtil.DOWNLOADS)
        # BusinessLogicUtil.write_like_person(string=rf"  choco install usbpid-win --silent ", interval=0.005)
        # BusinessLogicUtil.press("enter")
        # command=rf'curl -O "https://github.com/dorssel/usbipd-win/releases/download/v4.3.0/usbipd-win_4.3.0.msi" ' #fail 왜안되나 손으로 클릭하면 되는데
        # command=rf'explorer "https://github.com/dorssel/usbipd-win/releases/tag/v4.3.0" '
        # BusinessLogicUtil.command_run(command=command, show_mode=False)
        # BusinessLogicUtil.sleep(milliseconds=1200)
        # BusinessLogicUtil.click_text_coordinates_via_easy_ocr(string = "usbipd-win_4.3.0.msi")
        # command=rf'explorer "{StateManagementUtil.DOWNLOADS}\usbipd-win_4.3.0.msi" '
        # BusinessLogicUtil.command_run(command=command, show_mode=False)

        pass

    @staticmethod
    def print_windows_opened():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.print_list_as_vertical(items_list=BusinessLogicUtil.get_windows_opened(), items_list_name="windows_opened")
        BusinessLogicUtil.pause()

    @staticmethod
    def chdir(dst):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        os.chdir(path=dst)
        BusinessLogicUtil.print_as_log(string=rf'''pnx="{dst}" %%%FOO%%%''')

    @staticmethod
    # def does_text_bounding_box_exist_via_easy_ocr(string, mode="one_click"):  # GPU 없으면 동작안함
    def does_text_bounding_box_exist_via_easy_ocr(string):  # GPU 없으면 동작안함
        text_coordinates = BusinessLogicUtil.get_text_coordinates_via_easy_ocr(string=string)
        if not text_coordinates:
            print(rf"[not found] {string}")
            return False
        x_abs, y_abs = text_coordinates
        BusinessLogicUtil.print_as_log(string=rf'''x_abs="{x_abs}" %%%FOO%%%''')
        BusinessLogicUtil.print_as_log(string=rf'''y_abs="{y_abs}" %%%FOO%%%''')
        BusinessLogicUtil.move_mouse(x_abs=x_abs, y_abs=y_abs)
        return True

    @staticmethod
    def flash_evm_without_flash_image():
        wsl_linux_version = "Ubuntu-18.04"
        # wsl_linux_version = "Ubuntu-22.04"  # todo 집에서 테스트 시에만 사용
        linux_id = BusinessLogicUtil.get_token_from_text_file(token_file=rf'{StateManagementUtil.PKG_TXT}\token_linux_id.txt', initial_token="")
        linux_pw = BusinessLogicUtil.get_token_from_text_file(token_file=rf'{StateManagementUtil.PKG_TXT}\token_linux_pw.txt', initial_token="")
        wsl_working_directory = BusinessLogicUtil.get_working_directory()
        wsl_windows_title_seg = f"{linux_id}@{StateManagementUtil.HOSTNAME}"

        # wsl install check
        if BusinessLogicUtil.is_wsl_linux_installed(wsl_linux_version=wsl_linux_version) == False:
            return

        # wsl usb connection attach
        if BusinessLogicUtil.attach_wsl_usb_connection(wsl_linux_version=wsl_linux_version) == False:
            return

        # usb/ip
        wsl_command = rf"lsusb | xclip -sel clip"
        std_out_stream_lsusb = BusinessLogicUtil.run_command_run_via_wsl_exe(wsl_command=wsl_command, wsl_linux_version=wsl_linux_version, wsl_window_title_seg=wsl_windows_title_seg)
        BusinessLogicUtil.print_as_log(string=rf'''std_out_stream_lsusb="{std_out_stream_lsusb}" %%%FOO%%%''')

        # unique_str_positive = "~~~~~"
        # unique_str_negative = "제공된 이름의 배포가 없습니다"
        # BusinessLogicUtil.print_as_log(string=rf'''unique_str_negative="{unique_str_negative}" %%%FOO%%%''')
        # for line in lines:
        #     if unique_str_negative in line:
        #         BusinessLogicUtil.print_as_log(string=f'''"{unique_str_negative}"''', print_color="red")
        #         return

        # wsl/linux/flash
        # wsl_command = rf"sdkmanager --archived~~~~"
        # BusinessLogicUtil.command_run_via_wsl(wsl_command=wsl_command, wsl_linux_version=wsl_linux_version, window_title_seg=wsl_windows_title_seg)

        # run release server
        # BusinessLogicUtil.run_park4139_release_server(port=9090)
        pass

    @staticmethod
    def flash_evm_with_flash_image():
        # wsl_linux_version = "Ubuntu-18.04"
        wsl_linux_version = "Ubuntu-22.04"  # todo 집에서 테스트 시에만 사용
        linux_pw = BusinessLogicUtil.get_token_from_text_file(token_file=rf'{StateManagementUtil.PKG_TXT}\token_linux_pw.txt', initial_token="")
        linux_id = BusinessLogicUtil.get_token_from_text_file(token_file=rf'{StateManagementUtil.PKG_TXT}\token_linux_id.txt', initial_token="")
        wsl_working_directory = BusinessLogicUtil.get_working_directory()
        wsl_windows_title_seg = f"{linux_id}@{StateManagementUtil.HOSTNAME}"
        # ___________________________________________________________________________ wsl install check
        # if BusinessLogicUtil.is_wsl_linux_installed(wsl_linux_version=wsl_linux_version) == False:
        #     return
        # ___________________________________________________________________________ wsl usb connection attach
        # BusinessLogicUtil.attach_wsl_usb_connection(wsl_linux_version=wsl_linux_version)
        # ___________________________________________________________________________ usb/ip
        # wsl_command = rf"lsusb | xclip -sel clip"
        # std_out_stream_lsusb = BusinessLogicUtil.command_run_via_wsl(wsl_command=wsl_command, wsl_linux_version=wsl_linux_version, window_title_seg=wsl_windows_title_seg)
        # BusinessLogicUtil.print_as_log(string = rf'''std_out_stream_lsusb="{std_out_stream_lsusb}" %%%FOO%%%''')

        # # unique_str_positive = "~~~~~"
        # unique_str_negative = "제공된 이름의 배포가 없습니다"
        # BusinessLogicUtil.print_as_log(string=rf'''unique_str_negative="{unique_str_negative}" %%%FOO%%%''')
        # for line in lines:
        #     if unique_str_negative in line:
        #         BusinessLogicUtil.print_as_log(string=f'''"{unique_str_negative}"''', print_color="red")
        #         return
        # ___________________________________________________________________________ wsl/linux 경로이동
        # wsl_linux_pnx = "~/Downloads/flash/xc_flash/Linux_for_Tegra/"
        # wsl_command = rf"cd {wsl_linux_pnx} & pwd | xclip -sel clip"
        # wsl_working_directory = BusinessLogicUtil.command_run_via_wsl(wsl_command=wsl_command, wsl_linux_version=wsl_linux_version, window_title_seg=wsl_windows_title_seg)
        # BusinessLogicUtil.print_as_log(string = rf'''wsl_working_directory="{wsl_working_directory}" %%%FOO%%%''')
        # if wsl_working_directory != wsl_linux_pnx:
        #     BusinessLogicUtil.print_as_log(f'''"{wsl_linux_pnx} 경로가 없습니다."''', print_color="red")
        #     return
        # ___________________________________________________________________________ wsl/linux/flash
        # wsl_command = rf"sudo ./flash.sh -r jetson-xavier mmcblk0p1" # windows 10에서 실패
        # BusinessLogicUtil.command_run_via_wsl(wsl_command=wsl_command, wsl_linux_version=wsl_linux_version, window_title_seg=wsl_windows_title_seg)
        # BusinessLogicUtil.is_front_window_title(window_title_seg=wsl_windows_title_seg)
        # BusinessLogicUtil.press("enter")
        # BusinessLogicUtil.write_like_person(string=rf"{linux_pw}\n", interval=0.1)
        # BusinessLogicUtil.sleep(milliseconds=1000)
        # BusinessLogicUtil.copy_and_paste_with_keeping_clipboard(string= f"{linux_pw}\n", mode='wsl')
        # BusinessLogicUtil.press("enter")

        # wsl_command = rf"echo {linux_pw} | sudo -S ./flash.sh -r jetson-xavier mmcblk0p1" # 성공
        # BusinessLogicUtil.command_run_via_wsl(wsl_command=wsl_command, wsl_linux_version=wsl_linux_version, window_title_seg=wsl_windows_title_seg)
        # # ___________________________________________________________________________ run release server
        # BusinessLogicUtil.run_park4139_release_server(port=9090)
        pass

    @staticmethod
    def flash_xc_with_flash_image():
        wsl_linux_version = "Ubuntu-18.04"
        linux_pw = BusinessLogicUtil.get_token_from_text_file(token_file=rf'{StateManagementUtil.PKG_TXT}\token_linux_pw.txt', initial_token="")
        linux_id = BusinessLogicUtil.get_token_from_text_file(token_file=rf'{StateManagementUtil.PKG_TXT}\token_linux_id.txt', initial_token="")
        wsl_working_directory = BusinessLogicUtil.get_working_directory()
        wsl_window_title_seg = f"{linux_id}@{StateManagementUtil.HOSTNAME}"
        exit_mode = False

        # wsl install check
        # if BusinessLogicUtil.is_wsl_linux_installed(wsl_linux_version=wsl_linux_version) == False:
        #     return

        # wsl usb connection attach
        if BusinessLogicUtil.attach_wsl_usb_connection(wsl_linux_version=wsl_linux_version) == False:
            return

        # usb/ip
        command = rf"wsl lsusb"
        lines = BusinessLogicUtil.command_to_os(command)
        # unique_str_positive = "~~~~~"
        str_negative = "제공된 이름의 배포가 없습니다"
        BusinessLogicUtil.print_as_log(string=rf'''str_negative="{str_negative}" %%%FOO%%%''')
        for line in lines:
            if str_negative in line:
                BusinessLogicUtil.print_as_log(string=f'''"{str_negative}"''', print_color="red")
                return

        # 경로이동
        wsl_command = f'cd ~/Downloads/flash/xc_flash/'
        BusinessLogicUtil.run_command_run_via_wsl_exe(wsl_command=wsl_command, wsl_linux_version=wsl_linux_version, wsl_window_title_seg=wsl_window_title_seg, exit_mode=exit_mode)

        # wsl_linux_pnx = "~/Downloads/flash/xc_flash/Linux_for_Tegra/"
        # wsl_command = rf"cd {wsl_linux_pnx} & pwd | xclip -sel clip"
        # wsl_working_directory = BusinessLogicUtil.command_run_via_wsl(wsl_command=wsl_command, wsl_linux_version=wsl_linux_version, window_title_seg=wsl_window_title_seg)
        # BusinessLogicUtil.print_as_log(string = rf'''wsl_working_directory="{wsl_working_directory}" %%%FOO%%%''')
        # if wsl_working_directory != wsl_linux_pnx:
        #     BusinessLogicUtil.print_as_log(f'''"{wsl_linux_pnx} 경로가 없습니다."''', print_color="red")
        #     return
        # ___________________________________________________________________________ wsl/linux/flash
        # wsl_command = rf"sudo ./flash.sh -r jetson-xavier mmcblk0p1" # windows 10에서 실패
        # BusinessLogicUtil.command_run_via_wsl(wsl_command=wsl_command, wsl_linux_version=wsl_linux_version, window_title_seg=wsl_window_title_seg)
        # BusinessLogicUtil.is_front_window_title(window_title_seg=wsl_window_title_seg)
        # BusinessLogicUtil.press("enter")
        # BusinessLogicUtil.write_like_person(string=rf"{linux_pw}\n", interval=0.1)
        # BusinessLogicUtil.sleep(milliseconds=1000)
        # BusinessLogicUtil.copy_and_paste_with_keeping_clipboard(string= f"{linux_pw}\n", mode='wsl')
        # BusinessLogicUtil.press("enter")

        # wsl_command = rf"echo {linux_pw} | sudo -S ./flash.sh -r jetson-xavier mmcblk0p1" # 성공
        # BusinessLogicUtil.command_run_via_wsl(wsl_command=wsl_command, wsl_linux_version=wsl_linux_version, window_title_seg=wsl_window_title_seg)
        # # ___________________________________________________________________________ run release server
        # BusinessLogicUtil.run_park4139_release_server(port=9090)
        pass

    @staticmethod
    def attach_wsl_usb_connection(wsl_linux_version=None):
        # install usbipd
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        cmd = "usbipd list"
        lines = BusinessLogicUtil.command_to_os(cmd=cmd, show_mode=False)
        bus_id = None
        # string_positive = ["APX", "Attached" or "Shared"]
        string_positive = ["APX"]
        pattern = re.compile(r"\d+-\d")  # "2-3 패턴" # 2-12 는 안될듯 업데이트 필요
        BusinessLogicUtil.print_list_as_vertical(items_list=lines, items_list_name='lines')
        for line in lines:
            if all(text in line for text in string_positive):
                match = pattern.search(line)
                if not match:
                    BusinessLogicUtil.print_as_log(f'''"{string_positive}가 없습니다. %%%FOO%%%"''', print_color="red")
                    return False
                BusinessLogicUtil.print_as_log(string=rf'''match="{match}" %%%FOO%%%''')
                bus_id = match.group()
        if bus_id is None:
            BusinessLogicUtil.print_as_log(f'''"bus_id 가 None 입니다. %%%FOO%%% "''', print_color="red")
            return False
        BusinessLogicUtil.print_as_log(string=rf'''bus_id="{bus_id}" %%%FOO%%%''', print_color="green")

        cmd = "wsl --shutdown"
        BusinessLogicUtil.command_to_os(cmd=cmd)

        cmd = rf"wsl -d {wsl_linux_version} -- exit"
        # str_negative = "제공된 이름의 배포가 없습니다" or 'xxxx'
        lines = BusinessLogicUtil.command_to_os(cmd=cmd)
        if BusinessLogicUtil.check_str_negative_in_loop(timeout=10, items_list=lines, str_negative="제공된 이름의 배포가 없습니다", ment_negative=rf"'{cmd}' 할수없었습니다") == True:
            return

        cmd = "wsl -l -v"
        BusinessLogicUtil.command_to_os(cmd=cmd)

        cmd = rf"usbipd unbind -b {bus_id}"
        BusinessLogicUtil.command_to_os(cmd=cmd)

        cmd = rf"usbipd bind -b {bus_id}"
        BusinessLogicUtil.command_to_os(cmd=cmd)

        cmd = rf"usbipd attach --wsl --busid {bus_id} --auto-attach"
        BusinessLogicUtil.command_to_os_like_person(command=cmd)

        # usb/ip
        # str_negative = "제공된 이름의 배포가 없습니다" or 'xxxx'
        command = rf"wsl lsusb"
        lines = BusinessLogicUtil.command_to_os(command)
        if BusinessLogicUtil.check_str_negative_in_loop(timeout=10, items_list=lines, str_negative="제공된 이름의 배포가 없습니다", ment_negative="wsl 에 attach 할수없었습니다") == True:
            return
        if BusinessLogicUtil.check_str_positive_in_loop(timeout=10, items_list=lines, str_positive="NVidia Corp.", ment_positive="wsl 에 attach 되었습니다") == False:
            return

    @staticmethod
    def make_directory_with_timestamp_via_user_input():
        import inspect
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            work_name = None
            pnx = None

            # 첫 번째 입력: 업무용 타임스템프 파일을 만들 것인지 묻는 메시지
            dialog_btn_text_clicked = input("업무용 타임스템프 파일을 만들까요? (y/n): ")
            if dialog_btn_text_clicked != "y":
                return

            # 두 번째 입력: 업무명 입력
            dialog_input_box_text = input("업무명을 입력해주세요: ")
            work_name = dialog_input_box_text.strip()
            work_name = work_name.replace("\"", "")
            BusinessLogicUtil.print_light_black(
                f'''[{BusinessLogicUtil.get_time_as_('now')}] work_names={work_name} %%%FOO%%%''')
            if work_name == "":
                BusinessLogicUtil.print_light_black(
                    f'''[{BusinessLogicUtil.get_time_as_('now')}] work_name가 입력되지 않았습니다 %%%FOO%%%''')
                return

            # 세 번째 입력: 경로 입력
            dialog_input_box_text = input("어느 경로에 만들까요?: ")
            pnx = dialog_input_box_text.strip()
            pnx = BusinessLogicUtil.get_pnx_preprocessed(pnx)
            if BusinessLogicUtil.is_pnx_required(pnx):
                return
            BusinessLogicUtil.print_as_log(string=rf'''pnx="{pnx}" %%%FOO%%%''')
            BusinessLogicUtil.print_as_log(string=rf'''work_name="{work_name}" %%%FOO%%%''')

            # 타임스템프 생성
            timestamp = BusinessLogicUtil.get_time_as_("yyyy MM dd (weekday) HH mm")
            pnx_new = rf"{pnx}\{timestamp} {work_name}"
            BusinessLogicUtil.print_as_log(string=rf'''pnx_new="{pnx_new}" %%%FOO%%%''')

            # 디렉토리 생성 및 파일 탐색기 열기
            BusinessLogicUtil.make_pnx(pnx=rf'{pnx_new}', mode="d")
            BusinessLogicUtil.command_to_os(cmd=pnx_new, show_mode=False, mode="a")
            return
        except Exception as e:
            BusinessLogicUtil.print_light_black(f"Error: {str(e)}")

    @staticmethod
    def is_pnx_required(pnx):
        BusinessLogicUtil.print_as_log(f'''pnx={pnx} %%%FOO%%%''')
        if pnx == "":
            BusinessLogicUtil.print_as_log(f'''pnx가 입력되지 않았습니다 %%%FOO%%%''')
            return True
        connected_drives = []
        for drive_letter in string.ascii_uppercase:
            drive_path = drive_letter + ":\\"
            if os.path.exists(drive_path):
                connected_drives.append(drive_path)
                if pnx == drive_path:
                    BusinessLogicUtil.print_as_log(f'''입력된 pnx는 너무 광범위하여 진행할 수 없도록 설정되어 있습니다 %%%FOO%%%''')
                    return True
        if not os.path.exists(pnx):
            BusinessLogicUtil.print_as_log(f'''입력된 pnx가 존재하지 않습니다 %%%FOO%%%''')
            return True

    @staticmethod
    def print_and_open_original_log_position(vehicle_id, area_id, steering_date, course_id):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{function_name}() %%%FOO%%%''', print_color='blue')
        data_required = {}
        data_required["차량"] = vehicle_id
        data_required["지역"] = area_id
        data_required["주행일자"] = steering_date
        data_required["코스"] = course_id

        def get_origin_log_file_name(issue_file_name):
            # 정규식 패턴 정의: "_숫자(최대 2자리)_VIDEO"
            pattern = r"_\d{1,2}_VIDEO"
            original_filename = re.sub(pattern, "", issue_file_name)
            return original_filename

        # 정의
        original_log_position = rf"\\192.168.1.33\02_Orignal\{data_required["차량"]}\{data_required["지역"]}\{data_required["주행일자"]}\{data_required["코스"]}"
        BusinessLogicUtil.print_as_log(string=rf'''original_log_position="{original_log_position}" %%%FOO%%%''', print_color='blue')
        command = rf'explorer "{original_log_position}" '
        BusinessLogicUtil.command_to_os(cmd=command)
        return original_log_position

    @staticmethod
    def start_to_analize_add_up_issue():
        # 애드업이슈 검색

        # 애드업이슈 csv 다운로드

        # BusinessLogicUtil.print_and_open_original_log_position(vehicle_id='63_SEJONG_APOLLO_900_4', area_id='09_Sejong', steering_date='241204', course_id='05_BRT_Osong')

        # 필요데이터
        data_required = BusinessLogicUtil.get_data_required_from_f_csv(line_order=1)

        # 이슈로그.dat 다운로드
        BusinessLogicUtil.download_issue_data(data_required=data_required)

        # BusinessLogicUtil.quit_autoa2z_drive()

        BusinessLogicUtil.run_acu_update_v3_exe_and_login_and_run_autoa2zdrive_release_exe(data_required=data_required)

        BusinessLogicUtil.run_autoa2z_drive()

        # 애드업 이슈 분석 및 조치 보고용 텍스트 수집 및 가공
        # data_for_report = BusinessLogicUtil.get_data_required_from_xls(line_order=2)
        # 애드업 이슈 분석 및 조치 보고
        #     "파일명": "파일명",
        #     "차량": "차량",
        #     "지역": "지역",
        #     "코스": "코스",
        #     "SW 버전": "SW 버전",
        #     "운전자": "운전자",
        #     "로그 분석자": "로그 분석자",
        #     "프레임": "프레임",
        #     "문제점 상세": "문제점 상세",
        #     "Crew 요청사항": "Crew 요청사항",
        # df.head(10).to_csv("output.csv", index=False)  # 결과를 CSV 파일로 저장
        # explorer output.csv
        # 몇 행부터 몇 행까지 선택
        # ctrl c

        # 애드업이슈 csv 출력(비엑셀 스타일)
        # df = BusinessLogicUtil.get_df_from_issues_list_csv()
        # columns_required = df.columns.tolist()
        # columns_required = ["주행일자", "문제점 상세", "파일 위치", "파일명", "SW 버전", "지역", "코스", "차량"]
        # columns_required = ["파일명", "차량", "지역", "코스", "SW 버전", "운전자", "로그 분석자", "프레임", "문제점 상세", "Crew 요청사항"]
        # for line_order in range(0, len(df)):
        #     BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}line_order="{line_order}" %%%FOO%%%''')
        #     if df.empty:
        #         print("데이터프레임이 비어 있습니다.")
        #         return
        #     else:
        #         row = df.iloc[line_order]
        #         for col in columns_required:
        #             if col in df.columns:  # 열이 존재하는 경우만 출력
        #                 print(f"{col}: {row[col]}")
        #             else:
        #                 print(f"{col}: N/A(데이터없음)")  # 열이 없는 경우 기본값 출력
        # BusinessLogicUtil.print_as_log(string=rf'''엑셀 내의 데이터의 개수(헤더제외)="{len(df) - 1}" %%%FOO%%%''')
        # BusinessLogicUtil.pause()
        # 파일 위치 또는 파일명으로 로 콘솔에서 검색

        # 애드업이슈 csv 출력(엑셀 스타일)
        # df = BusinessLogicUtil.get_df_from_issues_list_csv()
        # columns_required = df.columns.tolist()
        # if not df.empty:
        #     # 열 순서를 재조정 (columns_required 기준으로 출력)
        #     df_to_display = df[columns_required] if all(col in df.columns for col in columns_required) else df
        #
        #     # 데이터프레임을 표 형태로 출력
        #     print(df_to_display.to_string(index=False))  # `index=False`로 인덱스 제거
        # else:
        #     print("데이터프레임이 비어 있습니다.")
        #     return
        # BusinessLogicUtil.print_as_log(string=rf'''엑셀 내의 데이터의 개수(헤더제외)="{len(df) - 1}" %%%FOO%%%''')
        # BusinessLogicUtil.pause()

        # 엑셀이 없다면
        # 애드업이슈 csv 출력(엑셀 스타일) via PrettyTable
        # df = BusinessLogicUtil.get_df_from_issues_list_csv()
        # columns_required = df.columns.tolist()
        # if df.empty:
        #     print("데이터프레임이 비어 있습니다.")
        #     return
        # else:
        #     table = PrettyTable()
        #     table.field_names = columns_required  # 필수 열 제목 설정
        #
        #     for _, row in df.iterrows():
        #         table.add_row([row.get(col, "N/A") for col in columns_required])
        #     print(table)
        # BusinessLogicUtil.print_as_log(string=rf'''엑셀 내의 데이터의 개수(헤더제외)="{len(df) - 1}" %%%FOO%%%''')
        # BusinessLogicUtil.pause()

        # 엑셀이 없다면
        # 애드업이슈 csv 출력(엑셀 스타일) via tubulate
        # df = BusinessLogicUtil.get_df_from_issues_list_csv()
        # columns_required = df.columns.tolist()
        # if df.empty:
        #     print("데이터프레임이 비어 있습니다.")
        #     return
        # else:
        #     # 필수 열만 출력, 누락된 열은 기본값으로 추가
        #     df_to_display = df[columns_required] if all(col in df.columns for col in columns_required) else df
        #     # 표로 출력
        #     table = tabulate(df_to_display, headers='keys', tablefmt='grid', showindex=True)
        #     print(table)
        # BusinessLogicUtil.print_as_log(string=rf'''엑셀 내의 데이터의 개수(헤더제외)="{len(df) - 1}" %%%FOO%%%''')
        # BusinessLogicUtil.pause()

        # 엑셀이 있다면
        # 이럴바에 엑셀로 여는게 나은 것 같은데,

    @staticmethod
    def get_df_from_issues_list_csv():
        # 경로
        Downloads = rf"{StateManagementUtil.USERPROFILE}/Downloads"
        issues_list_csv = rf"{StateManagementUtil.USERPROFILE}/Downloads/Issues_list.csv"
        issues_list_csv_alternative = rf"{StateManagementUtil.USERPROFILE}/Downloads/deprecated/Issues_list.csv"

        df = None
        pnx = issues_list_csv
        if BusinessLogicUtil.does_pnx_exist(pnx):
            df = pd.read_csv(filepath_or_buffer=pnx)
        else:
            pnx = issues_list_csv_alternative
            if BusinessLogicUtil.does_pnx_exist(pnx):
                df = pd.read_csv(filepath_or_buffer=pnx)
        BusinessLogicUtil.move_pnx_with_overwrite(src=pnx, dst=Downloads)
        return df

    @staticmethod
    def get_nth_row(df, n):
        # n번째 줄만 가져오기
        if n >= 0 and n <= len(df):
            return df.iloc[n]  # n번째 행
        else:
            print("유효하지 않은 행 번호입니다.")
            return None

    @staticmethod
    def make_directory_with_timestamp(work_name, dst):
        import inspect
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            # 두 번째 입력: 업무명 입력
            work_name = work_name.strip()
            work_name = work_name.replace("\"", "")
            BusinessLogicUtil.print_light_black(
                f'''[{BusinessLogicUtil.get_time_as_('now')}] work_names={work_name} %%%FOO%%%''')
            if work_name == "":
                BusinessLogicUtil.print_light_black(
                    f'''[{BusinessLogicUtil.get_time_as_('now')}] work_name가 입력되지 않았습니다 %%%FOO%%%''')
                return

            # 세 번째 입력: 경로 입력
            dst = dst.strip()
            dst = BusinessLogicUtil.get_pnx_preprocessed(dst)
            if BusinessLogicUtil.is_pnx_required(dst):
                return
            BusinessLogicUtil.print_as_log(string=rf'''work_name="{work_name}" %%%FOO%%%''')

            # 타임스템프 생성
            timestamp = BusinessLogicUtil.get_time_as_("yyyy MM dd (weekday) HH mm")
            pnx_new = rf"{dst}\{timestamp} {work_name}"
            pnx_new = BusinessLogicUtil.get_pnx_preprocessed(pnx_new)
            BusinessLogicUtil.print_as_log(string=rf'''pnx_new="{pnx_new}" %%%FOO%%%''')

            # 디렉토리 생성 및 파일 탐색기 열기 # todo
            BusinessLogicUtil.make_pnx(pnx=pnx_new, mode="d")
            command = rf'explorer "{pnx_new}"'
            BusinessLogicUtil.print_as_log(string=rf'''command="{command}" %%%FOO%%%''')
            # BusinessLogicUtil.command_run(command=command, show_mode=False)
            # BusinessLogicUtil.print_list_as_vertical(BusinessLogicUtil.get_windows_opened(), items_name="BusinessLogicUtil.get_windows_opened()")

            return
        except Exception as e:
            BusinessLogicUtil.print_light_black(f"Error: {str(e)}")

    @staticmethod
    def should_i_make_directory_for_a2z_with_timestamp_as_gui_v2():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            work_name = None
            pnx = None
            dialog_btn_text_clicked = None
            function = None
            dialog_input_box_text = None

            # dialog_btn_text_clicked, function, dialog_input_box_text = BusinessLogicUtil.should_i_do(
            #     ment="업무용 타임스템프 파일을 만들까요?",
            #     btns=["y", "n"],
            #     function=None,
            #     auto_click_negative_btn_after_seconds=30,
            #     title=f"{function_name}()",
            #     return_mode=True,
            #     input_box_mode=True,
            # )
            # if dialog_btn_text_clicked != "y":
            #     return

            dialog_btn_text_clicked, function, dialog_input_box_text = BusinessLogicUtil.should_i_do(
                string="업무명을 입력해주세요",
                btns=["입력", "n"],
                function=None,
                auto_click_negative_btn_after_seconds=30,
                title=f"{function_name}()",
                return_mode=True,
                input_box_mode=True,
            )
            if dialog_btn_text_clicked != "입력":
                return
            work_name = dialog_input_box_text
            work_name = work_name.strip()
            work_name = work_name.replace("\"", "")
            BusinessLogicUtil.print_light_black(
                f'''[{BusinessLogicUtil.get_time_as_('now')}] work_names={work_name} %%%FOO%%%''')
            if work_name == "":
                BusinessLogicUtil.print_light_black(
                    f'''[{BusinessLogicUtil.get_time_as_('now')}] work_name가 입력되지 않았습니다 %%%FOO%%%''')
                return

            dialog_btn_text_clicked, function, dialog_input_box_text = BusinessLogicUtil.should_i_do(
                string="어느 경로에 만들까요?",
                btns=["입력", "n"],
                function=None,
                auto_click_negative_btn_after_seconds=30,
                title=f"{function_name}()",
                return_mode=True,
                input_box_mode=True,
            )
            if dialog_btn_text_clicked != "입력":
                return
            pnx = dialog_input_box_text
            pnx = BusinessLogicUtil.get_pnx_preprocessed(pnx)
            if BusinessLogicUtil.is_pnx_required(pnx):
                return
            BusinessLogicUtil.print_as_log(string=rf'''pnx="{pnx}" %%%FOO%%%''')
            BusinessLogicUtil.print_as_log(string=rf'''work_name="{work_name}" %%%FOO%%%''')
            timestamp = BusinessLogicUtil.get_time_as_("yyyy MM dd (weekday) HH mm")
            pnx_new = rf"{pnx}\{timestamp} {work_name}"
            BusinessLogicUtil.print_as_log(string=rf'''pnx_new="{pnx_new}" %%%FOO%%%''')
            BusinessLogicUtil.make_pnx(pnx=pnx_new, mode="d")
            pnx = pnx_new
            command = rf'explorer "{pnx}"'
            BusinessLogicUtil.command_to_os(cmd=command, show_mode=False, mode="a")
            return
        except:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

    @staticmethod
    def send_pkg_to_house_to_park4139_release_server():  # todo 내용이 함수명 동기화 필요
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        # # 업로드
        # # fastapi + http server
        # # command = f'curl -X POST "https://api.telegram.org/bot{token}/sendDocument" -d "chat_id={chat_id}&document=@{pkg_to_house_zip}"'
        # # BusinessLogicUtil.command_to_os(command=command)
        # token_gitlab_repo_url = BusinessLogicUtil.get_token_from_text_file(token_file=rf'{StateManagementUtil.PKG_TXT}\token_gitlab_repo_url.txt', initial_token="")
        # # commit_ment = "test:initial git push test"
        # commit_ment = "feat:add functions to work automatically"
        # pnx = rf"{StateManagementUtil.PROJECT_DIRECTORY}\park4139.py"
        # BusinessLogicUtil.upload_pnx_to_git(git_repository_url=token_gitlab_repo_url, commit_msg=commit_ment, pnx=pnx)
        #
        # # 삭제
        # BusinessLogicUtil.sleep(milliseconds=250)  # (필수)
        # pnxs = [pkg_to_house, pkg_to_house_tar]
        # BusinessLogicUtil.move_pnxs_to_trash_bin(pnxs=pnxs)

    @staticmethod
    def compress_pnx(src, dst, with_timestamp=True):
        BusinessLogicUtil.compress_pnx_via_rar(src=src, dst=dst, with_timestamp=with_timestamp)

    @staticmethod
    def compress_pnx_via_rar(src, dst, with_timestamp=True):
        # wsl rar 기반

        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        # 전처리
        # src = BusinessLogicUtil.get_pnx_windows_style(pnx=src)
        src = BusinessLogicUtil.get_pnx_unix_style(pnx=src)
        dst = BusinessLogicUtil.get_pnx_unix_style(pnx=dst)

        # 정의
        working_directory = BusinessLogicUtil.get_working_directory()

        pnx = src
        p = BusinessLogicUtil.get_p(pnx)
        n = BusinessLogicUtil.get_n(pnx)
        nx = BusinessLogicUtil.get_nx(pnx)
        x = BusinessLogicUtil.get_x(pnx)
        x = x.lstrip('.')  # 확장자에서 점 제거

        _rar = ".rar"  # via rar
        timestamp = ""
        if with_timestamp:
            timestamp = rf"{StateManagementUtil.BLANK}{datetime.now().strftime('%Y %m %d %H %M %S')}"
        pn_rar = rf"{p}/{n}{_rar}"
        dst_nx_rar = rf"{dst}/{n}{_rar}"
        dst_nx_timestamp_rar = rf"{dst}/{n}{timestamp}{_rar}"

        # 로깅
        # BusinessLogicUtil.print_as_log(string=rf'''dst="{dst}" %%%FOO%%%''')
        # BusinessLogicUtil.print_as_log(string=rf'''pnx="{pnx}" %%%FOO%%%''')
        # BusinessLogicUtil.print_as_log(string=rf'''p="{p}" %%%FOO%%%''')
        # BusinessLogicUtil.print_as_log(string=rf'''n="{n}" %%%FOO%%%''')
        # BusinessLogicUtil.print_as_log(string=rf'''nx="{nx}" %%%FOO%%%''')
        # BusinessLogicUtil.print_as_log(string=rf'''x="{x}" %%%FOO%%%''')
        # BusinessLogicUtil.print_as_log(string=rf'''dst_nx_rar="{dst_nx_rar}" %%%FOO%%%''')
        # BusinessLogicUtil.print_as_log(string=rf'''dst_nx_timestamp_rar="{dst_nx_timestamp_rar}" %%%FOO%%%''')
        # BusinessLogicUtil.print_as_log(string = rf'''dst_nx_timestamp_rar="{dst_nx_timestamp_rar}" %%%FOO%%%''')

        # 삭제
        BusinessLogicUtil.move_pnx_to_trash_bin(src=pn_rar)

        # 생성
        BusinessLogicUtil.make_pnx(pnx=dst, mode='d')

        # 이동
        os.chdir(p)

        # 압축
        wsl_pn_rar = BusinessLogicUtil.get_pnx_unix_style_for_wsl(pnx=pn_rar)
        command = f'wsl rar a "{wsl_pn_rar}" "{nx}"'
        BusinessLogicUtil.command_to_os(command)

        # copy
        BusinessLogicUtil.copy_pnx_with_overwrite(src=pn_rar, dst=dst)

        # rename
        BusinessLogicUtil.pnx_rename(src=dst_nx_rar, pnx_new=dst_nx_timestamp_rar)

        BusinessLogicUtil.print_as_log(string=rf'''wsl_pn_rar="{wsl_pn_rar}" %%%FOO%%%''')
        dst_nx = rf"{dst}/{nx}"
        BusinessLogicUtil.print_as_log(string=rf'''desktop_nx="{dst_nx}" %%%FOO%%%''')

        # 삭제
        BusinessLogicUtil.move_pnx_to_trash_bin(src=dst_nx)
        BusinessLogicUtil.move_pnx_to_trash_bin(src=dst_nx_rar)

        # 복귀
        os.chdir(working_directory)

        # logging
        BusinessLogicUtil.print_as_log(string=rf'''dst_nx_rar="{dst_nx_rar}" %%%FOO%%%''', print_color='blue')
        BusinessLogicUtil.print_as_log(string=rf'''dst_nx_timestamp_rar="{dst_nx_timestamp_rar}" %%%FOO%%%''', print_color='blue')

    @staticmethod
    def copy_pnx_with_overwrite(src, dst):  # 같은이름의 파일이 이미 있으면 copy 하지 않음
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            # shutil.copy2(pnx, dst)  # shutil.copy2 copies the file and metadata, overwrites if exists # 사용중인 파일에 대해서는 권한문제있어서 복사불가한 방식
            # command = f'copy "{pnx}" "{dst}"' # 디렉토리 복사안됨
            # command = f'xcopy /E /H /K /Y "{pnx}" "{dst}"'
            # command = f'robocopy "{pnx}" "{dst}" /E /Z /R:3 /W:5 /COPYALL /DCOPY:T'
            # command = f'robocopy "{pnx}" "{dst}" /E /Z /R:3 /W:5 /COPY:DATSOU /DCOPY:T'
            # command = f'runas /user:Administrator robocopy "{pnx}" "{dst}" /E /Z /R:3 /W:5 /COPY:DATSOU /DCOPY:T'
            # command = rf'powershell -Command "Start-Process cmd -ArgumentList \'/c robocopy \"{pnx}\" \"{dst}\" /E /Z /R:3 /W:5 /COPY:DATSOU /DCOPY:T\' -Verb runAs"'
            # command = rf'powershell -Command "Start-Process cmd -ArgumentList \'/c xcopy \\"{pnx}\\" \\"{dst}\\" "'
            # command = rf'powershell -Command "Start-Process cmd -ArgumentList \'/c xcopy \\"{pnx}\\" \\"{dst}\\" /E /H /K /Y\' -Verb runAs"'
            # subprocess.run(command, shell=True, check=True)
            # BusinessLogicUtil.press("enter", interval=0.6)
            src = BusinessLogicUtil.get_pnx_preprocessed(pnx=src)
            src = src.replace("\"", "")
            if src.strip() == "":
                return
            pnx_dirname = os.path.dirname(src)
            pnx_basename = os.path.basename(src).split(".")[0]
            pnx_zip = rf'{pnx_dirname}\{pnx_basename}.zip'
            pnx_zip_new = rf"{dst}\{BusinessLogicUtil.get_nx(pnx=pnx_zip)}"

            # 로깅
            BusinessLogicUtil.print_as_log(f"pnx : {src}")
            BusinessLogicUtil.print_as_log(f"pnx_zip : {pnx_zip}")
            BusinessLogicUtil.print_as_log(f"pnx_zip_new : {pnx_zip_new}")

            # 삭제
            if BusinessLogicUtil.does_pnx_exist(src=pnx_zip_new):
                BusinessLogicUtil.move_pnx_to_trash_bin(src=pnx_zip_new)

            # 압축
            BusinessLogicUtil.compress_pnx_via_zip(pnx_zip=pnx_zip, src=src)

            # 이동
            try:
                shutil.move(src=pnx_zip, dst=dst)
            except:
                BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")

            # 압축해제
            BusinessLogicUtil.decompress_pnx_via_zip(pnx=pnx_zip_new)

            # 삭제
            BusinessLogicUtil.move_pnx_to_trash_bin(src=pnx_zip_new)
        except:
            BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
            os.chdir(StateManagementUtil.PROJECT_DIRECTORY)

    @staticmethod
    def get_str_from_text_file(pnx):
        strings = ""
        lines = BusinessLogicUtil.get_list_from_f_txt(pnx=pnx)
        lines = BusinessLogicUtil.get_list_removed_element_none(items=lines)
        for line in lines:
            strings = strings + line + "\n"
        return strings

    @staticmethod
    def generate_token_file(pnx, initial_token):
        if not BusinessLogicUtil.does_pnx_exist(src=pnx):
            BusinessLogicUtil.make_pnx(pnx=pnx, mode="f")
        lines = BusinessLogicUtil.get_list_from_f_txt(pnx=pnx)
        lines = BusinessLogicUtil.get_list_removed_element_preprocessed(items_list=lines)
        if len(lines) == 0:
            token = initial_token
            if initial_token != "":
                BusinessLogicUtil.write_str_to_file(txt_str=f"{token}\n", pnx=pnx, mode="w")

    @staticmethod
    def is_wsl_linux_installed(wsl_linux_version):
        cmd = rf'wsl -l -v'
        lines = BusinessLogicUtil.command_to_os(cmd=cmd, show_mode=False)
        lines = BusinessLogicUtil.get_list_removed_element_preprocessed(items_list=lines)
        BusinessLogicUtil.print_as_log(rf'''type(lines) = "{type(lines)}"''')
        BusinessLogicUtil.print_as_log(f'''lines = {lines}''')
        BusinessLogicUtil.print_as_log(rf'''len(lines) = "{len(lines)}"''')
        for line in lines:
            if wsl_linux_version in line:
                BusinessLogicUtil.print_as_log(string=f'''"{wsl_linux_version}이 설치 되어 있습니다"''', print_color="green")
                return True
        BusinessLogicUtil.print_as_log(string=f'''"{wsl_linux_version}이 설치되지 않았습니다"''', print_color="red")
        return False

    @staticmethod
    def get_str_from_clipboard():
        # Get-Clipboard  # 클립보드 내용 확인
        return clipboard.paste()

    @staticmethod
    def copy(string):
        # Set-Clipboard -Value "텍스트"  # 클립보드에 텍스트 저장
        clipboard.copy(string)

    @staticmethod
    def is_front_window_title(window_title_seg):
        if not BusinessLogicUtil.get_front_window_title() is None:
            if window_title_seg in BusinessLogicUtil.get_front_window_title():
                return True
        return False

    @staticmethod
    def get_front_window_title():
        try:
            active_window = pygetwindow.getActiveWindow()
            if active_window:
                return active_window.title
            else:
                return None  # 활성화된 창이 없다면 None 반환
        except Exception as e:
            return f"Error: {str(e)}"

    @staticmethod
    def run_command_run_via_wsl_exe(wsl_command, wsl_linux_version, wsl_window_title_seg, exit_mode):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        timeout = 20
        start_time = time.time()
        while True:
            if BusinessLogicUtil.is_window_open(window_title_seg=wsl_window_title_seg):
                break
            BusinessLogicUtil.run_ubuntu_via_wsl(wsl_linux_version=wsl_linux_version, window_title_seg=wsl_window_title_seg)
            BusinessLogicUtil.print_as_log(string=time.time() - start_time)
            if time.time() - start_time > timeout:
                break
            time.sleep(0.5)

        std_output_stream = ""
        timeout = 5
        start_time = time.time()
        while True:
            if BusinessLogicUtil.is_front_window_title(window_title_seg=wsl_window_title_seg):
                BusinessLogicUtil.copy_and_paste_with_keeping_clipboard(string=wsl_command, wsl_mode=True)
                BusinessLogicUtil.press("enter")
                break
            BusinessLogicUtil.move_window_to_front(window_title_seg=wsl_window_title_seg)

            # 5초가 지났는지 확인
            BusinessLogicUtil.print_as_log(string=time.time() - start_time)
            if time.time() - start_time > timeout:
                print("5 seconds passed. Exiting loop.")
                break
            time.sleep(0.5)  # CPU 점유율을 낮추기 위해 약간의 대기

        if exit_mode == True:
            timeout = 5
            start_time = time.time()
            while True:
                if BusinessLogicUtil.is_front_window_title(window_title_seg=wsl_window_title_seg):
                    BusinessLogicUtil.copy_and_paste_with_keeping_clipboard(string="exit", wsl_mode=True)
                    BusinessLogicUtil.press("enter")
                    BusinessLogicUtil.copy_and_paste_with_keeping_clipboard(string="exit", wsl_mode=True)
                    BusinessLogicUtil.press("enter")
                    break
                else:
                    BusinessLogicUtil.move_window_to_front(window_title_seg=wsl_window_title_seg)
                BusinessLogicUtil.print_as_log(string=time.time() - start_time)
                if time.time() - start_time > timeout:
                    print("5 seconds passed. Exiting loop.")
                    break
                time.sleep(0.5)  # CPU 점유율을 낮추기 위해 약간의 대기

        # return std_output_stream

    @staticmethod
    def command_to_os_like_person(command, admin_mode=False, mode_exit=True):
        # todo return 에 대해서 개선이 필요하다.
        '''
        return 재데로 안됨
        '''
        window_title_seg = rf'cmd.exe'
        # | clip 을 하여도 값을 읽어오기 어려운 경우가 있음
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.print_as_log(string=rf'''cmd_command="{command}" %%%FOO%%%''')
        if not BusinessLogicUtil.is_window_open(window_title_seg=window_title_seg):
            if admin_mode == False:
                BusinessLogicUtil.run_cmd_exe()
            else:
                BusinessLogicUtil.run_cmd_exe_as_admin()

        std_output_stream = ""
        timeout = 10
        start_time = time.time()
        while True:
            if BusinessLogicUtil.is_front_window_title(window_title_seg=window_title_seg):
                # command = rf"{command} | clip"
                BusinessLogicUtil.copy_and_paste_with_keeping_clipboard(string=command)
                # BusinessLogicUtil.sleep(milliseconds=1000)
                BusinessLogicUtil.sleep(milliseconds=500)
                BusinessLogicUtil.press("enter")
                std_output_stream = BusinessLogicUtil.get_str_from_clipboard()
                return std_output_stream
            BusinessLogicUtil.move_window_to_front(window_title_seg=window_title_seg)
            # BusinessLogicUtil.print_as_log(string=time.time() - start_time)
            if time.time() - start_time > timeout:
                BusinessLogicUtil.print_as_log(string=rf'''rf"{timeout} seconds passed. Exiting loop." %%%FOO%%%''')
                break
            time.sleep(0.5)  # CPU 점유율을 낮추기 위해 약간의 대기

        timeout = 5
        start_time = time.time()
        while True:
            if BusinessLogicUtil.is_front_window_title(window_title_seg=window_title_seg):
                if mode_exit == True:
                    BusinessLogicUtil.copy_and_paste_with_keeping_clipboard(string="exit")
                    BusinessLogicUtil.press("enter")
            BusinessLogicUtil.print_as_log(string=time.time() - start_time)
            if time.time() - start_time > timeout:
                print("5 seconds passed. Exiting loop.")
                break
            time.sleep(0.5)  # CPU 점유율을 낮추기 위해 약간의 대기

        return std_output_stream

    @staticmethod
    def process_kill_wsl_exe(show_mode=True):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        process_name = "wsl.exe"
        command = "wsl --shutdown"
        BusinessLogicUtil.command_to_os(cmd=command, mode="a", show_mode=show_mode)
        pids = BusinessLogicUtil.get_pids_by_process_name("wsl.exe")
        if pids is not None:
            for pid in pids:
                if pid is not None:
                    BusinessLogicUtil.process_kill(pid=pid, show_mode=show_mode)
        BusinessLogicUtil.write_like_person("exit")
        BusinessLogicUtil.press("enter")

    @staticmethod
    def process_kill_cmd_exe(show_mode=True):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            pids = BusinessLogicUtil.get_pids_by_process_name("cmd.exe")
            for pid in pids:
                BusinessLogicUtil.process_kill(pid=pid, show_mode=show_mode)
        except:
            BusinessLogicUtil.print_as_log(string=rf''' %%%FOO%%%''', print_color="red")

    @staticmethod
    def process_kill_powershell_exe(show_mode=True):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            pids = BusinessLogicUtil.get_pids_by_process_name("powershell.exe")
            for pid in pids:
                BusinessLogicUtil.process_kill(pid=pid, show_mode=show_mode)
        except:
            BusinessLogicUtil.print_as_log(string=rf''' %%%FOO%%%''', print_color="red")

    @staticmethod
    def create_script_file(commands, script_nx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        # 기존 script_nx 삭제
        if os.path.exists(script_nx):
            os.remove(script_nx)

        # 생성
        if not os.path.exists(script_nx):
            with open(script_nx, 'w') as bat_file:
                # 2. cmds에 있는 명령어들을 한 줄씩 배치 파일에 저장
                for cmd in commands:
                    bat_file.write(f"{cmd}\n")

    @staticmethod
    def get_token_from_text_file(token_file, initial_token):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.generate_token_file(pnx=token_file, initial_token=initial_token)
        token = BusinessLogicUtil.get_str_from_text_file(pnx=token_file)
        token = token.replace("\n", "")
        return token

    @staticmethod
    def make_shellscript_version_new_via_hard_coded():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.make_shellscript_version_new_via_hard_coded_v_1_0_1()
        pass

    @staticmethod
    def make_shellscript_version_new_via_hard_coded_v_1_0_0():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        import os
        import shutil
        import re

        def get_next_versioned_file_pnx(filename):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            # 파일 이름과 확장자를 분리
            name, ext = os.path.splitext(filename)

            # 현재 디렉토리에 있는 모든 파일 리스트
            files = os.listdir(".")

            # 정규표현식으로 "v1.x.y" 형태의 버전을 찾기
            versioned_files = [f for f in files if re.match(fr"{re.escape(name)}_v\d+\.\d+\.\d+{re.escape(ext)}", f)]

            if versioned_files:
                # 최신 버전을 찾기 위해 버전별로 분리하여 정렬
                latest_version = max(versioned_files, key=lambda x: list(map(int, re.findall(r"\d+", x)[-3:])))
                major, minor, patch = map(int, re.findall(r"\d+", latest_version)[-3:])

                # 버전을 업데이트, 다음 패치 버전 생성
                patch += 1
                next_version = f"{major}.{minor}.{patch}"
            else:
                # 기존 버전이 없으면 기본 v1.0.0으로 생성
                next_version = "1.0.0"

            return f"{name}_v{next_version}{ext}"

        def copy_with_version(file_pnx):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            # 파일 유효성 검사
            if not os.path.isfile(file_pnx):
                BusinessLogicUtil.print_as_log(string=rf'''file_pnx="{file_pnx}" %%%FOO%%%''')
                return

            # 복사
            file_pnx_new = get_next_versioned_file_pnx(os.path.basename(file_pnx))
            shutil.copy(file_pnx, file_pnx_new)
            BusinessLogicUtil.print_as_log(string=rf'''file_pnx_new="{file_pnx_new}" %%%FOO%%%''')

        # 절대 경로를 사용하여 대상 파일의 절대 경로를 입력
        file_pnxs = [
            os.path.expanduser(r"~/Downloads/jung_hoon_park/plain/park4139_info_collector.sh"),
            os.path.expanduser(r"~/Downloads/jung_hoon_park/plain/park4139_ip_connection_update_for_114.sh"),
            os.path.expanduser(r"~/Downloads/jung_hoon_park/plain/park4139_ip_connection_update_for_front.sh"),
            os.path.expanduser(r"~/Downloads/jung_hoon_park/plain/park4139_ip_connection_update_for_rear.sh"),
            os.path.expanduser(r"~/Downloads/jung_hoon_park/plain/park4139_ip_connection_update_for_reset.sh"),
        ]

        # 각 파일을 복사하여 버전별로 관리
        for file_pnx in file_pnxs:
            copy_with_version(file_pnx)

    @staticmethod
    def make_shellscript_version_new_via_hard_coded_v_1_0_1():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        def get_next_versioned_file_pnx(filename):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            name, ext = os.path.splitext(filename)
            files = os.listdir(".")

            # 정규표현식으로 "v1.x.y" 형태의 버전을 찾기
            versioned_files = [f for f in files if re.match(fr"{re.escape(name)}_v\d+\.\d+\.\d+{re.escape(ext)}", f)]

            if versioned_files:
                latest_version = max(versioned_files, key=lambda x: list(map(int, re.findall(r"\d+", x)[-3:])))
                major, minor, patch = map(int, re.findall(r"\d+", latest_version)[-3:])
                patch += 1
                next_version = f"{major}.{minor}.{patch}"
            else:
                next_version = "1.0.0"

            return f"{name}_v{next_version}{ext}"

        def copy_with_version(file_pnx):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            if not os.path.isfile(file_pnx):
                print(f"{file_pnx} 파일을 찾을 수 없습니다.")
                return

            file_pnx_new = get_next_versioned_file_pnx(os.path.basename(file_pnx))
            shutil.copy(file_pnx, file_pnx_new)
            print(f"''{file_pnx}'를  {file_pnx_new}'로 복사되었습니다.")
            manage_versions(os.path.basename(file_pnx))

        def manage_versions(original_filename):
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            name, ext = os.path.splitext(original_filename)
            files = os.listdir(".")

            # 해당 파일의 모든 버전 파일을 찾기

            versioned_files = sorted(
                [f for f in files if re.match(fr"{re.escape(name)}_v\d+\.\d+\.\d+{re.escape(ext)}", f)],
                key=lambda x: list(map(int, re.findall(r"\d+", x)[-3:]))
            )

            # 최신 버전 파일을 제외한 나머지 버전 파일을 archive 디렉토리로 이동
            dst = rf"{StateManagementUtil.DOWNLOADS}\archived"
            if len(versioned_files) > 1:
                latest_version = versioned_files[-1]
                os.makedirs(dst, exist_ok=True)

                for f in versioned_files[:-1]:
                    shutil.move(f, dst)
                    print(f"'{f}' 파일이 '{dst}' 디렉토리로 이동되었습니다.")

        file_pnxs = [  # 상대경로
            os.path.expanduser(r"~/Downloads/jung_hoon_park/plain/park4139_info_collector.sh"),
            os.path.expanduser(r"~/Downloads/jung_hoon_park/plain/park4139_ip_connection_update_for_114.sh"),
            os.path.expanduser(r"~/Downloads/jung_hoon_park/plain/park4139_ip_connection_update_for_front.sh"),
            os.path.expanduser(r"~/Downloads/jung_hoon_park/plain/park4139_ip_connection_update_for_rear.sh"),
            os.path.expanduser(r"~/Downloads/jung_hoon_park/plain/park4139_ip_connection_update_for_reset.sh"),
            os.path.expanduser(r"~/Downloads/jung_hoon_park/plain/park4139_evm_updater_for_front.sh"),
            # os.path.expanduser(r"~/Downloads/jung_hoon_park/plain/park4139_evm_updater_for_rear.sh"),
        ]

        for file_pnx in file_pnxs:
            copy_with_version(file_pnx)

        BusinessLogicUtil.print_list_as_foldable(items_list=file_pnxs, items_list_name="다운로드완료")

    @staticmethod
    def alert_as_gui(title_: str, ment: str, auto_click_positive_btn_after_seconds: int, input_text_default="", btns=["확인"]):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # should_i_do 가 앱 안과 밖에서도 잘 된다면 deprecated 하자
        if platform.system() == 'Windows':
            function_name = inspect.currentframe().f_code.co_name
            BusinessLogicUtil.print_with_underline(f"{function_name}()")

            # QApplication 인스턴스 확인
            app_foo = None
            app = QApplication.instance()
            if app is None:
                app_foo = QApplication()
            if input_text_default == "":
                is_input_text_box = False
            else:
                is_input_text_box = True

            dialog_ = BusinessLogicUtil.CustomQdialog(
                title=title_,
                ment=ment,
                btns=btns,
                input_box_mode=is_input_text_box,
                input_box_text_default=input_text_default,
                auto_click_positive_btn_after_seconds=auto_click_positive_btn_after_seconds
            )
            dialog_.exec()
            btn_text_clicked = dialog_.btn_text_clicked

            if btn_text_clicked == "":
                BusinessLogicUtil.print_light_black(f'버튼  입니다 {btn_text_clicked}')
            if app == True:  # .....app 은 bool 이 아닌데. 동작 되고있는데..
                BusinessLogicUtil.print_light_black("여기는 좀 확인을 해야하는데. 호출 안되면 좋겠는데1")
                if isinstance(app_foo, QApplication):
                    BusinessLogicUtil.print_light_black("여기는 좀 확인을 해야하는데. 호출 안되면 좋겠는데2")
                    app_foo.exec()
            if app == True:
                # app_foo.quit()# QApplication 인스턴스 제거시도 : fail
                # app_foo.deleteLater()# QApplication 인스턴스 파괴시도 : fail
                # del app_foo # QApplication 인스턴스 파괴시도 : fail
                # app_foo = None # QApplication 인스턴스 파괴시도 : fail
                BusinessLogicUtil.print_light_black("여기는 좀 확인을 해야하는데. 호출 안되면 좋겠는데3")
                app_foo.shutdown()  # QApplication 인스턴스 파괴시도 : success  # 성공요인은 app.shutdown()이 호출이 되면서 메모리를 해제까지 수행해주기 때문
                # sys.exit()
        else:
            BusinessLogicUtil.print_light_black(f"{ment}")

    @staticmethod
    def classify_pnxs_at_tree(src, mode, with_walking, debug_mode=False):
        function_name = inspect.currentframe().f_code.co_name

        # logging
        if debug_mode == True:
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
            BusinessLogicUtil.print_as_log(string=rf'''src="{src}" %%%FOO%%%''')
            BusinessLogicUtil.print_as_log(string=rf'''mode="{mode}" %%%FOO%%%''')

        if mode == 'f':
            # 파일이 너무 많을떄 수행 # file_cnt_limit이 100개(?) 넘어가면 without_walking=True
            # BusinessLogicUtil.classify_pnxs_to_pkg_compressed(pnx)
            # BusinessLogicUtil.classify_pnxs_to_pkg_document(pnx)
            # BusinessLogicUtil.classify_pnxs_to_pkg_video(pnx)
            # BusinessLogicUtil.classify_pnxs_to_pkg_image(pnx)
            # BusinessLogicUtil.classify_pnxs_to_pkg_soundtrack(pnx)
            # BusinessLogicUtil.classify_pnxs_to_special_keyword_dir(pnx)

            # BusinessLogicUtil.classify_pnxs_to_pkg_compressed(src=src, without_walking=False)
            # BusinessLogicUtil.classify_pnxs_to_pkg_document(pnx=src, without_walking=False)
            # BusinessLogicUtil.classify_pnxs_to_pkg_video(pnx=src, without_walking=False)
            # BusinessLogicUtil.classify_pnxs_to_pkg_image(pnx=src, without_walking=False)
            # BusinessLogicUtil.classify_pnxs_to_pkg_soundtrack(pnx=src, without_walking=False)
            BusinessLogicUtil.classify_pnxs_to_special_keyword_dir(src, with_walking=with_walking)

            # BusinessLogicUtil.classify_pnxs_to_pn_dir(src=src)
            # BusinessLogicUtil.classify_pnxs_to_pkg_image_via_ai() #todo AI 이미지 분류기
            # BusinessLogicUtil.classify_pnxs_to_pkg_video_via_ai() #todo AI 동영상 분류기 # 동영상 내용보고 분류기준에 따라 분류
            # BusinessLogicUtil.merge_pnxs_via_text_file() # todo

    @staticmethod
    def rename_pnxs_at_tree(src, mode, with_walking, debug_mode=False):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.print_as_log(string=rf'''src="{src}" %%%FOO%%%''')
        BusinessLogicUtil.print_as_log(string=rf'''mode="{mode}" %%%FOO%%%''')

        BusinessLogicUtil.rename_pnxs_from_keywords_to_keyword_new(src=src, mode=mode, debug_mode=debug_mode, with_walking=with_walking)
        BusinessLogicUtil.rename_pnxs_from_pattern_to_pattern_new_via_routines(src=src, mode=mode, with_walking=with_walking)
        BusinessLogicUtil.rename_pnxs_from_keywords_to_keyword_new(src=src, mode=mode, debug_mode=debug_mode, with_walking=with_walking)

    @staticmethod
    def gather_pnxs_useless_at_tree(src, mode):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.print_as_log(string=rf'''src="{src}" %%%FOO%%%''')
        BusinessLogicUtil.print_as_log(string=rf'''mode="{mode}" %%%FOO%%%''')

        if mode == 'd':
            # BusinessLogicUtil.gather_pnxs_useless(src=src, debug_mode=True) #쓸라면 테스트 필요
            pass

        if mode == 'f':
            BusinessLogicUtil.gather_pnxs_useless(src=src, debug_mode=True)

    @staticmethod
    def gather_pnxs_empty_at_tree(src):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        BusinessLogicUtil.gather_pnxs_empty(src=src, show_mode=False)

    @staticmethod
    def play_my_sound_track():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        # BusinessLogicUtil.command_to_os(command=rf'taskkill /f /im "alsong.exe" ', show_mode=False)

        BusinessLogicUtil.command_to_os(cmd=rf'explorer "{StateManagementUtil.PKG_SOUND_POTPLAYER64_DPL}" ', show_mode=False)

    @staticmethod
    def rename_pnxs_from_pattern_to_pattern_new_via_routines(src, mode, with_walking):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # pattern = r'(\[.*?\])'  # [문자열]
        BusinessLogicUtil.rename_pnxs_from_pattern_twice_to_pattern_new(pnx=src, pattern=r'\d{4}_\d{2}_\d{2}_(월|화|수|목|금|토|일)_\d{2}_\d{2}_\d{2}_\d{3}', mode=mode, with_walking=with_walking)
        BusinessLogicUtil.rename_pnxs_from_pattern_twice_to_pattern_new(pnx=src, pattern=r'\d{4}_\d{2}_\d{2}_\d{2}_\d{2}_\d{2}', mode=mode, with_walking=with_walking)
        BusinessLogicUtil.rename_pnxs_from_pattern_twice_to_pattern_new(pnx=src, pattern=r'_\d{11}_\d{11}_', mode=mode, with_walking=with_walking)
        BusinessLogicUtil.rename_pnxs_from_pattern_twice_to_pattern_new(pnx=src, pattern=r'_\d{10}_\d{10}_', mode=mode, with_walking=with_walking)
        BusinessLogicUtil.rename_pnxs_from_pattern_twice_to_pattern_new(pnx=src, pattern=r'_\d{11}_', mode=mode, with_walking=with_walking)

        BusinessLogicUtil.rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'\d{4}_\d{2}_\d{2}_(월|화|수|목|금|토|일)_\d{2}_\d{2}_\d{2}_\d{3}', pattern_new="_", mode=mode, with_walking=with_walking)
        BusinessLogicUtil.rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'jhp##\d{4}_\d{2}_\d{2}', pattern_new="[jhp##]", mode=mode, with_walking=with_walking)
        BusinessLogicUtil.rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'jhp##\d{8}', pattern_new="[jhp##]", mode=mode, with_walking=with_walking)
        BusinessLogicUtil.rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'\$\d{22}', pattern_new="_", mode=mode, with_walking=with_walking)
        BusinessLogicUtil.rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'_\d{29}_', pattern_new="_", mode=mode, with_walking=with_walking)
        BusinessLogicUtil.rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'\d{4}_\d{2}_\d{2}_\d{2}_\d{2}_\d{2}', pattern_new=".", mode=mode, with_walking=with_walking)
        BusinessLogicUtil.rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'_\d{8}_', pattern_new=".", mode=mode, with_walking=with_walking)
        BusinessLogicUtil.rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'_\d{11}.', pattern_new=".", mode=mode, with_walking=with_walking)
        BusinessLogicUtil.rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'_\d{11}_', pattern_new=".", mode=mode, with_walking=with_walking)
        BusinessLogicUtil.rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'_\d{11}', pattern_new="", mode=mode, with_walking=with_walking)
        BusinessLogicUtil.rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'^seg ', pattern_new="_", mode=mode, with_walking=with_walking)
        BusinessLogicUtil.rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'^_', pattern_new="[시작문자]", mode=mode, with_walking=with_walking)
        BusinessLogicUtil.rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'^#', pattern_new="[시작문자]", mode=mode, with_walking=with_walking)
        BusinessLogicUtil.rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'^The ', pattern_new="[시작문자]", mode=mode, with_walking=with_walking)
        BusinessLogicUtil.rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'_$', pattern_new="[끝문자]", mode=mode, with_walking=with_walking)
        BusinessLogicUtil.rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'\(([^)]+)\)(?=.*\(\1\))', pattern_new="[중복문자]", mode=mode, with_walking=with_walking)  # () 안의 중복문자인 경우데 대한 처리 (a)(a) 인 경우 (a)만 남김
        # BusinessLogicUtil.rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'^.', pattern_new="_", mode=mode)  # 시작문자 # 첫글자가 없어진다... 씆지말자
        # BusinessLogicUtil.rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'^ ', pattern_new="_", mode=mode)  # 시작문자 # 업데이트가 되긴하는데 ^_ 이 왜 안되는지 모르겠다.
        # BusinessLogicUtil.rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'_\d{11}$', pattern_new="",mode=mode) # 끝문자 # 끝문자 안되는 것 같은데...
        # BusinessLogicUtil.rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'_\d+$', pattern_new="",mode=mode) # 끝문자
        # BusinessLogicUtil.rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'_\d{10}_\d{10}_', pattern_new="",mode=mode)
        # BusinessLogicUtil.rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'_\d{10}_', pattern_new="",mode=mode)
        # BusinessLogicUtil.rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern= r'\d{10}', pattern_new="",mode=mode)
        # BusinessLogicUtil.rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'\$\d{22}', pattern_new="",mode=mode)
        # BusinessLogicUtil.rename_pnxs_from_pattern_once_to_pattern_new(src=src, pattern=r'_\d{11}', pattern_new="",mode=mode)

    @staticmethod
    def get_list_replaced_element_from_str_to_upper_case(items_list):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        if not isinstance(items_list, list):
            raise ValueError("Input must be a list.")
        return [item.upper() if isinstance(item, str) else item for item in items_list]

    @staticmethod
    def get_list_via_user_input(ment, function_name):
        positivie = "Positive"
        negative = "Negative"
        dialog_btn_text_clicked, function, dialog_input_box_text = BusinessLogicUtil.should_i_do(
            string=ment,
            btns=[positivie, negative],
            function=None,
            auto_click_negative_btn_after_seconds=30,
            title=f"{function_name}()",
            return_mode=True,
            input_box_mode=True,
        )
        if dialog_btn_text_clicked != positivie:
            return
        user_input = dialog_input_box_text.strip()
        item_list = user_input.split("\n")
        return item_list

    is_first_test_lap = True
    test_results = []

    @staticmethod
    def move_pnxs_to_trash_bin(pnxs):
        for pnx in pnxs:
            BusinessLogicUtil.print_as_log(string=rf'''pnx="{pnx}" %%%FOO%%%''')
            if BusinessLogicUtil.does_pnx_exist(pnx):
                BusinessLogicUtil.move_pnx_to_trash_bin(src=pnx)

    @staticmethod
    def close_windows_duplicated():
        pass

    @staticmethod
    def is_current_hostname(hostname):
        current_hostname = BusinessLogicUtil.get_hostname()
        BusinessLogicUtil.print_as_log(string=rf'''hostname="{hostname}" %%%FOO%%%''')
        BusinessLogicUtil.print_as_log(string=rf'''current_hostname="{current_hostname}" %%%FOO%%%''')
        if current_hostname == hostname:
            return True
        else:
            return False

    @staticmethod
    def get_data_required_from_f_csv(line_order):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{function_name}() %%%FOO%%%''', print_color='blue')
        df = BusinessLogicUtil.get_df_from_issues_list_csv()
        columns_required = df.columns.tolist()  # 전부
        # columns_required = ['주행일자','해결 여부', '문제점 상세',  'SW 버전', '파일 위치', '발생시각', '문제모듈', '개입(크루)',  'Crew 요청사항', '피드백 조치','차량', '지역', '코스', '날씨', 'Crew', '위치(UTM_E)', '위치(UTM_N)', '위치(Azimuth)', '위치(Altitude)','시작 Frame', '종료 Frame','개입(점검)', '위험도', 'DB 분석피드백', 'Comment','수정 여부', '수정 내용', '교육자료', '특이 DB', '파일 크기', ] # 중요도 높은것 앞으로 변경된
        # columns_required = ['주행일자', '해결 여부', '문제점 상세', 'SW 버전', '파일 위치', '발생시각', '문제모듈', '개입(크루)', 'Crew 요청사항', '피드백 조치']  # 필요한 것만
        # columns_required = ["파일명", "차량", "지역", "코스", "SW 버전", "운전자", "로그 분석자", "프레임", "문제점 상세", "Crew 요청사항"] ?
        data_required = {}
        nth_row = BusinessLogicUtil.get_nth_row(df, n=line_order)
        if nth_row is not None:
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}n="{line_order}" %%%FOO%%%''')
            for col in columns_required:
                if col in df.columns:  # 열이 존재하는 경우만 출력 # todo get은 get 기능만 출력은 따로..
                    BusinessLogicUtil.print_cyan(string=f"{col}: {nth_row[col]}")
                    # 필요한 것만 추가
                    if col == "파일 위치":
                        data_required["파일 위치"] = nth_row[col]
                    if col == "SW 버전":
                        data_required["SW 버전"] = nth_row[col]
                    if col == "차량":
                        data_required["차량"] = nth_row[col]
                    if col == "지역":
                        data_required["지역"] = nth_row[col]
                    if col == "주행일자":
                        data_required["주행일자"] = nth_row[col]
                    if col == "코스":
                        data_required["코스"] = nth_row[col]
                else:
                    print(f"{col}: N/A")  # 열이 없는 경우 기본값 출력
                    # data_required["차량아이디코드번호"] =
                # print(f"'차량아이디코드번호='{nth_row[col]}'") # 데이터 전처리하여 추출 및 딕셔너리 data_required에 추가
        return data_required

    @staticmethod
    def download_issue_data(data_required, original_log=False):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        # 전처리
        issue_file_name = data_required["파일 위치"].split('/')[-1]

        def get_origin_log_file_name(issue_file_name):
            # 정규식 패턴 정의: "_숫자(최대 2자리)_VIDEO"
            pattern = r"_\d{1,2}_VIDEO"
            original_filename = re.sub(pattern, "", issue_file_name)
            return original_filename

        origin_log_file_name = get_origin_log_file_name(issue_file_name)
        data_required["주행일자"] = data_required["파일 위치"].split('/')[0]
        data_required["파일 위치"] = data_required["파일 위치"].replace("/", f"\\")

        # 정의
        if original_log == False:
            src = rf"\\192.168.1.33\01_Issue\{data_required["파일 위치"]}"
        else:
            src = rf"\\192.168.1.33\02_Orignal\{data_required["차량"]}\{data_required["지역"]}\{data_required["주행일자"]}\{data_required["코스"]}\{origin_log_file_name}"
            BusinessLogicUtil.print_as_log(string=rf'''src="{src}" %%%FOO%%%''')
        # BusinessLogicUtil.pause()
        dst = rf"C:\log"
        command = rf"copy {src} {dst}"
        src_nx = BusinessLogicUtil.get_nx(pnx=src)
        src_new = rf"{dst}\{src_nx}"

        while True:
            if BusinessLogicUtil.does_pnx_exist(src=src_new):
                BusinessLogicUtil.print_as_log(string=rf'''{src_new} 가 이미 있습니다." %%%FOO%%%''')
                break
            else:
                if not BusinessLogicUtil.does_pnx_exist(src=src_new):
                    BusinessLogicUtil.command_to_os(cmd=command, mode="a")
                    BusinessLogicUtil.print_as_log(string=rf'''이슈데이터 다운로드 완료 "{src_new}" %%%FOO%%%''', print_color='blue')
                    return

    # @staticmethod
    # def download_torrent_magnet_from_nyaa_si(string_to_search, driver_selenium, exclude_elements_all, include_elements_any, include_elements_all):
    #     function_name = inspect.currentframe().f_code.co_name
    #     BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''', print_color='blue')
    #     function_name_txt = rf'{StateManagementUtil.PROJECT_DIRECTORY}\pkg_txt\{function_name}.txt'
    #     query = urllib.parse.quote(f"{string_to_search}")
    #     url = f'https://nyaa.si/?f=0&c=0_0&q={query}'
    #     url_decoded = BusinessLogicUtil.get_decoded_url(string=url)
    #     driver_selenium.get(url)
    #
    #     # 페이지 소스 RAW
    #     page_src = driver_selenium.page_source  # page_src={page_src} %%%FOO%%%''')
    #
    #     soup = BeautifulSoup(page_src, "html.parser")
    #
    #     titles = []
    #     magnets = []
    #
    #     string_to_search = string_to_search
    #     string_to_search = BusinessLogicUtil.get_str_removed_last_digit(string_to_search)
    #     string_to_search = string_to_search.strip()
    #
    #     lines = soup.find_all(name="a")
    #     for line in lines:
    #         magnet = line.get('href')
    #         if magnet:
    #             magnets.append(magnet)
    #     # data = BusinessLogicUtil.get_dict_removed_element_duplicated(item_dict=data)
    #
    #     BusinessLogicUtil.print_as_log(string=rf'''url="{url}" %%%FOO%%%''')
    #     BusinessLogicUtil.print_as_log(string=rf'''string_to_search="{string_to_search}" %%%FOO%%%''')
    #     BusinessLogicUtil.print_as_log(string=rf'''url_decoded="{url_decoded}" %%%FOO%%%''')
    #
    #     for magnet in magnets:
    #         if BusinessLogicUtil.is_regex_in_string(string=BusinessLogicUtil.get_decoded_url(magnet), regex=string_to_search, show_mode=False):
    #             # BusinessLogicUtil.print_as_log(string = rf'''BusinessLogicUtil.get_decoded_url(magnet)="{BusinessLogicUtil.get_decoded_url(magnet)}" %%%FOO%%%''')
    #             # if BusinessLogicUtil.is_regex_in_string(string=href, regex="magnet*", with_case_ignored=False, show_mode=False):
    #             exclude_check = not any(element in BusinessLogicUtil.get_decoded_url(magnet) for element in exclude_elements_all)
    #             include_all_check = all(element in BusinessLogicUtil.get_decoded_url(magnet) for element in include_elements_all)
    #             include_any_check = any(element in BusinessLogicUtil.get_decoded_url(magnet) for element in include_elements_any)
    #
    #             # 필터링 조건 평가
    #             if (
    #                     not exclude_check and
    #                     include_all_check and
    #                     include_any_check
    #             ):
    #                 # 결과 출력 및 브라우저 열기
    #                 BusinessLogicUtil.print_as_log(string=rf'''BusinessLogicUtil.get_decoded_url(magnet)="{BusinessLogicUtil.get_decoded_url(magnet)}" %%%FOO%%%''')
    #                 webbrowser.open(magnet)

    @staticmethod
    def get_torrent_magnets_set_from_nyaa_si(title_to_search, driver_selenium, exclude_elements_all=[], include_elements_any=[], include_elements_all=[]):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''', print_color='blue')
        function_name_txt = rf'{StateManagementUtil.PROJECT_DIRECTORY}\pkg_txt\{function_name}.txt'
        query = urllib.parse.quote(f"{title_to_search}")
        url = f'https://nyaa.si/?f=0&c=0_0&q={query}'
        BusinessLogicUtil.print_as_log(string=rf'''url="{url}" %%%FOO%%%''')
        url_decoded = BusinessLogicUtil.get_decoded_url(string=url)
        BusinessLogicUtil.print_as_log(string=rf'''url_decoded="{url_decoded}" %%%FOO%%%''')
        driver_selenium.get(url)

        # 페이지 소스 RAW
        page_src = driver_selenium.page_source
        soup = BeautifulSoup(page_src, "html.parser")

        magnets_list = []
        magnets_set = set()

        # 문자열에서 마지막 숫자 제거
        title_to_search = BusinessLogicUtil.get_str_removed_last_digit(title_to_search).strip()

        # 페이지에서 모든 링크 추출
        lines = soup.find_all(name="a")
        for line in lines:
            magnet = line.get('href')
            if magnet:
                magnets_list.append(magnet)

        for magnet in magnets_list:
            decoded_magnet = BusinessLogicUtil.get_decoded_url(magnet)
            # BusinessLogicUtil.print_as_log(string = rf'''decoded_magnet="{decoded_magnet}" %%%FOO%%%''')

            # 검색 문자열이 URL에 포함되어 있는지 확인
            if BusinessLogicUtil.is_pattern_in_string(string=decoded_magnet, pattern=title_to_search, show_mode=False):
                if exclude_elements_all and include_elements_any and include_elements_all:

                    # 필터링 조건 평가
                    include_all_check = all(include in decoded_magnet for include in include_elements_all)
                    exclude_check = not any(exclude in decoded_magnet for exclude in exclude_elements_all)
                    include_any_check = any(include in decoded_magnet for include in include_elements_any)

                    # 필터링 조건이 만족되면
                    if include_all_check and exclude_check and include_any_check:
                        magnets_set.add(magnet)
                else:
                    magnets_set.add(magnet)
        return magnets_set

    # @staticmethod
    # def download_torrent_magnet_from_nyaa_si(string_to_search, driver_selenium, except_elements_all, include_elements_any, include_elements_all):
    #     function_name = inspect.currentframe().f_code.co_name
    #     BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''', print_color='blue')
    #     function_name_txt = rf'{StateManagementUtil.PROJECT_DIRECTORY}\pkg_txt\{function_name}.txt'
    #     query = urllib.parse.quote(f"{string_to_search}")
    #     url = f'https://nyaa.si/?f=0&c=0_0&q={query}'
    #     url_decoded = BusinessLogicUtil.get_decoded_url(string=url)
    #     driver_selenium.get(url)
    #
    #     # Get page source
    #     page_src = driver_selenium.page_source
    #     soup = BeautifulSoup(page_src, "html.parser")
    #
    #     hrefs = []
    #     titles = []
    #     lines = soup.find_all(name="a")
    #     for line in lines:
    #         titles.append(line.get('title'))
    #         hrefs.append(line.get('href'))
    #
    #     hrefs = BusinessLogicUtil.get_list_removed_element_preprocessed(hrefs)
    #     titles = BusinessLogicUtil.get_list_removed_element_preprocessed(titles)
    #
    #     # Log search parameters
    #     string_to_search = BusinessLogicUtil.get_str_removed_last_digit(string_to_search).strip()
    #     BusinessLogicUtil.print_as_log(string=rf'''string_to_search="{string_to_search}" %%%FOO%%%''')
    #     BusinessLogicUtil.print_as_log(string=rf'''url_decoded="{url_decoded}" %%%FOO%%%''')
    #
    #     # Match titles with regex
    #     titles_matched_as_regex = [title for title in titles if title and BusinessLogicUtil.is_regex_in_contents_with_case_ignored(contents=title, regex=string_to_search, show_mode=False)]
    #     # BusinessLogicUtil.print_as_log(string = rf'''titles_matched_as_regex="{titles_matched_as_regex}" %%%FOO%%%''')
    #
    #     # Filter titles and magnets
    #     filtered_titles_and_magnets = []
    #     for title, magnet in zip(titles_matched_as_regex, hrefs):
    #
    #         if not magnet or not BusinessLogicUtil.is_regex_in_contents_v2( target=magnet, regex="magnet*"):
    #             continue
    #
    #         if except_elements_all and any(except_text in title for except_text in except_elements_all):
    #             continue
    #
    #         if include_elements_all and not all(include_text in title for include_text in include_elements_all):
    #             continue
    #
    #         if include_elements_any and not any(include_text in title for include_text in include_elements_any):
    #             continue
    #
    #         filtered_titles_and_magnets.append((title, magnet))
    #
    #     # log
    #     BusinessLogicUtil.print_as_log(f"Filtered Titles: {[tm for tm in filtered_titles_and_magnets]}")
    #     # BusinessLogicUtil.pause()
    #
    #     # Open magnets and log
    #     for i, (title, magnet) in enumerate(filtered_titles_and_magnets):
    #         BusinessLogicUtil.print_as_log(f"{i}:{title}:{magnet}")
    #         BusinessLogicUtil.pause()
    #         webbrowser.open(magnet)
    #
    #     # Update downloaded list
    #     function_name_txt_list = BusinessLogicUtil.get_list_from_text_file(pnx=function_name_txt)
    #     if function_name_txt_list is not None:
    #         string_to_search = string_to_search.strip()
    #         texts_updated = BusinessLogicUtil.get_list_striped_element(items=function_name_txt_list)
    #         texts_updated = list(dict.fromkeys(text for text in texts_updated if text and string_to_search not in text))
    #         BusinessLogicUtil.write_list_to_file(pnx=function_name_txt, texts=texts_updated, mode="w")
    #
    #     # Append next item to download list
    #     string_downloaded = string_to_search.strip()
    #     new_number = str(int(BusinessLogicUtil.get_last_digit(string_downloaded)) + 1).zfill(2).strip()
    #     text_removed_success_and_last_digit = BusinessLogicUtil.get_str_removed_last_digit(string_downloaded).strip()
    #     BusinessLogicUtil.write_str_to_file(pnx=function_name_txt, text=f"{text_removed_success_and_last_digit} {new_number}\n", mode="a")

    @staticmethod
    def print_list_as_foldable(items_list, items_list_name, foldable_mode=StateManagementUtil.FOLDABLE_MODE):
        if foldable_mode == True:
            BusinessLogicUtil.print_as_log(string=rf'''items_list="{items_list}" %%%FOO%%%''')
        else:
            BusinessLogicUtil.print_list_as_vertical(items_list=items_list, items_list_name=items_list_name)

    @staticmethod
    def run_command_via_powershell_exe(command, show_mode=True, console_keep_mode=False, admin_mode=False):
        # | clip 을 하여도 값을 읽어오기 어려운 경우가 있음
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        window_title_seg = rf'PowerShell'
        BusinessLogicUtil.print_as_log(string=rf'''cmd_command="{command}" %%%FOO%%%''')
        if not BusinessLogicUtil.is_window_open(window_title_seg=window_title_seg):
            # BusinessLogicUtil.run_cmd_exe()
            if admin_mode == False:
                window_title_seg = rf'powershell'
                BusinessLogicUtil.run_powershell_exe()
            else:
                window_title_seg = rf'PowerShell'
                BusinessLogicUtil.run_powershell_exe_as_admin()
        BusinessLogicUtil.move_window_to_front(window_title_seg=window_title_seg)

        std_output_stream = ""
        timeout = 5
        start_time = time.time()
        while True:
            if BusinessLogicUtil.is_front_window_title(window_title_seg=window_title_seg):
                # BusinessLogicUtil.copy_and_paste_with_keeping_clipboard(string=rf"cd {wsl_pnx} | xclip -sel clip", mode="wsl") # fail: cd는 xclip 으로 pipe 할 수 없음
                BusinessLogicUtil.copy_and_paste_with_keeping_clipboard(string=command)
                BusinessLogicUtil.press("enter", show_mode=show_mode)
                std_output_stream = BusinessLogicUtil.get_str_from_clipboard()
                break
            # 5초가 지났는지 확인
            BusinessLogicUtil.print_as_log(string=time.time() - start_time)
            if time.time() - start_time > timeout:
                print("5 seconds passed. Exiting loop.")
                break
            time.sleep(0.5)  # CPU 점유율을 낮추기 위해 약간의 대기

        if console_keep_mode == False:
            timeout = 5
            start_time = time.time()
            while True:
                if BusinessLogicUtil.is_front_window_title(window_title_seg=window_title_seg):
                    BusinessLogicUtil.copy_and_paste_with_keeping_clipboard(string="exit", show_mode=False)
                    BusinessLogicUtil.press("enter", show_mode=show_mode)
                    if admin_mode == False:
                        BusinessLogicUtil.copy_and_paste_with_keeping_clipboard(string="exit")
                        BusinessLogicUtil.press("enter", show_mode=show_mode)
                    break
                BusinessLogicUtil.print_as_log(string=time.time() - start_time)
                if time.time() - start_time > timeout:
                    print("5 seconds passed. Exiting loop.")
                    break
                time.sleep(0.5)  # CPU 점유율을 낮추기 위해 약간의 대기
        return std_output_stream

    @staticmethod
    def run_cmd_exe():
        BusinessLogicUtil.command_to_os(cmd=rf"start cmd.exe /k", mode="a")

    @staticmethod
    def change_os_to_screen_saver():
        # 성공
        # BusinessLogicUtil.command_to_os_like_person(command=rf'''%systemroot%\system32\scrnsave.scr /s''')

        # 성공
        BusinessLogicUtil.command_to_os(cmd=rf'''%systemroot%\system32\scrnsave.scr /s ''')

    @staticmethod
    def change_os_to_screen_locked():
        BusinessLogicUtil.command_to_os(cmd="rundll32.exe user32.dll,LockWorkStation")

    @staticmethod
    def run_powershell_exe():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        BusinessLogicUtil.command_to_os('start cmd /k powershell', mode='a')
        # BusinessLogicUtil.command_to_os('start cmd /k powershell')
        window_title_seg = "powershell"
        while True:
            if not BusinessLogicUtil.is_front_window_title(window_title_seg=window_title_seg):
                BusinessLogicUtil.move_window_to_front(window_title_seg=window_title_seg)
            if BusinessLogicUtil.is_front_window_title(window_title_seg=window_title_seg):
                break

    @staticmethod
    def click_string(string, doubleclick_mode=False):
        timeout = 20
        start_time = time.time()
        while True:
            BusinessLogicUtil.print_as_log(string=time.time() - start_time)
            if time.time() - start_time > timeout:
                break
            if BusinessLogicUtil.does_text_bounding_box_exist_via_easy_ocr(string=string):
                break
            time.sleep(0.5)
        BusinessLogicUtil.click_mouse_left_btn(doubleclick_mode=doubleclick_mode)

    @staticmethod
    def shoot_custom_screenshot():
        asyncio.run(BusinessLogicUtil.shoot_custom_screenshot_via_asyncio())

    @staticmethod
    def move_pnx_with_overwrite(src: str, dst: str):
        # Ensure the source file exists
        if not os.path.isfile(src):
            BusinessLogicUtil.print_red(f"Source file does not exist: {src}")

        dest_dir = os.path.dirname(dst)
        if dest_dir and not os.path.exists(dest_dir):
            os.makedirs(dest_dir)

        try:
            if os.path.exists(dst):
                os.remove(dst)  # Remove the existing file
            shutil.move(src, dst)
            BusinessLogicUtil.print_green(f"Successfully moved '{src}' to '{dst}'")
        except Exception as e:
            BusinessLogicUtil.print_red(f"Failed to move file: {e}")

    # @staticmethod
    # def make_plain_light_pkg_for_moving_to_house():
    #     pnxs = [
    #         rf"{StateManagementUtil.PROJECT_DIRECTORY}\.git",
    #         rf"{StateManagementUtil.PROJECT_DIRECTORY}\.idea",
    #         rf"{StateManagementUtil.PROJECT_DIRECTORY}\.venv",
    #     ]
    #     dst =  StateManagementUtil.PROJECT_PARENTS_DIRECTORY
    #     BusinessLogicUtil.move_pnxs_without_overwrite(pnxs=pnxs, dst=dst)
    #     BusinessLogicUtil.back_up_pnx_to_dst(src=StateManagementUtil.PROJECT_DIRECTORY, dst=StateManagementUtil.DESKTOP)

    @staticmethod
    def make_pkg(dst):
        """wsl rar   wsl unrar   bz.exe  의존 """
        pnxs_required = BusinessLogicUtil.get_list_pnxs_from_pnx(pnx=StateManagementUtil.PROJECT_DIRECTORY)
        exclude_paths = [
            rf"{StateManagementUtil.PROJECT_DIRECTORY}\.git",
            rf"{StateManagementUtil.PROJECT_DIRECTORY}\.idea",
            rf"{StateManagementUtil.PROJECT_DIRECTORY}\.venv",
            rf"{StateManagementUtil.PROJECT_DIRECTORY}\__pycache__",
        ]
        pnxs_required = [path for path in pnxs_required if path not in exclude_paths]

        # backup
        # BusinessLogicUtil.back_up_pnx_to_dst(src=StateManagementUtil.PROJECT_DIRECTORY, dst=StateManagementUtil.ARCHIVED)

        # del # 삭제됨...유의
        BusinessLogicUtil.move_pnx_to_trash_bin(src=dst)

        # make
        BusinessLogicUtil.make_pnx(pnx=dst, mode='d')

        # cp
        BusinessLogicUtil.copy_pnxs_with_overwrite(pnxs=pnxs_required, dst=dst)

        # compress
        BusinessLogicUtil.compress_pnx(src=dst, dst=StateManagementUtil.DESKTOP, with_timestamp=False)

        # del
        # BusinessLogicUtil.move_pnx_to_trash_bin(pnx=dst)

        # decompress
        # BusinessLogicUtil.decompress_pnx(src= rf"{dst}.rar", dst=StateManagementUtil.DESKTOP)

    @staticmethod
    def move_pnxs_without_overwrite(pnxs, dst):
        for pnx in pnxs:
            BusinessLogicUtil.move_pnx_without_overwrite(src=pnx, dst=dst)

    @staticmethod
    def get_list_pnxs_from_pnx(pnx, with_walking=False):
        if not os.path.exists(pnx):
            print(f"The directory '{pnx}' does not exist.")

        if not os.path.isdir(pnx):
            print(f"The path '{pnx}' is not a directory.")
        pnxs = []
        if with_walking == True:
            for root, dirs, files in os.walk(pnx):
                for directory in dirs:
                    pnxs.append(os.path.join(root, directory))
                for file in files:
                    pnxs.append(os.path.join(root, file))
            return pnxs
        if with_walking == False:
            if os.path.exists(pnx) and os.path.isdir(pnx):
                pnxs = [os.path.join(pnx, item) for item in os.listdir(pnx)]
            return pnxs

    @staticmethod
    def copy_pnxs_without_overwrite(pnxs, dst):
        for pnx in pnxs:
            BusinessLogicUtil.copy_pnx_without_overwrite(pnx=pnx, dst=dst)

    @staticmethod
    def copy_pnxs_with_overwrite(pnxs, dst):
        for pnx in pnxs:
            BusinessLogicUtil.copy_pnx_with_overwrite(src=pnx, dst=dst)

    @staticmethod
    def copy_pnx_without_overwrite(pnx, dst):
        BusinessLogicUtil.print_as_log(string=rf'''pnx="{pnx}" %%%FOO%%%''')
        BusinessLogicUtil.print_as_log(string=rf'''dst="{dst}" %%%FOO%%%''')
        if not os.path.exists(pnx):
            print(f"소스 경로 '{pnx}'가 존재하지 않습니다.")
            return

        if not os.path.exists(dst):
            BusinessLogicUtil.make_pnx(pnx=pnx, mode='d')
        if os.path.isfile(pnx):
            shutil.copy2(pnx, dst)
            print(f"파일 '{pnx}'을(를) '{dst}'로 복사했습니다.")
        elif os.path.isdir(pnx):
            try:
                pnx_p = os.path.dirname(pnx)
                time_pattern_with_underbar = rf"_{BusinessLogicUtil.get_time_as_('now')}"
                pnx_n = BusinessLogicUtil.get_n(pnx)
                pnx_x = BusinessLogicUtil.get_x(pnx)
                pnx_new = rf"{dst}\{pnx_n}{pnx_x}"
                pattern = r'\d{4}_\d{2}_\d{2}_(월|화|수|목|금|토|일)_\d{2}_\d{2}_\d{2}_\d{3}'
                pnx_n = re.sub(pattern=pattern, repl='', string=pnx_n)
                BusinessLogicUtil.print_as_log(string=rf'''pnx="{pnx}" %%%FOO%%%''')
                BusinessLogicUtil.print_as_log(string=rf'''dst="{dst}" %%%FOO%%%''')
                dst_nx = None
                if not BusinessLogicUtil.does_pnx_exist(src=pnx_new, show_mode=False):
                    dst_nx = rf"{dst}\{pnx_n}{pnx_x}"
                else:
                    dst_nx = rf"{dst}\{pnx_n}{time_pattern_with_underbar}{random.randint(10, 99)}{pnx_x}"
                shutil.copytree(src=pnx, dst=dst_nx)
            except:
                BusinessLogicUtil.print_light_black(f"{traceback.format_exc()}")
        else:
            print(f"소스 경로 '{pnx}'는 파일도 디렉토리도 아닙니다.")

    @staticmethod
    def get_str_from_list(items_list, delimiter=", ", prefix="", suffix=""):
        if not isinstance(items_list, list):
            raise ValueError("Input must be a list.")

        if not all(isinstance(item, str) for item in items_list):
            raise ValueError("All elements in the list must be strings.")

        return f"{prefix}{delimiter.join(items_list)}{suffix}"

    @staticmethod
    def download_torrent_magnets_from_nyaa_si(title_to_search=None, from_no=None, to_no=None, driver_selenium=None, debug_mode=False, via_txt_f=False, with_torrent_f_existance_check_mode=True):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        function_name_txt = rf'{StateManagementUtil.PROJECT_DIRECTORY}\pkg_txt\download_torrent_magnets_from_nyaa_si.txt'

        if via_txt_f or (title_to_search is not None and from_no is not None and to_no is not None):
            print(rf"{function_name}() 동작 조건 충족")
        else:
            print(rf"{function_name}() 동작 조건 불충족")
            return

        include_elements_all = ['1080']
        include_elements_any = ['SubsPlease', 'Moozzi']
        exclude_elements_all = ["[New-raws]", "[LoliHouse]", "[Erai-raws]", "[Koi-Raws]", '[EMBER]', '[Lilith-Raws]', '[Yameii]', '[ASW]', '[shincaps]', '[AsukaRaws]']

        if debug_mode == True:
            BusinessLogicUtil.print_as_log(string=rf'''include_elements_all="{include_elements_all}" %%%FOO%%%''')
            BusinessLogicUtil.print_as_log(string=rf'''include_elements_any="{include_elements_any}" %%%FOO%%%''')
            BusinessLogicUtil.print_as_log(string=rf'''exclude_elements_all="{exclude_elements_all}" %%%FOO%%%''')

        # 백업
        function_name_back_up_txt = rf'{StateManagementUtil.PROJECT_DIRECTORY}\pkg_txt\download_torrent_magnets_from_nyaa_si.txt.bkp'
        txts = BusinessLogicUtil.get_list_from_f_txt(pnx=function_name_txt)
        txts = BusinessLogicUtil.get_list_striped_element(items_list=txts)
        with open(function_name_back_up_txt, 'a', encoding='utf-8') as file:
            file.write(f"{StateManagementUtil.UNDERLINE}\n")
            for text in txts:
                file.write(text + "\n")
        # BusinessLogicUtil.run_pnx_via_explorer_exe(function_name_back_up_txt, print_mode=False)
        # BusinessLogicUtil.pause()


        if driver_selenium is None:
            driver_selenium = BusinessLogicUtil.get_driver_selenium(browser_show_mode=False)
        # 실행
        # if not BusinessLogicUtil.does_pnx_exist(src=function_name_txt):
        #     BusinessLogicUtil.make_pnx(src=function_name_txt, mode="f")
        # if BusinessLogicUtil.does_pnx_exist(src=function_name_txt):
        #     command = rf'explorer "{function_name_txt}" '
        #     BusinessLogicUtil.command_to_os(cmd=command, show_mode=False, mode="a")

        magnets_set = set()
        titles_to_search_list = []
        if via_txt_f:
            txts = BusinessLogicUtil.get_list_from_f_txt(pnx=function_name_txt)
        elif (title_to_search is not None and from_no is not None and to_no is not None):
            for i in range(from_no, to_no):
                titles_to_search_list.append(rf"{title_to_search} {str(i).zfill(2)}")
            txts = titles_to_search_list
        txts = BusinessLogicUtil.get_list_striped_element(items_list=txts)
        txts = BusinessLogicUtil.get_list_removed_element_duplicated(items_list=txts)
        items = txts
        for item in items:
            title_to_search = item
            magnets_set_from_nyaa_si = BusinessLogicUtil.get_torrent_magnets_set_from_nyaa_si(title_to_search=title_to_search, driver_selenium=driver_selenium, exclude_elements_all=exclude_elements_all, include_elements_any=include_elements_any, include_elements_all=include_elements_all)
            magnets_set = magnets_set | magnets_set_from_nyaa_si

        if with_torrent_f_existance_check_mode == True:
            # magnets_set 에서  magnet 제거 (.torrent 파일이 있는 경우)
            pnxs_interested = [
                rf'{StateManagementUtil.USERPROFILE}\AppData\Roaming\bittorrent',
            ]
            string_exclude = [
                rf'.dat', rf'.dll', rf'.exe', rf'.dmp', rf'.lng', rf'.zip'
                              ]
            pnx_list = BusinessLogicUtil.get_pnx_list_interested_from_file_system(pnxs_interested=pnxs_interested, string_exclude=string_exclude)
            pnx_list_interested = BusinessLogicUtil.get_list_interested_from_list(item_list=pnx_list, extension_list_include=[".torrent"])
            pnx_list_interested = BusinessLogicUtil.get_list_replaced_element_from_str_to_str(item_list=pnx_list_interested, from_str=f'C:\\Users\\WIN10PROPC3\\AppData\\Roaming\\bittorrent\\', to_str='')
            pnx_list_interested = BusinessLogicUtil.get_list_replaced_element_from_str_to_str(item_list=pnx_list_interested, from_str=rf'.torrent', to_str='')
            pnx_list_interested = BusinessLogicUtil.get_url_list_encoded_element(item_list=pnx_list_interested)
            pnx_list_to_exclude = pnx_list_interested
            pnx_list_from_magnets_set = magnets_set
            pnx_list_required = [item for item in pnx_list_from_magnets_set if not any(exclude in item for exclude in pnx_list_to_exclude)]  # 제외
            magnets_set = BusinessLogicUtil.get_set_from_list(items_list=pnx_list_required)
            # BusinessLogicUtil.print_list_as_vertical(items_list=BusinessLogicUtil.get_list_url_decoded_element(magnets_set), items_list_name="BusinessLogicUtil.get_url_list_decoded_element(magnets_set)")

        for magnet in magnets_set:
            decoded_magnet = BusinessLogicUtil.get_decoded_url(magnet)
            BusinessLogicUtil.print_as_log(string=rf'''decoded_magnet="{decoded_magnet}" %%%FOO%%%''')
            BusinessLogicUtil.sleep(milliseconds=1000, show_mode=False)
            webbrowser.open(magnet)

            # 마그넷 다운로드 받은 것 기록제거
            string_downloaded = BusinessLogicUtil.get_decoded_url(string=magnet)
            string_downloaded = BusinessLogicUtil.get_str_replaced_from_pattern_to_patternless(string=string_downloaded, pattern=r'magnet:\?xt=urn:btih:[^&]+&dn=')
            string_downloaded = BusinessLogicUtil.get_str_replaced_from_pattern_to_patternless(string=string_downloaded, pattern='&tr=[^&]+')
            # texts_updated_list = []
            pnx_list = BusinessLogicUtil.get_list_from_f_txt(pnx=function_name_txt)
            if pnx_list is not None:
                for pnx in pnx_list:
                    pnx = pnx.strip()
                    if pnx in string_downloaded:

                        # 삭제 downloaded
                        pnx_list = BusinessLogicUtil.get_list_striped_element(items_list=pnx_list)
                        pnx_list.remove(pnx)
                        BusinessLogicUtil.write_list_to_f_txt(pnx=function_name_txt, texts=pnx_list, mode="w")

                        # 추가 to download
                        text_prefix = ""
                        string_downloaded = pnx
                        new_number = str(str(int(BusinessLogicUtil.get_last_digit(string_downloaded)) + 1).zfill(2)).strip()
                        text_removed_success_and_last_digit = BusinessLogicUtil.get_str_removed_last_digit(string_downloaded).strip()
                        BusinessLogicUtil.write_str_to_file(pnx=function_name_txt, txt_str=f"{text_prefix}{text_removed_success_and_last_digit} {new_number}\n", mode="a")

    @staticmethod
    def print_torrent_magnets_list_from_nyaa_si(title_to_search, from_no, to_no, driver_selenium=None, debug_mode=False):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        magnets_set = set()
        if driver_selenium is None:
            driver_selenium = BusinessLogicUtil.get_driver_selenium(browser_show_mode=False)

        for i in range(from_no, to_no):
            string_to_search = rf"{title_to_search} {str(i).zfill(2)}"
            BusinessLogicUtil.print_as_log(string=rf'''string_to_search="{string_to_search}" %%%FOO%%%''')
            torrent_magnets_set_from_nyaa_si = BusinessLogicUtil.get_torrent_magnets_set_from_nyaa_si(title_to_search=string_to_search, driver_selenium=driver_selenium)
            magnets_set = magnets_set | torrent_magnets_set_from_nyaa_si
        # BusinessLogicUtil.print_list_as_vertical(items_list=BusinessLogicUtil.get_list_url_decoded_element(item_list=magnets_set), items_list_name="%%%FOO%%%")

        magnets_set_filtered = set()
        for magnet in magnets_set:
            if BusinessLogicUtil.is_pattern_in_string(string=magnet, pattern=r'magnet:\?xt=urn:btih:[^&]+&dn='):
                magnet = BusinessLogicUtil.get_str_replaced_from_pattern_to_patternless(string=magnet, pattern=r'magnet:\?xt=urn:btih:[^&]+&dn=')
                magnets_set_filtered.add(magnet)
        # BusinessLogicUtil.print_list_as_vertical(items_list=BusinessLogicUtil.get_list_url_decoded_element(item_list=magnets_set_filtered), items_list_name="%%%FOO%%%")
        magnets_set_filtered = BusinessLogicUtil.get_list_url_decoded_element(item_list=magnets_set_filtered)
        magnets_set_filtered = BusinessLogicUtil.get_list_sorted_element(item_list=magnets_set_filtered)
        BusinessLogicUtil.print_list_as_vertical(items_list=magnets_set_filtered, items_list_name="%%%FOO%%%")
        BusinessLogicUtil.pause()

    @staticmethod
    def run_acu_update_v3_exe_and_login_and_run_autoa2zdrive_release_exe(data_required):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        AUTOA2ZDRIVE_RELEASE_SW_VERSION_EXE = rf"{StateManagementUtil.USERPROFILE}\Desktop\AutoA2zDrive\AutoA2ZDrive_Release_{data_required["SW 버전"]}.exe"
        BusinessLogicUtil.print_as_log(string=rf'''AUTOA2ZDRIVE_RELEASE_SW_VERSION_EXE="{AUTOA2ZDRIVE_RELEASE_SW_VERSION_EXE}" %%%FOO%%%''')
        window_title_seg = "acu_update_v3_exe"
        if not BusinessLogicUtil.does_pnx_exist(src=AUTOA2ZDRIVE_RELEASE_SW_VERSION_EXE, show_mode=False):
            acu_update_v3_exe = rf"{StateManagementUtil.USERPROFILE}\Desktop\AutoA2zDrive\ACU_update_v3.exe"
            acu_update_v3_exe_p = BusinessLogicUtil.get_p(pnx=acu_update_v3_exe)
            os.chdir(acu_update_v3_exe_p)
            command = rf' start cmd.exe /k "title {window_title_seg} && {StateManagementUtil.USERPROFILE}\Desktop\AutoA2zDrive\ACU_update_v3.exe &" '
            BusinessLogicUtil.command_to_os(cmd=command, mode="a")
            linux_pw = BusinessLogicUtil.get_token_from_text_file(token_file=rf'{StateManagementUtil.PKG_TXT}\token_linux_pw.txt', initial_token="")
            linux_id = BusinessLogicUtil.get_token_from_text_file(token_file=rf'{StateManagementUtil.PKG_TXT}\token_linux_id.txt', initial_token="")
            while True:
                BusinessLogicUtil.sleep(milliseconds=2000)
                if BusinessLogicUtil.is_window_open(window_title_seg=window_title_seg):
                    BusinessLogicUtil.move_window_to_front(window_title_seg=window_title_seg, show_mode=True)
                    BusinessLogicUtil.sleep(milliseconds=500)
                    BusinessLogicUtil.write_like_person(string=linux_id)
                    BusinessLogicUtil.press("enter")
                    BusinessLogicUtil.write_like_person(string=linux_pw)
                    BusinessLogicUtil.press("enter")
                    BusinessLogicUtil.write_like_person("2")
                    BusinessLogicUtil.press("enter")
                    BusinessLogicUtil.write_like_person(rf"{data_required["SW 버전"]}")
                    BusinessLogicUtil.press("enter")
                    break
        else:
            BusinessLogicUtil.run_autoa2zdrive_release_exe()

            # BusinessLogicUtil.sleep(milliseconds=15000)
            # while True: #via ocr
            #     # text_string 바운딩박스 클릭 # GPU 연산 지원여부..
            #     # text_string = "downloading : 100%"
            #     text_string = "Press Enter Key To Quit Program...."
            #     text_coordinates = BusinessLogicUtil.get_text_coordinates_via_easy_ocr(string=text_string)
            #     # text_coordinates = (692.0, 1047.5)
            #     if not text_coordinates:
            #         BusinessLogicUtil.sleep(milliseconds=30000)
            #     if text_coordinates:
            #         x_abs, y_abs = text_coordinates
            #         BusinessLogicUtil.move_mouse(x_abs=x_abs, y_abs=y_abs)
            #         BusinessLogicUtil.click_mouse_left_btn(x_abs=x_abs, y_abs=y_abs)
            #         BusinessLogicUtil.print_as_log(string = rf'''text_string="{text_string}" %%%FOO%%%''')
            #         break
            # img_pnx = rf"{StateManagementUtil.PROJECT_DIRECTORY}\pkg_image\screenshot_Press_Enter_Key_To_Quit_Program_2024_11_21_11_30_35.png"
            # BusinessLogicUtil.click_center_of_img_recognized_by_mouse_left(img_pnx=img_pnx, loop_limit_cnt=10)

    @staticmethod
    def run_autoa2zdrive_release_exe():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # autoa2zdrive_release_exe 실행 # via local file

        window_title_seg = "AutoA2Z Drive"
        timeout = 20
        start_time = time.time()
        while True:
            if not BusinessLogicUtil.is_window_open(window_title_seg=window_title_seg, show_mode=False):
                pnx = rf"{StateManagementUtil.DESKTOP}\AutoA2ZDrive\AutoA2ZDrive_Release.exe"
                command = rf' explorer "{pnx}" '
                BusinessLogicUtil.command_to_os(cmd=command, show_mode=False, mode="a")
            while True:
                if BusinessLogicUtil.is_window_open(window_title_seg=window_title_seg, show_mode=False):
                    break
                if time.time() - start_time > timeout:
                    break
                BusinessLogicUtil.sleep(seconds=1, show_mode=False)
            break

        # 자동닫힘 여부확인 # 40초 동안에
        timeout = 40
        start_time = time.time()
        while True:
            if not BusinessLogicUtil.is_window_open(window_title_seg=window_title_seg, show_mode=False):
                break
            if time.time() - start_time > timeout:
                break
            BusinessLogicUtil.sleep(seconds=1, show_mode=False)

        # 40초 동안에 안열리면 VS code 실행
        window_title_seg = "AutoA2ZDrive_Release.exe"
        timeout = 5
        start_time = time.time()
        while True:
            if not BusinessLogicUtil.is_window_open(window_title_seg=window_title_seg, show_mode=False):
                command = rf' explorer "C:\Program Files (x86)\Microsoft Visual Studio\2019\Professional\Common7\IDE\devenv.exe" '
                BusinessLogicUtil.command_to_os(cmd=command, show_mode=False, mode="a")
                break
            while True:
                if BusinessLogicUtil.is_front_window_title(window_title_seg=window_title_seg):
                    BusinessLogicUtil.move_window_to_front(window_title_seg=window_title_seg, show_mode=True)
                    break
            BusinessLogicUtil.print_as_log(string=time.time() - start_time)
            if time.time() - start_time > timeout:
                break
            BusinessLogicUtil.sleep(milliseconds=1000, show_mode=False)

    @staticmethod
    def run_autoa2z_drive():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        window_title_seg = "AutoA2Z Drive"
        timeout = 5
        start_time = time.time()
        while True:
            if time.time() - start_time > timeout:
                break
            if not BusinessLogicUtil.is_window_open(window_title_seg=window_title_seg, show_mode=False):
                window_title_seg = "git log"
                BusinessLogicUtil.chdir(dst=rf"{StateManagementUtil.USERPROFILE}\source\repos\ms_proto_drive")
                command = rf' start cmd.exe /k "title {window_title_seg} && git log" '
                BusinessLogicUtil.print_as_log(string=rf'''command="{command}" %%%FOO%%%''')
                BusinessLogicUtil.command_to_os(cmd=command, show_mode=False, mode="a")
                break
            BusinessLogicUtil.sleep(milliseconds=1000, show_mode=False)

    @staticmethod
    def quit_autoa2z_drive():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        window_title_seg = "AutoA2Z Drive"
        timeout = 5
        start_time = time.time()
        while True:
            if time.time() - start_time > timeout:
                break
            if BusinessLogicUtil.is_window_open(window_title_seg=window_title_seg, show_mode=False):
                window_title_seg = "AutoA2ZDrive_Release.exe"
                while True:
                    pid = BusinessLogicUtil.get_pid_by_window_title_via_tasklist(window_title_seg=window_title_seg)
                    if BusinessLogicUtil.is_number_v2(value_string=pid):
                        # command = rf' taskkill /f /pid {pid} '
                        # BusinessLogicUtil.command_to_os_like_person(command=command, admin_mode=True) # fail
                        # BusinessLogicUtil.command_to_os_like_person_as_admin(command=command, show_mode=True)

                        command = rf' Stop-Process -Id {pid} -Force'
                        BusinessLogicUtil.run_command_via_powershell_exe(command=command, show_mode=True)
                        BusinessLogicUtil.write_like_person(string='exit')
                        BusinessLogicUtil.press("enter")
                    else:
                        break

                break
            else:
                break

    @staticmethod
    def get_pid_by_window_title_via_tasklist(window_title_seg):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            command = rf'tasklist'
            lines = BusinessLogicUtil.command_to_os(cmd=command)
            matching_lines = None
            for line in lines:
                if window_title_seg in line:
                    matching_lines = line

            pids = []
            parts = matching_lines.split()
            if len(parts) > 1 and window_title_seg in parts[0]:
                pids.append(parts[1])

            if len(pids) == 1:
                return pids[0]
            else:
                return pids
        except Exception as e:
            return str(e)

    @staticmethod
    def get_pid_by_window_title(window_title_seg):  # 테스트필요
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # window_titles = pygetwindow.getAllTitles()
        window_titles = BusinessLogicUtil.get_window_titles()
        matching_window = [w for w in window_titles if window_title_seg.lower() in w.lower()]

        if not matching_window:
            return f"No window found with title containing: '{window_title_seg}'"

        # Assuming the first match
        window_title_match = matching_window[0]
        print(f"Found window: {window_title_match}")

        import psutil
        for process in psutil.process_iter(['pid', 'name']):
            try:
                process_name = process.info['name']
                process_id = process.info['pid']
                process_window_titles = pygetwindow.getWindowsWithTitle(window_title_match)

                BusinessLogicUtil.print_as_log(string=f'process_name="{process_name}" %%%FOO%%%')
                BusinessLogicUtil.print_as_log(string=f'process_id="{process_id}" %%%FOO%%%')
                BusinessLogicUtil.print_as_log(string=f'process_window_titles="{process_window_titles}" %%%FOO%%%')

                if process_window_titles:
                    return process_id
            except (psutil.NoSuchProcess, psutil.AccessDenied) as e:
                BusinessLogicUtil.print_as_log(string=f"Error processing {process.info['pid']}: {e}")
                continue
        return f"No PID found for window title: '{window_title_match}'"

    @staticmethod
    def is_number_v2(value_string):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        try:
            float(value_string)  # 숫자 형태로 변환을 시도
            return True
        except ValueError:
            return False

    @staticmethod
    def get_pnx_unix_style(pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        pnx = pnx.replace(f"\\", rf"/")
        return pnx

    @staticmethod
    def get_pnx_unix_style_for_wsl(pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        pnx = pnx.replace(f"\\", rf"/")
        pnx = pnx.replace(f"C:/", rf"/mnt/c/")
        return pnx

    @staticmethod
    def compress_pnx_via_zip(pnx_zip, src):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        cmd = f'bz.exe c "{pnx_zip}" "{src}"'
        BusinessLogicUtil.command_to_os(cmd=cmd)

    @staticmethod
    def decompress_pnx(src, dst):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        # Validate the source file
        if not os.path.exists(src):
            raise FileNotFoundError(f"Source file not found: {src}")

        if not src.lower().endswith('.rar'):
            raise ValueError("The source file must be a .rar file")

        # Ensure the destination directory exists
        if not os.path.exists(dst):
            os.makedirs(dst)

        # Convert paths to WSL format
        src_wsl = BusinessLogicUtil.get_pnx_unix_style_for_wsl(pnx=src)
        dst_wsl = BusinessLogicUtil.get_pnx_unix_style_for_wsl(pnx=dst)

        # Decompress
        try:
            cmd = f"wsl rar x {src_wsl} {dst_wsl}"
            BusinessLogicUtil.command_to_os(cmd=cmd)

        except Exception as e:
            raise RuntimeError(f"Failed to decompress the .rar file: {e}")

    @staticmethod
    def get_pnx_windows_style(pnx):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        pnx = pnx.replace(rf"//", f"/")
        pnx = pnx.replace(rf"/", f"\\")
        pnx = pnx.replace(rf"/mnt/c/", f"C:/")
        pnx = pnx.replace(rf"/mnt/d/", f"D:/")
        pnx = pnx.replace(rf"/mnt/e/", f"E:/")
        pnx = pnx.replace(rf"/mnt/f/", f"F:/")
        return pnx

    @staticmethod
    def get_dict_removed_element_duplicated(item_dict):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        seen_values = set()
        unique_dict = {}
        for key, value in item_dict.items():
            if value not in seen_values:
                unique_dict[key] = value
                seen_values.add(value)
        return unique_dict

    @staticmethod
    def get_pnx_list_interested_from_file_system(pnxs_interested=None, string_exclude=None):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        function_name_txt = rf"{StateManagementUtil.PKG_TXT}\make_pnxs_interested_to_text_file.txt"

        if pnxs_interested is None:
            # todo make_pnxs_interested_to_text_file_x 파일이 없으면 만들도록
            BusinessLogicUtil.make_pnxs_interested_to_text_file_x(pnxs_interested=pnxs_interested, string_exclude=string_exclude)

            # PKG_TXT = rf"{StateManagementUtil.PKG_TXT}"
            # window_title_seg = BusinessLogicUtil.get_nx(PKG_TXT)
            # if not BusinessLogicUtil.is_window_open(window_title_seg=window_title_seg):
            #     BusinessLogicUtil.open_window_by_pnx(pnx=PKG_TXT)
        else:
            BusinessLogicUtil.make_pnxs_interested_to_text_file(pnxs_interested=pnxs_interested, string_exclude=string_exclude)

            # window_title_seg = BusinessLogicUtil.get_nx (function_name_txt)
            # if not BusinessLogicUtil.is_window_open(window_title_seg=window_title_seg):
            #     BusinessLogicUtil.open_window_by_pnx(pnx=function_name_txt)

        return BusinessLogicUtil.get_list_from_f_txt(pnx=function_name_txt)

    @staticmethod
    def get_list_url_decoded_element(item_list, show_mode=True):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        function_name = inspect.currentframe().f_code.co_name
        if show_mode == False:
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        return [urllib.parse.unquote(item) for item in item_list]

    @staticmethod
    def get_url_list_encoded_element(item_list, show_mode=True):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        import urllib.parse
        function_name = inspect.currentframe().f_code.co_name
        if not show_mode:
            BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        return [urllib.parse.quote(item) for item in item_list]

    @staticmethod
    def get_set_from_list(items_list):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        return set(items_list)

    @staticmethod
    def get_webdriver_options_customed(browser_show=True):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        # import selenium.webdriver as webdriver
        from selenium.webdriver.chrome.options import Options

        # Chrome 옵션 설정
        options = Options()
        # options = webdriver.ChromeOptions()

        # 셀레니움 브라우저 show 설정
        if browser_show == True:
            # options.add_argument('--headless')
            pass
        elif browser_show == False:
            options.add_argument('--headless')
        # options.add_argument('--window-size=3440x1440')
        # options.add_argument('--window-size=1920x1080')
        # options.add_argument("window-size=1200x600")
        # options.add_argument("window-size=1210x630")
        # options.add_argument('--window-size=800x800')
        # size 하드코딩 되어 있는 부분을 pyautogui 에서 size() 로 대체하는 것이 좋겠다.

        # 셀레니움 브라우저 언어
        options.add_argument("lang=ko_KR")

        # UserAgent
        # https://www.whatismybrowser.com/detect/what-is-my-user-agent/
        user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"
        BusinessLogicUtil.print_as_log(f'''user_agent={user_agent}''')
        options.add_argument(f"user-agent={user_agent}")

        options.add_argument("--disable-blink-features=AutomationControlled")  # 자동화 감지 비활성화
        options.add_experimental_option("excludeSwitches", ["enable-automation"])  # 자동화 스위치 비활성화
        options.add_experimental_option("useAutomationExtension", False)  # 자동화 확장 비활성화

        # Chrome 기본 프로필
        # profile_path = rf'{StateManagementUtil.USER_PROFILE}\AppData\Local\Google\Chrome\User Data'
        # options.add_argument(f"user-data-dir={profile_path}")
        # options.add_argument("profile-directory=Default")

        return options

    @staticmethod
    def get_driver_selenium(browser_show_mode):
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
        import selenium.webdriver as webdriver

        # 드라이버 옵션
        options = BusinessLogicUtil.get_webdriver_options_customed(browser_show=browser_show_mode)

        # 드라이버 as 크롬브라우저
        driver = webdriver.Chrome(options=options)
        # service = Service('path/to/chromedriver')  # 크롬 드라이버 경로
        # driver = webdriver.Chrome(service=service, options=options)

        # 브라우저 실행
        driver.get('about:blank')
        # driver.get('http://www.naver.com')

        # driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5]}})")  # hide plugin 0EA
        # driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")  # hide own lanuages
        # driver.execute_script("const getParameter = WebGLRenderingContext.getParameter;WebGLRenderingContext.prototype.getParameter = function(parameter) {if (parameter === 37445) {return 'NVIDIA Corporation'} if (parameter === 37446) {return 'NVIDIA GeForce GTX 980 Ti OpenGL Engine';}return getParameter(parameter);};")  # hide own gpu # WebGL렌더러를 Nvidia회사와 GTX980Ti엔진인 ‘척’ 하는 방법입니다.

        # 플러그인 언어 소유GPU 숨기기
        driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5]}});")
        # driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}});")
        driver.execute_script(
            "const getParameter = WebGLRenderingContext.getParameter; WebGLRenderingContext.prototype.getParameter = function(parameter) { if (parameter === 37445) { return 'NVIDIA Corporation'; } if (parameter === 37446) { return 'NVIDIA GeForce GTX 980 Ti OpenGL Engine'; } return getParameter(parameter); };")
        return driver

    @staticmethod
    def install_wsl(wsl_linux_version):
        if not BusinessLogicUtil.is_wsl_linux_installed(wsl_linux_version=wsl_linux_version):
            # todo install       wsl --install
            # todo install       wsl --install -d {wsl_linux_version}
            pass

    @staticmethod
    def run_wsl(wsl_linux_version, wsl_window_title_seg):
        # install wsl
        # BusinessLogicUtil.install_wsl(wsl_linux_version)

        if not BusinessLogicUtil.is_window_open(window_title_seg=wsl_window_title_seg):
            BusinessLogicUtil.run_ubuntu_via_wsl(wsl_linux_version=wsl_linux_version, window_title_seg=wsl_window_title_seg)
        while True:
            if BusinessLogicUtil.is_front_window_title(window_title_seg=wsl_window_title_seg):
                break
            BusinessLogicUtil.move_window_to_front(window_title_seg=wsl_window_title_seg)

    @staticmethod
    def cd_in_wsl(wsl_linux_version, wsl_window_title_seg, dst):
        BusinessLogicUtil.run_wsl(wsl_linux_version, wsl_window_title_seg)
        BusinessLogicUtil.copy_and_paste_with_keeping_clipboard(string=dst, wsl_mode=True)
        BusinessLogicUtil.press('enter')
        pwd = BusinessLogicUtil.get_pwd_in_wsl(wsl_linux_version=wsl_linux_version, wsl_window_title_seg=wsl_window_title_seg)
        BusinessLogicUtil.print_as_log(string=rf'''pwd="{pwd}" %%%FOO%%%''')
        if dst != pwd:
            BusinessLogicUtil.print_as_log(f'''"{dst}가 없습니다."''', print_color='red')
        else:
            BusinessLogicUtil.print_as_log(f'''"{dst}로 이동했습니다."''', print_color='blue')

    @staticmethod
    def get_pwd_in_wsl(wsl_linux_version, wsl_window_title_seg):
        BusinessLogicUtil.run_wsl(wsl_linux_version, wsl_window_title_seg)
        BusinessLogicUtil.copy_and_paste_with_keeping_clipboard(string='pwd | clip.exe', wsl_mode=True)
        BusinessLogicUtil.press('enter')
        return BusinessLogicUtil.paste()

    @staticmethod
    def paste():
        return clipboard.paste()

    @staticmethod
    def run_command_in_wsl(wsl_linux_version, wsl_window_title_seg, command, clip_mode=False):
        BusinessLogicUtil.run_wsl(wsl_linux_version=wsl_linux_version, wsl_window_title_seg=wsl_window_title_seg)
        if clip_mode == False:
            BusinessLogicUtil.copy_and_paste_with_keeping_clipboard(string=command, wsl_mode=True)
        else:
            BusinessLogicUtil.copy_and_paste_with_keeping_clipboard(string=rf'{command} | clip.exe', wsl_mode=True)
            BusinessLogicUtil.sleep(milliseconds=1000)
        BusinessLogicUtil.press('enter')
        return BusinessLogicUtil.paste()

    @staticmethod
    def test_wsl_util():
        # BusinessLogicUtil.install_wsl(wsl_linux_version)
        #
        # BusinessLogicUtil.run_wsl(wsl_linux_version=wsl_linux_version,wsl_window_title_seg=f"{token_users}@{StateManagementUtil.HOSTNAME}")
        #
        # wsl_command = rf"cd"
        # BusinessLogicUtil.run_command_in_wsl(wsl_linux_version=wsl_linux_version, wsl_window_title_seg=f"{token_users}@{StateManagementUtil.HOSTNAME}", command=wsl_command)
        #
        # dst = "~/Downloads/test/test/test"
        # wsl_command = rf"mkdir -p {dst}"
        # BusinessLogicUtil.run_command_in_wsl(wsl_linux_version=wsl_linux_version, wsl_window_title_seg=f"{token_users}@{StateManagementUtil.HOSTNAME}", command=wsl_command)
        #
        # dst = "~/Downloads/test/test/test/test"
        # wsl_command = rf"cd {dst}"
        # BusinessLogicUtil.run_command_in_wsl(wsl_linux_version=wsl_linux_version, wsl_window_title_seg=f"{token_users}@{StateManagementUtil.HOSTNAME}", command=wsl_command)
        #
        # # cd in wsl
        # # dst = "~/Downloads/flash/"
        # # BusinessLogicUtil.cd_in_wsl(wsl_linux_version=wsl_linux_version, wsl_window_title_seg=f"{token_users}@{StateManagementUtil.HOSTNAME}", dst=dst)
        #
        # # cd in wsl
        # # dst = "~/Downloads/flash/xc_flash/Linux_for_Tegra/"
        # # BusinessLogicUtil.cd_in_wsl(wsl_linux_version=wsl_linux_version, wsl_window_title_seg=f"{token_users}@{StateManagementUtil.HOSTNAME}", dst="~/Downloads/flash/")
        #
        # wsl_command = rf"pwd"
        # pwd = BusinessLogicUtil.run_command_in_wsl(wsl_linux_version=wsl_linux_version, wsl_window_title_seg=f"{token_users}@{StateManagementUtil.HOSTNAME}", command=wsl_command, clip_mode=True)
        # BusinessLogicUtil.print_as_log(string = rf'''pwd="{pwd}" %%%FOO%%%''')
        #
        # dst = "~/Downloads/test"
        # wsl_command = rf"rm -rf {dst}"
        # BusinessLogicUtil.run_command_in_wsl(wsl_linux_version=wsl_linux_version, wsl_window_title_seg=f"{token_users}@{StateManagementUtil.HOSTNAME}", command=wsl_command)
        #
        # wsl_command = rf"exit"
        # BusinessLogicUtil.run_command_in_wsl(wsl_linux_version=wsl_linux_version, wsl_window_title_seg=f"{token_users}@{StateManagementUtil.HOSTNAME}", command=wsl_command)
        #
        # command = "exit"
        # BusinessLogicUtil.command_to_os_like_person(command=command, admin_mode=True)
        #
        # # command = "wsl --shutdown"
        # # BusinessLogicUtil.command_to_os_like_person(command=command, admin_mode=True)
        #
        # # BusinessLogicUtil.process_kill_wsl_exe()
        pass

    @staticmethod
    def test_cmd_util():
        # command = "HOSTNAME"
        # temp = BusinessLogicUtil.command_to_os_like_person(command=command, admin_mode=True)
        # BusinessLogicUtil.print_as_log(string = rf'''temp="{temp}" %%%FOO%%%''')

        # ___________________________________________________________________________ 스크립트 파일생성
        # script_nx = "park4139_temp.bat"
        # commands = [
        #     "hostname",
        #         rf"""
        # hostname
        # ping google.com
        # hostname
        # hostname
        # hostname
        # hostname
        # hostname
        #         """,
        #     ]
        # BusinessLogicUtil.create_script_file(commands=commands, script_nx=script_nx)
        # # ___________________________________________________________________________ 스크립트 파일확인
        # command = rf"type {script_nx}"
        # BusinessLogicUtil.command_run_via_cmd(command=command, window_title_seg=window_title_seg)
        # # ___________________________________________________________________________ 스크립트 파일실행
        # command = rf"{script_nx}"
        # BusinessLogicUtil.command_run_via_cmd(command=command, window_title_seg=window_title_seg)
        # # ___________________________________________________________________________ 스크립트 파일삭제
        # command = rf"echo y | del {script_nx}"
        # BusinessLogicUtil.command_run_via_cmd(command=command, window_title_seg=window_title_seg)
        # # ___________________________________________________________________________ 스크립트 파일삭제
        # import os
        # if os.path.exists(script_nx):
        #     os.remove(script_nx)
        #     print(f"{script_nx} 파일이 삭제되었습니다.")
        # # ___________________________________________________________________________
        pass

    @staticmethod
    def test_explorer_util():
        # 탐색기 # 부분영역검색
        # pnxs_interested = [
        #     rf'{StateManagementUtil.USERPROFILE}\AppData\Roaming\bittorrent',
        # ]
        # string_exclude = [
        #     rf'.dat',
        #     rf'.dll',
        #     rf'.exe',
        #     rf'.dmp',
        #     rf'.lng',
        # ]
        # pnx_list = BusinessLogicUtil.get_pnx_list_interested_from_file_system(pnxs_interested=pnxs_interested, string_exclude=string_exclude)
        # pnx_list = BusinessLogicUtil.get_list_interested_from_list(item_list=pnx_list,  extension_list_include=[".torrent"])
        # BusinessLogicUtil.print_list_as_vertical(items_list=pnx_list, items_list_name="pnx_list")
        # string_list_include_any = [
        #     'ONE PIECE - 1123',
        #     'Boku no Hero Academia - 160',
        #     'Re Zero kara Hajimeru Isekai Seikatsu - 59',
        #     'Dungeon ni Deai wo Motomeru no wa Machigatteiru Darou ka S5 - 09',
        #     'Dragon Ball Daima - 08',
        #     'Sword Art Online Alternative - Gun Gale Online S2 - 09',
        #     'Ao no Exorcist - Yuki no Hate-hen - 09',
        #     'Dandadan - 11',
        #     'Amagami-san Chi no Enmusubi - 10',
        #     'Seirei Gensouki 2 - 01',
        # ]
        # pnx_list = BusinessLogicUtil.get_list_interested_from_list(item_list=pnx_list,  string_list_include_any=string_list_include_any)
        # BusinessLogicUtil.print_list_as_vertical(items_list=pnx_list, items_list_name="pnx_list")

        # 탐색기 # 전체영역검색
        # BusinessLogicUtil.get_pnx_list_found_from_file_system()
        # BusinessLogicUtil.find_pnxs_interested_from_text_file(including_texts=["심야 괴담회", "심야괴담회"], exclude_texts=[], including_extensions=[".torrent"], except_extensions=[])
        # pnxs_required = BusinessLogicUtil.get_found_pnxs_interested_from_text_file(including_texts=["심야 괴담회", "심야괴담회"], exclude_texts=[], including_extensions=[".torrent"], except_extensions=[])
        # pnxs_required = BusinessLogicUtil.get_list_replaced_element_from_str_to_str(items=pnxs_required, from_str="심야 괴담회", to_str="심야괴담회")
        # pnxs_required = BusinessLogicUtil.get_list_replaced_element_from_str_to_str(items=pnxs_required, from_str=rf"C:\Users\WIN10PROPC3\AppData\Roaming\bittorrent", to_str="")
        # pnxs_required = BusinessLogicUtil.get_list_replaced_element_from_str_to_str(items=pnxs_required, from_str="시즌4", to_str="4")
        # pnxs_required = BusinessLogicUtil.get_list_replaced_element_from_str_to_str(items=pnxs_required, from_str="심야괴담회 4", to_str="심야괴담회4")
        # pnxs_required = BusinessLogicUtil.get_list_replaced_element_from_pattern_to_patternless(items=pnxs_required, pattern=r"\.\d{6}\.720p-NEXT")
        # pnxs_required = BusinessLogicUtil.get_list_replaced_element_from_pattern_to_patternless(items=pnxs_required, pattern=r"\.\d{6}\.1080p-NEXT")
        # pnxs_required = BusinessLogicUtil.get_list_replaced_element_from_pattern_to_patternless(items=pnxs_required, pattern=r"\.\d{6}\.1080p\.WANNA")
        # pnxs_required = BusinessLogicUtil.get_list_replaced_element_from_pattern_to_patternless(items=pnxs_required, pattern=r"\.\d{6}\.1080p\.H264-F1RST")
        # pnxs_required = BusinessLogicUtil.get_list_replaced_element_from_pattern_to_patternless(items=pnxs_required, pattern=rf"^\\") # \로 시작하는 부분 삭제
        # pnxs_required = BusinessLogicUtil.get_list_removed_element_duplicated(items=pnxs_required)
        # pnxs_required = BusinessLogicUtil.get_list_sorted_element(items=pnxs_required, mode="asc")
        # BusinessLogicUtil.print_list_as_vertical(items_list=pnxs_required, items_name="pnxs_required")
        # pnxs_required = BusinessLogicUtil.get_found_pnxs_interested_from_text_file(including_texts=["ONE PIECE", "ONEPIECE", "one piece", "onepiece", "One Piece", "Onepiece"], exclude_texts=[], including_extensions=[], except_extensions=[".torrent",".jpg",".jpeg",".png",".PNG"])
        # pnxs_required = BusinessLogicUtil.get_list_replaced_element_from_str_to_str(items=pnxs_required, from_str="ONE PIECE", to_str="ONEPIECE")
        # pnxs_required = BusinessLogicUtil.get_list_replaced_element_from_str_to_str(items=pnxs_required, from_str="ONEPIECE 4", to_str="ONEPIECE4")
        # pnxs_required = BusinessLogicUtil.get_list_replaced_element_from_pattern_to_patternless(items=pnxs_required, pattern=r"\.\d{6}\.720p-NEXT")
        # pnxs_required = BusinessLogicUtil.get_list_replaced_element_from_pattern_to_patternless(items=pnxs_required, pattern=r"\.\d{6}\.1080p-NEXT")
        # pnxs_required = BusinessLogicUtil.get_list_replaced_element_from_pattern_to_patternless(items=pnxs_required, pattern=r"\.\d{6}\.1080p\.WANNA")
        # pnxs_required = BusinessLogicUtil.get_list_replaced_element_from_pattern_to_patternless(items=pnxs_required, pattern=r"\.\d{6}\.1080p\.H264-F1RST")
        # pnxs_required = BusinessLogicUtil.get_list_replaced_element_from_pattern_to_patternless(items=pnxs_required, pattern=rf"^\\") # \로 시작하는 부분 삭제
        # pnxs_required = BusinessLogicUtil.get_list_removed_element_duplicated(items=pnxs_required)
        # pnxs_required = BusinessLogicUtil.get_list_sorted_element(items=pnxs_required, mode="asc")
        # BusinessLogicUtil.print_list_as_vertical(items_list=pnxs_required, items_name="pnxs_required")
        # BusinessLogicUtil.print_as_log(string = rf'''len(pnxs_required)="{len(pnxs_required)}" %%%FOO%%%''')
        pass

    @staticmethod
    def test_string_handling():
        # %%%FOO%%% 부분 autofill dev tool 적용 # todo

        # mkr_로깅 (시간, 객체, 함수, 필드)
        # class command_modes():
        #     cli = 'cli'
        #     gui = 'gui'
        #     startup = 'startup'
        #     scheduler = 'scheduler'
        #     sequence = 'test'
        # BusinessLogicUtil.print_class_field_and_value(class_name=command_modes)

        # mkr_텍스트 변환
        # text = r"""
        # python -m PyInstaller -i ".\pkg_png\icon.PNG" console_blurred.py
        # """
        # BusinessLogicUtil.print_text_converted(text=text)

        # mkr_텍스트 변환
        # texts = [
        #     # rf'echo y | rmdir /s "{}"',
        #     # rf'echo y | del /f "{}"',
        #     rf".\dist\console_blurred\console_blurred.exe"
        # ]
        # for text in texts:
        #     BusinessLogicUtil.print_and_get_text_converted(text = text)
        pass

    @staticmethod
    def command_to_remote_os(command, users, ip, wsl_linux_version, wsl_window_title_seg, pw, exit_mode):

        # sudo visudo
        # rf"{users} ALL=(ALL) NOPASSWD: /sbin/reboot"

        BusinessLogicUtil.ssh(users=users, ip=ip, wsl_linux_version=wsl_linux_version, wsl_window_title_seg=wsl_window_title_seg, pw=pw, exit_mode=exit_mode)

        BusinessLogicUtil.command_to_wsl_os_like_person(command, wsl_linux_version=wsl_linux_version, wsl_window_title_seg=wsl_window_title_seg)

    @staticmethod
    def play_my_video_track():
        function_name = inspect.currentframe().f_code.co_name
        BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')

        # BusinessLogicUtil.command_to_os(command=rf'taskkill /f /im "PotPlayer64.exe" ', show_mode=False)

        # 보던 거 재생
        # 바탕화면에 있는 PotPlayer64.dpl 를 pkg_video에 복사
        BusinessLogicUtil.make_pnx(pnx=StateManagementUtil.PKG_VIDEO_POTPLAYER64_DPL, mode='f')
        BusinessLogicUtil.command_to_os(cmd=rf'explorer "{StateManagementUtil.PKG_VIDEO_POTPLAYER64_DPL}" ', show_mode=False)

        # 보지않은 거 틀기
        # classifying 안의 비디오들 재생
        pass

    @staticmethod
    def remmina(users, ip, wsl_linux_version, wsl_window_title_seg, pw, exit_mode):
        command = 'wsl sudo apt update'
        BusinessLogicUtil.command_to_os(command)

        command = 'sudo apt install remmina'
        BusinessLogicUtil.command_to_os(command)

        BusinessLogicUtil.command_to_wsl_os_like_person(rf'remmina -c rdp://{users}@{ip}', wsl_linux_version=wsl_linux_version, wsl_window_title_seg=wsl_window_title_seg)
        pass

    @staticmethod
    def xfreerdp(users, ip, wsl_linux_version, wsl_window_title_seg, pw, exit_mode):
        command = 'wsl sudo apt update'
        BusinessLogicUtil.command_to_os(command)

        command = 'sudo apt install freerdp2-x11'
        BusinessLogicUtil.command_to_os(command)

        #         BusinessLogicUtil.write_like_person(rf'xfreerdp /v:{ip}:3390 /u:{users} /p:{pw} /sec:nla /clipboard',wsl_linux_version=wsl_linux_version, wsl_window_title_seg=wsl_window_title_seg)
        #         BusinessLogicUtil.write_like_person(rf'xfreerdp /v:{ip}:3390 /u:{users} /p:{pw} /sec:tls /clipboard',wsl_linux_version=wsl_linux_version, wsl_window_title_seg=wsl_window_title_seg)
        BusinessLogicUtil.command_to_wsl_os_like_person(rf'xfreerdp /v:{ip}:3390 /u:{users} /p:{pw} /clipboard', wsl_linux_version=wsl_linux_version, wsl_window_title_seg=wsl_window_title_seg)

        pass

    @staticmethod
    def ping(ip):
        while True:
            command = rf'ping {ip}'
            lines = BusinessLogicUtil.command_to_os(cmd=command)
            string_positive = '0% loss'
            for line in lines:
                if string_positive in line:
                    BusinessLogicUtil.print_as_log(f'''"ping 확인되었습니다 {ip}"''', print_color='blue')
                    return True
            BusinessLogicUtil.sleep(seconds=1)
            BusinessLogicUtil.print_as_log(f'''"ping 재시도 {ip}"''')

    @staticmethod
    def command_to_wsl_os_like_person(command, wsl_linux_version, wsl_window_title_seg, sleep_time=500):
        BusinessLogicUtil.run_wsl(wsl_linux_version=wsl_linux_version, wsl_window_title_seg=wsl_window_title_seg)
        BusinessLogicUtil.write_like_person(command)
        BusinessLogicUtil.sleep(milliseconds=sleep_time)
        BusinessLogicUtil.press('enter')

    @staticmethod
    def install_chrome_remote_desktop_server_to_remote_os(users, ip, wsl_linux_version, wsl_window_title_seg, pw, exit_mode):
        BusinessLogicUtil.ssh(users=users, ip=ip, wsl_linux_version=wsl_linux_version, wsl_window_title_seg=wsl_window_title_seg, pw=pw, exit_mode=exit_mode)

        # Update package list
        BusinessLogicUtil.command_to_wsl_os_like_person('sudo apt update')

        # Install wget
        BusinessLogicUtil.command_to_wsl_os_like_person('sudo apt install wget')

        # Download Google Chrome .deb package
        BusinessLogicUtil.command_to_wsl_os_like_person('wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb')

        # Install Google Chrome
        BusinessLogicUtil.command_to_wsl_os_like_person('sudo apt install ./google-chrome-stable_current_amd64.deb')

    @staticmethod
    def install_chrome_remote_desktop_client_to_remote_os(users, ip, wsl_linux_version, wsl_window_title_seg, pw, exit_mode):
        command = 'wsl sudo apt update'
        BusinessLogicUtil.command_to_os(command)

        # command = 'wsl sudo apt install wget curl'
        # BusinessLogicUtil.command_to_os(command)
        #
        # command = 'wsl curl -fsSL https://dl.google.com/linux/linux_signing_key.pub | sudo gpg --dearmor -o /usr/share/keyrings/google-archive-keyring.gpg'
        # BusinessLogicUtil.command_to_os(command)
        #
        # command = 'wsl echo "deb [signed-by=/usr/share/keyrings/google-archive-keyring.gpg] https://dl.google.com/linux/chrome/deb/ stable main" | sudo tee /etc/apt/sources.list.d/google-chrome.list'
        # BusinessLogicUtil.command_to_os(command)
        #
        # command = 'wsl sudo apt install chrome-remote-desktop'
        # BusinessLogicUtil.command_to_os(command)

        # BusinessLogicUtil.run_wsl(wsl_linux_version=wsl_linux_version, wsl_window_title_seg=wsl_window_title_seg)
        # BusinessLogicUtil.run_command_like_person('sudo apt install chrome-remote-desktop')

    @staticmethod
    def check_str_positive_in_loop(timeout, items_list, str_positive, ment_positive):
        lines = items_list
        start_time = time.time()
        while True:

            for line in lines:
                if str_positive in line:
                    BusinessLogicUtil.print_as_log(string=rf'''{ment_positive} %%%FOO%%%''', print_color="green")
                    return True

            BusinessLogicUtil.print_as_log(string=time.time() - start_time)
            if time.time() - start_time > timeout:
                return False
            time.sleep(0.5)

    @staticmethod
    def check_str_negative_in_loop(timeout, items_list, str_negative, ment_negative):
        lines = items_list
        start_time = time.time()
        while True:

            for line in lines:
                if str_negative in line:
                    BusinessLogicUtil.print_as_log(string=rf'''{ment_negative} %%%FOO%%%''', print_color="red")
                    return True

            BusinessLogicUtil.print_as_log(string=time.time() - start_time)
            if time.time() - start_time > timeout:
                return False
            time.sleep(0.5)

    @staticmethod
    def run_plain(): #mkr.
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        # BusinessLogicUtil.print_and_speak("i am commander plain. please. speak command.",after_delay=1.0)
        mode = None
        mode = 'cli'# todo cli 모드 테스트
        while True:
            try:
                BusinessLogicUtil.print_as_log("Please give a command", print_color='blue')
                if mode != 'cli':
                    with sr.Microphone() as source:
                        # recognizer.adjust_for_ambient_noise(source)
                        recognizer.adjust_for_ambient_noise(source, duration=0.5)
                        # audio = recognizer.listen(source, timeout=15, phrase_time_limit=10)
                        audio = recognizer.listen(source, phrase_time_limit=10)  # phrase_time_limit: Limit the maximum length of a phrase.
                        string_recognized = recognizer.recognize_google(audio, language="ko")
                else:
                    # string_recognized = input('string_recognized=')
                    # string_recognized = '토렌트다운' # todo 토렌트다운 테스트
                    string_recognized = '유튜브다운로드' # todo 유튜브다운로드 테스트
                string_recognized = string_recognized.replace(' ','')
                BusinessLogicUtil.print_as_log(rf"{string_recognized}", print_color='white')
                if any(keyword in string_recognized for keyword in ["테스트"]):
                    BusinessLogicUtil.speak('this is tested')
                elif any(keyword in string_recognized for keyword in ["휴지통비워", "휴지통정리"]):
                    BusinessLogicUtil.empty_recycle_bin()
                elif any(keyword in string_recognized for keyword in ["트리정리"]):
                    # src = rf"D:\pkg_classifying"
                    # mode='f'
                    # with_walking = True
                    # # BusinessLogicUtil.empty_recycle_bin() # 비우기
                    # BusinessLogicUtil.gather_pnxs_useless_at_tree(src=src, mode=mode)
                    # BusinessLogicUtil.rename_pnxs_at_tree(src=src, mode=mode, debug_mode=True, with_walking=with_walking)
                    # BusinessLogicUtil.classify_pnxs_at_tree(src=src, mode=mode, with_walking=with_walking)
                    # BusinessLogicUtil.rename_pnxs_at_tree(src=src, mode=mode, debug_mode=True, with_walking=with_walking)
                    # BusinessLogicUtil.gather_pnxs_empty_at_tree(src=src)
                    # # BusinessLogicUtil.empty_recycle_bin() # 비우기
                    #
                    # src = rf"D:\pkg_classifying"
                    # mode='d'
                    # with_walking = True
                    # # BusinessLogicUtil.empty_recycle_bin()  # 비우기
                    # BusinessLogicUtil.gather_pnxs_useless_at_tree(src=src, mode=mode)
                    # BusinessLogicUtil.rename_pnxs_at_tree(src=src, mode=mode, debug_mode=True, with_walking=with_walking)
                    # BusinessLogicUtil.classify_pnxs_at_tree(src=src, mode=mode, with_walking=with_walking)
                    # BusinessLogicUtil.rename_pnxs_at_tree(src=src, mode=mode, debug_mode=True, with_walking=with_walking)
                    # BusinessLogicUtil.gather_pnxs_empty_at_tree(src=src)
                    # # BusinessLogicUtil.empty_recycle_bin()  # 비우기
                    pass
                elif any(keyword in string_recognized for keyword in ["디렉토리트리정리"]):
                    src = rf"D:\pkg_classifying"
                    mode = 'd'
                    with_walking = True
                    # BusinessLogicUtil.empty_recycle_bin()  # 비우기
                    BusinessLogicUtil.gather_pnxs_useless_at_tree(src=src, mode=mode)
                    BusinessLogicUtil.rename_pnxs_at_tree(src=src, mode=mode, debug_mode=True, with_walking=with_walking)
                    BusinessLogicUtil.classify_pnxs_at_tree(src=src, mode=mode, with_walking=with_walking)
                    BusinessLogicUtil.rename_pnxs_at_tree(src=src, mode=mode, debug_mode=True, with_walking=with_walking)
                    BusinessLogicUtil.gather_pnxs_empty_at_tree(src=src)
                    # BusinessLogicUtil.empty_recycle_bin()  # 비우기
                elif any(keyword in string_recognized for keyword in ["파일트리정리"]):
                    src = rf"D:\pkg_classifying"
                    mode = 'f'
                    with_walking = True
                    # BusinessLogicUtil.empty_recycle_bin() # 비우기
                    BusinessLogicUtil.gather_pnxs_useless_at_tree(src=src, mode=mode)
                    BusinessLogicUtil.rename_pnxs_at_tree(src=src, mode=mode, debug_mode=True, with_walking=with_walking)
                    BusinessLogicUtil.classify_pnxs_at_tree(src=src, mode=mode, with_walking=with_walking)
                    BusinessLogicUtil.rename_pnxs_at_tree(src=src, mode=mode, debug_mode=True, with_walking=with_walking)
                    BusinessLogicUtil.gather_pnxs_empty_at_tree(src=src)
                    # BusinessLogicUtil.empty_recycle_bin() # 비우기
                elif any(keyword in string_recognized for keyword in ["토렌트", "토렌트다운로드"]):
                    # 다운로드 si
                    # BusinessLogicUtil.print_torrent_magnets_list_from_nyaa_si(title_to_search="Dandadan", from_no=1, to_no=12)
                    BusinessLogicUtil.download_torrent_magnets_from_nyaa_si(via_txt_f=True)

                    # 다운로드 qq
                    # BusinessLogicUtil.download_torrent_magnets_from_torrentqq(title_to_search="1080 베놈 Last")
                    # BusinessLogicUtil.download_torrent_magnets_from_torrentqq(via_txt_f=True)
                elif any(keyword in string_recognized for keyword in ["유튜브다운로드"]):
                    # 유튜브 다운로드
                    BusinessLogicUtil.download_youtube_list(via_text_file=True)
                    BusinessLogicUtil.pause()
                elif any(keyword in string_recognized for keyword in ["오늘무슨날", "무슨날"]):
                    BusinessLogicUtil.speak('today is christmas. happy christmas')
                    BusinessLogicUtil.speak('today is newyear')
                elif any(keyword in string_recognized for keyword in ["오늘날짜",  "날짜"]):
                    BusinessLogicUtil.speak_today_info_as_korean()
                elif any(keyword in string_recognized for keyword in ["요일", "오늘요일", "몇요일"]):
                    BusinessLogicUtil.speak(f'{BusinessLogicUtil.get_weekday_as_english()}')
                elif any(keyword in string_recognized for keyword in ["시간", "몇시야", "몇시"  ]):
                    HH = TimeUtil.get_time_as_('%H')
                    mm = TimeUtil.get_time_as_('%M')
                    BusinessLogicUtil.speak(f'{int(HH)} hour {int(mm)} minutes')
                elif any(keyword in string_recognized for keyword in ["몇분이야", "몇분", "몇분"]):
                    mm = TimeUtil.get_time_as_('%M')
                    BusinessLogicUtil.speak(f'{int(mm)} minutes')
                elif any(keyword in string_recognized for keyword in ["몇초야",  "몇초"]):
                    server_seconds = TimeUtil.get_time_as_('%S')
                    BusinessLogicUtil.speak(f'{server_seconds} seconds')
                elif any(keyword in string_recognized for keyword in ["날씨"]):
                    BusinessLogicUtil.print_and_speak("Searching for weather...")
                    BusinessLogicUtil.get_comprehensive_weather_information_from_web()
                elif any(keyword in string_recognized for keyword in ["음악"]):
                    BusinessLogicUtil.play_my_sound_track()
                    BusinessLogicUtil.print_and_speak("Playing music...")
                elif any(keyword in string_recognized for keyword in ["게임", "미니게임"]):
                    BusinessLogicUtil.run_up_and_down_game()
                    BusinessLogicUtil.print_and_speak("Playing mini game...")
                elif any(keyword in string_recognized for keyword in ["비디오"]):
                    BusinessLogicUtil.play_my_video_track()
                    BusinessLogicUtil.print_and_speak("Playing video...")
                elif any(keyword in string_recognized for keyword in ["최대절전모드", "최대절전"]):
                    BusinessLogicUtil.change_os_to_power_saving_mode()
                elif any(keyword in string_recognized for keyword in ["화면보호기", "화면보호"]):
                    BusinessLogicUtil.change_os_to_screen_saver()
                else:
                    BusinessLogicUtil.print_as_log(rf"Unknown command.", print_color='red')


            except sr.UnknownValueError:
                # BusinessLogicUtil.print_as_log("못 알아 들었습니다", print_color='red')
                pass
            except OSError:
                BusinessLogicUtil.print_as_log(f'''"마이크 장비가 없습니다. cli 모드로 전환합니다."''', print_color='red')
                mode = 'cli'
            except:
                BusinessLogicUtil.print_as_log(f'''""음성 인식 서비스에 오류가 발생했습니다""''', print_color='red')
                BusinessLogicUtil.print_as_log(f"{traceback.format_exc()}", print_color='red')

        # command = 'pip install SpeechRecognition'
        # BusinessLogicUtil.command_to_os(command)
        #
        # command = 'pip install PyAudio'
        # BusinessLogicUtil.command_to_os(command)
        #
        # if not BusinessLogicUtil.is_os_windows():
        #     command = 'sudo apt install mpg123'
        #     BusinessLogicUtil.command_to_os(command)

        # listen and answer


        # 인터넷 없이
        # import speech_recognition as sr
        # recognizer = sr.Recognizer()
        # with sr.Microphone() as source:
        #     print("음성을 말하세요...")
        #     recognizer.adjust_for_ambient_noise(source)
        #     audio = recognizer.listen(source)
        #
        # # CMU Sphinx로 음성 인식 (오프라인 사용 가능)
        # try:
        #     BusinessLogicUtil.speak("음성을 인식 중...")
        #     text = recognizer.recognize_sphinx(audio)
        #     BusinessLogicUtil.speak("인식된 텍스트: " + text)
        # except sr.UnknownValueError:
        #     BusinessLogicUtil.speak("음성을 이해할 수 없습니다.")
        # except sr.RequestError as e:
        #     BusinessLogicUtil.speak(f"음성 인식 서비스에 오류가 발생했습니다: {e}")

        # BusinessLogicUtil.speak_like_parrot("테스트입니다")

        # os.system(rf"mpg123 ./{temp_mp3}")  # Linux 재생 명령
        # os.system(rf"start {temp_mp3}")  # Windows용 재생 명령
        pass

    @staticmethod
    def run_voice_note():
        import traceback
        f_txt = rf"{StateManagementUtil.PKG_TXT}/voice_memo.txt"

        f_txt = BusinessLogicUtil.get_pnx_unix_style(pnx=f_txt)
        if not BusinessLogicUtil.does_pnx_exist(src=f_txt):
            BusinessLogicUtil.make_pnx(pnx=f_txt, mode='f')

        BusinessLogicUtil.write_str_to_file(txt_str=f"{StateManagementUtil.UNDERLINE}{BusinessLogicUtil.get_time_as_('now')}\n", pnx=f_txt)

        f_txt = BusinessLogicUtil.get_pnx_windows_style(pnx=f_txt)
        cmd = rf"explorer {f_txt}"
        BusinessLogicUtil.command_to_os(cmd=cmd, mode='a')

        BusinessLogicUtil.print_and_speak("저는 텍스트파일에 받아쓰는 음성메모장 voice_note 입니다")
        import speech_recognition as sr
        recognizer = sr.Recognizer()

        while True:
            try:
                BusinessLogicUtil.print_and_speak("말씀해주세요", print_color='blue')
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source)
                string_recognized = recognizer.recognize_google(audio, language="ko")
                BusinessLogicUtil.print_and_speak(rf"{string_recognized}")

                # 텍스트를 파일에 저장
                with open(rf"{StateManagementUtil.PKG_TXT}/voice_memo.txt", "a", encoding="utf-8") as file:
                    file.write(string_recognized + "\n")
            except sr.UnknownValueError:
                pass  # 음성을 인식하지 못한 경우 무시
            except OSError:
                BusinessLogicUtil.print_as_log(f'''"마이크 장비가 없습니다"''', print_color='red')
                break
            except:
                BusinessLogicUtil.print_as_log(f'''""음성 인식 서비스에 오류가 발생했습니다""''', print_color='red')
                BusinessLogicUtil.print_as_log(f"{traceback.format_exc()}", print_color='red')

    @staticmethod
    def run_parrot():
        import speech_recognition as sr
        recognizer = sr.Recognizer()
        BusinessLogicUtil.print_and_speak("저는 따라쟁이 앵무새 parrot 입니다")
        while True:
            try:
                BusinessLogicUtil.print_as_log("말씀해주세요", print_color='blue')
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source)
                    audio = recognizer.listen(source)
                string_recognized = recognizer.recognize_google(audio, language="ko")
                BusinessLogicUtil.print_and_speak(rf"{string_recognized}")
            except sr.UnknownValueError:
                pass
            except OSError:
                BusinessLogicUtil.print_as_log(f'''"마이크 장비가 없습니다"''', print_color='red')
                break
            except:
                BusinessLogicUtil.print_as_log(f'''""음성 인식 서비스에 오류가 발생했습니다""''', print_color='red')
                BusinessLogicUtil.print_as_log(f"{traceback.format_exc()}", print_color='red')


# class 로깅
# __init__() 에서 class 명 로깅
# function_name = inspect.currentframe().f_code.co_name
# class_name = self.__class__.__name__
# BusinessLogicUtil.print_as_log(string = rf'''class_name="{class_name}/{function_name}()" %%%FOO%%%''')

# raise ValueError("의도적으로 에러 발생") # 에러 로깅
# BusinessLogicUtil.print_as_log(f"{df.head()}") # df 로깅 (df 내 데이터 유무 확인)
# BusinessLogicUtil.print_as_log(f"{df.columns.tolist()}") # df 로깅 (df 내의 모든 컬럼명 출력)
# BusinessLogicUtil.print_as_log(f"{len(df)}") # df 로깅 (df 전체 행의 줄이 몇개인지 출력)
# BusinessLogicUtil.print_as_log(f"{df.iloc[0]}") # df 로깅 (df 내의 첫번째 줄만 출력)

# mkr_자주쓰는 텍스트 템플릿
# BusinessLogicUtil.hold_console()  # cmd /k

# del routines[cursor_position]  # get_list_removed_element_by_index(items)

# function_name = inspect.currentframe().f_code.co_name
# BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
# function_name_txt = rf'{StateManagementUtil.PROJECT_DIRECTORY}\pkg_txt\{function_name}.txt'
# BusinessLogicUtil.make_pnx(leaf_pnx=function_name_txt, mode="f")
# if not BusinessLogicUtil.is_window_open(window_title=function_name_txt):
#     BusinessLogicUtil.run_pnx_via_explorer_exe(function_name_txt, show_mode=False)
#
# function_name = inspect.currentframe().f_code.co_name
# BusinessLogicUtil.print_as_log(string=rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
# function_name_directory = rf"{target_pnx}\{function_name}"  # function_name_directory 에 저장
# BusinessLogicUtil.make_pnx(leaf_pnx=function_name_txt, mode="d")
# if not BusinessLogicUtil.is_window_open(window_title=function_name):
#     BusinessLogicUtil.run_pnx_via_explorer_exe(function_name_directory, show_mode=False)

# TimeUtil.get_time_as_('%Y-%m-%d %H:%M:%S %f')

# BusinessLogicUtil.print_as_log(string = rf'''{StateManagementUtil.UNDERLINE}{function_name}() %%%FOO%%%''')
# BusinessLogicUtil.print_as_log(string=rf''' %%%FOO%%%''', print_color="red")

# BusinessLogicUtil.should_i_do(ment="깃허브에서 직접확인하시겠요요?", function=partial(BusinessLogicUtil.run_pnx_via_explorer_exe, git_repository_url), auto_click_negative_btn_after_seconds=5)

# import 최적화 방법 # todo
# del sys.modules['numpy']

# python decorater 를 통한 fail tracking      [fail] module function(), red          [success] module function() , green




# BusinessLogicUtil.print_as_log(f'''"%%%FOO%%%"''', print_color='green')
# BusinessLogicUtil.print_as_log(f'''"%%%FOO%%%"''', print_color='red')
