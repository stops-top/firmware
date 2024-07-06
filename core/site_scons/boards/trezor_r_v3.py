from __future__ import annotations

from . import get_hw_model_as_number
from .stm32f4_common import stm32f4_common_files


def configure(
    env: dict,
    features_wanted: list[str],
    defines: list[str | tuple[str, str]],
    sources: list[str],
    paths: list[str],
) -> list[str]:
    features_available: list[str] = []
    hw_model = get_hw_model_as_number("T2B1")
    hw_revision = 3
    board = "trezor_r_v3.h"
    display = "ug-2828tswig01.c"

    mcu = "STM32F427xx"

    stm32f4_common_files(env, defines, sources, paths)

    env.get("ENV")[
        "CPU_ASFLAGS"
    ] = "-mthumb -mcpu=cortex-m4 -mfloat-abi=hard -mfpu=fpv4-sp-d16"
    env.get("ENV")[
        "CPU_CCFLAGS"
    ] = "-mthumb -mcpu=cortex-m4 -mfloat-abi=hard -mfpu=fpv4-sp-d16 -mtune=cortex-m4 "
    env.get("ENV")["RUST_TARGET"] = "thumbv7em-none-eabihf"

    defines += [mcu]
    defines += [f'TREZOR_BOARD=\\"boards/{board}\\"']
    defines += [f"HW_MODEL={hw_model}"]
    defines += [f"HW_REVISION={hw_revision}"]
    sources += [
        "embed/models/model_T2B1_layout.c",
    ]
    sources += [f"embed/trezorhal/stm32f4/displays/{display}"]

    if "input" in features_wanted:
        sources += ["embed/trezorhal/stm32f4/button.c"]
        features_available.append("button")

    if "rgb_led" in features_wanted:
        sources += ["embed/trezorhal/stm32f4/rgb_led.c"]
        features_available.append("rgb_led")

    if "sbu" in features_wanted:
        sources += ["embed/trezorhal/stm32f4/sbu.c"]
        features_available.append("sbu")

    if "usb" in features_wanted:
        sources += [
            "embed/trezorhal/stm32f4/usb.c",
            "embed/trezorhal/stm32f4/usbd_conf.c",
            "embed/trezorhal/stm32f4/usbd_core.c",
            "embed/trezorhal/stm32f4/usbd_ctlreq.c",
            "embed/trezorhal/stm32f4/usbd_ioreq.c",
            "vendor/micropython/lib/stm32lib/STM32F4xx_HAL_Driver/Src/stm32f4xx_ll_usb.c",
        ]
        features_available.append("usb")

    env.get("ENV")["TREZOR_BOARD"] = board
    env.get("ENV")["MCU_TYPE"] = mcu

    return features_available