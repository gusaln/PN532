LIBS="PN532 PN532_HSU PN532_I2C PN532_SPI PN532_SWHSU"

mkdir out &> /dev/null

for lib in $LIBS; do
    echo "Packaging $lib"
    zip out/$lib $lib/*
done