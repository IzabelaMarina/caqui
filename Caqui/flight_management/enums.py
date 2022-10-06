from shelve import BsdDbShelf
from wsgiref.handlers import CGIHandler
from django.db import models

class Status(models.IntegerChoices):
    PREVISTO = 0
    CANCELADO = 1
    EMBARCANDO = 2
    PROGRAMADO = 3
    TAXIANDO_IDA = 4
    PRONTO = 5
    AUTORIZADO = 6
    EM_VOO = 7
    ATERRISSADO = 8
    DESEMBARCANDO = 9

class Role(models.IntegerChoices):
    PILOTO = 0
    OPERADOR_DE_VOO = 1
    GERENTE_DE_OPERACOES = 2
    CONTROLADOR_DE_VOO = 3

class AirportCodes(models.IntegerChoices):
    BSB = 0
    CGH = 1
    GIG = 2
    SSA = 3
    FLN = 4
    POA = 5
    VCP = 6
    REC = 7
    CWB = 8
    BEL = 9
    VIX = 10
    SDU = 11
    CGB = 12
    CGR = 13
    FOR = 14
    MCP = 15
    MGF = 16
    GYN = 17
    NVT = 18
    MAO = 19
    NAT = 20
    BPS = 21
    MCZ = 22
    PMW = 23
    SLZ = 24
    GRU = 25
    LDB = 26
    PVH = 27
    RBR = 28
    JOI = 29
    UDI = 30
    CXJ = 31
    IGU = 32
    THE = 33
    AJU = 34
    JPA = 35
    PNZ = 36
    CNF = 37
    BVB = 38
    CPV = 39
    STM = 40
    IOS = 41
    JDO = 42
    IMP = 43
    XAP = 44
    MAB = 45
    CZS = 46
    PPB = 47
    CFB = 48
    FEN = 49
    JTC = 50
    MOC = 51