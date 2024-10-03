import os
import shutil

def sync_directories(source_dir, target_dir):
    # ソースディレクトリが存在するか確認
    if not os.path.exists(source_dir):
        print(f"ソースディレクトリが見つかりません: {source_dir}")
        return
    
    # ターゲットディレクトリが存在しない場合は作成
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"ターゲットディレクトリを作成しました: {target_dir}")

    # ソースディレクトリ内のファイルとサブディレクトリを取得
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        target_item = os.path.join(target_dir, item)

        # ファイルの場合
        if os.path.isfile(source_item):
            shutil.copy2(source_item, target_item)
            # print(f"ファイルをコピーしました: {source_item} -> {target_item}")

        # ディレクトリの場合
        elif os.path.isdir(source_item):
            sync_directories(source_item, target_item)

    # ターゲットディレクトリ内のアイテムをチェックし、ソースに存在しないものを削除
    for item in os.listdir(target_dir):
        target_item = os.path.join(target_dir, item)
        source_item = os.path.join(source_dir, item)
        
        if not os.path.exists(source_item):
            if os.path.isfile(target_item):
                os.remove(target_item)
                # print(f"ファイルを削除しました: {target_item}")
            elif os.path.isdir(target_item):
                shutil.rmtree(target_item)
                # print(f"ディレクトリを削除しました: {target_item}")

if __name__ == "__main__":
    source_directory = input("ソースディレクトリのパスを入力してください: ")
    target_directory = input("ターゲットディレクトリのパスを入力してください: ")
    
    sync_directories(source_directory, target_directory)
    print("ディレクトリの同期が完了しました。")
