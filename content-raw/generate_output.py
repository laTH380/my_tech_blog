# このディレクトリを更新したら以下を実行することで正式なContentディレクトリに反映されるようになります。
# python C:\Users\thiro\Documents\CreationProgram\my_homepage\teqh_blog\content-raw\generate_output.py



import os
import shutil
from sync_directories import sync_directories
from manage_randomFilename import get_randomized_dir_name, generate_randomized_dir_name

def create_md_tree(root_dir, base_url, output_file):
    # 開始のMarkdownテキスト
    md_content = f"# Directory Structure of content-raw\n\n"
    
    # ツリー構造を作成する関数
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # 相対パスを計算して、Markdown用のインデントを作成
        level = dirpath.replace(root_dir, '').count(os.sep)
        indent = '  ' * level
        folder_name = os.path.basename(dirpath)
        
        # フォルダ名を追加
        randamized_folder_name = get_randomized_dir_name(folder_name)
        md_content += f"{indent}- {folder_name}\\ {randamized_folder_name} \n"
        
        # ファイル名もリンク付きで追加
        subindent = '  ' * (level + 1)
        for filename in filenames:
            if os.path.splitext(filename)[1] != '.md':
                continue
            file_url = f"{base_url}/{filename}"
            md_content += f"{subindent}- [{filename}]({file_url})\n"
    
    # 結果をMarkdownファイルに書き込む
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(md_content)



def output_post_dir_for_build(source, destination):
    source_children = os.listdir(source)
    if 'index.md' in source_children:
        source_dir_name = os.path.basename(source)
        is_exists = get_randomized_dir_name(source_dir_name)
        if not is_exists:
            randomized_folder_name = generate_randomized_dir_name(source_dir_name)
            new_dir_path = os.path.join(destination, randomized_folder_name)
            try:
                shutil.copytree(source, new_dir_path)  # srcをnew_dir_pathにコピー
                print(f"ディレクトリ '{source}' を '{new_dir_path}' にコピーしました。")
            except FileExistsError:
                print(f"エラー: '{new_dir_path}' はすでに存在します。")
            except Exception as e:
                print(f"エラーが発生しました: {e}")
        else:
            sync_directories(source, destination)
    else:
        for source_child in source_children:
            source_child_path = os.path.join(source, source_child)
            if os.path.isfile(source_child_path):
                continue
            new_destination_path = ""
            randomized_folder_name = get_randomized_dir_name(source_child)
            if not randomized_folder_name:
                randomized_folder_name = generate_randomized_dir_name(source_child)
                new_destination_path = os.path.join(destination, randomized_folder_name)
                os.makedirs(new_destination_path, exist_ok=True)
            else:
                new_destination_path = os.path.join(destination, randomized_folder_name)
            output_post_dir_for_build(source_child_path, new_destination_path)


if __name__ == "__main__":
    current_file_path = os.path.abspath(__file__)
    current_dir = os.path.dirname(current_file_path)
    # URLのためビルド用のディレクトリにしてcontent/に出力
    source_dir = f"{current_dir}/content/post"
    destination_dir = f'{current_dir}/../content/post'
    output_post_dir_for_build(source_dir, destination_dir)
    # root_dirには取得したいディレクトリのパスを指定
    # base_urlは表示用のリンク先のベースURLを指定
    content_raw_dir = f'{current_dir}/content'
    base_url = 'content'
    output_file = f'{current_dir}/article_structure.md'
    create_md_tree(content_raw_dir, base_url, output_file)
    
