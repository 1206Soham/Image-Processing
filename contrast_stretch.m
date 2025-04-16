function contrast_stretch(input_path, output_path, min_thresh, max_thresh)
    input_path = convertCharsToStrings(input_path);
    img = imread(input_path);
    if size(img, 3) == 3
        img = rgb2gray(img);
    end
    stretched = imadjust(img, [double(min_thresh)/255, double(max_thresh)/255], []);
    imwrite(stretched, output_path);
end