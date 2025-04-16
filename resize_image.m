function resize_image(input_path, output_path, new_width, new_height)
    input_path = convertCharsToStrings(input_path);
    img = imread(input_path);
    resized = imresize(img, [new_height, new_width]);
    imwrite(resized, output_path);
end