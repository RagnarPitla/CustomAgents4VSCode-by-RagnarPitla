# Configuration: General Ledger in D365 Finance & Operations

## Overview

- **Configuration Area**: General Ledger module
- **Business Purpose**: Core financial accounting foundation for recording, classifying, and reporting financial transactions
- **Impact**: Affects all financial modules (AP, AR, Fixed Assets, Project Accounting, etc.)
- **Prerequisites**: Legal entities must be created, fiscal calendars defined

---

## Key Configuration Components

### 1. Fiscal Calendar Setup

**Navigation Path**: `General ledger > Calendars > Fiscal calendars`

#### Steps:

1. Click **New** to create a calendar
2. Enter **Calendar name** (e.g., "US Standard Calendar")
3. Define **Start date** and **End date** for fiscal year
4. Click **New fiscal year** to generate periods
5. Set **Length of period** (Monthly, Quarterly, etc.)
6. Set **Number of periods**
7. Click **Create calendar** to auto-generate periods
8. Manually adjust period names and dates if needed
9. Mark periods as **Closed** or **On hold** as needed

**Validation**: Verify all 12 months (or custom periods) are generated correctly

---

### 2. Chart of Accounts Configuration

**Navigation Path**: `General ledger > Chart of accounts > Accounts > Main accounts`

#### Steps:

1. **Create Main Accounts**:

   - Click **New**
   - Enter **Main account number** (e.g., 110000)
   - Enter **Name** (e.g., "Cash - Operating Account")
   - Select **Main account type**: Asset, Liability, Revenue, Expense, Equity
   - Select **Main account category** (for financial reporting)
   - Set **Debit/Credit default** (optional)
   - Configure **Legal entity overrides** if needed

2. **Configure Account Properties**:
   - **Posting type restrictions** tab: Control what can post to this account
   - **Financial reporting** tab: Map to financial statement categories
   - **Default dimensions** tab: Set default dimension values

#### Main Account Categories:

- Balance Sheet: Assets, Liabilities, Equity
- Income Statement: Revenue, Cost of Goods Sold, Operating Expenses
- Statistical accounts (non-financial tracking)

---

### 3. Financial Dimensions Setup

**Navigation Path**: `General ledger > Chart of accounts > Dimensions > Financial dimensions`

#### Steps:

1. **Create Financial Dimensions**:

   - Click **New**
   - Select **Use values from**: Choose dimension source (Department, Cost Center, Project, etc.)
   - Or create custom dimension
   - Enter **Dimension name** and **Report column name**
   - Define **Dimension values** (manually or from entity)

2. **Activate Dimensions**:

   - Navigate to `General ledger > Chart of accounts > Dimensions > Activate financial dimensions`
   - Select dimensions to activate
   - Click **Activate** (Warning: Cannot be undone easily)

3. **Create Account Structures**:
   - Navigate to `General ledger > Chart of accounts > Structures > Configure account structures`
   - Click **New**
   - Enter **Name** (e.g., "Standard Account Structure")
   - Add **Segments**:
     - Main Account (always required)
     - Department, Cost Center, etc.
   - Define **Allowed values** for each segment
   - Define **Advanced rules** for specific account combinations
   - Click **Activate**

**Example Account Structure**:

```
Main Account - Department - Cost Center
110000       - 010        - CC001
```

---

### 4. Ledger Setup

**Navigation Path**: `General ledger > Ledger setup > Ledger`

#### Steps:

1. **Select Legal Entity** from company picker
2. Click **Edit** to configure ledger for that legal entity

3. **Configure Ledger Parameters**:

| Field                         | Description                          | Recommendation                                                |
| ----------------------------- | ------------------------------------ | ------------------------------------------------------------- |
| **Chart of accounts**         | Primary chart of accounts            | Select your configured COA                                    |
| **Fiscal calendar**           | Fiscal year definition               | Select your fiscal calendar                                   |
| **Accounting currency**       | Base currency for GL                 | USD, EUR, etc.                                                |
| **Reporting currency**        | Secondary reporting currency         | Optional - for consolidation                                  |
| **Exchange rate type**        | Default rate for currency conversion | Create in `General ledger > Currencies > Exchange rate types` |
| **Account structure**         | Active account structure             | Select your configured structure                              |
| **Budget exchange rate type** | For budget currency translation      | Optional                                                      |

4. **Configure Posting Layers**:

   - **Current**: Standard business transactions
   - **Operations**: Operational adjustments
   - **Tax**: Tax-related postings
   - **Elimination**: Intercompany eliminations

5. **Save** the ledger configuration

---

### 5. General Ledger Parameters

**Navigation Path**: `General ledger > Ledger setup > General ledger parameters`

#### Key Tabs to Configure:

**Ledger Tab**:

- **Allow financial year to be closed**: Enable year-end close
- **Allow editing of voucher date**: Control date changes
- **Settle with the same voucher**: Allow offset entries in same voucher
- **Require balanced journal**: Enforce debit = credit
- **Use ledger settlement process**: Enable detailed reconciliation

**Number Sequences Tab**:
Configure number sequences for:

- General journal voucher
- Daily journal voucher
- Allocation journal voucher
- Year-end result voucher
- Financial dimension value close tokens

**Sales Tax Tab**:

- **Rounding of sales tax**: Rounding method
- **Apply sales tax minimum**: Threshold for tax calculation
- **Total discount on tax**: How discounts affect tax

**Accounting Rules Tab**:

- Configure matching rules for advanced ledger entries

---

### 6. Journal Names Configuration

**Navigation Path**: `General ledger > Journal setup > Journal names`

#### Steps:

1. Click **New** to create journal name
2. Configure:

| Field                           | Description                 | Example                  |
| ------------------------------- | --------------------------- | ------------------------ |
| **Name**                        | Unique identifier           | GEN001                   |
| **Description**                 | Purpose description         | General Journal Entries  |
| **Journal type**                | Type of journal             | Daily, Payment, etc.     |
| **Voucher series**              | Number sequence             | Select from dropdown     |
| **Default account type**        | Default debit account       | Ledger, Customer, Vendor |
| **Default offset account type** | Default credit account      | Ledger                   |
| **Detail level**                | Posting summarization       | Summary/Detail           |
| **New voucher**                 | When new voucher is created | Date, Transaction type   |

3. **Workflow Configuration** (optional):

   - Assign workflow if journal approval is needed

4. **Posting restrictions**:
   - Set user groups allowed to use this journal name

---

### 7. Posting Definitions (Optional but Recommended)

**Navigation Path**: `General ledger > Posting setup > Posting definitions`

Used for automatic account determination and complex posting scenarios.

#### When to Use:

- Purchase order encumbrances
- Budget reservations
- Pre-encumbrances
- Complex posting patterns

---

### 8. Currency Configuration

**Navigation Path**: `General ledger > Currencies > Currencies`

#### Steps:

1. **Create/Verify Currencies**:

   - Click **New** or edit existing
   - Enter **Currency code** (USD, EUR, etc.)
   - Enter **Name** and **Symbol**
   - Set **Decimal places** for rounding

2. **Configure Exchange Rates**:
   - Navigate to `General ledger > Currencies > Exchange rate types`
   - Create rate types (e.g., "Default", "Budget", "Daily")
   - Navigate to `General ledger > Currencies > Currency exchange rates`
   - Enter **From currency** and **To currency**
   - Enter **Exchange rate** and **Start/End dates**
   - Set **Exchange rate type**

---

### 9. Sales Tax Setup (If Applicable)

**Navigation Path**: `Tax > Indirect taxes > Sales tax`

#### Core Components:

1. **Sales tax codes** (`Sales tax codes`)
2. **Sales tax groups** (`Sales tax groups`)
3. **Item sales tax groups** (`Item sales tax groups`)
4. **Ledger posting groups** (`Ledger posting groups`)

---

## Complete Configuration Checklist

- [ ] **Legal entities created** (`Organization administration > Organizations > Legal entities`)
- [ ] **Fiscal calendar defined** with all periods
- [ ] **Chart of accounts created** with main accounts
- [ ] **Financial dimensions defined** and activated
- [ ] **Account structures configured** and activated
- [ ] **Ledger assigned** to legal entity with COA and fiscal calendar
- [ ] **General ledger parameters** configured
- [ ] **Journal names created** for all needed journal types
- [ ] **Number sequences** assigned to GL vouchers
- [ ] **Currencies and exchange rates** configured
- [ ] **Sales tax** setup (if applicable)
- [ ] **Posting profiles** configured for subledgers
- [ ] **Opening balances** entered (if migrating from another system)

---

## Testing & Validation

### Test Scenarios:

1. **Create Test Journal**:

   - Navigate to `General ledger > Journal entries > General journals`
   - Click **New**
   - Select journal name
   - Click **Lines**
   - Enter debit and credit entries
   - Validate account and dimension combinations work
   - Post journal

2. **Verify Posting**:

   - Navigate to `General ledger > Inquiries and reports > Trial balance`
   - Verify journal posted correctly
   - Check balance = 0 for trial balance

3. **Currency Conversion**:

   - Create journal in foreign currency
   - Verify exchange rate applies correctly
   - Check accounting currency amounts

4. **Dimension Validation**:

   - Enter invalid dimension combination
   - Verify system prevents posting
   - Test advanced rules if configured

5. **Financial Reporting**:
   - Generate trial balance report
   - Verify accounts and dimensions display correctly

---

## Common Issues & Troubleshooting

### Issue: "Account structure not activated"

**Symptoms**: Cannot create journal entries
**Cause**: Account structure not activated or no active structure assigned to ledger
**Resolution**:

1. Navigate to `General ledger > Chart of accounts > Structures > Configure account structures`
2. Ensure structure is **Activated**
3. Verify structure is assigned in `General ledger > Ledger setup > Ledger`

### Issue: "Dimension combination is not valid"

**Symptoms**: Cannot post journal entry
**Cause**: Dimension combination violates advanced rules or allowed values
**Resolution**:

1. Check advanced rules in account structure
2. Verify dimension values exist and are active
3. Check financial dimension activation status

### Issue: "Fiscal calendar period is closed"

**Symptoms**: Cannot post to prior periods
**Cause**: Period status set to "Closed" or "On hold"
**Resolution**:

1. Navigate to `General ledger > Calendars > Fiscal calendars`
2. Check period status
3. If authorized, change status to "Open" temporarily
4. Post entry, then re-close period

### Issue: Exchange rate not found

**Symptoms**: Cannot post foreign currency transaction
**Cause**: No exchange rate defined for date and currency pair
**Resolution**:

1. Navigate to `General ledger > Currencies > Currency exchange rates`
2. Create rate for specific date and currency combination
3. Ensure correct exchange rate type is assigned

---

## Best Practices

### Design Phase:

✅ **Plan financial dimensions carefully** - difficult to change after activation  
✅ **Use standard account structures** - avoid overly complex dimension logic  
✅ **Document account coding logic** - create COA reference guide  
✅ **Align COA with reporting requirements** - map accounts to financial statements early  
✅ **Establish naming conventions** - consistent account and dimension naming

### Configuration Phase:

✅ **Configure in DEV environment first** - test thoroughly before production  
✅ **Use data packages** - export/import configuration across environments  
✅ **Test all posting scenarios** - validate before go-live  
✅ **Create comprehensive journal names** - separate by business process  
✅ **Configure security by journal name** - limit access to sensitive journals

### Operational Phase:

✅ **Monitor trial balance regularly** - ensure books balance  
✅ **Perform monthly reconciliations** - reconcile subledgers to GL  
✅ **Archive historical data** - maintain system performance  
✅ **Review and maintain exchange rates** - update regularly  
✅ **Close periods promptly** - prevent backdated entries

### DON'T:

❌ Don't activate dimensions without thorough testing  
❌ Don't allow multiple account structures without clear business need  
❌ Don't skip fiscal calendar period setup  
❌ Don't post directly to balance sheet accounts without proper controls  
❌ Don't modify chart of accounts after go-live without change control

---

## Related Configurations

- **Accounts Payable**: Vendor posting profiles linked to GL accounts
- **Accounts Receivable**: Customer posting profiles linked to GL accounts
- **Fixed Assets**: FA posting profiles and depreciation GL accounts
- **Inventory Management**: Item posting profiles for inventory valuation
- **Financial Reporting**: Management Reporter integration with COA
- **Budget Module**: Budget models and allocation rules

---

## References

- [General ledger home page](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/general-ledger)
- [Configure chart of accounts](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/plan-chart-of-accounts)
- [Financial dimensions](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/financial-dimensions)
- [Fiscal calendars, fiscal years, and periods](https://learn.microsoft.com/en-us/dynamics365/finance/budgeting/fiscal-calendars-fiscal-years-periods)
- [Ledger settlements](https://learn.microsoft.com/en-us/dynamics365/finance/general-ledger/ledger-settlements)
- [FastTrack Implementation Assets](https://github.com/microsoft/Dynamics-365-FastTrack-Implementation-Assets)

---

## Additional Tips

### For New Implementations:

1. **Start with standard account structure** - one main account + 2-3 dimensions maximum
2. **Leverage data entities** - Use "Ledger fiscal calendar" and "Main account" entities for bulk load
3. **Use configuration templates** - Microsoft provides starter COAs for different industries
4. **Plan for reporting early** - Map accounts to financial statement line definitions

### For Migration Projects:

1. **Map legacy COA** to new D365 chart of accounts
2. **Create data migration templates** using DMF
3. **Test opening balance import** thoroughly before cutover
4. **Plan for dual-run period** - run parallel systems during transition
