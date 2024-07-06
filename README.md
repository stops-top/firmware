# Firmware

[Trezor Firmware](https://github.com/stops-top) 

## 使用方式

```sh
sudo apt install -y scons llvm-dev libclang-dev clang protobuf-compiler python3-pip python3-poetry
ln -s /usr/bin/python3 /usr/bin/python
pip3 install poetry trezor mako munch protobuf
```

```sh
sudo apt install -y scons libsdl2-dev libsdl2-image-dev llvm-dev libclang-dev clang
```

可选 `poetry` Python虚拟环境和依赖管理的工具，poetry和pipenv类似，另外还提供了打包和发布的功能。

```sh
git submodule update --init --recursive --force
# poetry install
# poetry install --sync
# poetry shell
```


安装编译器
```sh
apt install -y gcc-arm-none-eabi libnewlib-arm-none-eabi openocd
```

在ubuntu20之前的默认安装的gcc版本过低，下载特定版本[`arm-gnu-toolchain`](https://developer.arm.com/downloads/-/arm-gnu-toolchain-downloads)

```sh
wget https://developer.arm.com/-/media/Files/downloads/gnu/13.3.rel1/binrel/arm-gnu-toolchain-13.3.rel1-x86_64-arm-none-eabi.tar.xz
sudo mkdir -p /opt/gcc-arm/
sudo tar xvf arm-gnu-toolchain-13.3.rel1-x86_64-arm-none-eabi.tar.xz -C /opt/gcc-arm/
vim ~/.bashrc
PATH=$PATH:/opt/gcc-arm/arm-gnu-toolchain-13.3.rel1-x86_64-arm-none-eabi/bin
```
* 13.3.rel1 (July 4, 2024)
* [Arm GNU Toolchain deprecated](https://developer.arm.com/downloads/-/gnu-rm)

安装rust工具 [`rustup`](https://rustup.rs/):

```sh
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
sudo apt install rustup
rustup target add thumbv7em-none-eabihf  # for TT
rustup target add thumbv7m-none-eabi     # for T1

rustup default nightly
rustup update
rustup component add rust-src --toolchain nightly-x86_64-unknown-linux-gnu
```

开始编译

```sh
cd core
make vendor build
```

## flashing

For flashing firmware to blank device (without bootloader) use `make flash`.

You need to have OpenOCD installed.

```sh
sudo openocd -f /usr/share/openocd/scripts/interface/stlink-v2-1.cfg -f /usr/share/openocd/scripts/target/stm32f4x.cfg
```