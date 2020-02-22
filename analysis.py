from pathlib import Path

import mne

data_file = Path('~/Desktop/eeg-categorization/cba/cba1ff01.cnt').expanduser().resolve()
raw_data = mne.io.read_raw_cnt(str(data_file))

data = {
    channel: raw_data[channel]
    for channel in raw_data.ch_names
}
onset = raw_data.annotations.onset

#raw_data.plot()
