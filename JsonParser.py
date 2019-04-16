import json
import csv
from enum import Enum
from typing import Optional, Union, Any, Dict, TypeVar, Type, Callable, cast

T = TypeVar("T")
EnumT = TypeVar("EnumT", bound=Enum)


def from_str(x: Any) -> str:
    assert isinstance(x, str)
    return x


def from_none(x: Any) -> Any:
    assert x is None
    return x


def from_union(fs, x):
    for f in fs:
        try:
            return f(x)
        except:
            pass
    assert False


def from_bool(x: Any) -> bool:
    assert isinstance(x, bool)
    return x


def from_float(x: Any) -> float:
    assert isinstance(x, (float, int)) and not isinstance(x, bool)
    return float(x)


def from_int(x: Any) -> int:
    assert isinstance(x, int) and not isinstance(x, bool)
    return x


def is_type(t: Type[T], x: Any) -> T:
    assert isinstance(x, t)
    return x


def to_enum(c: Type[EnumT], x: Any) -> EnumT:
    assert isinstance(x, c)
    return x.value


def to_float(x: Any) -> float:
    assert isinstance(x, float)
    return x


def from_dict(f: Callable[[Any], T], x: Any) -> Dict[str, T]:
    assert isinstance(x, dict)
    return {k: f(v) for (k, v) in x.items()}


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


class PreMinedValue(Enum):
    CONSORTIUM = "Consortium"
    DPOS = "DPOS"
    D_PO_C = "DPoC"
    D_PO_R = "DPoR"
    D_PO_S = "DPoS"
    D_PO_S_L_PO_S = "DPoS/LPoS"
    D_PO_W_PO_W = "dPoW/PoW"
    E_PO_W = "ePoW"
    H_PO_W = "HPoW"
    LFT = "LFT"
    LIMITED_CONFIDENCE_PROOF_OF_ACTIVITY = "Limited Confidence Proof-of-Activity "
    L_PO_S = "LPoS"
    M_FBA = "mFBA"
    N_A = "N/A"
    POS = "Pos"
    POW_PO_S = "Pow/PoS"
    POW_PO_SC = "Pow/PoSC"
    PO_A = "PoA"
    PO_B = "PoB"
    PO_BH = "POBh"
    PO_B_PO_S = "PoB/PoS"
    PO_C = "PoC"
    PO_I = "PoI"
    PO_P = "PoP"
    PO_PP = "PoPP"
    PO_P_PO_V_PO_Q = "PoP/PoV/PoQ"
    PO_R = "PoR"
    PO_S = "PoS"
    PO_SIGN = "PoSign"
    PO_ST = "PoST"
    PO_S_L_PO_S = "PoS/LPoS"
    PO_S_PO_B = "PoS/PoB"
    PO_S_PO_D = "PoS/PoD"
    PO_S_PO_P = "PoS/PoP"
    PO_S_PO_W = "PoS/PoW"
    PO_S_PO_W_PO_T = "PoS/PoW/PoT"
    PO_W = "PoW"
    PO_WT = "PoWT"
    PO_W_AND_PO_S = "PoW and PoS"
    PO_W_D_PO_W = "PoW/DPoW"
    PO_W_HI_PO_S = "PoW/HiPoS"
    PO_W_N_PO_S = "PoW/nPoS"
    PO_W_PO_M_PO_SII = "PoW/PoM/PoSII"
    PO_W_PO_S = "PoW/PoS"
    PO_W_PO_S_PO_C = "PoW/PoS/PoC"
    PO_W_PO_W = "PoW/PoW"
    PO_W_PO_Z = "PoW/PoZ"
    PRE_MINED_VALUE_PO_S = "PoS "
    PRE_MINED_VALUE_PO_W_PO_S = "PoW/PoS "
    PROOF_OF_AUTHORITY = "Proof of Authority"
    PROOF_OF_OWNERSHIP = "Proof of Ownership"
    PROOF_OF_STAKE = "Proof of Stake"
    PURPLE_PO_W_PO_S = " PoW/PoS"
    SCRYPT_ADAPTIVE_N_ASIC_RESISTANT = "Scrypt-adaptive-N (ASIC resistant)"
    S_PO_S = "SPoS"
    TANGLE = "Tangle"
    T_PO_S = "TPoS"
    ZERO_KNOWLEDGE_PROOF = "Zero-Knowledge Proof"


class Datum:
    id: int
    url: str
    image_url: Optional[str]
    name: str
    symbol: str
    coin_name: str
    full_name: str
    algorithm: str
    proof_type: Union[PreMinedValue, int]
    fully_premined: int
    total_coin_supply: str
    built_on: Union[PreMinedValue, int]
    smart_contract_address: str
    pre_mined_value: PreMinedValue
    total_coins_free_float: PreMinedValue
    sort_order: int
    sponsored: bool
    is_trading: bool
    total_coins_mined: Optional[float]
    block_number: Optional[int]
    net_hashes_per_second: Optional[float]
    block_reward: Optional[float]
    block_time: Optional[int]

    def __init__(self, id: int, url: str, image_url: Optional[str], name: str, symbol: str, coin_name: str,
                 full_name: str, algorithm: str, proof_type: Union[PreMinedValue, int], fully_premined: int,
                 total_coin_supply: str, built_on: Union[PreMinedValue, int], smart_contract_address: str,
                 pre_mined_value: PreMinedValue, total_coins_free_float: PreMinedValue, sort_order: int,
                 sponsored: bool, is_trading: bool, total_coins_mined: Optional[float], block_number: Optional[int],
                 net_hashes_per_second: Optional[float], block_reward: Optional[float],
                 block_time: Optional[int]) -> None:
        self.id = id
        self.url = url
        self.image_url = image_url
        self.name = name
        self.symbol = symbol
        self.coin_name = coin_name
        self.full_name = full_name
        self.algorithm = algorithm
        self.proof_type = proof_type
        self.fully_premined = fully_premined
        self.total_coin_supply = total_coin_supply
        self.built_on = built_on
        self.smart_contract_address = smart_contract_address
        self.pre_mined_value = pre_mined_value
        self.total_coins_free_float = total_coins_free_float
        self.sort_order = sort_order
        self.sponsored = sponsored
        self.is_trading = is_trading
        self.total_coins_mined = total_coins_mined
        self.block_number = block_number
        self.net_hashes_per_second = net_hashes_per_second
        self.block_reward = block_reward
        self.block_time = block_time

    @staticmethod
    def from_dict(obj: Any) -> 'Datum':
        assert isinstance(obj, dict)
        id = int(from_str(obj.get("Id")))
        url = from_str(obj.get("Url"))
        image_url = from_union([from_str, from_none], obj.get("ImageUrl"))
        name = from_str(obj.get("Name"))
        symbol = from_str(obj.get("Symbol"))
        coin_name = from_str(obj.get("CoinName"))
        full_name = from_str(obj.get("FullName"))
        algorithm = from_str(obj.get("Algorithm"))
        proof_type = from_union([lambda x: from_union([PreMinedValue, lambda x: int(x)], from_str(x))],
                                obj.get("ProofType"))
        fully_premined = int(from_str(obj.get("FullyPremined")))
        total_coin_supply = from_str(obj.get("TotalCoinSupply"))
        built_on = from_union([lambda x: from_union([PreMinedValue, lambda x: int(x)], from_str(x))],
                              obj.get("BuiltOn"))
        smart_contract_address = from_str(obj.get("SmartContractAddress"))
        pre_mined_value = PreMinedValue(obj.get("PreMinedValue"))
        total_coins_free_float = PreMinedValue(obj.get("TotalCoinsFreeFloat"))
        sort_order = int(from_str(obj.get("SortOrder")))
        sponsored = from_bool(obj.get("Sponsored"))
        is_trading = from_bool(obj.get("IsTrading"))
        total_coins_mined = from_union([from_float, from_none], obj.get("TotalCoinsMined"))
        block_number = from_union([from_int, from_none], obj.get("BlockNumber"))
        net_hashes_per_second = from_union([from_float, from_none], obj.get("NetHashesPerSecond"))
        block_reward = from_union([from_float, from_none], obj.get("BlockReward"))
        block_time = from_union([from_int, from_none], obj.get("BlockTime"))
        return Datum(id, url, image_url, name, symbol, coin_name, full_name, algorithm, proof_type, fully_premined,
                     total_coin_supply, built_on, smart_contract_address, pre_mined_value, total_coins_free_float,
                     sort_order, sponsored, is_trading, total_coins_mined, block_number, net_hashes_per_second,
                     block_reward, block_time)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Id"] = from_str(str(self.id))
        result["Url"] = from_str(self.url)
        result["ImageUrl"] = from_union([from_str, from_none], self.image_url)
        result["Name"] = from_str(self.name)
        result["Symbol"] = from_str(self.symbol)
        result["CoinName"] = from_str(self.coin_name)
        result["FullName"] = from_str(self.full_name)
        result["Algorithm"] = from_str(self.algorithm)
        result["ProofType"] = from_union(
            [lambda x: from_str((lambda x: to_enum(PreMinedValue, (lambda x: is_type(PreMinedValue, x))(x)))(x)),
             lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.proof_type)
        result["FullyPremined"] = from_str(str(self.fully_premined))
        result["TotalCoinSupply"] = from_str(self.total_coin_supply)
        result["BuiltOn"] = from_union(
            [lambda x: from_str((lambda x: to_enum(PreMinedValue, (lambda x: is_type(PreMinedValue, x))(x)))(x)),
             lambda x: from_str((lambda x: str((lambda x: is_type(int, x))(x)))(x))], self.built_on)
        result["SmartContractAddress"] = from_str(self.smart_contract_address)
        result["PreMinedValue"] = to_enum(PreMinedValue, self.pre_mined_value)
        result["TotalCoinsFreeFloat"] = to_enum(PreMinedValue, self.total_coins_free_float)
        result["SortOrder"] = from_str(str(self.sort_order))
        result["Sponsored"] = from_bool(self.sponsored)
        result["IsTrading"] = from_bool(self.is_trading)
        result["TotalCoinsMined"] = from_union([to_float, from_none], self.total_coins_mined)
        result["BlockNumber"] = from_union([from_int, from_none], self.block_number)
        result["NetHashesPerSecond"] = from_union([to_float, from_none], self.net_hashes_per_second)
        result["BlockReward"] = from_union([to_float, from_none], self.block_reward)
        result["BlockTime"] = from_union([from_int, from_none], self.block_time)
        return result


class RateLimit:
    pass

    def __init__(self, ) -> None:
        pass

    @staticmethod
    def from_dict(obj: Any) -> 'RateLimit':
        assert isinstance(obj, dict)
        return RateLimit()

    def to_dict(self) -> dict:
        result: dict = {}
        return result


class CoinList:
    response: str
    message: str
    data: Dict[str, Datum]
    base_image_url: str
    base_link_url: str
    rate_limit: RateLimit
    has_warning: bool
    type: int

    def __init__(self, response: str, message: str, data: Dict[str, Datum], base_image_url: str, base_link_url: str,
                 rate_limit: RateLimit, has_warning: bool, type: int) -> None:
        self.response = response
        self.message = message
        self.data = data
        self.base_image_url = base_image_url
        self.base_link_url = base_link_url
        self.rate_limit = rate_limit
        self.has_warning = has_warning
        self.type = type

    @staticmethod
    def from_dict(obj: Any) -> 'CoinList':
        assert isinstance(obj, dict)
        response = from_str(obj.get("Response"))
        message = from_str(obj.get("Message"))
        data = from_dict(Datum.from_dict, obj.get("Data"))
        base_image_url = from_str(obj.get("BaseImageUrl"))
        base_link_url = from_str(obj.get("BaseLinkUrl"))
        rate_limit = RateLimit.from_dict(obj.get("RateLimit"))
        has_warning = from_bool(obj.get("HasWarning"))
        type = from_int(obj.get("Type"))
        return CoinList(response, message, data, base_image_url, base_link_url, rate_limit, has_warning, type)

    def to_dict(self) -> dict:
        result: dict = {}
        result["Response"] = from_str(self.response)
        result["Message"] = from_str(self.message)
        result["Data"] = from_dict(lambda x: to_class(Datum, x), self.data)
        result["BaseImageUrl"] = from_str(self.base_image_url)
        result["BaseLinkUrl"] = from_str(self.base_link_url)
        result["RateLimit"] = to_class(RateLimit, self.rate_limit)
        result["HasWarning"] = from_bool(self.has_warning)
        result["Type"] = from_int(self.type)
        return result


def coin_list_from_dict(s: Any) -> CoinList:
    return CoinList.from_dict(s)


def coin_list_to_dict(x: CoinList) -> Any:
    return to_class(CoinList, x)


def main():
    with open('coin_info.csv', mode='w') as csv_file:
        employee_writer = csv.writer(csv_file, delimiter=';')
        with open("coin_info.json", "r") as read_file:
            data = json.load(read_file)
            result = coin_list_from_dict(data)
            for coin in result.data.items():
                coin_name = coin[0]
                coin_id = coin[1].id
                employee_writer.writerow([coin_name, coin_id])


main()
