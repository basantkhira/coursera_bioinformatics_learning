from collections import Counter

def spectral_convolution(spectrum):
    result = []
    n = len(spectrum)

    for i in range(n):
        for j in range(n):
            diff = spectrum[j] - spectrum[i]
            if diff > 0:
                result.append(diff)

    return Counter(result)

def spectral_spectral_convolution_top_element(counts,M):
    filtered = {mass: cnt for mass, cnt in counts.items() if 57 <= mass <= 200}
    if not filtered:
        return []
    
    sorted_elements = sorted(filtered.items(), key=lambda x: (x[1], x[0]), reverse=True)
    
    if M >= len(sorted_elements):
        return [mass for mass, cnt in sorted_elements]
    
    threshold = sorted_elements[M - 1][1]  
    return [mass for mass, cnt in sorted_elements if cnt >= threshold]
    

if __name__ == "__main__":
    spectrum = list(map(int,input("spectrum: ").split(" ")))
    M = int(input("M: ").strip())
    
    counts = spectral_convolution(spectrum)
    top = spectral_spectral_convolution_top_element(counts,M)
    print(top)
