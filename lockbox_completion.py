import streamlit as st

def score_lockbox_vs_completion(
    company_stability,  # 0-10
    seller_trustworthiness,  # 0-10
    duration_months,  # integer
    cashflow_volatility,  # 0-10
    buyer_risk_appetite  # 0-10
):
    # Normalize duration to a 0-10 scale where 0 months = 10 points, 12+ months = 0
    duration_score = max(0, 10 - (duration_months * (10/12)))

    # Calculate overall Lockbox and Completion Accounts scores
    lockbox_score = (
        0.3 * company_stability +
        0.25 * seller_trustworthiness +
        0.2 * duration_score +
        0.15 * (10 - cashflow_volatility) +
        0.1 * buyer_risk_appetite
    )

    completion_score = 50 - lockbox_score  # inverse logic

    return lockbox_score, completion_score

def main():
    st.title("M&A Pricing Mechanism Chooser \U0001F4BC")
    st.subheader("Should you use a Lockbox or Completion Accounts?")

    company_stability = st.slider("Company Stability (0=chaotic, 10=stable)", 0, 10, 5)
    seller_trustworthiness = st.slider("Seller Trustworthiness (0=gremlin, 10=saint)", 0, 10, 5)
    duration_months = st.slider("Duration Between Lockbox and Closing (months)", 0, 18, 6)
    cashflow_volatility = st.slider("Cashflow Volatility (0=steady, 10=wild)", 0, 10, 5)
    buyer_risk_appetite = st.slider("Buyer Risk Appetite (0=chicken, 10=daredevil)", 0, 10, 5)

    if st.button("Score My Deal!"):
        lockbox_score, completion_score = score_lockbox_vs_completion(
            company_stability,
            seller_trustworthiness,
            duration_months,
            cashflow_volatility,
            buyer_risk_appetite
        )

        st.write(f"**Lockbox Suitability Score:** {lockbox_score:.2f}/50")
        st.write(f"**Completion Accounts Suitability Score:** {completion_score:.2f}/50")

        if lockbox_score > completion_score:
            st.success("\U0001F512 Recommendation: Use LOCKBOX mechanism.")
        else:
            st.info("\U0001F4B0 Recommendation: Use COMPLETION ACCOUNTS mechanism.")

if __name__ == "__main__":
    main()
