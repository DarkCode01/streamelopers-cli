'''
Template of a config file with scenes collecitons.
'''

from sdcli.config._config import Config


class ConfigOBS(Config):
    TEMPLATE = {
        "current_program_scene": "StandBy",
        "current_scene": "StandBy",
        "current_transition": "Fade",
        "groups": [],
        "modules": {
            "auto-scene-switcher": {
                "active": False,
                "interval": 300,
                "non_matching_scene": "",
                "switch_if_not_matching": False,
                "switches": []
            },
            "output-timer": {
                "autoStartRecordTimer": False,
                "autoStartStreamTimer": False,
                "pauseRecordTimer": True,
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
        "preview_locked": False,
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
        "scaling_enabled": False,
        "scaling_level": 0,
        "scaling_off_x": 0.0,
        "scaling_off_y": 0.0,
        "scene_order": [
            {
                "name": "StandBy"
            },
            {
                "name": "Camara"
            },
            {
                "name": "End"
            }
        ],
        "sources": [
            {
                "balance": 0.5,
                "deinterlace_field_order": 0,
                "deinterlace_mode": 0,
                "enabled": True,
                "flags": 0,
                "hotkeys": {},
                "id": "image_source",
                "mixers": 0,
                "monitoring_type": 0,
                "muted": False,
                "name": "Image",
                "prev_ver": 402653190,
                "private_settings": {},
                "push-to-mute": False,
                "push-to-mute-delay": 0,
                "push-to-talk": False,
                "push-to-talk-delay": 0,
                "settings": {
                    "file": ""
                },
                "sync": 0,
                "volume": 1.0
            },
            {
                "balance": 0.5,
                "deinterlace_field_order": 0,
                "deinterlace_mode": 0,
                "enabled": True,
                "flags": 0,
                "hotkeys": {
                    "libobs.mute": [],
                    "libobs.push-to-mute": [],
                    "libobs.push-to-talk": [],
                    "libobs.unmute": []
                },
                "id": "coreaudio_input_capture",
                "mixers": 255,
                "monitoring_type": 2,
                "muted": False,
                "name": "Audio Input Capture",
                "prev_ver": 402653190,
                "private_settings": {},
                "push-to-mute": False,
                "push-to-mute-delay": 0,
                "push-to-talk": False,
                "push-to-talk-delay": 0,
                "settings": {
                    "device_id": ""
                },
                "sync": 0,
                "volume": 0.35172048211097717
            },
            {
                "balance": 0.5,
                "deinterlace_field_order": 0,
                "deinterlace_mode": 0,
                "enabled": True,
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
                "muted": False,
                "name": "Image Slide Show 2",
                "prev_ver": 402653190,
                "private_settings": {},
                "push-to-mute": False,
                "push-to-mute-delay": 0,
                "push-to-talk": False,
                "push-to-talk-delay": 0,
                "settings": {
                    "files": [
                        {
                            "hidden": False,
                            "selected": False,
                            "value": ""
                        },
                        {
                            "hidden": False,
                            "selected": False,
                            "value": ""
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
                "enabled": True,
                "flags": 0,
                "hotkeys": {},
                "id": "av_capture_input",
                "mixers": 0,
                "monitoring_type": 0,
                "muted": False,
                "name": "Video Capture Device",
                "prev_ver": 402653190,
                "private_settings": {},
                "push-to-mute": False,
                "push-to-mute-delay": 0,
                "push-to-talk": False,
                "push-to-talk-delay": 0,
                "settings": {
                    "device": "0x14200000046d0841",
                    "device_name": "Logitech Webcam C920-C",
                    "preset": "AVCaptureSessionPresetHigh",
                    "resolution": "{\n    \"height\": 1080,\n    \"width\": 1920\n}",
                    "use_preset": True
                },
                "sync": 0,
                "volume": 1.0
            },
            {
                "balance": 0.5,
                "deinterlace_field_order": 0,
                "deinterlace_mode": 0,
                "enabled": True,
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
                "monitoring_type": 0,
                "muted": False,
                "name": "Media Source",
                "prev_ver": 402653190,
                "private_settings": {},
                "push-to-mute": False,
                "push-to-mute-delay": 0,
                "push-to-talk": False,
                "push-to-talk-delay": 0,
                "settings": {
                    "local_file": "",
                    "looping": True
                },
                "sync": 0,
                "volume": 0.25562769174575806
            },
            {
                "balance": 0.5,
                "deinterlace_field_order": 0,
                "deinterlace_mode": 0,
                "enabled": True,
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
                "muted": False,
                "name": "Image Slide Show",
                "prev_ver": 402653190,
                "private_settings": {},
                "push-to-mute": False,
                "push-to-mute-delay": 0,
                "push-to-talk": False,
                "push-to-talk-delay": 0,
                "settings": {
                    "files": [
                        {
                            "hidden": False,
                            "selected": False,
                            "value": ""
                        }
                    ],
                    "slide_time": 5000,
                    "transition": "cut",
                    "transition_speed": 300
                },
                "sync": 0,
                "volume": 1.0
            },
            {
                "balance": 0.5,
                "deinterlace_field_order": 0,
                "deinterlace_mode": 0,
                "enabled": True,
                "flags": 0,
                "hotkeys": {
                    "OBSBasic.SelectScene": [],
                    "libobs.hide_scene_item.Audio Input Capture": [],
                    "libobs.hide_scene_item.Image": [],
                    "libobs.hide_scene_item.Video Capture Device": [],
                    "libobs.show_scene_item.Audio Input Capture": [],
                    "libobs.show_scene_item.Image": [],
                    "libobs.show_scene_item.Video Capture Device": []
                },
                "id": "scene",
                "mixers": 0,
                "monitoring_type": 0,
                "muted": False,
                "name": "Camara",
                "prev_ver": 402653190,
                "private_settings": {},
                "push-to-mute": False,
                "push-to-mute-delay": 0,
                "push-to-talk": False,
                "push-to-talk-delay": 0,
                "settings": {
                    "custom_size": False,
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
                            "group_item_backup": False,
                            "id": 1,
                            "locked": False,
                            "name": "Video Capture Device",
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
                            "visible": True
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
                            "group_item_backup": False,
                            "id": 2,
                            "locked": False,
                            "name": "Audio Input Capture",
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
                            "visible": True
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
                            "group_item_backup": False,
                            "id": 3,
                            "locked": False,
                            "name": "Image",
                            "pos": {
                                "x": 0.0,
                                "y": 932.0
                            },
                            "private_settings": {},
                            "rot": 0.0,
                            "scale": {
                                "x": 0.47999998927116394,
                                "y": 0.47999998927116394
                            },
                            "scale_filter": "disable",
                            "visible": True
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
                "enabled": True,
                "flags": 0,
                "hotkeys": {
                    "OBSBasic.SelectScene": [],
                    "libobs.hide_scene_item.Image Slide Show 2": [],
                    "libobs.hide_scene_item.Media Source": [],
                    "libobs.show_scene_item.Image Slide Show 2": [],
                    "libobs.show_scene_item.Media Source": []
                },
                "id": "scene",
                "mixers": 0,
                "monitoring_type": 0,
                "muted": False,
                "name": "End",
                "prev_ver": 402653190,
                "private_settings": {},
                "push-to-mute": False,
                "push-to-mute-delay": 0,
                "push-to-talk": False,
                "push-to-talk-delay": 0,
                "settings": {
                    "custom_size": False,
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
                            "group_item_backup": False,
                            "id": 1,
                            "locked": False,
                            "name": "Image Slide Show 2",
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
                            "visible": True
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
                            "group_item_backup": False,
                            "id": 2,
                            "locked": False,
                            "name": "Media Source",
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
                            "visible": True
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
                "enabled": True,
                "flags": 0,
                "hotkeys": {
                    "OBSBasic.SelectScene": [],
                    "libobs.hide_scene_item.Image Slide Show": [],
                    "libobs.hide_scene_item.Media Source": [],
                    "libobs.show_scene_item.Image Slide Show": [],
                    "libobs.show_scene_item.Media Source": []
                },
                "id": "scene",
                "mixers": 0,
                "monitoring_type": 0,
                "muted": False,
                "name": "StandBy",
                "prev_ver": 402653190,
                "private_settings": {},
                "push-to-mute": False,
                "push-to-mute-delay": 0,
                "push-to-talk": False,
                "push-to-talk-delay": 0,
                "settings": {
                    "custom_size": False,
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
                            "group_item_backup": False,
                            "id": 1,
                            "locked": False,
                            "name": "Image Slide Show",
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
                            "visible": True
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
                            "group_item_backup": False,
                            "id": 2,
                            "locked": False,
                            "name": "Media Source",
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
                            "visible": True
                        }
                    ]
                },
                "sync": 0,
                "volume": 1.0
            }
        ],
        "transition_duration": 300,
        "transitions": []
    }