class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unique = set()
        for email in emails:
            ##find position of the @ symbol
            ##find position of the first + symbol
            at = email.index('@')
            email = email[:at].replace(".", "") + email[at:]
            if '+' in email:
                plus = email.index('+')
                at = email.index('@')
                email = email[:plus] + email[at:]
            unique.add(email)
        return len(unique)