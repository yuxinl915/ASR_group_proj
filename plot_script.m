function plot_emg_datasets()
    % File names
    file_paper = 'dataset/s1_r_1/s1_r_1-paper-8-emg.csv';
    file_rock = 'dataset/s1_r_1/s1_r_1-rock-8-emg.csv';
    file_scissors = 'dataset/s1_r_1/s1_r_1-scissors-8-emg.csv';

    % Load and plot the first dataset (Paper)
    data_paper = load_emg_data(file_paper);
    figure('Name', 'Paper EMG Data');
    plot_emg_data(data_paper);

    % Load and plot the first dataset (Rock)
    data_rock = load_emg_data(file_rock);
    figure('Name', 'Rock EMG Data');
    plot_emg_data(data_rock);

    % Load and plot the second dataset (Scissors)
    data_scissors = load_emg_data(file_scissors);
    figure('Name', 'Scissors EMG Data');
    plot_emg_data(data_scissors);
end

function emg_data = load_emg_data(filename)
    % Load EMG data from a CSV file
    opts = detectImportOptions(filename, 'NumHeaderLines', 1); % Skip the header
    opts.SelectedVariableNames = [3:10]; % Select only the EMG channel columns
    emg_data = readtable(filename, opts);
    emg_data = table2array(emg_data); % Convert to array if needed
end

function plot_emg_data(emg_data)
    % Plot all channels of EMG data
    for i = 1:size(emg_data, 2)
        subplot(size(emg_data, 2), 1, i);
        plot(emg_data(:,i));
        title(['EMG Channel ', num2str(i)]);
        xlabel('Time (samples)');
        ylabel('Amplitude');
    end
    % Adjust figure properties as needed
end