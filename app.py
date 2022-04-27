from datetime import datetime
from transactions.zmm_mrp_masivo import masivo
from transactions.zpp_tablero import tablero
from transactions.mb52 import mb52
from transactions.me2n import me2n
from log_class import log


def main(key):
    
    Log = log()
    masivo(key,Log)
    tablero(key,Log)
    mb52(key,Log)
    me2n(key,Log)
    log.Level = 'INFO'
    log.ProcesoInterno = 'Fin Transaccion'
    log.Mensaje = 'Fin Transaccion'
    log.FinTransaccion = datetime.now()
    log.postFin()      