import json
import random
import numpy as np
def generate_ecg_sample(sample_id, label, channels=12, signal_length=1000, sampling_rate=360):
    # 生成模拟ECG信号
    ecg_signal = (np.random.normal(0, 1, (channels, signal_length))).tolist()
    # 时域特征
    rr_intervals = [round(random.uniform(0.6, 1.2), 3) for _ in range(10)]
    mean_rr = round(np.mean(rr_intervals), 3)
    std_rr = round(np.std(rr_intervals), 3)
    rmssd = round(np.sqrt(np.mean(np.diff(rr_intervals) ** 2)), 3)
    pnn50 = round(sum(abs(np.diff(rr_intervals)) > 0.05) / len(rr_intervals), 2)
    heart_rate = int(60 / mean_rr)
    # 形态特征
    p_wave_duration = round(random.uniform(0.07, 0.12), 3)
    p_wave_amplitude = round(random.uniform(0.1, 0.2), 2)
    qrs_duration = round(random.uniform(0.08, 0.12), 3)
    qrs_amplitude = round(random.uniform(0.8, 2.0), 2)
    st_segment_offset = round(random.uniform(-0.2, 0.2), 2)
    qt_interval = round(random.uniform(0.32, 0.44), 3)
    t_wave_duration = round(random.uniform(0.12, 0.2), 3)
    t_wave_amplitude = round(random.uniform(0.2, 0.4), 2)
    # 频域特征
    hf_lf_ratio = round(random.uniform(0.5, 2.5), 2)
    dominant_frequency = round(random.uniform(0.1, 0.3), 2)
    energy_density = {
        "0.04-0.15Hz": round(random.uniform(0.1, 0.5), 2),
        "0.15-0.4Hz": round(random.uniform(0.2, 0.6), 2)
    }
    return {
        "id": f"ECG_{sample_id}",
        "label": label,
        "channels": channels,
        "sampling_rate": sampling_rate,
        "ecg_signal": ecg_signal,
        "features": {
            "time_domain": {
                "rr_intervals": rr_intervals,
                "mean_rr": mean_rr,
                "std_rr": std_rr,
                "rmssd": rmssd,
                "pnn50": pnn50,
                "heart_rate": heart_rate
            },
            "morphological": {
                "p_wave_duration": p_wave_duration,
                "p_wave_amplitude": p_wave_amplitude,
                "qrs_duration": qrs_duration,
                "qrs_amplitude": qrs_amplitude,
                "st_segment_offset": st_segment_offset,
                "qt_interval": qt_interval,
                "t_wave_duration": t_wave_duration,
                "t_wave_amplitude": t_wave_amplitude
            },
            "frequency_domain": {
                "hf_lf_ratio": hf_lf_ratio,
                "dominant_frequency": dominant_frequency,
                "energy_density": energy_density
            }
        }
    }
def generate_dataset(num_samples=100, output_file="ecg_dataset.json"):
    labels = ["normal", "arrhythmia", "afib", "mi"]
    data = []
    for i in range(num_samples):
        label = random.choice(labels)
        sample = generate_ecg_sample(i+1, label)
        data.append(sample)
    with open(output_file, "w") as f:
        json.dump(data, f, indent=2)

if __name__ == "__main__":
    generate_dataset(num_samples=100, output_file="ecg_dataset.json")

