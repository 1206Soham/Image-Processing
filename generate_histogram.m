function generate_histogram(input_path)
    input_path = convertCharsToStrings(input_path);
    img = imread(input_path);
    if size(img, 3) == 3
        img = rgb2gray(img);
    end
    figure('Visible','off');
    imhist(img);
    saveas(gcf, 'images/histogram.jpg');  % Save histogram image in output folder
    close;
end