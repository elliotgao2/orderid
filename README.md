# OrderId

- Short. 32 digit lengths.
- Unique. Any time any computer.
- Ordered. By time.

## Installation

`pip install orderid`

## Usage

millisecond timestamp + threading uniq_id + process_time

```python
import orderid

order_id = orderid.orderid() # 15651676055260064963218265906703
```
