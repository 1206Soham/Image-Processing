function filter_noise(input_path, output_path, filter_type)
    input_path = convertCharsToStrings(input_path);
    img = imread(input_path);
    if strcmp(filter_type, 'salt_pepper')
        noisy = imnoise(img, 'salt & pepper', 0.02);
        filtered = medfilt2(rgb2gray(noisy), [3 3]);
    elseif strcmp(filter_type, 'gaussian')
        noisy = imnoise(img, 'gaussian', 0, 0.01);
        h = fspecial('gaussian', [3 3], 0.5);
        filtered = imfilter(rgb2gray(noisy), h);
    else
        error('Unsupported filter type');
    end
    imwrite(filtered, output_path);
end