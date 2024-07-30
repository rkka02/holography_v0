import cv2

class Resizer:
    def resize(source, original_resolution, target_resolution):
        M, N = source.shape
        if M != N:
            raise ValueError('Source shape should be same')
        
        ratio = original_resolution/target_resolution

        start_idx = int((N-N/ratio)//2)
        end_idx = int((N+N/ratio)//2)
        temp = source[start_idx:end_idx, start_idx:end_idx]
        temp = cv2.resize(temp, dsize=(N,N))
        
        return temp