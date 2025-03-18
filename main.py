import pandas as pd
import matplotlib.pyplot as plt

# ファイルの読み込み
filename = ''  #ファイルのパスをコピー
df = pd.read_csv(filename, header=None, sep=',')

# 列名の設定
df.columns = ['time', 'battery_voltage', 'temperature', 
              'accel_x', 'accel_y', 'accel_z', 
              'gyro_x', 'gyro_y', 'gyro_z', 
              'mag_x', 'mag_y', 'mag_z']


# 2×2グリッドでサブプロット作成
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

# 1. mag_x vs 時間
axes[0, 0].scatter(df['time'], df['mag_x'], s=10, color='blue')
axes[0, 0].set_title('Magnetic Field X vs Time')
axes[0, 0].set_xlabel('Time')
axes[0, 0].set_ylabel('Magnetic Field X')
axes[0, 0].grid()

# 2. mag_y vs 時間
axes[0, 1].scatter(df['time'], df['mag_y'], s=10, color='green')
axes[0, 1].set_title('Magnetic Field Y vs Time')
axes[0, 1].set_xlabel('Time')
axes[0, 1].set_ylabel('Magnetic Field Y')
axes[0, 1].grid()

# 3. mag_z vs 時間
axes[1, 0].scatter(df['time'], df['mag_z'], s=10, color='red')
axes[1, 0].set_title('Magnetic Field Z vs Time')
axes[1, 0].set_xlabel('Time')
axes[1, 0].set_ylabel('Magnetic Field Z')
axes[1, 0].grid()

# 4. mag_y と mag_z の2次元プロット（横軸: mag_y, 縦軸: mag_z）
axes[1, 1].scatter(df['mag_y'], df['mag_z'], s=10, color='purple')
axes[1, 1].set_title('Magnetic Field: Z vs Y')
axes[1, 1].set_xlabel('Magnetic Field Y')
axes[1, 1].set_ylabel('Magnetic Field Z')
axes[1, 1].grid()

plt.tight_layout()
plt.show()
