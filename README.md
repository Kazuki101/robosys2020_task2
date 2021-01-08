# robosys2020_task2
ROSを用いてウェブカメラから取得した動画をパブリッシュして, サブスクライバ側でOpenCVを用いてグレースケール化と二値化させて, カラーとグレースケール, モノクロの動画を同時に表示するパッケージを作成しました。
## 前提条件
ROSを既にインストールしていて, ターミナルでroscoreを打った場合にROSが立ち上がる状態であることを前提に以下を記述していきます。
## 実行環境
|OS|Ubuntu18.04|
|:---|:---|
|ROS|Melodic|
## 実行手順
### uvc_cameraパッケージのインストール
    $sudo apt-get install ros-melodic-uvc-camera
### 今回作成したパッケージのインストール
    $cd catkin_ws/src
    $git clone https://github.com/Kazuki101/robosys2020_task2.git
### ビルド
    $catkin build
### 実行
    $roslaunch color_mono 
