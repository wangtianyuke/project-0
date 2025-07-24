{
    "id": "样本唯一编号",
    "label": "标签（如normal, arrhythmia, afib, mi等）",
    "channels": 12,  // 通道数
    "sampling_rate": 360,  // 采样率Hz
    "ecg_signal": [
      // shape: [channels, signal_length]
      // 例如12通道，每通道1000个采样点
      [[0.1, 0.2, ...], ...]
    ],
    "features": {
      "time_domain": {
        "rr_intervals": [0.8, 0.82, ...], // RR间期（秒）
        "mean_rr": 0.81,
        "std_rr": 0.02,
        "rmssd": 0.015,
        "pnn50": 0.12,
        "heart_rate": 75
      },
      "morphological": {
        "p_wave_duration": 0.09,
        "p_wave_amplitude": 0.15,
        "qrs_duration": 0.11,
        "qrs_amplitude": 1.2,
        "st_segment_offset": 0.05,
        "qt_interval": 0.38,
        "t_wave_duration": 0.16,
        "t_wave_amplitude": 0.3
      },
      "frequency_domain": {
        "hf_lf_ratio": 1.5,
        "dominant_frequency": 0.18,
        "energy_density": {
          "0.04-0.15Hz": 0.25,
          "0.15-0.4Hz": 0.45
        }
      }
    }
  }