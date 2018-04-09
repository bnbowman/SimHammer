
class Unit(object):
    """
    Represent a generic unit from Warhammer 40k
    """
    def __init__(self, name=None, m=0, ws=7, bs=7, s=0, t=0, a=0, ld=0, sv=0, isv=None, weap=[]):
        self._name = name
        self._m    = m
        self._ws   = ws
        self._bs   = bs
        self._s    = s
        self._t    = t
        self._a    = a
        self._ld   = ld
        self._sv   = sv
        self._isv   = isv
        self._weap = []

    @property
    def Name(self):
        return self._name

    @property
    def Move(self):
        return self._m

    @property
    def M(self):
        return self._m

    @property
    def WeaponSkill(self):
        return self._ws

    @property
    def WS(self):
        return self._ws

    @property
    def BallisticSkill(self):
        return self._bs

    @property
    def BS(self):
        return self._bs

    @property
    def Strength(self):
        return self._s

    @property
    def S(self):
        return self._s

    @property
    def Toughness(self):
        return self._t

    @property
    def T(self):
        return self._t

    @property
    def Attacks(self):
        return self._a

    @property
    def A(self):
        return self._a

    @property
    def BallisticSkill(self):
        return self._bs

    @property
    def BS(self):
        return self._bs

    @property
    def Leadership(self):
        return self._ld

    @property
    def Ld(self):
        return self._ld

    @property
    def ArmorSave(self):
        return self._sv

    @property
    def Sv(self):
        return self._sv

    @property
    def InvulnSave(self):
        return self._sv

    @property
    def ISv(self):
        return self._isv

    @property
    def Weapons(self):
        return self._weap

    def toWound(self, strength):
        if strength > (self._t * 2):
            return 2
        elif strength > self._t:
            return 3
        elif strength == self._t:
            return 4
        elif (strength * 2) < self._t:
            return 6
        else:
            return 5

    def __repr__(self):
        if self.ISv:
            isv_str = "({}++)".format(self._isv)
        else:
            isv_str = ""
        return '<{0}: M{1}" WS{2}+ BS{3}+ S{4} T{5} A{6} Ld{7} Sv{8}+{9}>'.format(self.Name, self.M, self.WS, self.BS, self.S, self.T, self.A, self.Ld, self.Sv, isv_str)
