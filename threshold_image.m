function threshold_image(input_path, output_path, thresh)
    input_path = convertCharsToStrings(input_path);
    img = imread(input_path);
    if size(img, 3) == 3
        img = rgb2gray(img);
    end
    bw = imbinarize(img, double(thresh)/255);
    imwrite(bw, output_path);
end