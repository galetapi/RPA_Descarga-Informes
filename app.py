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
    log.level = 'INFO'
    log.procesointerno = 'Fin Transaccion'
    log.mensaje = 'Fin Transaccion'
    log.fintransaccion = datetime.now()
    log.postFin()      