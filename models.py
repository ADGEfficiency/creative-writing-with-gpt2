from google_drive_downloader import GoogleDriveDownloader as gdd


models = {
    'alan-watts': '1TxMWBLuN-GLBMB3ebi5uIbq374jt6HE7',
    'bible': '1x8SQgqZyLGRdHRV6BUIHEPxZuWUCyhRc',
    'harry': '1-3iQhw89Biyv1QMf4o2BEahoPX9g3fNd',
    'meditations': '1-9TiibA0_dqD7dqyJnBNBrZnLuegAa_E',
    'tolkien': '1-0lq9cGClSqcvcI3WqGkxdmAdoWrhD4e'
}


def download_pretrained_model(model_name):
    print('downloading {}'.format(model_name))
    drive_id = models[model_name]
    gdd.download_file_from_google_drive(
        file_id=drive_id,
        dest_path='./models/{}.zip'.format(model_name),
        unzip=True
    )

if __name__ == '__main__':
    for key in models.keys():
        download_pretrained_model(key)
