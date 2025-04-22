from pydantic import SecretStr, BaseModel
from typing import Literal, TypeAlias
from ..api import DBConfig, DBCaseConfig, MetricType


ChromaMetric: TypeAlias = Literal["l2", "cosine", "ip"]


class ChromaConfig(DBConfig):
    password: SecretStr
    host: SecretStr
    port: int = 8000

    def to_dict(self) -> dict:
        return {
            "host": self.host.get_secret_value(),
            "port": self.port,
            "password": self.password.get_secret_value(),
        }


class ChromaHNSWConfig(BaseModel, DBCaseConfig):
    metric_type: MetricType = MetricType.COSINE
    M: int = 16
    efConstruction: int = 100
    ef: int = 100

    def parse_metric(self) -> ChromaMetric:
        match self.metric_type:
            case MetricType.COSINE:
                return "cosine"
            case MetricType.L2:
                return "l2"
            case MetricType.IP:
                return "ip"
            case _:
                raise NotImplementedError

    def index_param(self) -> dict:
        return {
            "hnsw:space": self.parse_metric(),
            "hnsw:construction_ef": self.efConstruction,
            "hnsw:M": self.M,
            "hnsw:search_ef": self.ef,
        }

    def search_param(self) -> dict:
        raise NotImplementedError
