function convert_image(input_path, output_path, mode)
    input_path = convertCharsToStrings(input_path);
    img = imread(input_path);
    if strcmp(mode, 'gray')
        out = rgb2gray(img);
    elseif strcmp(mode, 'binary')
        gray = rgb2gray(img);
        level = graythresh(gray);
        out = imbinarize(gray, level);
    else
        error('Invalid mode. Use "gray" or "binary".');
    end
    imwrite(out, output_path);
end