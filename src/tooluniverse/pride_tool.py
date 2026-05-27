import requests
from typing import Any, Dict
from urllib.parse import urlencode
from .base_tool import BaseTool
from .http_utils import request_with_retry
from .tool_registry import register_tool


@register_tool("PRIDERESTTool")
class PRIDERESTTool(BaseTool):
    def __init__(self, tool_config: Dict):
        super().__init__(tool_config)
        self.base_url = "https://www.ebi.ac.uk/pride/ws/archive/v2"
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json"})
        self.timeout = 30

    def _build_url(self, args: Dict[str, Any]) -> str:
        url = self.tool_config["fields"]["endpoint"]
        for k, v in args.items():
            url = url.replace(f"{{{k}}}", str(v))
        # Append query params that aren't URL-template slots (e.g. pageSize).
        # Start from the tool's configured defaults, then honor a per-call page_size.
        extra = dict(self.tool_config["fields"].get("params") or {})
        if "page_size" in args and args["page_size"] is not None:
            try:
                extra["pageSize"] = str(max(1, min(int(args["page_size"]), 100)))
            except (TypeError, ValueError):
                pass
        if extra:
            url += ("&" if "?" in url else "?") + urlencode(extra)
        return url

    def run(self, arguments: Dict[str, Any]) -> Dict[str, Any]:
        url = None
        try:
            url = self._build_url(arguments)
            response = request_with_retry(
                self.session, "GET", url, timeout=self.timeout, max_attempts=3
            )
            if response.status_code != 200:
                return {
                    "status": "error",
                    "error": "PRIDE API error",
                    "url": url,
                    "status_code": response.status_code,
                    "detail": (response.text or "")[:500],
                }
            data = response.json()
            return {"status": "success", "data": data, "url": url}
        except Exception as e:
            return {
                "status": "error",
                "error": f"PRIDE API error: {str(e)}",
                "url": url,
            }
