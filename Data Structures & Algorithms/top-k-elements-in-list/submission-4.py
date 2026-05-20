class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frecuencias = {}
        for n in nums:
            if n in frecuencias:
                frecuencias[n] +=1
            else:
                frecuencias[n] = 1
        resultados = []
        
        for _ in range(k):
            max_frecuencia = 0
            num_ganador = 0
            
            for num, conteo in frecuencias.items():
                if conteo > max_frecuencia:
                    num_ganador = num
                    max_frecuencia = conteo
                
            resultados.append(num_ganador)
            frecuencias[num_ganador] = 0
            
        return resultados