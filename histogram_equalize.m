function histogram_equalize(input_path, output_path)
    input_path = convertCharsToStrings(input_path);
    img = imread(input_path);
    if size(img, 3) == 3
        img = rgb2gray(img);
    end
    eq_img = histeq(img);
    imwrite(eq_img, output_path);
end