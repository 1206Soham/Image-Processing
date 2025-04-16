function info = get_image_info(input_path)
    input_path = convertCharsToStrings(input_path);
    img = imread(input_path);
    dims = size(img);
    if ndims(img) == 2
        type = 'Grayscale';
    elseif ndims(img) == 3 && dims(3) == 3
        type = 'RGB';
    else
        type = 'Unknown';
    end
    info = sprintf('Type: %s\nDimensions: %d x %d', type, dims(1), dims(2));
end