moduleInfo = {
    "meta": {
        "name": "SystemStatus",
        "version": "1.0.1",
        "description": "获取系统内存、CPU、硬盘占用",
        "author": "ShanFish",
        "homepage": "https://github.com/shanfishapp/SystemStatus",
        "license": "MIT",
    },
    "dependencies": {
        "requires": [],
        "optional": [],
        "pip": ["psutil"]
    }
}

from .Core import Main
# build_hash="a6fa91df10f81e518984202560c681421d10238aa697cec1b161742d75e9898a"
