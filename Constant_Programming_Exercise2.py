Index: Constant_Programming_Exercise2.py
IDEA additional info:
Subsystem: com.intellij.openapi.diff.impl.patch.CharsetEP
<+>UTF-8
===================================================================
diff --git a/Constant_Programming_Exercise2.py b/Constant_Programming_Exercise2.py
new file mode 100644
--- /dev/null	(date 1771090668330)
+++ b/Constant_Programming_Exercise2.py	(date 1771090668330)
@@ -0,0 +1,85 @@
+
+# List of 30 common spam keywords/phrases
+spam_keywords = [
+    "free", "winner", "click here", "urgent", "act now",
+    "limited time", "offer", "prize", "money", "cash",
+    "guaranteed", "risk-free", "bonus", "cheap", "credit",
+    "loan", "earn", "income", "urgent response", "discount",
+    "buy now", "save big", "investment", "win big", "100% free",
+    "exclusive deal", "apply now", "no cost", "claim", "instant"
+]
+
+# calculate_spam_score
+
+def calculate_spam_score(message, keywords):
+    """
+    Scans the message for spam keywords.
+    Returns:
+      - score: total spam points (counting multiple occurrences)
+      - found_words: dictionary of keywords found and their counts
+    """
+    score = 0  # Initialize spam score
+    found_words = {}  # Dictionary to store keyword and count
+    lower_message = message.lower()  # Convert message to lowercase for case-insensitive matching
+
+    # Check each keyword
+    for word in keywords:
+        count = lower_message.count(word)  # Count occurrences of this keyword
+        if count > 0:
+            score += count  # Add occurrences to spam score
+            found_words[word] = count  # Record keyword and how many times it appeared
+
+    return score, found_words
+
+
+# ---------------------------
+# Function: rate_spam
+# ---------------------------
+def rate_spam(score):
+    """
+    Determines the likelihood of spam based on the score.
+    Returns a string describing the likelihood.
+    """
+    if score >= 10:
+        return "High likelihood of spam"
+    elif score >= 5:
+        return "Moderate likelihood of spam"
+    else:
+        return "Low likelihood of spam"
+
+
+
+# Function: display_results
+def display_results(score, found_words, likelihood):
+    """
+    Prints the spam analysis report.
+    """
+    print("\n--- Spam Analysis Report ---")
+    print(f"Spam score: {score}")
+    print(f"Likelihood: {likelihood}")
+
+    if found_words:
+        print("Words/phrases detected:")
+        for word, count in found_words.items():
+            print(f"  '{word}' → {count} occurrence(s)")
+    else:
+        print("No spam keywords detected.")
+
+# Main program
+def main():
+    print("Welcome to the Spam Detector!")
+    message = input("Enter the email message to scan:\n")
+
+    # Step 1: Calculate spam score and detected keywords
+    score, found_words =calculate_spam_score(message, spam_keywords)
+
+    # Step 2: Determine likelihood of spam
+    likelihood = rate_spam(score)
+
+    # Step 3: Display results
+    display_results(score, found_words, likelihood)
+
+
+# Run the program
+if __name__ == "__main__":
+    main()
