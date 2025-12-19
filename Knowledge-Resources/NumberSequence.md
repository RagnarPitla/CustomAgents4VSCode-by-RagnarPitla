# 📋 Number Sequence Overview

## Two Types of Number Sequences

| Type               | Description                                                                                         |
| ------------------ | --------------------------------------------------------------------------------------------------- |
| **Continuous**     | Does NOT skip any numbers (no gaps) - also called "No Gap Number Sequence"                          |
| **Non-Continuous** | Numbers used sequentially but MAY skip numbers (if a transaction is cancelled, that number is lost) |

## Key Configuration Areas

- **Scope:** Company, Legal Entity, Operating Unit
- **Segments:** Company code, Fiscal calendar period, Constants, Alphanumeric auto-generated numbers
- **Continuous Flag:** Checkbox that makes sequence continuous vs non-continuous

---

# ⚠️ The Problem (Before the Feature)

## Legal Requirements

- Many countries (Europe, APAC, India) have legal compliance requirements for no gaps in number series
- **Critical for:** Invoices, Vouchers, Journals

## Performance Issues

- Continuous number sequences caused severe SQL blocking
- Bulk operations were time-consuming
- Concurrent requests got serialized
- Blocking sessions occurred on `NumberSequenceTable` and `NumberSequenceList` tables
- Numbers were lost during AOS crashes or unexpected terminations

## Business Scenarios Impacted

- Journals
- Vouchers
- Customer Invoices
- Vendor Invoices
- Sales Orders

---

# ✅ The Solution: Pre-Allocation for Continuous Number Sequences

## Key Improvements

### Pre-Allocation Now Works for Continuous Sequences

- Previously only worked for non-continuous
- Default pre-allocation quantity: **5 numbers**
- Can be configured based on business needs (10, 100, etc.)
- **Example:** Pre-allocating 100 numbers reduces SQL calls by 99!

### SQL Optimizations

| Hint       | Purpose                                  |
| ---------- | ---------------------------------------- |
| `READPAST` | Enables reading rows without locks       |
| `NOLOCK`   | Avoids locking entire table during reads |
| `ROWLOCK`  | Prevents table-level locks               |

### New Status Value: "Active Non-Blocking"

- New status in `NumberSequenceList` table
- Indicates the number is from the new feature with reduced blocking

### Automatic Cleanup Job

- Runs every **24 hours** by default (configurable to 6-8 hours)
- Recovers numbers lost due to crashes/unexpected terminations
- Runs as a backend job (not visible in batch jobs)

---

# 🔧 Configuration Steps

1. **Enable the Feature in Feature Management**
2. Navigate to: **Organization Administration → Number Sequences** (or module parameters)
3. Check **"Continuous"** checkbox in General tab
4. Go to **Performance** tab:
   - Set **Pre-allocation:** Yes
   - Set **Quantity:** 5 (default) or higher based on volume
5. Configure **Automatic Cleanup** interval if needed

---

# 📊 Performance Impact

| Metric                | Before              | After                           |
| --------------------- | ------------------- | ------------------------------- |
| SQL Calls             | Multiple per number | 1 call per pre-allocation batch |
| Blocking              | High (serialized)   | Minimal                         |
| Number Loss (crashes) | Possible            | Recovered via cleanup           |

---

# 🎯 Key Takeaways

- ✅ Test in **Sandbox first** before production
- ✅ Adjust pre-allocation quantity based on your transaction volume
- ✅ Configure cleanup interval based on business needs
- ✅ This feature has existed since the beginning of AX - now finally addressed
- ✅ Legal compliance can now be met without sacrificing performance
- ✅ Unused pre-allocated numbers from cancelled or failed transactions are reclaimed before being assigned, helping maintain the _no gaps_ behavior
