function gray_level_slicing(input_path, output_path, min_level, max_level)
    input_path = convertCharsToStrings(input_path);
    img = rgb2gray(imread(input_path));
    sliced = uint8(zeros(size(img)));
    sliced(img >= min_level & img <= max_level) = 255;
    imwrite(sliced, output_path);
end