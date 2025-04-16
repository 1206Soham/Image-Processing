function bit_plane_slicing(input_path, output_path, bit)
    input_path = convertCharsToStrings(input_path);
    img = imread(input_path);
    if size(img, 3) == 3
        img = rgb2gray(img);
    end
    plane = bitget(img, bit + 1);  % MATLAB uses 1-based indexing
    result = uint8(plane) * 255;
    imwrite(result, output_path);
end