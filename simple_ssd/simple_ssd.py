import argparse
class DirectMappedFTL:
    def __init__(self, blocks, pages_per_block, tr, tp, te):
        self.B = blocks
        self.P = pages_per_block
        self.TR = tr
        self.TP = tp
        self.TE = te

        # no mapeamento direto, capacidade logica == capacidade fisica
        self.capacidade_logica = blocks * pages_per_block
        self.capacidade_fisica = blocks * pages_per_block

        self.total_paginas_programadas = 0
        self.total_escritas_logicas = 0
        
    
    def _endereco_fisico(self, lpn):
        if lpn < 0 or lpn >= self.capacidade_logica:
            raise ValueError(f"LPN {lpn} fora da capacidade lógica. ({self.capacidade_logica})")
        bloco =  lpn // self.P
        offset = lpn % self.P
        return bloco, offset
    
    def read(self, lpn):
        self._endereco_fisico(lpn)
        return self.TR
    
    def write(self, lpn):
        self._endereco_fisico(lpn)
        self.total_escritas_logicas += 1
        
        custo_leitura = self.TR * self.P
        custo_apagamento = self.TE 
        custo_escrita = self.TP * self.P
        
        self.total_paginas_programadas += self.P
        
        return custo_apagamento + custo_escrita + custo_leitura
    
    
