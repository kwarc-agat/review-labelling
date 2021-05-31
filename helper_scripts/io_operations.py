import pandas as pd

critics = ["Dennis+Schwartz", "James+Berardinelli", "Scott+Renshaw", "Steve+Rhodes"]


def read_file_to_series(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        lines = [elem.strip() for elem in lines]

    return pd.Series(lines, range(len(lines)))


def create_dataset():
    frames = []
    for name in critics:
        directory = "scale_data\\scaledata\\" + name + "\\"
        filename_subj = directory + "subj."+name
        filename_rating = directory + "rating." + name
        filename_label3 = directory + "label.3class." + name
        filename_label4 = directory + "label.4class." + name
        subj = read_file_to_series(filename_subj)
        rating = read_file_to_series(filename_rating)
        label3 = read_file_to_series(filename_label3)
        label4 = read_file_to_series(filename_label4)

        d = {
            "review": subj,
            "rating": rating,
            "label3": label3,
            "label4": label4
        }

        df = pd.DataFrame(d)
        frames.append(df)

    dataset = pd.concat(frames, ignore_index=True)
    print(dataset)
    dataset.to_csv(path_or_buf='dataset.csv', index=False)


def read_dataset(filename):
    return pd.read_csv(filename)