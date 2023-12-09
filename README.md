# PN532 NFC library

This library is for the PN532 chip to use NFC technology.

This is a fork of the [PN532 library by Seeed-Studio](https://github.com/Seeed-Studio/PN532).

It provides a small bit a configuration code and small changes to be able to use its components as libraries in [PlatformIO](https://platformio.org/).

## Getting started

1. Add both the core library and communication adapter to the `platformio.ini` file

    ```ini
    lib_deps = 
      ; ...
      PN532=https://github.com/gusaln/PN532/releases/download/1.0.0/PN532.tar.gz
      PN532_SPI=https://github.com/gusaln/PN532/releases/download/1.0.0/PN532_SPI.tar.gz
    ```

2. We need to include the these dependencies in a header file and **not** in a `.cpp` file. This can be done in an existing `.h` file in your project or you can create one at either the `src` directory or the `include` directory. For example, say we create an `include/NFC.h` file

    ```cpp
    #include <NfcAdapter.h>
    #include <PN532.h>
    #include <PN532_SPI.h>
    ```

    and then include it into our `main.cpp` file

    ```cpp
    #include "NFC.h"
    ```

    This is required in order to allow the [Library Dependency Finder (LDF)](https://docs.platformio.org/en/latest/librarymanager/ldf.html#library-dependency-finder-ldf) of PlatformIO to include them correctly during compilation.
    Including the PN532* dependencies directly into a `.cpp` will cause errors.
    For more information, read the [PlatformIO docs on the matter](https://docs.platformio.org/en/latest/librarymanager/ldf.html).
