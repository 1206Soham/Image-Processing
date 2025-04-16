function flip_image(input_path, output_path, direction, angle)
    input_path = convertCharsToStrings(input_path);
    img = imread(input_path);
    if strcmp(direction, 'horizontal')
        flipped = flip(img, 2);
    elseif strcmp(direction, 'vertical')
        flipped = flip(img, 1);
    else
        error('Invalid direction');
    end
    rotated = imrotate(flipped, angle);
    imwrite(rotated, output_path);
end