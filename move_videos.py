import os
import shutil

from app.utils import utils

if __name__ == '__main__':

    # 移动视频文件到指定目录
    # 视频文件所在目录
    video_dir = utils.task_dir()
    print(f"video_dir: {video_dir}")

    # 目标目录: 视频文件存储目录 storage/videos
    target_dir = utils.storage_dir("videos")
    print(f"target_dir: {target_dir}")

    # 遍历视频目录下的所有文件

    for filename in os.listdir(video_dir):
        # 遍历 tasks 每个子目录的下一层级里面的所有文件
        sub_dir = os.path.join(video_dir, filename)
        if not os.path.isdir(sub_dir):
            continue

        for sub_filename in os.listdir(sub_dir):
            origin_sub_filename = sub_filename

            # print(f"sub_filename: {sub_filename}")

            if sub_filename.endswith(".mp4") and sub_filename.find("final") > 0:
                # 构建源文件的完整路径
                source_path = os.path.join(video_dir, filename, origin_sub_filename)

                # 去掉 sub_filename 中的 final
                sub_filename = sub_filename.replace("-", "").strip()
                sub_filename = sub_filename.replace("final1", "").strip()
                # 构建目标文件的完整路径, 目标文件路径: storage/videos/sub_filename
                target_path = os.path.join(target_dir, sub_filename)

                # 如果目标文件已存在, 则覆盖
                if os.path.exists(target_path):
                    os.remove(target_path)

                # print(f"source_path: {source_path}")
                # print(f"target_path: {target_path}")

                # 移动文件
                shutil.move(source_path, target_path)
                print(f"Moved: {sub_filename}")
