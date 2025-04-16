function negative_image(input_path, output_path)
    input_path = convertCharsToStrings(input_path);
    img = imread(input_path);
    neg = 255 - img;
    imwrite(neg, output_path);
end