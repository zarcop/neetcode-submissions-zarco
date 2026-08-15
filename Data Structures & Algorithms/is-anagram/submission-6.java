class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int univLength = t.length();
        Map<Character, Integer> letterDictS = new HashMap<>();
        Map<Character, Integer> letterDictT = new HashMap<>();
        for (int i = 0; i < univLength; i++ ) {
            char c = t.charAt(i);
            letterDictT.put(c, letterDictT.getOrDefault(c, 0) + 1);
        }
        for (int i = 0; i < univLength; i++ ) {
            char c = s.charAt(i);
            letterDictS.put(c, letterDictS.getOrDefault(c, 0) + 1);
        }
       return letterDictS.equals(letterDictT);
    }
}
