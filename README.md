# robosys2020_task2
ROSを用いてウェブカメラから取得した動画をパブリッシュして, サブスクライバ側でOpenCVを用いてグレースケール化と二値化させて, カラーとグレースケール, モノクロの動画を同時に表示するパッケージを作成しました。
始めはカラーとグレースケール, モノクロでそれぞれパブリッシュしようとしていましたが, サブスクライバ側で変換させることでパブリッシュ側からの送るnodeを1個に減らしました。
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
mono.launchにcamera_node.launchとpub.py, sub.pyを纏めたのでroscoreなども必要なく以下のコマンドを実行するだけで全部起動することができます。

    $roslaunch color_mono mono.launch
## 二値化処理の閾値について
sub.pyの12行目のmono = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)の125を0~255の間で任意に変化させることで白と黒の判定基準を自由に変更することができます。
## 動画のリンク
https://youtu.be/yxHQgNMbwm8
