'''
Template of a config file with scenes collecitons.
'''

from sdcli.config._config import Config


class ConfigOBS(Config):
    TEMPLATE = {
    "current_program_scene": "Presentacion",
    "current_scene": "Presentacion",
    "current_transition": "Fade",
    "groups": [],
    "modules": {
        "auto-scene-switcher": {
            "active": false,
            "interval": 300,
            "non_matching_scene": "",
            "switch_if_not_matching": false,
            "switches": []
        },
        "captions": {
            "enabled": false,
            "lang_id": 1033,
            "provider": "mssapi",
            "source": ""
        },
        "output-timer": {
            "autoStartRecordTimer": false,
            "autoStartStreamTimer": false,
            "pauseRecordTimer": false,
            "recordTimerHours": 0,
            "recordTimerMinutes": 0,
            "recordTimerSeconds": 30,
            "streamTimerHours": 0,
            "streamTimerMinutes": 0,
            "streamTimerSeconds": 30
        },
        "scripts-tool": []
    },
    "name": "",
    "preview_locked": false,
    "quick_transitions": [
        {
            "duration": 300,
            "hotkeys": [],
            "id": 3,
            "name": "Cut"
        },
        {
            "duration": 300,
            "hotkeys": [],
            "id": 4,
            "name": "Fade"
        }
    ],
    "saved_projectors": [],
    "scaling_enabled": false,
    "scaling_level": 0,
    "scaling_off_x": 0.0,
    "scaling_off_y": 0.0,
    "scene_order": [
        {
            "name": "StandBy"
        },
        {
            "name": "Presentacion"
        },
        {
            "name": "Only Camera"
        },
        {
            "name": "Only Desktop"
        },
        {
            "name": "EndScreen"
        }
    ],
    "sources": [
        {
            "balance": 0.5,
            "deinterlace_field_order": 0,
            "deinterlace_mode": 0,
            "enabled": true,
            "flags": 0,
            "hotkeys": {},
            "id": "image_source",
            "mixers": 0,
            "monitoring_type": 0,
            "muted": false,
            "name": "Logo Streamelopers - (transparente)",
            "prev_ver": 402653185,
            "private_settings": {},
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "settings": {
                "file": ""  # TODO: Add URL of logo streameloeprs
            },
            "sync": 0,
            "volume": 1.0
        },
        {
            "balance": 0.5,
            "deinterlace_field_order": 0,
            "deinterlace_mode": 0,
            "enabled": true,
            "flags": 0,
            "hotkeys": {},
            "id": "color_source",
            "mixers": 0,
            "monitoring_type": 0,
            "muted": false,
            "name": "Color de fondo - (presentacion)",
            "prev_ver": 402653185,
            "private_settings": {},
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "settings": {},
            "sync": 0,
            "volume": 1.0
        },
        {
            "balance": 0.5,
            "deinterlace_field_order": 0,
            "deinterlace_mode": 0,
            "enabled": true,
            "flags": 0,
            "hotkeys": {
                "OBSBasic.SelectScene": [],
                "libobs.hide_scene_item.Color Source": [],
                "libobs.hide_scene_item.Image Slide Show": [],
                "libobs.hide_scene_item.Musica": [],
                "libobs.show_scene_item.Color Source": [],
                "libobs.show_scene_item.Image Slide Show": [],
                "libobs.show_scene_item.Musica": []
            },
            "id": "scene",
            "mixers": 0,
            "monitoring_type": 0,
            "muted": false,
            "name": "StandBy",
            "prev_ver": 402653185,
            "private_settings": {},
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "settings": {
                "custom_size": false,
                "id_counter": 5,
                "items": [
                    {
                        "align": 5,
                        "bounds": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "bounds_align": 0,
                        "bounds_type": 0,
                        "crop_bottom": 0,
                        "crop_left": 0,
                        "crop_right": 0,
                        "crop_top": 0,
                        "group_item_backup": false,
                        "id": 3,
                        "locked": true,
                        "name": "Color de Fondo - (StandBy)",
                        "pos": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "private_settings": {},
                        "rot": 0.0,
                        "scale": {
                            "x": 4.8000001907348633,
                            "y": 4.8000001907348633
                        },
                        "scale_filter": "disable",
                        "visible": true
                    },
                    {
                        "align": 5,
                        "bounds": {
                            "x": 1920.0,
                            "y": 1080.0
                        },
                        "bounds_align": 0,
                        "bounds_type": 2,
                        "crop_bottom": 0,
                        "crop_left": 0,
                        "crop_right": 0,
                        "crop_top": 0,
                        "group_item_backup": false,
                        "id": 1,
                        "locked": false,
                        "name": "Slide de los patrons & art comunidad",
                        "pos": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "private_settings": {},
                        "rot": 0.0,
                        "scale": {
                            "x": 1.0,
                            "y": 1.0
                        },
                        "scale_filter": "disable",
                        "visible": true
                    },
                    {
                        "align": 5,
                        "bounds": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "bounds_align": 0,
                        "bounds_type": 0,
                        "crop_bottom": 0,
                        "crop_left": 0,
                        "crop_right": 0,
                        "crop_top": 0,
                        "group_item_backup": false,
                        "id": 2,
                        "locked": false,
                        "name": "Musica de StandBy",
                        "pos": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "private_settings": {},
                        "rot": 0.0,
                        "scale": {
                            "x": 1.0,
                            "y": 1.0
                        },
                        "scale_filter": "disable",
                        "visible": true
                    }
                ]
            },
            "sync": 0,
            "volume": 1.0
        },
        {
            "balance": 0.5,
            "deinterlace_field_order": 0,
            "deinterlace_mode": 0,
            "enabled": true,
            "flags": 0,
            "hotkeys": {
                "OBSBasic.SelectScene": [],
                "libobs.hide_scene_item.Camera": [],
                "libobs.hide_scene_item.Color Source 2": [],
                "libobs.hide_scene_item.Escritorio": [],
                "libobs.hide_scene_item.Logo Streamelopers": [],
                "libobs.hide_scene_item.Logo evento": [],
                "libobs.hide_scene_item.Microfono": [],
                "libobs.show_scene_item.Camera": [],
                "libobs.show_scene_item.Color Source 2": [],
                "libobs.show_scene_item.Escritorio": [],
                "libobs.show_scene_item.Logo Streamelopers": [],
                "libobs.show_scene_item.Logo evento": [],
                "libobs.show_scene_item.Microfono": []
            },
            "id": "scene",
            "mixers": 0,
            "monitoring_type": 0,
            "muted": false,
            "name": "Presentacion",
            "prev_ver": 402653185,
            "private_settings": {},
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "settings": {
                "custom_size": false,
                "id_counter": 15,
                "items": [
                    {
                        "align": 5,
                        "bounds": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "bounds_align": 0,
                        "bounds_type": 0,
                        "crop_bottom": 0,
                        "crop_left": 0,
                        "crop_right": 0,
                        "crop_top": 0,
                        "group_item_backup": false,
                        "id": 11,
                        "locked": true,
                        "name": "Color de Fondo - (presentacion)",
                        "pos": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "private_settings": {},
                        "rot": 0.0,
                        "scale": {
                            "x": 4.8000001907348633,
                            "y": 4.8000001907348633
                        },
                        "scale_filter": "disable",
                        "visible": true
                    },
                    {
                        "align": 5,
                        "bounds": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "bounds_align": 0,
                        "bounds_type": 0,
                        "crop_bottom": 0,
                        "crop_left": 0,
                        "crop_right": 0,
                        "crop_top": 0,
                        "group_item_backup": false,
                        "id": 5,
                        "locked": false,
                        "name": "Logo Streamelopers - (fondo blanco)",
                        "pos": {
                            "x": 0.0,
                            "y": 113.0
                        },
                        "private_settings": {},
                        "rot": 0.0,
                        "scale": {
                            "x": 0.54583334922790527,
                            "y": 0.54583334922790527
                        },
                        "scale_filter": "disable",
                        "visible": true
                    },
                    {
                        "align": 5,
                        "bounds": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "bounds_align": 0,
                        "bounds_type": 0,
                        "crop_bottom": 0,
                        "crop_left": 0,
                        "crop_right": 0,
                        "crop_top": 0,
                        "group_item_backup": false,
                        "id": 1,
                        "locked": false,
                        "name": "Camara del charlista",
                        "pos": {
                            "x": -73.0,
                            "y": 407.0
                        },
                        "private_settings": {},
                        "rot": 0.0,
                        "scale": {
                            "x": 0.27135416865348816,
                            "y": 0.27129629254341125
                        },
                        "scale_filter": "disable",
                        "visible": true
                    },
                    {
                        "align": 5,
                        "bounds": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "bounds_align": 0,
                        "bounds_type": 0,
                        "crop_bottom": 0,
                        "crop_left": 0,
                        "crop_right": 0,
                        "crop_top": 0,
                        "group_item_backup": false,
                        "id": 3,
                        "locked": false,
                        "name": "Escritorio del charlista",
                        "pos": {
                            "x": 389.0,
                            "y": 99.0
                        },
                        "private_settings": {},
                        "rot": 0.0,
                        "scale": {
                            "x": 0.79739582538604736,
                            "y": 0.79722219705581665
                        },
                        "scale_filter": "disable",
                        "visible": true
                    },
                    {
                        "align": 5,
                        "bounds": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "bounds_align": 0,
                        "bounds_type": 0,
                        "crop_bottom": 0,
                        "crop_left": 0,
                        "crop_right": 0,
                        "crop_top": 0,
                        "group_item_backup": false,
                        "id": 4,
                        "locked": false,
                        "name": "Microfono del charlista",
                        "pos": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "private_settings": {},
                        "rot": 0.0,
                        "scale": {
                            "x": 1.0,
                            "y": 1.0
                        },
                        "scale_filter": "disable",
                        "visible": true
                    },
                    {
                        "align": 5,
                        "bounds": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "bounds_align": 0,
                        "bounds_type": 0,
                        "crop_bottom": 0,
                        "crop_left": 0,
                        "crop_right": 0,
                        "crop_top": 0,
                        "group_item_backup": false,
                        "id": 15,
                        "locked": false,
                        "name": "Logo evento - (comunidad)",
                        "pos": {
                            "x": 94.0,
                            "y": 766.0
                        },
                        "private_settings": {},
                        "rot": 0.0,
                        "scale": {
                            "x": 0.17576317489147186,
                            "y": 0.17592592537403107
                        },
                        "scale_filter": "disable",
                        "visible": true
                    }
                ]
            },
            "sync": 0,
            "volume": 1.0
        },
        {
            "balance": 0.5,
            "deinterlace_field_order": 0,
            "deinterlace_mode": 0,
            "enabled": true,
            "flags": 0,
            "hotkeys": {
                "OBSBasic.SelectScene": [],
                "libobs.hide_scene_item.Backgrund Image": [],
                "libobs.hide_scene_item.Camera": [],
                "libobs.hide_scene_item.Color Source": [],
                "libobs.hide_scene_item.Image": [],
                "libobs.hide_scene_item.Microfono": [],
                "libobs.show_scene_item.Backgrund Image": [],
                "libobs.show_scene_item.Camera": [],
                "libobs.show_scene_item.Color Source": [],
                "libobs.show_scene_item.Image": [],
                "libobs.show_scene_item.Microfono": []
            },
            "id": "scene",
            "mixers": 0,
            "monitoring_type": 0,
            "muted": false,
            "name": "Only Camera - (charlista)",
            "prev_ver": 402653185,
            "private_settings": {},
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "settings": {
                "custom_size": false,
                "id_counter": 7,
                "items": [
                    {
                        "align": 5,
                        "bounds": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "bounds_align": 0,
                        "bounds_type": 0,
                        "crop_bottom": 0,
                        "crop_left": 0,
                        "crop_right": 0,
                        "crop_top": 0,
                        "group_item_backup": false,
                        "id": 1,
                        "locked": true,
                        "name": "Color de Fondo",
                        "pos": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "private_settings": {},
                        "rot": 0.0,
                        "scale": {
                            "x": 4.8000001907348633,
                            "y": 4.8000001907348633
                        },
                        "scale_filter": "disable",
                        "visible": true
                    },
                    {
                        "align": 5,
                        "bounds": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "bounds_align": 0,
                        "bounds_type": 0,
                        "crop_bottom": 0,
                        "crop_left": 0,
                        "crop_right": 0,
                        "crop_top": 0,
                        "group_item_backup": false,
                        "id": 5,
                        "locked": false,
                        "name": "Backgrund Image",
                        "pos": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "private_settings": {},
                        "rot": 0.0,
                        "scale": {
                            "x": 1.0,
                            "y": 1.0
                        },
                        "scale_filter": "disable",
                        "visible": true
                    },
                    {
                        "align": 5,
                        "bounds": {
                            "x": 1920.0,
                            "y": 1080.0
                        },
                        "bounds_align": 0,
                        "bounds_type": 2,
                        "crop_bottom": 0,
                        "crop_left": 0,
                        "crop_right": 0,
                        "crop_top": 0,
                        "group_item_backup": false,
                        "id": 2,
                        "locked": false,
                        "name": "Camera",
                        "pos": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "private_settings": {},
                        "rot": 0.0,
                        "scale": {
                            "x": 1.0,
                            "y": 1.0
                        },
                        "scale_filter": "disable",
                        "visible": true
                    },
                    {
                        "align": 5,
                        "bounds": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "bounds_align": 0,
                        "bounds_type": 0,
                        "crop_bottom": 0,
                        "crop_left": 0,
                        "crop_right": 0,
                        "crop_top": 0,
                        "group_item_backup": false,
                        "id": 3,
                        "locked": false,
                        "name": "Microfono",
                        "pos": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "private_settings": {},
                        "rot": 0.0,
                        "scale": {
                            "x": 1.0,
                            "y": 1.0
                        },
                        "scale_filter": "disable",
                        "visible": true
                    },
                    {
                        "align": 5,
                        "bounds": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "bounds_align": 0,
                        "bounds_type": 0,
                        "crop_bottom": 0,
                        "crop_left": 0,
                        "crop_right": 0,
                        "crop_top": 0,
                        "group_item_backup": false,
                        "id": 7,
                        "locked": false,
                        "name": "Image",
                        "pos": {
                            "x": 0.0,
                            "y": 901.0
                        },
                        "private_settings": {},
                        "rot": 0.0,
                        "scale": {
                            "x": 0.60500001907348633,
                            "y": 0.60500001907348633
                        },
                        "scale_filter": "disable",
                        "visible": true
                    }
                ]
            },
            "sync": 0,
            "volume": 1.0
        },
        {
            "balance": 0.5,
            "deinterlace_field_order": 0,
            "deinterlace_mode": 0,
            "enabled": true,
            "flags": 0,
            "hotkeys": {
                "OBSBasic.SelectScene": [],
                "libobs.hide_scene_item.Escritorio": [],
                "libobs.hide_scene_item.Microfono": [],
                "libobs.show_scene_item.Escritorio": [],
                "libobs.show_scene_item.Microfono": []
            },
            "id": "scene",
            "mixers": 0,
            "monitoring_type": 0,
            "muted": false,
            "name": "Only Desktop",
            "prev_ver": 402653185,
            "private_settings": {},
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "settings": {
                "custom_size": false,
                "id_counter": 3,
                "items": [
                    {
                        "align": 5,
                        "bounds": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "bounds_align": 0,
                        "bounds_type": 0,
                        "crop_bottom": 0,
                        "crop_left": 0,
                        "crop_right": 0,
                        "crop_top": 0,
                        "group_item_backup": false,
                        "id": 1,
                        "locked": false,
                        "name": "Escritorio",
                        "pos": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "private_settings": {},
                        "rot": 0.0,
                        "scale": {
                            "x": 1.0,
                            "y": 1.0
                        },
                        "scale_filter": "disable",
                        "visible": true
                    },
                    {
                        "align": 5,
                        "bounds": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "bounds_align": 0,
                        "bounds_type": 0,
                        "crop_bottom": 0,
                        "crop_left": 0,
                        "crop_right": 0,
                        "crop_top": 0,
                        "group_item_backup": false,
                        "id": 2,
                        "locked": false,
                        "name": "Microfono",
                        "pos": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "private_settings": {},
                        "rot": 0.0,
                        "scale": {
                            "x": 1.0,
                            "y": 1.0
                        },
                        "scale_filter": "disable",
                        "visible": true
                    }
                ]
            },
            "sync": 0,
            "volume": 1.0
        },
        {
            "balance": 0.5,
            "deinterlace_field_order": 0,
            "deinterlace_mode": 0,
            "enabled": true,
            "flags": 0,
            "hotkeys": {
                "OBSBasic.SelectScene": [],
                "libobs.hide_scene_item.Imagen": [],
                "libobs.hide_scene_item.Musica": [],
                "libobs.show_scene_item.Imagen": [],
                "libobs.show_scene_item.Musica": []
            },
            "id": "scene",
            "mixers": 0,
            "monitoring_type": 0,
            "muted": false,
            "name": "EndScreen",
            "prev_ver": 402653185,
            "private_settings": {},
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "settings": {
                "custom_size": false,
                "id_counter": 2,
                "items": [
                    {
                        "align": 5,
                        "bounds": {
                            "x": 1920.0,
                            "y": 1080.0
                        },
                        "bounds_align": 0,
                        "bounds_type": 2,
                        "crop_bottom": 0,
                        "crop_left": 0,
                        "crop_right": 0,
                        "crop_top": 0,
                        "group_item_backup": false,
                        "id": 1,
                        "locked": false,
                        "name": "Imagen",
                        "pos": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "private_settings": {},
                        "rot": 0.0,
                        "scale": {
                            "x": 1.0,
                            "y": 1.0
                        },
                        "scale_filter": "disable",
                        "visible": true
                    },
                    {
                        "align": 5,
                        "bounds": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "bounds_align": 0,
                        "bounds_type": 0,
                        "crop_bottom": 0,
                        "crop_left": 0,
                        "crop_right": 0,
                        "crop_top": 0,
                        "group_item_backup": false,
                        "id": 2,
                        "locked": false,
                        "name": "Musica",
                        "pos": {
                            "x": 0.0,
                            "y": 0.0
                        },
                        "private_settings": {},
                        "rot": 0.0,
                        "scale": {
                            "x": 1.0,
                            "y": 1.0
                        },
                        "scale_filter": "disable",
                        "visible": true
                    }
                ]
            },
            "sync": 0,
            "volume": 1.0
        },
        {
            "balance": 0.5,
            "deinterlace_field_order": 0,
            "deinterlace_mode": 0,
            "enabled": true,
            "flags": 0,
            "hotkeys": {
                "SlideShow.NextSlide": [],
                "SlideShow.PlayPause": [],
                "SlideShow.PreviousSlide": [],
                "SlideShow.Restart": [],
                "SlideShow.Stop": []
            },
            "id": "slideshow",
            "mixers": 0,
            "monitoring_type": 0,
            "muted": false,
            "name": "Image Slide Show",
            "prev_ver": 402653185,
            "private_settings": {},
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "settings": {
                "files": [
                    {
                        "hidden": false,
                        "selected": false,
                        "value": "C:/Users/Lisa/Google Drive/Streamelopers/Assets/Common"
                    }
                ]
            },
            "sync": 0,
            "volume": 1.0
        },
        {
            "balance": 0.5,
            "deinterlace_field_order": 0,
            "deinterlace_mode": 0,
            "enabled": true,
            "flags": 0,
            "hotkeys": {},
            "id": "image_source",
            "mixers": 0,
            "monitoring_type": 0,
            "muted": false,
            "name": "Imagen",
            "prev_ver": 402653185,
            "private_settings": {},
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "settings": {
                "file": "C:/SantiagOps/Common_/Copy of 3_suscribete.png"
            },
            "sync": 0,
            "volume": 1.0
        },
        {
            "balance": 0.5,
            "deinterlace_field_order": 0,
            "deinterlace_mode": 0,
            "enabled": true,
            "flags": 0,
            "hotkeys": {
                "MediaSource.Restart": [],
                "libobs.mute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": [],
                "libobs.unmute": []
            },
            "id": "ffmpeg_source",
            "mixers": 255,
            "monitoring_type": 2,
            "muted": false,
            "name": "Musica",
            "prev_ver": 402653185,
            "private_settings": {},
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "settings": {
                "local_file": "C:/SantiagOps/Musica/Copy of bensound-dreams.mp3",
                "looping": true
            },
            "sync": 0,
            "volume": 0.087687581777572632
        },
        {
            "balance": 0.5,
            "deinterlace_field_order": 0,
            "deinterlace_mode": 0,
            "enabled": true,
            "flags": 0,
            "hotkeys": {
                "libobs.mute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": [],
                "libobs.unmute": []
            },
            "id": "dshow_input",
            "mixers": 255,
            "monitoring_type": 0,
            "muted": true,
            "name": "Camera",
            "prev_ver": 402653185,
            "private_settings": {},
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "settings": {
                "active": true,
                "last_resolution": "1920x1080",
                "last_video_device_id": "Microsoft® LifeCam Studio(TM):\\\\?\\usb#22vid_045e&pid_0772&mi_00#226&7cd012b&0&0000#22{65e8773d-8f56-11d0-a3b9-00a0c9223196}\\global",
                "res_type": 1,
                "resolution": "1920x1080",
                "video_device_id": "Microsoft® LifeCam Studio(TM):\\\\?\\usb#22vid_045e&pid_0772&mi_00#226&7cd012b&0&0000#22{65e8773d-8f56-11d0-a3b9-00a0c9223196}\\global"
            },
            "sync": 0,
            "volume": 1.0
        },
        {
            "balance": 0.5,
            "deinterlace_field_order": 0,
            "deinterlace_mode": 0,
            "enabled": true,
            "flags": 0,
            "hotkeys": {},
            "id": "color_source",
            "mixers": 0,
            "monitoring_type": 0,
            "muted": false,
            "name": "Color Source",
            "prev_ver": 402653185,
            "private_settings": {},
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "settings": {
                "color": 4294967295
            },
            "sync": 0,
            "volume": 1.0
        },
        {
            "balance": 0.5,
            "deinterlace_field_order": 0,
            "deinterlace_mode": 0,
            "enabled": true,
            "flags": 0,
            "hotkeys": {
                "libobs.mute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": [],
                "libobs.unmute": []
            },
            "id": "dshow_input",
            "mixers": 255,
            "monitoring_type": 0,
            "muted": true,
            "name": "Escritorio",
            "prev_ver": 402653185,
            "private_settings": {},
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "settings": {
                "active": true,
                "deactivate_when_not_showing": false,
                "last_video_device_id": "FHD Capture:\\\\?\\usb#22vid_1bcf&pid_2c99&mi_00#226&313c67af&0&0000#22{65e8773d-8f56-11d0-a3b9-00a0c9223196}\\global",
                "video_device_id": "FHD Capture:\\\\?\\usb#22vid_1bcf&pid_2c99&mi_00#226&313c67af&0&0000#22{65e8773d-8f56-11d0-a3b9-00a0c9223196}\\global"
            },
            "sync": 0,
            "volume": 1.0
        },
        {
            "balance": 0.5,
            "deinterlace_field_order": 0,
            "deinterlace_mode": 0,
            "enabled": true,
            "flags": 0,
            "hotkeys": {
                "libobs.mute": [],
                "libobs.push-to-mute": [],
                "libobs.push-to-talk": [],
                "libobs.unmute": []
            },
            "id": "wasapi_input_capture",
            "mixers": 255,
            "monitoring_type": 2,
            "muted": false,
            "name": "Microfono",
            "prev_ver": 402653185,
            "private_settings": {},
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "settings": {
                "device_id": "{0.0.1.00000000}.{01f72d31-d28c-403c-99bb-0664ec016d01}"
            },
            "sync": 0,
            "volume": 0.32677963376045227
        },
        {
            "balance": 0.5,
            "deinterlace_field_order": 0,
            "deinterlace_mode": 0,
            "enabled": true,
            "flags": 0,
            "hotkeys": {},
            "id": "image_source",
            "mixers": 0,
            "monitoring_type": 0,
            "muted": false,
            "name": "Logo Streamelopers",
            "prev_ver": 402653185,
            "private_settings": {},
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "settings": {
                "file": "C:/SantiagOps/Logos/Copy of Logo grande blanco.png"
            },
            "sync": 0,
            "volume": 1.0
        },
        {
            "balance": 0.5,
            "deinterlace_field_order": 0,
            "deinterlace_mode": 0,
            "enabled": true,
            "flags": 0,
            "hotkeys": {},
            "id": "image_source",
            "mixers": 0,
            "monitoring_type": 0,
            "muted": false,
            "name": "Backgrund Image",
            "prev_ver": 402653185,
            "private_settings": {},
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "settings": {
                "file": "C:/Users/Lisa/Downloads/Untitled design (2).png"
            },
            "sync": 0,
            "volume": 1.0
        },
        {
            "balance": 0.5,
            "deinterlace_field_order": 0,
            "deinterlace_mode": 0,
            "enabled": true,
            "flags": 0,
            "hotkeys": {},
            "id": "image_source",
            "mixers": 0,
            "monitoring_type": 0,
            "muted": false,
            "name": "Logo evento",
            "prev_ver": 402653185,
            "private_settings": {},
            "push-to-mute": false,
            "push-to-mute-delay": 0,
            "push-to-talk": false,
            "push-to-talk-delay": 0,
            "settings": {
                "file": "C:/Users/Lisa/Downloads/White_Black Background MobileDevDay Logo.png"
            },
            "sync": 0,
            "volume": 1.0
        }
    ],
    "transition_duration": 300,
    "transitions": []
}