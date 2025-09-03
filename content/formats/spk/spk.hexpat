import std.io;
import std.core;

struct Bitmap {
    u16 width  [[color("005583")]];
    u16 height [[color("FFC200")]];
    u8 image[width * height];
};

struct Star {
    u16 x_pos;
    u16 y_pos;
    u32 bitmap_offset;
    Bitmap bitmap @ bitmap_offset;
};

fn count_stars(ref u16 layer) {
    u16 count = 0;
    for (u64 i = std::core::array_index(), i < std::core::member_count(layer), i = i + 1) {
        count += layer[i].number_of_stars_in_layer;
    }
    return count;
};

struct Layer_count {
    u16 number_of_stars_in_layer;
};

struct Data {
    u16 number_of_layers;
    Layer_count layer_count[number_of_layers];
    Star star[count_stars(layer_count)];
};

Data data @ 0x00;

std::print("Number of layers: {} ", data.number_of_layers);
std::print("Number of stars:  {} ", count_stars(data.layer_count));
